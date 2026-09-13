# Handoff for Claude Code: port the 7 dark-pattern checks to `src/lib/assertions.ts`

Date: 13 September 2026. The system side is done in `Content_Design_System_AI`:
`compliance/dark-patterns.md` (the rules), `evals/assertions.py` (reference
implementation), `evals/assertions.md` (catalog), 19 golden cases (`dark.*`), `rules.json`
(69 checks, new lists and patterns) and the rebuilt skill. All seven gates are green.

This note carries what the app must port to keep parity. Read `rules.json` first: every
word list and every regex below is already there, so the TypeScript holds no copy of its own.

## New checks (7)

| ID | Level | Reads from `rules.json` |
| --- | --- | --- |
| `A-CONFIRMSHAME` | slot | `lists.decline_labels`, `patterns.decline_first_person`, `patterns.decline_cost_or_loss` |
| `A-SCARCITY` | slot, universal | `lists.scarcity_terms` (phrase template: `\b` + words joined by `\s+` + `\b`; `{n}` becomes `\d+`), `patterns.countdown` |
| `A-DOUBLE-NEGATIVE` | slot | `patterns.negator` (fail when 2 or more matches) |
| `A-PRICE-ASTERISK` | slot | `patterns.asterisk_price`; `patterns.from_price` per sentence, passes if `patterns.price_condition` matches the same sentence |
| `A-SOCIAL-PROOF` | slot, universal | `lists.social_proof_terms` |
| `A-GUILT` | slot, universal, skipped when the surface is in `lists.guilt_exempt_surfaces` | `lists.guilt_terms` |
| `A-DECLINE-PRESENT` | screen | `lists.decline_labels`: passes if any non-empty line of the joined screen equals one of them (case-insensitive, trimmed) |

Universal means: appended to every surface list, like `A-NO-BANNED`. `surfaces` in
`rules.json` already carries them, so if the app applies checks from `surfaces`, nothing to
do beyond implementing the functions.

## New surfaces (2)

- `decline-cta`: `A-CONFIRMSHAME`, `A-CTA`, `A-NO-EMOJI`, `A-CASE` plus universal. In the
  checker, the **second CTA slot** of an offer or consent surface should run as
  `decline-cta`, not as `cta`.
- `offer-screen`: body checks plus `A-DECLINE-PRESENT`. Screen level, like
  `system-error-screen`: join title, body and both CTAs with line breaks, buttons last,
  one per line, and run the screen checks on the joined text.

Owners (for the gallery and "which file governs this"): `decline-cta` →
`compliance/dark-patterns.md`, `patterns/ctas.md`; `offer-screen` →
`compliance/dark-patterns.md`.

## Messages (keep the wording; it names the pattern, which is what teaches)

- `A-CONFIRMSHAME`: `'{label}' is not a decline label ({first person} and {a cost or a loss} in the decline: confirmshaming); use 'Not now', 'Cancel', 'Back', 'Skip'`
- `A-SCARCITY`: `false scarcity: {terms}; a real deadline is a date, written plainly`
- `A-DOUBLE-NEGATIVE`: `double negative ({negators}); nobody can tell what the unchecked state means. Write what happens when it is selected`
- `A-PRICE-ASTERISK`: `'{match}': the asterisk is where the cost hides; state the condition in the sentence` / `'{from …}' with no condition in the same sentence; say what the price depends on, or give the exact amount`
- `A-SOCIAL-PROOF`: `unsourced social proof: {terms}; a number with its source may be used, a crowd without one may not`
- `A-GUILT`: `guilt or fear framing: {terms}; state the benefit or the fact and let the person decide`
- `A-DECLINE-PRESENT`: `no way to say no: the screen asks for an acceptance and carries no decline; add 'Not now' or 'Cancel' beside the primary, at the same cost in taps`

## Acceptance (all are golden cases, `dark.*` in `evals/golden-set/cases.jsonl`)

| Surface | Candidate | Expected |
| --- | --- | --- |
| decline-cta | `Not now` | pass |
| decline-cta | `No, I'll keep paying fees` | fail A-CONFIRMSHAME (and A-CTA) |
| decline-cta | `Keep paying fees` | fail A-CONFIRMSHAME only (3 words pass A-CTA) |
| banner | `The 2% rate on Spaces applies until 31 October 2026.` | pass |
| banner | `Only 3 spots left at this rate.` | fail A-SCARCITY |
| banner | `Offer ends in 04:59.` | fail A-SCARCITY |
| banner | `Sent now, it arrives today. After 22:00 it arrives the next working day.` | pass (a clock time is not a countdown) |
| checkbox | `Send me offers from Vanker by email` | pass |
| checkbox | `Untick this box to not receive offers` | fail A-DOUBLE-NEGATIVE |
| banner | `Plus costs 4 € a month and includes 5 free international transfers.` | pass |
| banner | `Free* international transfers.` | fail A-PRICE-ASTERISK |
| banner | `From 0,99 € a month.` | fail A-PRICE-ASTERISK |
| banner | `From 0,99 € a month if you pay yearly.` | pass |
| chart-copy | `Your spending went from 480 € to 505 €.` | pass (a range, not a floor) |
| banner | `Join thousands who already switched to Plus.` | fail A-SOCIAL-PROOF |
| onboarding-step | `Don't let your savings lose value.` | fail A-GUILT |
| security | `Someone tried to sign in from a new device. If it was not you, lock your card now.` | pass (exempt surface) |
| offer-screen | `Plus for 4 € a month` / body / `Upgrade` / `Not now` | pass |
| offer-screen | same without `Not now` | fail A-DECLINE-PRESENT, card under the second button |

Amounts above carry a no-break space before `€` (U+00A0), as everywhere in the system.

## UI

- No new panel: the seven checks render as the other 62 do (red card under the slot, FAIL +
  check, Flagged, Reason, Suggestion).
- `A-DECLINE-PRESENT` (revised 13/09, after the first port): the second button of
  `offer-screen` is optional in the form; the check runs only when that slot is empty, and
  its card renders **under the second button slot**, where the defect is fixed, not under
  "Whole-screen checks". When the slot is filled, `A-CONFIRMSHAME` owns the judgment.
  Done in the app in `560dee0` (`SLOT_OWNED` in `App.tsx`, shared `ScreenFailCard`).
- The gallery needs at least one `offer-screen` surface (an upgrade sheet: title, body,
  primary, tertiary) so the demo can load a bad example and watch the three screen and
  slot checks fire together.
- The behavioral lens (opt-in review, unlocked after the editorial review meets the rubric)
  is a later phase and is **not** part of this handoff.

## Known divergence to keep in mind

The app lists the dimension "structure" where the rubric says "pattern fit" (unchanged,
still open).

## Addendum, 13 September (evening): `patterns/offers.md` now exists

The offer surface has its own pattern file. Two things for the app:

- The gallery example title changes from "Upgrade to Plus" to "Plus for 4 € a month"
  (with the no-break space): `offers.md` rule 1 puts the price in the title so the first
  thing seen is the real cost. Primary "Upgrade", decline "Not now", body unchanged.
- Owners for `offer-screen` are now `patterns/offers.md` and `compliance/dark-patterns.md`;
  for `decline-cta`, `patterns/offers.md`, `compliance/dark-patterns.md`, `patterns/ctas.md`
  (see `rules.json` / `owners.json` after the next build).
