# Amount input

**Status: normative.**

The field where a person types money: how much to send, add, save, or set as a limit. It is
a component of its own, not a text field with a euro sign, because money has a fixed format,
a decimal separator that changes with the keyboard, a maximum, a cost, and a consequence
that cannot be undone with a backspace.

Field mechanics it inherits (the label model, focus, error styling) live in
`text-field.md`; the money format lives in `../../terminology/glossary.md`; what must be
disclosed before the person commits lives in `../../compliance/disclosures.md`.

## Variants

| Variant | Where | The question is asked by |
| --- | --- | --- |
| **Hero** | A full screen whose only job is the amount (send money, add money, top up a space) | A heading above the amount ("How much do you want to send?") |
| **Inline** | One field inside a form (set a target, set a card limit) | The label in, per `text-field.md` |

Both share every content rule below. Only the presentation of the question differs.

## Slots

- **Question** (hero) or **label in** (inline), required. The hero heading is a real
  question and takes a question mark. The inline label in is a short noun ("Amount",
  "Monthly target"), sentence case, no ending punctuation.
- **Amount value** (required): the digits the person types, in European format, tabular
  numbers.
- **Currency adornment** (required): `€`, after the amount, with a space. It is part of the
  field, not part of the value: the person never types it and never deletes it.
- **Context line** (optional but usual): one line under the field carrying what the person
  needs to decide — the available balance, the remaining limit, the fee, the arrival time.
- **Preset amounts** (optional): two to four suggested amounts. See below.
- **Error** (conditional): replaces the context line. One sentence, per
  `../../patterns/errors.md`.

## Input rules

1. **The person types digits; the field does the formatting.** Thousands separators appear
   as they type (`1.240`), the decimal separator is a comma, and at most two decimals are
   accepted. The value is never silently rounded, truncated, or reordered.
2. **Cents are never there by default.** The field never starts with `,00`, never appends
   `,00` to a round amount, and never pre-fills a decimal part. Decimals appear only when
   the amount has cents or the person types them: `150 €`, `10,50 €`.
   - **While typing, show exactly what was typed.** A person mid-keystroke at `10,1` sees
     `10,1`; the field does not jump in to complete or pad the decimals, and does not move
     the caret.
   - **Once rendered, an amount with cents shows exactly two decimals.** On blur, on the
     confirmation screen, in a transaction row, in a statement: `10,10 €`, not `10,1 €`. A
     round amount still shows none: `150 €`, never `150,00 €`.
3. **Accept both `,` and `.` as the decimal separator, and render a comma.** Numeric
   keypads on phones offer one or the other depending on the device and locale. Typing
   `52.40` is a keyboard, not a mistake: it must produce `52,40 €`, never an error. A second
   separator is simply not accepted as a character.
4. **The currency symbol is never typed.** If a pasted value carries `€`, `EUR`, or spaces,
   the field strips them and keeps the number.
5. **Never auto-scale a typed number.** "50" means 50 €, never 0,50 €. A field that turns
   keystrokes into cents from the right is a trap in a bank.
6. **Money is never truncated.** If the amount outgrows the width, the type size steps down
   (no smaller than 24px in the hero variant); the digits are never clipped or replaced by
   an ellipsis.
7. **The empty hero field shows `0 €`,** not a placeholder, so the format is visible before
   the first keystroke. The inline field starts empty with its label in.
8. **`inputmode="decimal"`**, not `numeric`: the person needs a separator.

## Content rules

- **The question names the money, not the mechanism.** "How much do you want to send?", not
  "Enter transfer amount value".
- **The label in never carries the currency symbol or a digit.** "Amount", not "Amount (€)"
  and not "Amount in euros". The adornment shows the currency; the accessible name carries
  it for screen readers (see Accessibility).
- **The context line states cost, limit, and timing before the person commits**, never
  after (see `../../compliance/principles.md`). One line, one fact, in this order of
  priority when only one fits: a blocking limit, then the fee, then the balance.
