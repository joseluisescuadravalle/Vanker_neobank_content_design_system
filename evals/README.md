# Evals

**Status: tooling, not customer-facing content.**

The evaluation suite for Vanker's content design system. It answers one question: does a
piece of copy generated with this system stay **on-brand and compliant**?

## Files

- `approach.md` — the strategy: the two eval layers, the golden set, and the loop. Read
  this first.
- `assertions.md` — the catalog of deterministic (code-checkable) rules.
- `assertions.py` — a runnable starter implementing the deterministic checks.
- `golden-set/` — the fixed set of test cases (`cases.jsonl`) with expected behavior.
- `rubric.md` — the LLM-as-judge scoring rubric for subjective quality.
- `judge-prompt.md` — the prompt template for the judge model.

## Where the rules come from

Every "Eval hooks" block across the system (in `../patterns/`, `../components/`, and
`../compliance/`) is a source of checks. `assertions.md` collects the deterministic ones;
`rubric.md` covers the ones that need judgment.

## Running the checks

- `python run_golden.py` runs the deterministic layer over the golden set.
- `python terms_sync.py` checks that `../terminology/banned-terms.md` and `assertions.py`
  still agree. Run both after any change to either.
