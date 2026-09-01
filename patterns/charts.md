# Charts and spending breakdowns

**Status: normative (rules) + example (samples).**

The spending donut, the monthly bars, the balance line, the category list under them.

## A chart here is a claim about someone's money

Not a data visualization: **a claim**. Every simplification a chart makes — rounding,
grouping the tail into "Other", starting an axis above zero, sorting a payment into a
category — is an assertion about a person's own money that they cannot verify by looking at
the picture.

That is the difference from charting anything else, and every rule below comes from it:

> **The chart is never the source of truth. The numbers are, and they are always one tap
> away.**

## The numbers are always reachable

- **Every chart has its data as text**, in a list or a table on the same screen or one tap
  from it. Not a described summary: the figures (see `alt-text.md`).
- A person using a screen reader gets **the data**, not a sentence about the data.
- The total shown by the chart and the total in the list are the same number, or the copy
  says why they differ.

## What a chart may not do

- **Never truncate an axis.** A bar chart whose scale starts at 400 € turns a 5% change
  into a cliff. In a bank that is not a design shortcut, it is a misrepresentation of
  someone's finances.
- **Never group without a way in.** Collapsing the tail into "Other" is allowed only if
  "Other" opens and lists what is inside it. Otherwise we have hidden part of a person's
  money behind a word.
- **Never round silently.** If the chart rounds, the copy says so, and the parts still add
  up to the stated total.
- **Never animate figures into place.** Money does not count up (see `loading.md`).
- **Never compare a person with other customers** (see
  `../voice-and-tone/inclusive-language.md`).

## Categories are a guess, and they are labeled as one

Automatic categorization is inference. It is usually right and it is sometimes badly wrong,
and a person will act on "you spent 400 € on eating out" as though it were a fact we
checked.

- **Present a category as our reading, with a way to correct it**: "We sorted this as
  Groceries. Change category."
- **Never present a guessed category as a fact**, and never build a claim on top of one
  without saying it is built on a guess.
- A corrected category stays corrected, and the correction is acknowledged in one line.
- **An uncategorized payment says so** rather than being swept into "Other".

## The copy around the chart

- **Report, never grade.** "You spent 32% more than last month" is a fact. "You overspent"
  is a verdict, and it is banned (`../voice-and-tone/inclusive-language.md`).
- **Label an incomplete period.** The current month is not comparable with a full one: "so
  far this month", never a bare "this month" next to a completed one.
- **Name the baseline of every comparison.** "32% more than in August", not "32% more".
- **Amounts follow the money format**, and the axis labels follow
  `../terminology/numbers-and-dates.md`: written months, never numeric dates.
- No exclamation, no celebration of a fall in spending, no encouragement about a rise.

## When there is not enough data

- **Two or three points are a list, not a chart.** Below about five, show the numbers.
- **No data yet is an empty state**, not an empty chart (see `empty-states.md`): an axis
  with nothing on it looks like a failure.
- A partial period is drawn as partial, never extrapolated. A dotted projection is a
  prediction about someone's money and this system does not make one.

## Color and legibility

- **Categorical colors come from `../components/foundations/color.md`**, and the semantic
  ones keep their meaning: a category tinted `success` green reads as "good spending",
  which is a judgement nobody made.
- **Never color alone.** Each series is labeled directly, or the legend is text beside the
  value; money in and out keep the sign rule from
  `../components/library/transaction-row.md`.
- A value readout on a data point is a **value**, not a tooltip (`tooltip.md` does not
  apply), and it must be reachable without hover, because a phone has none.

## Accessibility

- The text alternative is the data, reachable and navigable; the chart image itself is
  decorative once the data is there.
- The chart is never the only route to a figure.
- Focus moves through the series or through a control that swaps the chart for its table.
- Color contrast between adjacent series meets 3:1, and no meaning rests on hue.

## Machine-readable spec

```json
{
  "charts": {
    "thesis": "a chart is a claim about someone's money; the numbers are the source of truth",
    "data-as-text": { "required": true, "same-screen-or-one-tap": true, "totals-match": true },
    "forbidden": {
      "truncated-axis": true,
      "grouping-without-a-way-in": true,
      "silent-rounding": true,
      "animated-figures": true,
      "comparison-with-other-customers": true,
      "projection": true
    },
    "categories": {
      "presented-as": "our reading, with a correction",
      "as-fact": false,
      "uncategorized-stated": true,
      "correction-persists": true
    },
    "copy": { "grades": false, "incomplete-period-labeled": true, "baseline-named": true, "exclamation": false },
    "sparse-data": { "below-points": 5, "show": "numbers", "no-data": "empty state" },
    "color": { "categorical-from": "foundations/color.md", "semantic-as-category": false, "color-alone": false },
    "a11y": { "text-alternative": "the data", "sole-route": false, "series-contrast": 3.0, "hover-required": false }
  }
}
```

## Eval hooks

- Every chart's figures are available as text, and the totals agree with the chart.
- No axis is truncated, no grouping hides money without a way in, and no rounding is silent.
- A category is presented as our reading with a way to correct it, never as a fact.
- An uncategorized payment says so rather than being swept into "Other".
- The copy reports and never grades; an incomplete period is labeled; every comparison names
  its baseline.
- Fewer than about five points are shown as numbers, and no data is an empty state.
- No semantic color is used as a category, and no series depends on color alone.
