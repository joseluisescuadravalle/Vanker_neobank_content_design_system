"""
Run the golden set through the deterministic assertion layer.

Cases that carry an approved `context.candidate` are checked now (regression).
Cases without one need a model to generate a candidate first, and are skipped here.
A case with `expect_fail: true` is a negative test: it is OK precisely when it FAILS.
"""
import json
import assertions

CASES = "golden-set/cases.jsonl"


def load():
    with open(CASES, encoding="utf-8") as fh:
        return [json.loads(line) for line in fh if line.strip()]


def main():
    cases = load()
    run = skipped = ok = 0
    for c in cases:
        cand = c.get("context", {}).get("candidate")
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
            tag = "PASS (correctly caught)" if c.get("expect_fail") else "PASS"
            print(f"{tag:>22}  {c['id']}")
        else:
            bad = {k: v["message"] for k, v in res.items() if not v["passed"]}
            print(f"{'FAIL':>22}  {c['id']}: {bad}")
    print(f"\nDeterministic layer: {ok}/{run} candidate cases OK "
          f"({skipped} need a model to generate first).")


if __name__ == "__main__":
    main()
