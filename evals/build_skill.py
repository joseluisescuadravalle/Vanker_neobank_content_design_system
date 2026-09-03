"""Build the Claude skill from the system, so the skill cannot drift from the source.

The skill in ../skill/vanker-content-design/ is the system loaded as instructions instead
of applied as a judge. Its SKILL.md is hand-written; everything else in it is a copy of
this repository: the documents go to references/, the checker to scripts/. A copy kept by
hand is how the desktop app fell behind twice, so this script is the only writer, and its
--check mode is the seventh gate.

    python build_skill.py           rebuild references/, scripts/, INDEX.md and MANIFEST.json
    python build_skill.py --check   fail if the skill is stale, or a surface has no owner
    python build_skill.py --package rebuild and zip it as ../skill/vanker-content-design.skill,
                                    the file that installs with "Save skill" in a Claude chat
"""
import hashlib
import json
import os
import re
import shutil
import sys

import assertions

HERE = os.path.dirname(os.path.abspath(__file__))
ROOT = os.path.dirname(HERE)
SKILL = os.path.join(ROOT, "skill", "vanker-content-design")
REFS = os.path.join(SKILL, "references")
SCRIPTS = os.path.join(SKILL, "scripts")

# Documents copied verbatim. Foundations (tokens) carry no copy rules and stay out.
COPY_DIRS = ["terminology", "voice-and-tone", "compliance", "patterns", "components/library"]
COPY_FILES = ["CLAUDE.md"]
# The checker travels with the skill, so the agent runs the same code the golden set runs.
SCRIPT_FILES = ["assertions.py", "rules.json"]

# Which files own each surface. This is data a person wrote, so --check fails when a surface
# exists in assertions.SURFACE_CHECKS and not here: an unmapped surface is a surface the
# agent would write blind.
SURFACE_OWNERS = {
    "cta": ["patterns/ctas.md", "components/library/button.md"],
    "button": ["patterns/ctas.md", "components/library/button.md"],
    "link": ["patterns/links.md"],
    "field-error": ["patterns/errors.md", "patterns/forms.md", "components/library/text-field.md"],
    "validation": ["patterns/errors.md", "patterns/forms.md", "components/library/text-field.md"],
    "error-summary-title": ["patterns/errors.md", "patterns/forms.md"],
    "error": ["patterns/errors.md", "components/library/sheet-modal.md"],
    "system-error": ["patterns/system-errors.md"],
    "system-error-title": ["patterns/system-errors.md"],
    "system-error-screen": ["patterns/system-errors.md", "components/library/empty-state.md"],
    "loading": ["patterns/loading.md"],
    "loading-screen": ["patterns/loading.md"],
    "skeleton": ["patterns/loading.md"],
    "confirmation": ["patterns/confirmations.md", "components/library/sheet-modal.md"],
    "card-action": ["patterns/cards.md", "patterns/confirmations.md"],
    "success": ["patterns/success.md"],
    "empty-state": ["patterns/empty-states.md", "components/library/empty-state.md"],
    "no-results": ["patterns/search.md", "patterns/empty-states.md"],
    "search-placeholder": ["patterns/search.md"],
    "notification": ["patterns/notifications.md"],
    "push-title": ["patterns/notifications.md"],
    "push-body": ["patterns/notifications.md"],
    "toast": ["components/library/banner-toast.md"],
    "banner": ["components/library/banner-toast.md"],
    "email-subject": ["patterns/emails.md"],
    "email-preheader": ["patterns/emails.md"],
    "email-body": ["patterns/emails.md"],
    "onboarding-step": ["components/library/onboarding-step.md", "patterns/flow-intro.md"],
    "flow-intro-body": ["patterns/flow-intro.md"],
    "flow-intro-cta": ["patterns/flow-intro.md", "patterns/ctas.md"],
    "carousel-headline": ["patterns/welcome-carousel.md"],
    "carousel-body": ["patterns/welcome-carousel.md"],
    "permission-heading": ["patterns/permissions.md"],
    "permission-body": ["patterns/permissions.md"],
    "auth": ["patterns/auth.md", "components/library/code-input.md"],
    "auth-error": ["patterns/auth.md", "patterns/errors.md"],
    "code-screen": ["components/library/code-input.md", "patterns/auth.md", "compliance/security-payments.md"],
    "security": ["compliance/security-payments.md", "patterns/auth.md"],
    "disclosure": ["compliance/disclosures.md"],
    "risk-warning": ["compliance/risk-warnings.md"],
    "fx-quote": ["patterns/currency-exchange.md", "compliance/disclosures.md"],
    "complaint-acknowledgement": ["patterns/complaints.md", "compliance/complaints.md"],
    "complaint-answer": ["patterns/complaints.md", "compliance/complaints.md"],
    "label-in": ["components/library/text-field.md", "patterns/forms.md"],
    "label-out": ["components/library/text-field.md", "patterns/forms.md"],
    "legend": ["components/library/text-field.md", "components/library/radio-group.md", "patterns/forms.md"],
    "helper-text": ["components/library/text-field.md", "patterns/forms.md"],
    "placeholder": ["components/library/text-field.md", "patterns/forms.md"],
    "counter": ["components/library/textarea.md"],
    "date-unavailable": ["components/library/date-field.md"],
    "dropdown-option": ["components/library/dropdown.md"],
    "option": ["components/library/dropdown.md"],
    "checkbox": ["components/library/checkbox.md"],
    "radio-option": ["components/library/radio-group.md"],
    "radio": ["components/library/radio-group.md"],
    "toggle-label": ["components/library/toggle.md"],
    "toggle-description": ["components/library/toggle.md"],
    "status-label": ["components/library/status-label.md"],
    "status": ["components/library/status-label.md"],
    "badge": ["components/library/status-label.md"],
    "tag": ["components/library/status-label.md"],
    "count-badge": ["components/library/count-badge.md"],
    "chip": ["components/library/chip.md"],
    "amount-value": ["components/library/amount-input.md"],
    "preset-amount": ["components/library/amount-input.md"],
    "amount-label": ["components/library/amount-input.md"],
    "tooltip": ["components/library/tooltip.md"],
    "tooltip-trigger": ["components/library/tooltip.md"],
    "accordion-header": ["components/library/accordion.md"],
    "accordion-body": ["components/library/accordion.md"],
    "alt-text": ["patterns/alt-text.md", "patterns/accessibility.md"],
    "category": ["patterns/charts.md", "components/library/transaction-row.md"],
    "chart-copy": ["patterns/charts.md"],
}
# Read for every string, whatever the surface.
ALWAYS = ["CLAUDE.md", "terminology/glossary.md", "terminology/banned-terms.md",
          "terminology/numbers-and-dates.md", "terminology/capitalization-and-punctuation.md",
          "voice-and-tone/voice.md", "voice-and-tone/tone.md"]


