"""Build the editorial review prompt for copy in the delivery format.

The deterministic checks (check_copy.py) catch shape. The editorial review is the judge
layer of evals/: a strict reviewer scores the copy on voice, tone fit, clarity, terminology,
pattern fit, compliance and accessibility, 0 to 2 each, against the rubric. This script
writes the prompt; a reviewer with a clean context answers it.

    python3 editorial_review.py --file screen.txt > review-prompt.md
    python3 editorial_review.py --file screen.txt --task "Full-screen error when a card payment is rejected"

The prompt lists the reference files the reviewer must read (by surface, from
references/owners.json) rather than inlining them, so the reviewer reads exactly what
governs the surface and nothing else. It never includes the writer's reasoning, only the
task and the copy: a reviewer that sees the writer's argument grades the argument.
"""
import json
import os
import re
import sys

HERE = os.path.dirname(os.path.abspath(__file__))
SKILL = os.path.dirname(HERE)
REFS = os.path.join(SKILL, "references")
SLOT = re.compile(r"^([A-Za-z0-9_-]+)\s*\(([A-Za-z0-9_-]+)\)\s*:\s?(.*)$")


def parse(text):
    slots, screen = [], None
    for line in text.splitlines():
        if line.startswith("Screen:"):
            screen = line[len("Screen:"):].strip(); continue
        if line.startswith("Editorial review:"):
            continue
        m = SLOT.match(line)
        if m:
            slots.append([m.group(1), m.group(2), m.group(3)])
        elif slots:
            slots[-1][2] += "\n" + line
    return screen, [(s, sf, t.strip()) for s, sf, t in slots]


def files_for(surfaces, owners):
    out = list(owners["always"])
    for s in surfaces:
        for f in owners["by_surface"].get(s.lower(), owners["body_default"]):
            if f not in out:
                out.append(f)
    for f in ("evals/rubric.md",):
        if f not in out:
            out.append(f)
    return out


def main(argv):
    if "--file" not in argv:
        print(__doc__); return 2
    path = argv[argv.index("--file") + 1]
    text = sys.stdin.read() if path == "-" else open(path, encoding="utf-8").read()
    task = argv[argv.index("--task") + 1] if "--task" in argv else None
    screen, slots = parse(text)
    if not slots:
        raise SystemExit("no slots found; expected the delivery format `slot (surface): text`")
    owners = json.load(open(os.path.join(REFS, "owners.json"), encoding="utf-8"))
    files = files_for([sf for _, sf, _ in slots], owners)
    lines = []
    lines.append("You are a strict editorial reviewer for Vanker, a fictional euro-area neobank. You did not write this copy and you have not seen the writer's reasoning. Score it against the system, not against your taste.")
    lines.append("")
    lines.append("READ FIRST, in this order (paths relative to the skill's references/ folder):")
    for f in files:
        lines.append("- references/" + f)
    lines.append("")
    lines.append("TASK: " + (task or screen or "(not stated; judge the copy on its surfaces alone)"))
    lines.append("")
    lines.append("COPY UNDER REVIEW (one slot per line, `slot (surface): text`; a body keeps its paragraph breaks):")
    lines.append("```")
    for s, sf, t in slots:
        lines.append("%s (%s): %s" % (s, sf, t))
    lines.append("```")
    lines.append("")
    lines.append("Read the screen as one thing before scoring: does the title agree with the body, is it clear whose side the problem is on, is the money accounted for, does each button do what the body promised, would a person who cannot see the screen know what to do.")
    lines.append("")
    lines.append("Score each dimension 0, 1 or 2 using references/evals/rubric.md: voice, tone_fit, clarity, terminology, pattern_fit, compliance, accessibility. Score a dimension \"na\" when it does not apply to these surfaces (a lone button has no compliance content). Default to the lower score when unsure. Judge only against the system as given; do not invent rules.")
    lines.append("")
    lines.append("Pass requires all three: every applicable dimension is at least 1; compliance and tone_fit are never 0; the total is at least 85% of the maximum available over the applicable dimensions.")
    lines.append("")
    lines.append("Return JSON only:")
    lines.append('{')
    lines.append('  "scores": { "voice": 0-2|"na", "tone_fit": 0-2|"na", "clarity": 0-2|"na", "terminology": 0-2|"na", "pattern_fit": 0-2|"na", "compliance": 0-2|"na", "accessibility": 0-2|"na" },')
    lines.append('  "total": "<points> of <maximum available>",')
    lines.append('  "pass": true|false,')
    lines.append('  "reasons": { "<dimension>": "one short reason for any score below 2" },')
    lines.append('  "fix": "one concrete change that would make it pass, quoting the slot, or null"')
    lines.append('}')
    print("\n".join(lines))
    return 0


if __name__ == "__main__":
    sys.exit(main(sys.argv[1:]))
