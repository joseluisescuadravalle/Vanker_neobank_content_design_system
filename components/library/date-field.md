# Date field

**Status: normative.**

Where a person gives a date: their date of birth, the day a payment should go out, the
range a statement covers.

The written format lives in `../../terminology/numbers-and-dates.md`; the label model and
the error families are in `../../patterns/forms.md`.

## A date they know, or a date they choose

The two are different problems and take different controls. Getting this backwards is the
most common failure of the component.

| The date is | Control | Why |
| --- | --- | --- |
| **Known and remembered** (date of birth, the date on a document) | **Typed**, in day, month and year fields | Nobody navigates a calendar forty years back. They know the answer; the field's job is to accept it |
| **Chosen from what is available** (a scheduled payment, a statement range) | **Calendar** | The question is not "which date" but "which of the days that work", and only a calendar shows that |
| Either, depending on the person | Both: typed fields, with the calendar as an alternative | The calendar is never the only route |

- **Never a dropdown for the year.** A list of a hundred years is a scroll, not an answer.
- **Never a calendar as the only way to give a date of birth.**

## Split or single: the rule that decides it

`code-input.md` says a six-digit code is **one field**, and this file says a date is
**three**. That is one rule, not two:

> **Split the field when each part is a distinct value with a name of its own. Keep one
> field when the parts are meaningless fragments of a single value.**

The third digit of a code means nothing on its own. A month does: it has a name, its own
range, and its own errors. So a date of birth is three inputs — **Day**, **Month**,
**Year** — each with its own visible label, inside a group with a legend ("Date of birth"),
per `../../patterns/forms.md`.

- Each part accepts what a person naturally types: `3`, not only `03`.
- The month accepts digits, and a typed name where the locale makes that natural.
- Autofill is per part (`bday-day`, `bday-month`, `bday-year`), so the platform can help.
- `inputmode="numeric"`, and moving between parts is the person's choice: **never
  auto-advance the focus**, which is how someone typing `1` for January loses the caret
  before typing the second digit of `12`.

## Echo the date back in words

**As soon as the three parts are complete, show the date written out**: `3 April 2026`.

This is the cheapest safeguard the component has. A person who typed `03` and `04` finds
out immediately whether we read it as 3 April or 4 March, and corrects it themselves. It
costs one line and it removes the single most expensive misunderstanding a date field can
produce (see `../../terminology/numbers-and-dates.md`).

## Dates that are not available

For a payment, some days do not work: weekends, bank holidays, a cutoff that has already
passed today.

- **Show what is unavailable, and say why** — not a calendar with silent gaps. "Banks are
  closed on weekends."
- **Never move a date silently.** If the chosen day cannot be used, say what will happen
  instead: "4 September is a Saturday, so your payment will arrive on 6 September."
- **The cutoff is part of the date.** Where sending after a time changes the day, say so
  before the person picks: "Payments sent after 4:00 pm arrive the next working day."
- A disabled day in the calendar carries its reason where the person can reach it, in the
  layout and not only as a grey square (see `../../patterns/forms.md`).

## Errors

The two families from `../../patterns/forms.md` apply: what is missing, or what is
expected.

| Case | Message |
| --- | --- |
| Nothing entered | "Your date of birth is missing." |
| One part missing | "The month is missing." |
| The date does not exist | "There is no 31 September." |
| In the future when it cannot be | "A date of birth cannot be in the future." |
| Outside an allowed range | "You can schedule a payment up to 12 months ahead." |
| An age rule | "You must be 18 or older to open a Vanker account." |

- **Name the part that is wrong**, not the whole group, and put the error on the group so a
  screen reader reads it once.
- **An age rule is a rule, not a judgement.** State the rule; never "you are too young", and
  never explain what someone should do about their own date of birth.

## States

| State | Treatment |
| --- | --- |
| Empty | Three fields with their labels, and the written echo absent |
| Complete | The written date shown below the group |
| Unavailable day chosen | The consequence stated in place, with the resulting date |
| Error | Group-level message, the offending part outlined, `aria-invalid` on it |
| Read-only | The written date, with no field affordance |

## Accessibility

- A `fieldset` with a legend for the group; each part has its own visible label, and the
  labels are not placeholders.
- The written echo is in a **polite** live region, so it is announced as it resolves.
- The calendar is fully keyboard-operable, announces the month as it changes, and states
  why a day is unavailable rather than only disabling it.
- The error is associated with the group through `aria-describedby` and names the part.
- Minimum 44px targets for every day cell and every stepper.

## Machine-readable spec

```json
{
  "date-field": {
    "control-by-kind": {
      "known-date": "typed day, month and year fields",
      "chosen-date": "calendar",
      "either": "typed, with the calendar as an alternative"
    },
    "year-dropdown": false,
    "calendar-as-only-route": false,
    "split-rule": "split when each part is a named value of its own; keep one field when the parts are fragments of a single value (see code-input.md)",
    "parts": { "labels": ["Day", "Month", "Year"], "legend": true, "leading-zero-required": false, "auto-advance-focus": false, "autocomplete": ["bday-day", "bday-month", "bday-year"], "inputmode": "numeric" },
    "echo": { "required": true, "format": "written", "example": "3 April 2026", "live-region": "polite" },
    "unavailable": { "reason-stated": true, "silent-move": false, "consequence-stated": true, "cutoff-stated-before-choosing": true },
    "errors": { "families": ["what is missing", "what is expected"], "names-the-part": true, "age-rule-not-judgement": true },
    "a11y": { "fieldset-legend": true, "visible-part-labels": true, "keyboard-calendar": true, "min-target": 44 }
  }
}
```

## Eval hooks

- A date the person remembers is typed, never picked from a calendar as the only route, and
  never from a year dropdown.
- The parts carry visible labels inside a group with a legend, and focus never auto-advances.
- The completed date is echoed in words, so an ambiguous entry is caught by the person.
- An unavailable day states why, and any change of date states the resulting date; nothing
  moves silently.
- Errors name the missing or wrong part, and an age rule is stated as a rule, never as a
  judgement about the person.
