# Error messages

**Status: normative (rules) + example (samples).**

What Vanker says when something goes wrong. Errors are where a bank earns or loses
trust, so tone matters most here (see `../voice-and-tone/tone.md`, "Errors and things
going wrong").

This file is the anatomy and the two in-product shapes (field validation and modal). When
the problem is the connection or our systems — offline, a server failure, maintenance, an
expired session, a missing page, a required update — the surface choice and the copy live
in `system-errors.md`.

## Anatomy

A Vanker error has up to three parts, in this order:

1. **What happened** — plain, specific, no error code.
2. **Reassurance** — especially that money is safe, when money could be involved.
3. **What to do next** — one clear action.

## Rules

- Reassure before you instruct. If money could be affected, say it is safe.
- Never blame the person (see `../terminology/banned-terms.md`, "Blame").
- Be specific about the cause when you know it. Do not say "something went wrong" if
  you know what did.
- One clear next step, and put it in the button, not buried in prose.
- Actions live in their own buttons, never inline in the body. The body says what happened;
  it never contains a call to action like "Cancel or Retry".
- No error codes in the visible message. A reference code may sit in a small secondary
  line for support.
- No jokes, no emoji. Calm and human.
- Contractions are welcome, but in a critical instruction spell out the negative ("do
  not", "cannot") instead of "don't"/"can't" where a misread could cause harm — an error
  message is exactly this case. See `../voice-and-tone/voice.md` (Contractions).

## Variables

`{amount}`, `{recipient}`, `{n}` (attempts left), `{support_ref}`

## Examples

**Payment failed, funds not moved**
- Do: "That payment did not go through, and no money has left your account. Please check your card details and try again."
- Not: "Payment error. Invalid input. Code 402."

**Insufficient funds**
- Do: "You do not have enough in your current account to send {amount} €." with buttons
  "Add money" (primary) and "Cancel". The body says what happened; the way out is a
  button, and one fact is one paragraph.
- Not: "Transaction declined: insufficient funds."

**Connection problem**
- Do: "We could not reach our systems just now. Your money is safe. Please try again in a moment."
- Not: "Network error. Retry."

**Wrong passcode**
- Do: "That passcode was not right. Please try again. After {n} more tries we will lock the app to keep your account safe."
- Not: "Invalid credentials."

**Unknown cause (fallback)**
- Do: "Something did not work on our side, and your money is safe. Please try again. If it keeps happening, contact us and mention {support_ref}."
- Not: "Unexpected error occurred."

## Machine-readable spec

```json
{
  "errors": {
    "anatomy": ["what happened", "reassurance", "what to do next"],
    "shapes": {
      "field-validation": { "sentences": 1, "ends-with-period": true, "families": ["what is missing", "what is expected"], "imperative": false, "generic": false },
      "modal": { "title": { "ending-period": false, "blame": false }, "body": { "optional": true, "cta-inside": false, "max-paragraphs": 3 }, "actions": { "max": 2, "inform-only": "Close" } }
    },
    "visible-error-code": false,
    "reference-line": "allowed, tertiary",
    "money-reassurance-required-when": "money could be affected",
    "blame": false,
    "spell-out-negation-when": ["money-outcome", "security-instruction"]
  }
}
```

## Eval hooks

- No visible error code in the primary message.
- Contains a clear next step (an imperative verb).
- No inline call to action in the body (actions are separate buttons).
- For money-related errors, contains a safety reassurance.
- Contains no banned blame terms.

## Modal errors (interrupting): content structure

The content model for an error shown in a **modal** that interrupts the person. It is a set
of slots, each with its own rules.

### Slots

- **Title** (required): one clear, direct sentence saying what happened, never blaming the
  person. **No ending period.** One line.
- **Body** (optional): included **only when needed**. When present, it gives more context on
  what happened and how to solve it. It explains; it **never contains the CTA**. One fact per
  paragraph, at most three paragraphs, left aligned from three lines
  (see `../components/foundations/typography.md`).
- **Actions** (one or two, never more):
  - **Inform only** (the person can only acknowledge): a single **Close** button. Never
    "OK".
  - **Actionable** (there is a fix): a **primary** CTA that leads to the solution the text
    offers (for example "Retry"), plus a **secondary** CTA to exit ("Cancel"). Stacked,
    primary on top (see `../components/library/sheet-modal.md`).
- **Reference code** (optional): for hard errors, a small, discreet support reference line.
  A tertiary element, not a CTA and not body.

### Rules

- Two CTAs maximum in a modal error. If it needs three or more exits, rethink the error.
- The action lives in the CTA, never inline in the body.

### Examples

- **Inform only:** Title "We could not load your transactions" / (no body) / **Close**.
- **Retry:** Title "Your transfer did not go through" / Body (optional) "A technical problem
  stopped it, and no money has left your account." / **Retry** (primary), **Cancel**
  (secondary).
- **Insufficient funds:** Title "You do not have enough to send this payment" / Body "Your
  current account balance is lower than the amount." / **Add money** (primary), **Cancel**
  (secondary).

### Eval hooks (per slot)

- Title has no ending period and does not blame the person.
- Body appears only when it adds context, and never contains a CTA.
- Inform-only errors use "Close", never "OK".
- No more than two CTAs.

## Field validation (inline) errors: content structure

The content for a validation error shown **inline, next to the field** (not a modal). It
does not interrupt and has a single slot: the message. It pairs with the field's error
state (see `../components/library/text-field.md`).

### The message

- **One sentence**, brief and direct, ending with a period. A comma is fine if a single
  clear sentence needs one, but **never two sentences**, and never two different messages.
- **Specific and useful**: it compares what the person typed with what the field expects and
  gives the hint to fix it. Never generic ("Error", "Review the data").
- **Guidance, not blame**: state what is expected ("A postal code has 5 digits.") rather
  than what the person did wrong.
- **A fact, not an order.** Someone who has not filled a field in yet has done nothing
  wrong, and an imperative treats them as if they had. There are two families, and between
  them they cover every field error:

  | What happened | What the message does | Example |
  | --- | --- | --- |
  | The field is empty | **States what is missing** | "Your street is missing." |
  | There is a value, but it is wrong | **States what is expected** | "An IBAN must contain 24 characters." |

  Never "Enter your street." (an order), and never "This is required." (the same sentence
  for every field: in an error summary, six of them are indistinguishable, and for someone
  using a screen reader the six links are literally identical). See `forms.md`.
- Not a question, no exclamation, no humor.

### Presentation and behavior

- Shown in red, **with an icon and announced to screen readers** (color is never the only
  signal), associated to the field.
- Appears on blur or when the person pauses typing, and **clears as soon as the input
  becomes valid**.

### Examples

- Postal code, 4 digits typed: "A postal code has 5 digits."
- IBAN, wrong length: "An IBAN must contain 24 characters."
- Email, missing "@": "An email address needs an @ sign."

### Eval hooks

- One sentence, ends with a period, no "?" or "!".
- Not generic; gives a specific hint. "This is required" fails: it is the same sentence for
  every field.
- States a fact rather than giving an order: what is missing, or what is expected.
- Not conveyed by color alone (text plus icon, associated to the field).