- **Fees are exact or free.** "This transfer is free." / "There is a 2 € fee for same-day
  delivery." Never "a small fee", "low fees", or "fees may apply" (see
  `../../compliance/disclosures.md`).
- **A currency conversion states the markup over the European Central Bank (ECB) reference
  rate**, not just the rate.
- **No call to action in the context line.** The action is the button below it (see
  `CLAUDE.md`).

## Preset amounts

Two to four suggested amounts beside or under the field, so a person can skip typing.

- A preset carries **an amount and nothing else**: `20 €`, `50 €`, `100 €`. No verb, no
  "Add", no "+", no emoji.
- **A preset is not a call to action.** The button rules (a verb, no digits) do not apply to
  it, and must not be applied to it: it is a value selector whose whole content is a number.
  It is checked as `preset-amount`, never as `cta`.
- Presets replace the amount, they never add to it, and choosing one never submits the
  form.
- Amounts are round and plausible for the flow; never anchor with a large default to push a
  bigger transfer (see `CLAUDE.md`, section 2).
- A preset never appears for a field with a legal maximum it could exceed.

## Limits, balance, and fees

| Situation | Where it goes | Example (normative form) |
| --- | --- | --- |
| Available balance matters | Context line | "You have 1.240,50 € available." |
| A fee applies | Context line, before confirming | "There is a 2 € fee for same-day delivery." |
| No fee | Context line | "This transfer is free." |
| A per-transaction or daily limit exists | Context line, from the start, not on failure | "You can send up to 3.000 € a day." |
| A currency conversion applies | Context line | "Exchange rate: 1 € = 1,08 USD. Our markup: 0,5% over the ECB rate." |

A limit the person can hit is stated **before** they type, not only when they exceed it.

## Errors

Field validation errors: one sentence, ending with a period, specific, never blaming (see
`../../patterns/errors.md`). Critical negatives are spelled out ("cannot", not "can't"),
per `../../voice-and-tone/voice.md`.

| Case | Message (normative) |
| --- | --- |
| Amount is empty | "The amount is missing." |
| Amount is zero | "The amount must be more than zero." |
| More than the available balance | "That is more than the 1.240,50 € available in your current account." |
| Below the minimum | "The smallest amount you can send is 1 €." |
| Over the per-transaction limit | "You cannot send more than 3.000 € in one transfer." |
| Over the remaining daily limit | "Today you can still send up to 450 €." |
| More than two decimals | "Amounts take at most two decimals." |

- Validate **on submit or on blur**, never on every keystroke: an error that appears while
  someone is still typing the second digit of `1.240` is wrong and reads as blame.
- **Prefer an enabled action with a specific error over a silently disabled button.** A
  disabled button explains nothing. If the action is disabled, the reason is visible next to
  the field, never only in the button's appearance.

## States

| State | Treatment |
| --- | --- |
| Empty | Hero: `0 €` in `color.text-tertiary`. Inline: label in centered, per `text-field.md` |
| Focus | Caret after the digits; border `color.accent` and focus ring (inline) |
| Filled | Value in `color.text-primary`, tabular numbers, `€` in `color.text-secondary` |
| Over limit | Value in `color.error-text`, error message below, `aria-invalid`; never color alone |
| Disabled | Not editable, `color.text-tertiary`; the reason is stated in the context line |
| Read-only | The value with no field affordance (a confirmation screen), not a disabled field |

## Motion

- The type size step-down when the amount grows uses `motion.duration.fast` (160ms,
  ease-out).
- Digits do not roll, count up, or animate: a changing money figure must be readable at
  every frame.
- Under `prefers-reduced-motion`, the size change is applied without a transition.

## Accessibility

- The accessible name carries the currency even though the visible label does not: "Amount
  in euros".
- The value is announced as money, not as loose digits: "one thousand two hundred forty
  euros and fifty cents", not "one two four zero five zero".
- `inputmode="decimal"`, `autocomplete="off"` for a transfer amount, and no spinner
  controls.
- The context line is tied to the field with `aria-describedby`, so the balance, the fee,
  and the limit are read with it.
- When the fee or the remaining limit changes as the amount changes, announce it in a
  **polite** live region; never move focus.
