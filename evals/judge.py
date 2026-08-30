"""The LLM-as-judge layer: build the prompts, then score the verdicts.

    python judge.py build [--limit N] [--ids a,b,c]
    python judge.py score judge-runs/<file>.jsonl

`build` writes one filled prompt per case into judge-batch/, following judge-prompt.md.
A judge model answers each one with the JSON verdict, and those verdicts, one per line,
go into a run file. `score` aggregates them and, crucially, compares the verdict against
what the case expected.

Two things this deliberately does NOT do:

- It never puts the case's `expected` note into the prompt. That note is the human's
  answer key; giving it to the judge is asking it to mark its own homework.
- It never sends a candidate that the deterministic layer already rejected. The cheap
  gate runs first (see approach.md); the judge is for what code cannot see.
"""
import json
import os
import sys

import assertions

CASES = "golden-set/cases.jsonl"
OUT = "judge-batch"

# The reference a judge needs is the part of the system that governs the surface, not the
# whole repository: a judge with too much context grades on the wrong rules.
ALWAYS = ["../CLAUDE.md", "../voice-and-tone/voice.md", "../voice-and-tone/tone.md",
          "../terminology/glossary.md", "../terminology/banned-terms.md",
          "../terminology/capitalization-and-punctuation.md",
          "../terminology/numbers-and-dates.md"]

BY_SURFACE = {
    "cta": ["../patterns/ctas.md"],
    "link": ["../patterns/links.md"],
    "field-error": ["../patterns/errors.md", "../patterns/forms.md"],
    "auth-error": ["../patterns/errors.md", "../patterns/auth.md"],
    "auth": ["../patterns/auth.md", "../compliance/security-payments.md"],
    "system-error": ["../patterns/system-errors.md", "../patterns/errors.md"],
    "system-error-title": ["../patterns/system-errors.md"],
    "system-error-screen": ["../patterns/system-errors.md", "../patterns/errors.md"],
    "loading": ["../patterns/loading.md"],
    "loading-screen": ["../patterns/loading.md"],
    "skeleton": ["../patterns/loading.md"],
    "card-action": ["../patterns/cards.md", "../patterns/confirmations.md"],
    "code-screen": ["../components/library/code-input.md", "../compliance/security-payments.md"],
    "permission-body": ["../patterns/permissions.md", "../compliance/data-privacy.md"],
    "permission-heading": ["../patterns/permissions.md"],
    "flow-intro-body": ["../patterns/flow-intro.md"],
    "flow-intro-cta": ["../patterns/flow-intro.md", "../patterns/ctas.md"],
    "carousel-headline": ["../patterns/welcome-carousel.md", "../compliance/disclosures.md"],
    "carousel-body": ["../patterns/welcome-carousel.md", "../compliance/disclosures.md"],
    "email-subject": ["../patterns/emails.md"],
    "email-preheader": ["../patterns/emails.md"],
    "email-body": ["../patterns/emails.md", "../compliance/security-payments.md"],
    "push-title": ["../patterns/notifications.md"],
    "push-body": ["../patterns/notifications.md"],
    "toast": ["../components/library/banner-toast.md"],
    "banner": ["../components/library/banner-toast.md"],
    "tooltip": ["../components/library/tooltip.md"],
    "tooltip-trigger": ["../components/library/tooltip.md"],
    "accordion-header": ["../components/library/accordion.md"],
    "toggle-label": ["../components/library/toggle.md"],
    "toggle-description": ["../components/library/toggle.md"],
    "status-label": ["../components/library/status-label.md"],
    "amount-label": ["../components/library/amount-input.md"],
    "amount-value": ["../components/library/amount-input.md"],
    "preset-amount": ["../components/library/amount-input.md"],
    "helper-text": ["../patterns/forms.md", "../components/library/text-field.md"],
    "label-in": ["../patterns/forms.md"], "label-out": ["../patterns/forms.md"],
    "checkbox": ["../components/library/checkbox.md"],
    "radio-option": ["../components/library/radio-group.md"],
    "confirmation": ["../patterns/confirmations.md"],
    "success": ["../patterns/success.md"],
    "empty-state": ["../patterns/empty-states.md"],
    "disclosure": ["../compliance/disclosures.md"],
    "risk-warning": ["../compliance/risk-warnings.md"],
    "security": ["../compliance/security-payments.md"],
    "transaction-row": ["../components/library/transaction-row.md"],
    "error": ["../patterns/errors.md"],
    "onboarding-step": ["../components/library/onboarding-step.md"],
}

