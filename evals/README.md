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
- `python judge.py generate` writes the prompts for the cases that ship **without** a
  candidate: those are a task, not a sample, and a model has to write the copy first. Its
  answers go into `generation-runs/<date>-<model>.jsonl`.
- `python judge.py build --candidates generation-runs/<file>.jsonl` then judges them
  alongside the rest, and `python judge.py score <run>` aggregates the verdicts.

**The generator and the judge must not be the same run.** A model that just wrote the copy
is not a neutral reviewer of it, and a model that helped write the system has already read
the answer. `generation-runs/2026-09-01-claude-opus.jsonl` is exactly that case and says so
in every line: it proves the pipeline runs end to end, it does not measure how well a model
writes Vanker copy. For a real number, generate in a fresh session with a model that has
only the reference, and judge with a different one.

Run all of them after any change.
