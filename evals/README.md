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
  still agree.
- `python run_golden.py --strict` audits the gap between what a case declares and what its
  surface would apply.
- `python check_structure.py` checks that every component and pattern file carries the shape
  described in `../CONTRIBUTING.md`.
- `python check_examples.py` runs the surface-agnostic checks over the **approved examples in
  the documentation**, which the golden set never sees: a rule added in August can contradict
  an example written in July, and nobody re-reads 40 files.
- `python judge.py build` and `python judge.py score <run>` exercise the second layer.

Run all of them after any change.
