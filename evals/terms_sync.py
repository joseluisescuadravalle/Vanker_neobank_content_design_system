"""Keep terminology/banned-terms.md and assertions.py in sync.

The markdown file is the source of truth; this script fails if a documented term is not
implemented, or if an implemented term is not documented. Run it from evals/.
"""
import io
import os
import re
import sys

import assertions

DOC = os.path.join(os.path.dirname(__file__), "..", "terminology", "banned-terms.md")

# Documented rules that a word list cannot express; each has its own logic in assertions.py.
NOT_A_WORD_LIST = {"login / log-in", "& in body copy"}


def documented_terms(path=DOC):
    terms = []
    for line in io.open(path, encoding="utf-8"):
        # The closing section documents how the non-list rules are checked, not more terms.
        if line.startswith("## Keeping this file and the checks in sync"):
            break
        if not line.startswith("| ") or line.startswith("| ---") or line.startswith("| Avoid"):
            continue
        cell = line.split("|")[1].strip()
        for t in cell.split(","):
            t = re.sub(r"\(.*?\)", "", t)
            t = re.sub(r"`[^`]*`", "", t).strip(" .").lower()
            if t and t not in {"avoid", "rule"}:
                terms.append(t)
    return terms


def main():
    doc = documented_terms()
    impl = {t.lower() for t in assertions.BANNED_TERMS}
    # "do not miss out" is implemented as the narrower "miss out", which also catches "don't".
    aliases = {"do not miss out": "miss out"}
    missing, extra = [], []
    for t in doc:
        if t in NOT_A_WORD_LIST:
            continue
        if aliases.get(t, t) not in impl:
            missing.append(t)
    documented = {aliases.get(t, t) for t in doc} | NOT_A_WORD_LIST
    for t in sorted(impl):
        if t not in documented:
            extra.append(t)

    for t in missing:
        print("MISSING in assertions.py: " + t)
    for t in extra:
        print("UNDOCUMENTED in banned-terms.md: " + t)
    if missing or extra:
        print("\n%d documented, %d implemented, %d difference(s)." % (len(set(doc)), len(impl), len(missing) + len(extra)))
        return 1
    print("In sync: %d documented terms, %d implemented." % (len(set(doc)), len(impl)))
    return 0


if __name__ == "__main__":
    sys.exit(main())
