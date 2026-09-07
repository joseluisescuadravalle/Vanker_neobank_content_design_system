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
- **One fact per sentence.** A sentence never has three clauses: two joined once
  (", and", ", so", ", but") is the most it carries, and a sentence past 25 words is not
  read on a phone. `A-PARAGRAPHS` fails both with "one fact per sentence". The reason: a reader in trouble reads the
  first clause and acts; whatever came after the second comma did not reach them.
- **The exception: merge two related facts into a two-clause sentence only when the slot
  would otherwise need a fourth paragraph.** A modal body holds three paragraphs, one fact
  each. When a screen has four facts to tell, the answer is not a fourth paragraph and it
  is not dropping one: it is one sentence that joins the two facts that belong together
  ("The card network rejected the payment on our side, and no money has left your
  account."), written in voice and tone, with any fixed formula kept intact inside it.
  This is a way out, not a style: three facts that fit in three paragraphs stay in three
  paragraphs. The fixed sentences about money (see `system-errors.md`, rule 1) can be
  joined to a neighbor, never paraphrased.
- **The body never repeats the title.** The title says what happened; the body adds why,
  the money, and what to do. A first body sentence that restates the title is a wasted
  paragraph and, on a modal, one of only three. Code cannot check this reliably (word
  overlap is a weak signal), so it is the editorial review's job, under Clarity.

## Variables

`{amount}`, `{recipient}`, `{n}` (attempts left), `{support_ref}`

## Examples

**Payment failed, funds not moved**
- Do: "That payment did not go through, and no money has left your account. Please check your card details and try again."
- Not: "Payment error. Invalid input. Code 402."

**Insufficient funds**
- Do: "You do not have enough in your current account to send {amount} €." with buttons
  "Add money" (primary) and "Cancel". The body says what happened; the way out is a
  button, and one fact is one paragraph.
- Not: "Transaction declined: insufficient funds."

**Connection problem**
- Do: "We could not reach our systems just now. Your money is safe." with a "Retry"
  button. The way back is the button, and a vague "in a moment" promises a timing we
  have not measured.
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
      "modal": {
        "title": { "required": true, "carries-impact": true, "ending-period": false, "blame": false, "lines": 1 },
        "body": { "optional": true, "adds-what-title-lacks": true, "repeats-title": false, "cta-inside": false, "paragraphs": [1, 3], "facts-per-paragraph": 1, "facts-per-sentence": 1, "sentence": { "max-words": 25, "max-clauses": 2, "two-clause-merge-only-when": "a fourth paragraph would otherwise be needed" } },
        "actions": { "role": "exits", "max": 2, "inform-only": "Close" }
      }
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
- No sentence chains three clauses or runs past 25 words (`A-PARAGRAPHS`).
- The body never exceeds the slot's paragraph limit and no fact is dropped to meet it; the
  two-clause merge is used only when a fourth paragraph would otherwise be needed
  (editorial review).
- The body does not restate the title (editorial review, Clarity).

## Modal errors (interrupting): content structure

The content model for an error shown in a **modal** that interrupts the person. It is a set
of slots, each with its own rules.

### Slots

- **Title** (required, and the only required slot): what happened and what it means for the
  person, in one clear sentence that never blames them. **No ending period.** One line. A
  title that carries the impact ("We could not complete your payment") can stand alone;
  a title that only names an event ("Payment rejected") cannot.
- **Body** (optional): only when it adds what the title does not say: why, whose side, what
  happened to the money, what to do. One fact per sentence and one fact per paragraph, one
  to three paragraphs, left aligned from three lines (see
  `../components/foundations/typography.md`). It **never repeats the title** (the editorial
  review scores that under Clarity) and it **never contains the CTA**.
- **Actions** (the exits, one or two, never more):
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
- Body appears only when it adds what the title does not say, never restates the title,
  and never contains a CTA.
- One fact per sentence and per paragraph in the body (`A-PARAGRAPHS`).
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
