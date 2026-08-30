"""Check that every component and pattern file follows the system's shape.

The convention in CONTRIBUTING.md is only a convention until something reads it. This
verifies the parts that can be verified: the status line, a valid machine-readable block,
eval hooks, and that every relative cross-reference resolves.

    python check_structure.py
"""
import io
import json
import os
import re
import sys

ROOT = os.path.join(os.path.dirname(__file__) or ".", "..")
# Files that carry rules an agent must follow, so they carry the full shape.
SPEC_DIRS = ["components/library", "components/foundations", "patterns"]
# These are indexes, not specs.
SKIP = {"README.md"}


def spec_files():
    for d in SPEC_DIRS:
        path = os.path.join(ROOT, d)
        for name in sorted(os.listdir(path)):
            if name.endswith(".md") and name not in SKIP:
                yield os.path.join(d, name)


def check(rel):
    path = os.path.join(ROOT, rel)
    src = io.open(path, encoding="utf-8").read()
    problems = []
    if not re.search(r"^\*\*Status:", src, re.M):
        problems.append("no **Status:** line")
    blocks = re.findall(r"```json\n(.*?)\n```", src, re.S)
    if not blocks:
        problems.append("no machine-readable JSON block: it is what the agent and the copy checker consume")
    for i, b in enumerate(blocks, 1):
        try:
            json.loads(b)
        except Exception as exc:
            problems.append("JSON block %d does not parse: %s" % (i, exc))
    # Foundations are tokens, not copy rules: they carry a machine-readable block and no
    # eval hooks, because there is no string to check.
    if not rel.startswith("components/foundations"):
        if "## Eval hooks" not in src:
            problems.append("no '## Eval hooks' section: the rules restated as things that can be verified")
    if "## Accessibility" not in src and rel.startswith("components/library"):
        problems.append("no '## Accessibility' section")
    base = os.path.dirname(path)
    refs = re.findall(r"\]\(([^)#][^)]*\.md)\)", src) + [r for r in re.findall(r"`([\w./-]+\.md)`", src) if "/" in r]
    for ref in sorted(set(refs)):
        target = ref.lstrip("/") if ref.startswith("/") else os.path.join(base, ref)
        target = os.path.normpath(target if ref.startswith("/") is False else os.path.join(ROOT, ref.lstrip("/")))
        if not os.path.exists(target):
            problems.append("cross-reference does not resolve: %s" % ref)
    return problems


def main():
    total = 0
    for rel in spec_files():
        problems = check(rel)
        if problems:
            total += len(problems)
            print(rel)
            for p in problems:
                print("    " + p)
    if total:
        print("\n%d structural problem(s)." % total)
        return 1
    print("Structure: every component and pattern file carries the shape.")
    return 0


if __name__ == "__main__":
    sys.exit(main())