def sha(path):
    with open(path, "rb") as fh:
        return hashlib.sha256(fh.read()).hexdigest()


def source_files():
    out = list(COPY_FILES)
    for d in COPY_DIRS:
        for name in sorted(os.listdir(os.path.join(ROOT, d))):
            if name.endswith(".md"):
                out.append(d + "/" + name)
    return out


def thesis(rel):
    """The first prose paragraph after the status line: the one idea the file exists for."""
    with open(os.path.join(ROOT, rel), encoding="utf-8") as fh:
        text = fh.read()
    paras = [p.strip() for p in re.split(r"\n\s*\n", text)]
    for p in paras:
        if p.startswith("#") or p.startswith("**Status") or p.startswith("<!--"):
            continue
        return re.sub(r"\s+", " ", p)[:220]
    return ""


def index_md():
    lines = ["# Index: surfaces, checks, and the files that own them", "",
             "**Generated by `evals/build_skill.py`. Do not edit here.**", "",
             "Start from the surface you are writing. Read the owning files before writing, and",
             "run `scripts/check_copy.py --surface <id>` on the result. Every surface also runs the",
             "universal checks: " + ", ".join("`%s`" % c for c in assertions.UNIVERSAL) + ".", "",
             "## Always read, whatever the surface", ""]
    for rel in ALWAYS:
        lines.append("- `%s`: %s" % (rel, thesis(rel)))
    lines += ["", "## Surfaces", "", "| Surface id | Checks (besides the universal ones) | Owning files |", "| --- | --- | --- |"]
    for surface in sorted(assertions.SURFACE_CHECKS):
        checks = [c for c in assertions.SURFACE_CHECKS[surface] if c not in assertions.UNIVERSAL]
        owners = SURFACE_OWNERS.get(surface, [])
        lines.append("| `%s` | %s | %s |" % (surface, ", ".join("`%s`" % c for c in checks),
                                             ", ".join("`%s`" % o for o in owners) or "**unmapped**"))
    lines += ["", "A string whose surface is not listed runs the body checks: " +
              ", ".join("`%s`" % c for c in assertions.BODY_CHECKS) + ".", "",
              "## Compliance, by what the string touches", "",
              "- Money movement, fees, timing: `compliance/disclosures.md`, `compliance/security-payments.md`",
              "- Investment, crypto, credit: `compliance/risk-warnings.md`",
              "- Identity, documents, selfies: `compliance/identity-kyc.md`",
              "- Personal data, permissions, masking: `compliance/data-privacy.md`",
              "- Complaints, or anything a person could complain about: `compliance/complaints.md`",
              "- Screen readers, color, alt text: `compliance/accessibility.md`, `patterns/accessibility.md`",
              "- The frame behind all of them: `compliance/framework.md`, `compliance/principles.md`", "",
              "## Every file, with its thesis", ""]
    for rel in source_files():
        if rel.endswith("README.md") or rel in ALWAYS:
            continue
        lines.append("- `%s`: %s" % (rel, thesis(rel)))
    return "\n".join(lines) + "\n"


