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
