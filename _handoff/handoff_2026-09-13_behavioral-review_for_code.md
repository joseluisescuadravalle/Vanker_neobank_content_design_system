# Handoff for Claude Code: the Behavioral review panel

Date: 13 September 2026 (evening). The system side is committed in
`Content_Design_System_AI`: `behavioral/README.md`, `behavioral/biases.md`,
`behavioral/lens.md`, `patterns/offers.md`, and a **Behavioral lens** block in every file
of `patterns/`. The Claude skill already runs the lens on an explicit ask, and it was
verified end to end on a success screen. This note carries what the app must add.

Read first: `behavioral/lens.md` (the review), then the Behavioral lens block of two or
three pattern files (`patterns/success.md`, `patterns/offers.md`, `patterns/errors.md` for
a "does not apply").

## What it is

A third review panel in the Review column, **below** Editorial review, called
**Behavioral review**. It is the third step of a ladder:

1. Rules (the 69 deterministic checks): correct.
2. Editorial review: good.
3. Behavioral review: effective, and only with the person's interest in view.

## Gating (both conditions, in this order)

- Grey with "Available once the editorial review meets the rubric" until the editorial
  review reports "Meets the rubric" (the existing 85% threshold). Passing the rules is not
  enough.
- Once unlocked, it still does not run until the author picks a **target behavior**. The
  panel shows a select with the behaviors the pattern allows and the text "Pick what this
  screen is for". No behavior, no review.
- If the pattern's Behavioral lens block says **does not apply**, the panel says so in one
  line ("The behavioral lens does not apply to {pattern}: {reason}") and offers nothing
  else. The reason is the sentence in the block.
- Any change to the copy invalidates the panel, as it already does for the editorial
  review and the rewrite.

## Inputs

- `behavioral/lens.md`: the list of target behaviors (7 ids), the 9 measures, the pass
  rule, the output order, the prompt skeleton.
- The Behavioral lens block of the pattern file that owns the surface (owners are in
  `rules.json` / `owners.json`): which behaviors apply, which biases are allowed, which
  are forbidden, which measures the reviewer scores. Parse the block's "Target behavior(s)"
  line to fill the select; if the block starts with "Does not apply", the surface is out.
- `behavioral/biases.md`: reference for the reviewer prompt.
- `compliance/dark-patterns.md`: reference for the reviewer prompt.

The lens block is prose, not JSON, on purpose: it is read by people and by the model. The
app needs three things from it, and each has a fixed shape:

- First bullet starts with `- **Applies**` or `- **Does not apply**`.
- On "Applies", the same bullet carries `Target behavior:` or `Target behaviors:` followed
  by backticked ids (`start-saving`, ...).
- The bullet `- **What the reviewer scores.**` lists the measures in quotes; everything
  else is `na`.

## The reviewer call

Same mechanism as the editorial review (a model call with the reference and the copy,
never the same run that wrote the copy). Build the prompt from the skeleton in `lens.md`:
surface, pattern, declared behavior, the copy, and the four references. Ask for:

1. The 9 measures, each 0, 1, 2 or `na`.
2. The verdict line, verbatim format: `Behavioral lens: pass, N of M applicable, against 85%`
   (or `fail`).
3. "What the behavioral reviewer would change": judgment, never rewritten copy. If the
   model returns copy, drop it and show a note ("The reviewer proposed copy; the lens
   does not rewrite. Use Rewrite, then run the reviews again.").

Pass rule (compute it in the app, do not trust the model's arithmetic): every applicable
measure at least 1, "Uses only allowed biases" equal to 2, total at least 85% of the
maximum available for the applicable measures.

## UI

- Panel title: **Behavioral review**. Under it, the select "What is this screen for?"
  with the allowed behaviors, labels from `lens.md` (id in a smaller type).
- Button: **Review the nudge** (verb, 3 words, as every CTA in the app).
- Output, in this order: 9 meters 0 to 2 in the same style as the editorial ones, with
  `na` rendered as a muted "not applicable"; the verdict line; the block **What the
  behavioral reviewer would change**.
- No "Use this copy" button on this panel: it never produces copy.
- A short line under the title, always visible: "Runs after the editorial review. It judges
  whether the copy serves the behavior you declare, with only the biases the pattern
  allows." (Normative wording; keep it.)

## The Offer example in the gallery

The title changes from "Upgrade to Plus" to "Plus for 4 € a month" (no-break space before
€): `patterns/offers.md` rule 1 puts the price in the title. Primary "Upgrade", decline
"Not now", body unchanged. This is the natural demo for the panel: target behavior
`decide-freely`, the only pattern where the lens and the dark-pattern checks meet.

## Acceptance

| Case | Expected |
| --- | --- |
| Rules pass, editorial not run | Panel grey, "Available once the editorial review meets the rubric" |
| Editorial meets the rubric, no behavior picked | Panel unlocked, select shown, no review yet |
| Surface `system-error-screen` | "The behavioral lens does not apply to system errors: {reason}" |
| Offer example, behavior `decide-freely` | 4 measures scored, 5 `na`, verdict line, "would change" block |
| Copy edited after a review | Panel back to its unlocked state; editorial invalidated too |
| Reviewer returns rewritten copy | Copy dropped, note shown |

## Out of scope

- The home card "07 Behavioral design": later, when the section is complete and this panel
  is in.
- The `success` surface gap: the index has no `success-title` / `success-body`; the skill
  used `confirmation`. Separate cleanup, not this handoff.