def manifest():
    m = {"_": "Generated by evals/build_skill.py. Hash of every source file copied into this skill.",
         "sources": {rel: sha(os.path.join(ROOT, rel)) for rel in source_files()},
         "scripts": {rel: sha(os.path.join(HERE, rel)) for rel in SCRIPT_FILES}}
    return m


def unmapped():
    return [s for s in sorted(assertions.SURFACE_CHECKS) if s not in SURFACE_OWNERS]


def missing_owner_files():
    out = []
    for s, files in SURFACE_OWNERS.items():
        for f in files:
            if not os.path.exists(os.path.join(ROOT, f)):
                out.append("%s -> %s" % (s, f))
    return out


def build():
    expected = {os.path.join(REFS, rel) for rel in source_files()}
    expected |= {os.path.join(REFS, "INDEX.md"), os.path.join(REFS, "MANIFEST.json")}
    # Remove copies whose source is gone. File by file rather than rmtree: the Cowork mount
    # forbids deletion, and a build that cannot delete must still be able to write.
    for base, _dirs, files in os.walk(REFS):
        for name in files:
            path = os.path.join(base, name)
            if path not in expected:
                try:
                    os.remove(path)
                except PermissionError:
                    print("WARN   could not remove orphan %s (delete it by hand)" % os.path.relpath(path, SKILL))
    for rel in source_files():
        dst = os.path.join(REFS, rel)
        os.makedirs(os.path.dirname(dst), exist_ok=True)
        shutil.copyfile(os.path.join(ROOT, rel), dst)
    os.makedirs(SCRIPTS, exist_ok=True)
    for rel in SCRIPT_FILES:
        shutil.copyfile(os.path.join(HERE, rel), os.path.join(SCRIPTS, rel))
    with open(os.path.join(REFS, "INDEX.md"), "w", encoding="utf-8") as fh:
        fh.write(index_md())
    with open(os.path.join(REFS, "MANIFEST.json"), "w", encoding="utf-8") as fh:
        json.dump(manifest(), fh, indent=2)
        fh.write("\n")


def check():
    problems = []
    problems += ["surface '%s' has no owning file in build_skill.SURFACE_OWNERS" % s for s in unmapped()]
    problems += ["owner file does not exist: %s" % f for f in missing_owner_files()]
    mpath = os.path.join(REFS, "MANIFEST.json")
    if not os.path.exists(mpath):
        problems.append("skill has never been built (no MANIFEST.json)")
    else:
        with open(mpath, encoding="utf-8") as fh:
            old = json.load(fh)
        new = manifest()
        for kind in ("sources", "scripts"):
            for rel, h in new[kind].items():
                if old.get(kind, {}).get(rel) != h:
                    problems.append("stale or missing in skill: %s" % rel)
            for rel in old.get(kind, {}):
                if rel not in new[kind]:
                    problems.append("in skill but no longer in source: %s" % rel)
        # The copies themselves, not only the manifest.
        for rel in source_files():
            dst = os.path.join(REFS, rel)
            if not os.path.exists(dst) or sha(dst) != new["sources"][rel]:
                problems.append("reference copy differs from source: %s" % rel)
        for rel in SCRIPT_FILES:
            dst = os.path.join(SCRIPTS, rel)
            if not os.path.exists(dst) or sha(dst) != new["scripts"][rel]:
                problems.append("script copy differs from source: %s" % rel)
        ipath = os.path.join(REFS, "INDEX.md")
        if not os.path.exists(ipath) or open(ipath, encoding="utf-8").read() != index_md():
            problems.append("INDEX.md is stale")
    if problems:
        for p in problems:
            print("STALE  " + p)
        print("\nSkill is out of date: run `python build_skill.py`.")
        return 1
    n = len(source_files())
    print("Skill is current: %d reference files, %d surfaces mapped, checker copied." % (n, len(assertions.SURFACE_CHECKS)))
    return 0


def package():
    import zipfile
    out = os.path.join(ROOT, "skill", "vanker-content-design.skill")
    with zipfile.ZipFile(out, "w", zipfile.ZIP_DEFLATED) as zf:
        for base, dirs, files in os.walk(SKILL):
            dirs[:] = [d for d in dirs if d != "__pycache__"]
            for name in sorted(files):
                path = os.path.join(base, name)
                zf.write(path, os.path.relpath(path, os.path.dirname(SKILL)))
    print("Packaged %s" % out)


if __name__ == "__main__":
    if "--check" in sys.argv:
        sys.exit(check())
    if unmapped():
        print("Refusing to build: unmapped surfaces " + ", ".join(unmapped()))
        sys.exit(1)
    build()
    print("Built %s" % SKILL)
    rc = check()
    if rc == 0 and "--package" in sys.argv:
        package()
    sys.exit(rc)
