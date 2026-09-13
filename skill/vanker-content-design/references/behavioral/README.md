# Behavioral design

**Status: normative (rules) + example (samples).**

The persuasion Vanker allows. This folder is the second half of the behavioral layer: the
first half, the prohibitions, lives in `../compliance/dark-patterns.md` and is checked by
code. What is here is judgment: which bias may be used to help the person, on which
pattern, and where it is forbidden even when it would work.

**The thesis: a nudge is legitimate only when the person would thank you for it after
seeing how it was done.** That test excludes every dark pattern in one line, and it admits
a short list of biases that a bank can use on the person's side: a protective default, a
visible goal, a gain frame, a sensible preset, money kept apart by purpose, an extra step
before the irreversible, a fixed day and amount, and a good ending.

## Files

- `biases.md`: the eight biases Vanker may use, one card each: the mechanism, where it
  helps, where it turns into a dark pattern, a good and a bad Vanker example, and what
  watches it.
- `lens.md`: the behavioral lens as a review. The target behaviors an author may declare
  for a pattern, the rubric the behavioral reviewer scores, and how the review is run.

## Where it sits

In the precedence of `/CLAUDE.md` this folder is layer 5, below voice and above patterns:
a nudge never breaks compliance, terminology or voice, and the patterns implement it. Each
file in `../patterns/` carries a **Behavioral lens** block that says whether the lens
applies to that pattern, which biases it may use, and which are forbidden there. A pattern
that says "does not apply" means exactly that, and the reviewer scores it `na`.

## Forbidden zones

Three products get a neutral frame by regulation, whatever the bias: **investment**
(MiFID II), **credit** (CCD2) and **crypto-assets** (MiCA). On those screens the lens is
off: no default that favors the product, no gain frame, no preset that anchors upward, no
progress bar toward a purchase. `../compliance/risk-warnings.md` owns the wording.
Identity verification (KYC, Know Your Customer) is a fourth zone: nothing accelerates it.

## How the review is ordered

Rules first (the deterministic checks), then the editorial review, then this lens. A copy
that has not met the rubric is not ready for a nudge; the behavioral review unlocks only
when the editorial review meets the rubric. See `lens.md`.
