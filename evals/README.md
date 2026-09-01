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
- `python export_rules.py --check` fails when `rules.json` is stale. That file is the
  machine-readable export of every rule that is data (word lists, surface map, patterns),
  and the desktop app's copy checker reads it instead of holding its own copy. A rule added
  here that never reaches `rules.json` is a rule the app does not enforce.
- `python check_examples.py` runs the surface-agnostic checks over the **approved examples in
  the documentation**, which the golden set never sees: a rule added in August can contradict
  an example written in July, and nobody re-reads 40 files.
- `python judge.py generate` writes the prompts for the cases that ship **without** a
  candidate: those are a task, not a sample, and a model has to write the copy first. Its
  answers go into `generation-runs/<date>-<model>.jsonl`.
- `python judge.py build --candidates generation-runs/<file>.jsonl` then judges them
  alongside the rest, and `python judge.py score <run>` aggregates the verdicts.

**One case never gets a candidate.** `statements.none-yet` is the permanent generation
slot: if every case carries approved copy, `judge.py generate` has nothing to do and the
whole generation path rots without a single test going red. Approved copy for that screen,
if it is ever needed, goes in a separate case with its own id.

**The generator and the judge must not be the same run.** A model that just wrote the copy
is not a neutral reviewer of it, and a model that helped write the system has already read
the answer. `generation-runs/2026-09-01-claude-opus.jsonl` is exactly that case and says so
in every line: it proves the pipeline runs end to end, it does not measure how well a model
writes Vanker copy. For a real number, generate in a fresh session with a model that has
only the reference, and judge with a different one.

That run exists: `generation-runs/2026-09-01-blind-generation.jsonl` and
`judge-runs/2026-09-01-blind-judge.jsonl`. Two separate fresh contexts, each given one
prompt file and told not to open the golden set. The copy passed the deterministic gate and
the judge scored it 2 on every applicable dimension. Blind on context, not on model: both
runs are the same model family, so it measures whether the system alone is enough to write
and to grade, not whether a different vendor would agree.

Run all of them after any change.