TEMPLATE = """You are a strict reviewer for Vanker, a fictional euro-area neobank. You are
given the content design system and a candidate string written for a specific surface.
Score the candidate against the rubric.

SYSTEM REFERENCE (authoritative):
{reference}

RUBRIC:
{rubric}

SURFACE: {surface}
TASK: {task}
CONTEXT: {context}
CANDIDATE:
"{candidate}"

Score each dimension 0, 1, or 2. Mark a dimension "na" when it does not apply to this
surface (a button has no compliance dimension of its own). Compliance and tone_fit must not
be 0 on a pass. Default to the lower score when unsure.

Return JSON only:
{{"id": "{case_id}",
  "scores": {{"voice": 0-2|"na", "tone_fit": 0-2|"na", "clarity": 0-2|"na",
             "terminology": 0-2|"na", "pattern_fit": 0-2|"na", "compliance": 0-2|"na",
             "accessibility": 0-2|"na"}},
  "pass": true|false,
  "reasons": {{"<dimension>": "one short reason for any score below 2"}},
  "fix": "one concrete suggestion, or null"}}
"""


def load_cases():
    with open(CASES, encoding="utf-8") as fh:
        return [json.loads(line) for line in fh if line.strip()]


def reference_for(surface):
    paths = ALWAYS + BY_SURFACE.get(surface, [])
    out = []
    for rel in paths:
        path = os.path.join(os.path.dirname(__file__) or ".", rel)
        if os.path.exists(path):
            with open(path, encoding="utf-8") as fh:
                out.append("----- %s -----\n%s" % (rel.lstrip("./"), fh.read()))
    return "\n\n".join(out)


def build(limit=None, ids=None):
    os.makedirs(OUT, exist_ok=True)
    rubric = open(os.path.join(os.path.dirname(__file__) or ".", "rubric.md"), encoding="utf-8").read()
    built, skipped = 0, []
    for c in load_cases():
        if not c.get("judge"):
            continue
        if ids and c["id"] not in ids:
            continue
        cand = c.get("context", {}).get("candidate")
        # An empty string is a candidate: a decorative image's alt is deliberately "".
        # Only a missing candidate means the case still needs a model to generate one.
        if cand is None:
            skipped.append((c["id"], "no candidate yet"))
            continue
        res = assertions.run(cand, c.get("must_pass"), surface=c.get("surface"))
        if res and not all(v["passed"] for v in res.values()):
            skipped.append((c["id"], "rejected by the deterministic gate"))
            continue
        ctx = {k: v for k, v in c.get("context", {}).items() if k != "candidate"}
        text = TEMPLATE.format(reference=reference_for(c.get("surface")), rubric=rubric,
                               surface=c.get("surface"), task=c.get("task", ""),
                               context=json.dumps(ctx, ensure_ascii=False) or "{}",
                               candidate=cand, case_id=c["id"])
        with open(os.path.join(OUT, c["id"].replace("/", "_") + ".txt"), "w", encoding="utf-8") as fh:
            fh.write(text)
        built += 1
        if limit and built >= limit:
            break
    print("built %d prompt(s) in %s/" % (built, OUT))
    for cid, why in skipped:
        print("  skipped %-28s %s" % (cid, why))
    return 0


def score(path):
    cases = {c["id"]: c for c in load_cases()}
    verdicts = [json.loads(l) for l in open(path, encoding="utf-8") if l.strip()]
    dims = ["voice", "tone_fit", "clarity", "terminology", "pattern_fit", "compliance", "accessibility"]
    agree = disagree = 0
    totals = {d: [] for d in dims}
    print("%-28s %-6s %-6s %s" % ("case", "judge", "expect", "note"))
    for v in verdicts:
        c = cases.get(v["id"], {})
        # Two different expectations, and the difference is the whole point of the layer:
        #   expect_fail        the deterministic layer must reject it
        #   expect_judge_fail  code passes it and the JUDGE must reject it. This is the
        #                      class of case the second layer exists for.
        expected_pass = not (c.get("expect_fail") or c.get("expect_judge_fail"))
        ok = v["pass"] == expected_pass
        agree, disagree = (agree + 1, disagree) if ok else (agree, disagree + 1)
        for d in dims:
            s = v["scores"].get(d)
            if isinstance(s, int):
                totals[d].append(s)
        note = "" if ok else "DISAGREES with the case"
        print("%-28s %-6s %-6s %s" % (v["id"], "pass" if v["pass"] else "FAIL",
                                      "pass" if expected_pass else "FAIL", note))
    print()
    for d in dims:
        vals = totals[d]
        if vals:
            print("  %-14s mean %.2f over %d scored" % (d, sum(vals) / len(vals), len(vals)))
    print("\nJudge agrees with the golden set on %d of %d case(s)." % (agree, agree + disagree))
    return 1 if disagree else 0


if __name__ == "__main__":
    cmd = sys.argv[1] if len(sys.argv) > 1 else "build"
    if cmd == "build":
        ids = None
        limit = None
        for i, arg in enumerate(sys.argv):
            if arg == "--ids":
                ids = set(sys.argv[i + 1].split(","))
            if arg == "--limit":
                limit = int(sys.argv[i + 1])
        sys.exit(build(limit, ids))
    elif cmd == "score":
        sys.exit(score(sys.argv[2]))
    else:
        print(__doc__)
        sys.exit(2)