- The error is linked with `aria-describedby`, carries an icon and text, and never relies on
  color alone.
- Minimum 44px tap targets for presets and the keypad; the field itself is 48px (inline).

## Content examples

- ✅ Question: "How much do you want to send?" · Context: "You have 1.240,50 € available."
- ✅ Preset: `50 €`
- ✅ Error: "That is more than the 1.240,50 € available in your current account."
- ❌ "Amount (€)" as a visible label (the adornment already shows the currency).
- ❌ "Add 50 €" as a preset (a verb turns a value into an action).
- ❌ "€50", "50,00 €", or "10,1 €" as a rendered amount (wrong money format).
- ❌ "A small fee may apply." (a fee is exact or the service is free).
- ❌ An error shown on the second keystroke of an amount still being typed.

## Machine-readable spec

```json
{
  "amount-input": {
    "variants": ["hero", "inline"],
    "slots": {
      "question": { "variant": "hero", "required": true, "form": "question", "question-mark": true },
      "label-in": { "variant": "inline", "required": true, "case": "sentence", "currency-symbol": false, "digits": false },
      "value": { "required": true, "format": "european", "numbers": "tabular", "decimals-max": 2, "decimals-rendered": "0-or-2", "decimals-while-typing": "as-typed", "pad-with-zeros": false, "truncate": false },
      "currency": { "required": true, "symbol": "€", "position": "after", "typed-by-user": false },
      "context-line": { "required": false, "one-line": true, "cta": false, "priority": ["limit", "fee", "balance"] },
      "presets": { "required": false, "count": [2, 4], "content": "amount-only", "verb": false, "submits": false },
      "error": { "required": false, "sentences": 1, "ends-with-period": true }
    },
    "input": {
      "inputmode": "decimal",
      "decimal-separators-accepted": [",", "."],
      "decimal-separator-rendered": ",",
      "thousands-separator": ".",
      "strips-on-paste": ["€", "EUR", " "],
      "auto-scale-to-cents": false,
      "empty-hero-value": "0 €",
      "default-cents": false,
      "normalize-decimals-on": "blur",
      "min-type-size-hero": 24
    },
    "validation": {
      "trigger": ["submit", "blur"],
      "on-keystroke": false,
      "prefer-enabled-action-with-error": true,
      "messages": {
        "empty": "The amount is missing.",
        "zero": "The amount must be more than zero.",
        "over-balance": "That is more than the {available} € available in your current account.",
        "below-minimum": "The smallest amount you can send is {min} €.",
        "over-transaction-limit": "You cannot send more than {limit} € in one transfer.",
        "over-daily-limit": "Today you can still send up to {remaining} €.",
        "too-many-decimals": "Amounts take at most two decimals."
      }
    },
    "disclosure": {
      "fee": "exact-amount-or-free",
      "banned": ["a small fee", "low fees", "fees may apply"],
      "limit-stated-before-typing": true,
      "fx-markup-over-ecb": true
    },
    "motion": { "resize": "motion.duration.fast", "digit-animation": false, "reduced-motion": "none" },
    "a11y": {
      "accessible-name": "Amount in euros",
      "value-announced-as-money": true,
      "context-describedby": true,
      "live-region": "polite",
      "error-describedby": true,
      "min-target": 44
    }
  }
}
```

## Eval hooks

- The visible label of an amount field carries no currency symbol and no digits.
- A preset amount is an amount and nothing else: no verb, no emoji, correct European format.
- A preset amount is never evaluated as a call to action, and a call to action never carries
  an amount.
- Every rendered amount uses the European format: `€` after the amount, dot thousands, comma
  decimals, and either no decimals (a round amount) or exactly two (`10,10 €`). Cents are
  never added by default, and `,00` never appears.
- A fee is stated as an exact amount or as "free"; "a small fee", "low fees", and "fees may
  apply" fail.
- A limit that can block the person appears before they type, not only in the error.
- A field error is one sentence, ends with a period, names the actual constraint with its
  amount, and spells out the negative ("cannot").
- The context line contains no call to action.
