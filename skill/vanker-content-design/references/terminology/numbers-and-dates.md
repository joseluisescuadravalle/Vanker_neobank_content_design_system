# Numbers and dates

**Status: normative. Always applied.**

How Vanker writes every figure that is not money. The money format itself lives in
`glossary.md`; how the amount input behaves while someone types is in
`../components/library/amount-input.md`.

## The rule that surprises people

Vanker writes **English text with European numbers**. `2.540,75 €`, `1 September 2026`,
`0,5%`. This is deliberate, not an oversight: the product is written in English for a
euro-area audience, and the figures follow the convention its customers read on their bank
statements, their invoices, and their card terminals. An agent that "corrects" the numbers
to American convention is introducing a bug, not fixing one.

## Numbers

- **Digits in body copy and instructions**: "3 steps", not "three steps". Digits are easier
  to scan, and a person skimming reads them first.
- **Thousands take a dot**: `2.540`. Decimals take a comma.
- **Never abbreviate a figure**: no `2,5k`, no `1.2M`, no `bn`. A person's money is never
  rounded into shorthand.
- **Percentages have no space and take a comma**: `0,5%`. A rate always says what it applies
  to and over what period: "0,5% a year", never a bare number.
- **Never round money in copy**, and never present a rounded figure as exact. If a figure is
  approximate, the word "about" carries it and the exact one is available.
- **Counts agree with their noun**: "1 payment", "2 payments". Never "1 payment(s)" and
  never "payment(s)": if the count can be one, the sentence handles both.
- **Zero is a fact, not an absence**: "No payments yet" reads better than "0 payments", but
  a figure that is genuinely zero is shown as `0 €`, never hidden or left blank.
- **Ordinals stay out of dates** ("1 September", not "1st September") and are fine in steps
  ("Step 2 of 3").
- **Masked identifiers** keep their last digits and nothing else: `···· 4321`, `+34 ··· ···
  123` (see `A-MASK` and `../compliance/data-privacy.md`).

## Dates

- **The format is day month year, written out**: `1 September 2026`. No comma, no ordinal.
- **Never a numeric date in copy.** `03/04/2026` is 3 April to a European reader and 4 March
  to an American one, and neither of them knows which one we meant. Numeric dates are for
  format placeholders (`DD/MM/YYYY`) and data tables only.
- **Never month-first**: not "September 1, 2026".
- **"Today" is the only relative date.** Not "Yesterday", not "Tomorrow": a day that is not
  today shows its concrete date (see `../components/library/transaction-row.md`).
- **Anything with a consequence gets an absolute date.** "Your payment arrives on 4
  September" — never "in 3 days", which the person has to compute, and which is wrong the
  moment they read it a day later. Relative time is allowed only beside a timestamp that is
  already on the screen.

## Times

- **12-hour with a space and lowercase am/pm**: `2:32 pm`, `9:00 am`.
- **Show the time when the moment matters** (a transaction, a cutoff, a login), and pair it
  with the date when the day is not obvious.
- **A cutoff states its time zone**, or is shown in the person's own time and says so. A
  payment deadline that is ambiguous by an hour is a payment that misses it.

## Durations and waits

- **Ranges use "to"**: "3 to 5 working days" (see `capitalization-and-punctuation.md`).
- **Say working days or calendar days.** They are different, and in a payment the difference
  is a weekend. "3 to 5 working days", never a bare "3 to 5 days" for anything that depends
  on a bank being open.
- **A duration is only given when it is measured**, and always as a range: "about 2
  minutes". Never "soon", "shortly", "in a moment", or "in no time" (see
  `../patterns/loading.md`).
- **Never promise a date we cannot keep.** A range from real data, or nothing.

## Eval hooks

- Figures follow the European convention even though the text is English.
- No numeric dates, no ordinals in dates, and no month-first dates in copy.
- "Yesterday" and "Tomorrow" do not appear; only "Today" is relative.
- Anything with a consequence carries an absolute date rather than "in 3 days".
- No abbreviated figures (`2,5k`, `1.2M`) and no "(s)" plurals.
- A percentage carries what it applies to and its period.
- A payment timing says working days when a bank being open matters.
- No vague timing: "soon", "shortly", "in a moment".
