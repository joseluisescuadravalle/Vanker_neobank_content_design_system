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
- `expected` — a short note on the expected behavior. **For humans only: it is never put
  into the judge prompt**, because handing the judge the answer key is asking it to mark
  its own homework.
- `expect_fail` — a negative test for the **deterministic** layer: the case is OK precisely
  when the assertions catch it.
- `expect_judge_fail` — code passes it and the **judge** must reject it. This is the class
  of case the second layer exists for: copy that is impeccably formed and still wrong (a
  push that shows the balance, a screen that asks someone to sit and wait for their money).

Grow the set as new surfaces and edge cases appear. Keep it small enough to run often and
representative enough to catch regressions.

## Running it

`python run_golden.py --strict` audits the gap between what a case declares and what its
surface would apply; it is how a check added later reaches the cases written before it.

`python run_golden.py` (from `evals/`) runs the deterministic layer over every case that
carries an approved `context.candidate`, and skips the ones that still need a model to
generate a candidate. A case with `expect_fail: true` is a **negative test**: it is OK
precisely when the checks catch it. The LLM-as-judge layer (`rubric.md`) runs separately.
