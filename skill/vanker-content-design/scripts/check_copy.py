"""Run Vanker's deterministic checks on copy before it is delivered.

Same code as evals/assertions.py in the repository (copied here by evals/build_skill.py),
so a string that passes here passes the golden set's deterministic layer.

    python3 check_copy.py --surface cta "Try again"
    python3 check_copy.py --surface system-error-screen "We could not ... " 
    python3 check_copy.py --file screen.txt
    cat screen.txt | python3 check_copy.py --file -

The file format is the skill's delivery format: one slot per line, `slot (surface): text`,
with a multi-paragraph body continuing on the following lines until the next slot. Lines
starting with `Screen:` and blank lines are ignored.

Exit status is 1 when any check fails. A clean run means "no rule broken", not "the copy is
good": read the screen back as one thing before delivering it.
"""
import os
import re
import sys

sys.path.insert(0, os.path.dirname(os.path.abspath(__file__)))
import assertions  # noqa: E402

SLOT = re.compile(r"^([A-Za-z0-9_-]+)\s*\(([A-Za-z0-9_-]+)\)\s*:\s?(.*)$")


def parse(text):
    slots = []
    for line in text.splitlines():
        if line.startswith("Screen:") or line.startswith("Editorial review:"):
            continue
        m = SLOT.match(line)
        if m:
            slots.append([m.group(1), m.group(2), m.group(3)])
        elif slots:
            # Blank lines are kept: a paragraph break is part of the copy, and the checks
            # read the shape of a block (one fact per paragraph).
            slots[-1][2] += "\n" + line
        elif not line.strip():
            continue
        else:
            raise SystemExit("first line is not a slot: %r (expected `slot (surface): text`)" % line)
    return [(s, sf, t.strip()) for s, sf, t in slots]


def check(slot, surface, text):
    surface_l = surface.lower()
    known = surface_l in assertions.SURFACE_CHECKS
    results = assertions.run(text, surface=surface_l)
    failed = {k: v["message"] for k, v in results.items() if not v["passed"]}
    head = "%s (%s)" % (slot, surface)
    if not known:
        print("%-28s  ?     surface not in the system; body checks applied" % head)
    if failed:
        print("%-28s  FAIL  %d of %d checks" % (head, len(failed), len(results)))
        for k, msg in failed.items():
            print("%-28s        %s: %s" % ("", k, msg))
    else:
        print("%-28s  ok    %d checks" % (head, len(results)))
    return not failed


def main(argv):
    if "--file" in argv:
        path = argv[argv.index("--file") + 1]
        text = sys.stdin.read() if path == "-" else open(path, encoding="utf-8").read()
        slots = parse(text)
    elif "--surface" in argv:
        i = argv.index("--surface")
        surface = argv[i + 1]
        rest = [a for j, a in enumerate(argv) if j not in (i, i + 1) and not a.startswith("--")]
        text = " ".join(rest) if rest else sys.stdin.read()
        slots = [("string", surface, text.strip())]
    else:
        print(__doc__)
        return 2
    ok = all([check(*s) for s in slots])
    print()
    if ok:
        print("No rule broken (%d slot%s). Meaning not evaluated: read the screen back before delivering." % (len(slots), "" if len(slots) == 1 else "s"))
        return 0
    print("Fix the failures above and run again. Do not deliver a failing string.")
    return 1


if __name__ == "__main__":
    sys.exit(main(sys.argv[1:]))
