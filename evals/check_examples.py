"""Run the deterministic checks over the approved examples inside the documentation.

The golden set only holds copy someone chose to put in it. The documentation holds hundreds
of approved examples that nobody re-reads when a rule changes, so a rule added in August can
silently contradict an example written in July. This script closes that gap: it extracts the
quoted copy that the docs present as approved and runs the surface-agnostic checks over it.

Counter-examples ("Not:", "Never", tables of what to avoid) are skipped, as are fenced code
blocks. Anything the checks flag is either a doc to fix or an entry for ALLOW below, with a
reason. Run it from evals/: python check_examples.py
"""
import io
import os
import re
import sys

import assertions

ROOT = os.path.join(os.path.dirname(os.path.abspath(__file__)), "..")
DIRS = ["components", "patterns", "terminology", "voice-and-tone", "compliance"]

# Checks that need no surface to be meaningful. Surface-specific rules (CTA length, toast
# punctuation, field-error shape) are not run here: the docs do not say which surface each
# quoted string belongs to, and guessing produces noise instead of findings.
CHECKS = ["A-NO-BANNED", "A-NO-CLAIMS", "A-INCLUSIVE", "A-REPEATED-CHARS", "A-EURO-FORMAT"]

# A line, a block, or a section that presents copy as wrong. Its quoted strings are meant
# to fail, so extracting them would report the documentation for documenting the rule.
COUNTER = re.compile(
    r"\*\*Not:?\*\*|\*\*Avoid|\*\*Never|\*\*No:\*\*|\*\*Wrong|\bnever\b|\bnot\b|\bno\b|"
    r"\bnothing\b|\bavoid\b|\binstead of\b|\brather than\b|\bbanned\b|\bwrong\b|"
    r"\bfails?\b|\brejects?\b|\bbad\b|\bprohibit|\bunevidenced\b|\bfiller\b|❌",
    re.IGNORECASE,
)
# "Not this", "What not to write": a block of counter-examples that runs to the next heading.
COUNTER_BLOCK = re.compile(r"^\s*[*_>-]*\s*(not this|not these|never this|what not to write|"
                           r"avoid|do not write)\b", re.IGNORECASE)
COUNTER_HEADING = re.compile(r"\b(not|never|avoid|banned|wrong|prohibit|noises)\b", re.IGNORECASE)
# A catalog of forbidden words quotes them on every line; checking it against itself is noise.
SKIP_FILES = {os.path.join("terminology", "banned-terms.md")}
# A quoted fragment that IS a forbidden term is a citation of the rule, not copy using it.
CITED = ({t.lower() for t in assertions.BANNED_TERMS}
         | {c.lower() for c in assertions.PROHIBITED_CLAIMS}
         | {t.lower() for t in assertions.NOT_INCLUSIVE})

QUOTED = re.compile(r'"([^"\n]{3,200})"')

# Approved examples that a surface-agnostic check flags for a reason that does not apply.
# Each entry is (fragment of the string, reason). Keep this list short: an entry is a
# statement that the check is right in general and wrong here, and it needs to be true.
ALLOW = [
    ("&", "an ampersand is allowed in a tight label; this check runs without a surface"),
]


def allowed(text):
    for frag, _reason in ALLOW:
        if frag in text:
            return True
    return False


def main():
    findings = 0
    checked = 0
    for d in DIRS:
        base = os.path.join(ROOT, d)
        for root, _dirs, files in os.walk(base):
            for f in sorted(files):
                if not f.endswith(".md"):
                    continue
                path = os.path.join(root, f)
                rel = os.path.relpath(path, ROOT)
                if rel in SKIP_FILES:
                    continue
                fenced = False
                counter_block = False
                heading = ""
                for n, line in enumerate(io.open(path, encoding="utf-8"), 1):
                    stripped = line.lstrip()
                    if stripped.startswith("```"):
                        fenced = not fenced
                        continue
                    if fenced:
                        continue
                    if stripped.startswith("#"):
                        heading = stripped
                        counter_block = False
                        continue
                    if COUNTER_BLOCK.match(line):
                        counter_block = True
                        continue
                    if counter_block or COUNTER_HEADING.search(heading) or COUNTER.search(line):
                        continue
                    for m in QUOTED.finditer(line):
                        text = m.group(1).strip()
                        if not re.search(r"[A-Za-z]", text) or allowed(text):
                            continue
                        if text.lower().strip(".,;:") in CITED:
                            continue
                        checked += 1
                        for cid in CHECKS:
                            ok, msg = assertions.REGISTRY[cid](text, None)
                            if not ok:
                                findings += 1
                                print("%s:%d  [%s] %s" % (rel, n, cid, msg))
                                print('          "%s"' % text)
    print("")
    if findings:
        print("%d approved example(s) contradict a current rule, out of %d checked."
              % (findings, checked))
        return 1
    print("Approved examples: %d checked, none contradicts a current rule." % checked)
    return 0


if __name__ == "__main__":
    sys.exit(main())
