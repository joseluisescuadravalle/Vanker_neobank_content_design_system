"""
Run the golden set through the deterministic assertion layer.

Cases that carry an approved `context.candidate` are checked now (regression).
Cases without one need a model to generate a candidate first, and are skipped here unless
a generation run is passed in: `python run_golden.py --candidates generation-runs/<f>.jsonl`
gates the generated copy with the same checks, before any judge sees it.
A case with `expect_fail: true` is a negative test: it is OK precisely when it FAILS.
"""
import json
import assertions

CASES = "golden-set/cases.jsonl"


def load():
    with open(CASES, encoding="utf-8") as fh:
        return [json.loads(line) for line in fh if line.strip()]


def load_generated(argv):
    """Candidates a model wrote for the cases that ship without one."""
    if "--candidates" not in argv:
        return {}
    path = argv[argv.index("--candidates") + 1]
    with open(path, encoding="utf-8") as fh:
        rows = [json.loads(l) for l in fh if l.strip()]
    print("generated candidates from %s (%d)\n" % (path, len(rows)))
    return {r["id"]: r["candidate"] for r in rows}


def audit_declared_vs_applicable(cases):
    """Report cases that declare fewer checks than their surface would apply.

    The golden set runs the assertions each case declares in `must_pass`, so a check added
    to a surface later never re-tests older cases. That gap hid a real defect (a tooltip
    using an unexpanded acronym) until the judge found it. This makes it visible.
    """
    gaps = 0
    for c in cases:
        cand = c.get("context", {}).get("candidate")
        if cand is None or c.get("expect_fail"):
            continue
        applicable = assertions.checks_for(c.get("surface"))
        declared = set(c.get("must_pass") or [])
        undeclared = [a for a in applicable if a not in declared]
        if not undeclared:
            continue
        res = assertions.run(cand, undeclared, surface=c.get("surface"))
        failing = {k: v["message"] for k, v in res.items() if not v["passed"]}
        if failing:
            gaps += 1
            print(f"{'GAP':>22}  {c['id']}: would fail undeclared {failing}")
    print(f"\nDeclared-vs-applicable audit: {gaps} case(s) hiding a real failure.")
    return gaps


def main():
    import sys
    cases = load()
    if "--strict" in sys.argv:
        return audit_declared_vs_applicable(cases)
    generated = load_generated(sys.argv)
    run = skipped = ok = 0
    for c in cases:
        cand = c.get("context", {}).get("candidate")
        if cand is None:
            cand = generated.get(c["id"])
        if cand is None:
            skipped += 1
            print(f"skip  {c['id']}  (needs a model to generate)")
            continue
        run += 1
        # The surface must reach the checks: some of them are surface-aware (the ampersand
        # rule allows a tight label and rejects body copy).
        res = assertions.run(cand, c.get("must_pass"), surface=c.get("surface"))
        passed = all(v["passed"] for v in res.values()) if res else True
        case_ok = (not passed) if c.get("expect_fail") else passed
        if case_ok:
            ok += 1
            tag = ("PASS (correctly caught)" if c.get("expect_fail")
                   else ("PASS (generated)" if c["id"] in generated else "PASS"))
            print(f"{tag:>22}  {c['id']}")
        else:
            bad = {k: v["message"] for k, v in res.items() if not v["passed"]}
            print(f"{'FAIL':>22}  {c['id']}: {bad}")
    print(f"\nDeterministic layer: {ok}/{run} candidate cases OK "
          f"({skipped} need a model to generate first).")


if __name__ == "__main__":
    main()
