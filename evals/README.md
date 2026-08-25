# Evals

**Status: tooling, not customer-facing content.**

The evaluation suite for the system. It turns the rules in `/CLAUDE.md` and the
other layers into checks: does a generated string stay on-brand and compliant?

This is where the project connects to evaluation practice: assertions derived from
the `never` / `always` rules, a golden set of inputs with expected behavior, and a
rubric for an LLM-as-judge that scores on-brand and compliance.

Contents (to be added):
- `assertions.md` — rule-based pass/fail checks.
- `golden-set/` — input cases with expected output or expected behavior.
- `rubric.md` — LLM-as-judge scoring rubric.
