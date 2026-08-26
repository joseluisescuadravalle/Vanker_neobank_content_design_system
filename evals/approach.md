# Evals: approach

**Status: tooling, not customer-facing content.**

## What we evaluate

Whether copy produced with this system follows the voice, tone, terminology, patterns, and
compliance rules. The unit under test is a **generated string for a given surface** (an
error, a CTA, an onboarding step, a risk warning), produced by a model using this
repository as context.

## Two layers

| Layer | Catches | How | Cost |
| --- | --- | --- | --- |
| **Deterministic assertions** | Objective, black-and-white violations | Code, `assertions.py` | Cheap, instant, fully reliable |
| **LLM-as-judge** | Subjective quality | A model scores against `rubric.md` | Slower, needs a good rubric |

Rule of thumb: if a rule can be checked by code, it is an **assertion**; if it needs
judgment ("is the tone right?", "is this warning adequate?"), it is for the **judge**. Run
the deterministic layer first as a cheap gate, then the judge for nuance.

## The golden set

A fixed, curated set of representative tasks (`golden-set/cases.jsonl`), each with the
expected behavior. Running the model over it, with both layers, gives a **pass rate** you
can track. It is the regression net: when you change `CLAUDE.md` or a pattern, re-run it to
see what improved and what broke.

## The loop

Generate (model + this system as context) -> assert (code) -> judge (model + rubric) ->
if it fails, fix the **system** (the rule, not the single output) -> re-run the golden set.
The point of evals is to improve the system, not to patch one string.

## Metrics

- Assertion pass rate, per assertion and per surface.
- Judge score per rubric dimension, and overall.
- Both tracked across versions of the system, so quality is measurable, not a matter of
  opinion.
