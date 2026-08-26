# Golden set

**Status: tooling.**

The fixed set of representative tasks the system is measured against. Each line in
`cases.jsonl` is one case:

- `id` — unique name.
- `surface` — the component or pattern under test (error, cta, confirmation, ...).
- `task` — what the model is asked to write.
- `context` — the situation and any variables.
- `must_pass` — deterministic assertion IDs (from `../assertions.md`) that must all pass.
- `judge` — whether to run the LLM-as-judge (`rubric.md`) on this case.
- `expected` — a short note on the expected behavior (for humans; not scored directly).

Grow the set as new surfaces and edge cases appear. Keep it small enough to run often and
representative enough to catch regressions.

## Running it

`python run_golden.py` (from `evals/`) runs the deterministic layer over every case that
carries an approved `context.candidate`, and skips the ones that still need a model to
generate a candidate. A case with `expect_fail: true` is a **negative test**: it is OK
precisely when the checks catch it. The LLM-as-judge layer (`rubric.md`) runs separately.
