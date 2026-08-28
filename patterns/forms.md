# Forms

**Status: normative (rules) + example (samples).**

How Vanker asks people for data. Forms are where trust is won or lost in a bank: every
extra field, every ambiguous label, every dark pattern costs confidence. This file is the
form-level pattern; the field visuals and per-slot rules live in
`../components/library/text-field.md`, `dropdown.md`, `checkbox.md`, `radio-group.md`, and
`amount-input.md` (any field that takes money).

## Three principles

1. **Brevity and simplicity.** Ask for the minimum data. Do not duplicate a field as its
   own confirmation (no "confirm your password", no "re-enter your email"); use a
   show/hide toggle instead.
2. **Maximum clarity.** No ambiguity. Each field names exactly one thing, in plain
   language, with the format made obvious.
3. **Do not forget the person.** In long forms, lean on narrative and **group related
   fields** under a legend, so the form reads as steps a person takes, not a database to
   fill.

## The field-text hierarchy

Five kinds of text can surround an input. Each has one job; used together they must not
repeat one another.

| Slot | Where | Job | Required |
| --- | --- | --- | --- |
| **Label in** | Inside the field, floats up on input | Names the data | **Yes** |
| **Label out** | Above the field | Adds a description or question a short label cannot carry | Only when needed |
| **Legend** | Heads a group of fields | Presents or divides a group of related data | Only for groups |
| **Helper text** | Below the field | Complementary guidance to complete the field | Optional |
| **Placeholder** | Inside the field, muted | A format example only | Rare |

### Label in (the base)

Every input has a **label in**: the text inside the empty field that names the data. When
the person types, the label **does not disappear** — it shrinks and floats to the top of
the field, staying visible above the value ("floating label"). This is the accessible
default: the field is never left without a visible, persistent name.

- A short noun in sentence case, the fewest words possible ("Monthly income", not "Please
  enter the monthly income"). Aim for one to three words.
- Only the first word is capitalized (plus proper nouns). No ending period, colon, or
  question mark.
- Watch pronouns and articles: "Surname", not "Your surnames".

### Label out (when the short label is not enough)

Use a **label out** — text above the field — when the data needs a **descriptive or
interrogative phrase** that a short label in cannot carry. The word count is a symptom,
not the rule: reach for a label out when you need to qualify or disambiguate, not merely
because a noun is a little long.

- A descriptive phrase or a question. A question mark is allowed; a **period and a colon
  are not**.
- When a label out is used, the **label in stays** as the short reference. They must not
  repeat the same words: the label in is the short tag, the label out carries the extra
  information.
  - Label out: "Combined monthly income of both spouses" · Label in: "Monthly income" ✅
  - Label out: "Enter your name" · Label in: "Name" ❌ (the label out only repeats the
    label in — drop it)

### Legend (grouping)

A **legend** introduces or divides a **group of related fields**, so a long form reads in
sections. It is a short word or phrase, with no ending period or colon, and it must not
restate the labels of the fields it heads.

- "Home address" over Street / Number / Floor / Door
- "We also need your measurements" over Chest / Waist / Hips (in cm)

The three levels can coexist on one screen: a **legend** heads the group, each field keeps
its **label in**, and a **label out** is added only where a field needs the extra context.

### Helper text

Complementary guidance to complete a field, below it. At most about three lines. Prefer a
single sentence; avoid several sentences separated by periods, and do not phrase it as a
question. Not a place for legal text or for a call to action.

- "Password" + helper "Your password should be long, unique to you, and hard to guess."

### Placeholder

A **format example only**, in muted text, inside the field ("DD/MM/YYYY",
"you@example.com"). Most fields have none. A placeholder **never** carries essential
information, because it disappears the moment the person types, and it never stands in for
the label. If you are tempted to put guidance in a placeholder, it belongs in the label
in, a label out, or helper text.

#### Exception: guide-phrase placeholders (search and marketing surfaces)

The "format example only" rule governs **data-entry forms**, where a disappearing hint is
a liability. It does **not** govern **search fields and marketing / conversational
surfaces**, where a placeholder legitimately does more work. On those surfaces a
placeholder may be a **guide phrase** — a conversational prompt or an example that invites
the action — because there is no data-integrity risk if it vanishes and the field is
self-evidently a search or compose box.

Where this exception applies (search bars, global search, compose boxes, marketing landing
inputs), a guide-phrase placeholder may:

- **Invite a conversational search** — "Search artists, albums, and podcasts", "What are
  you looking for?"
- **Motivate the action in a critical field** — a compose or prompt box, "Ask anything".
- **Signal categories or scope** — "Search products, categories, services…".
- **Offer an example that invites interaction** — 'Try "create a mobile app"'.

It still must not replace a needed **label** when the input collects structured data (a
date, an amount, an IBAN): those remain form fields under the rule above. And even here the
placeholder never carries information the person must keep to complete the task, and it
follows voice and tone. Treat this as a scoped exception, not a licence to move field
guidance back into placeholders.

## Choices (dropdown, radio, checkbox)

- **Dropdown** — choose one value from a short, predefined list (2 to 5). Options are
  parallel and do not repeat the label's verb. See `../components/library/dropdown.md`.
- **Radio** — choose one option and discard the rest, when all options should be visible.
  Keep articles and pronouns; one line each. See `../components/library/radio-group.md`.
- **Checkbox** — mark one or more options, or give consent. Concise but keep the articles;
  the person may speak in the first person ("I agree to…"); never a dark pattern. See
  `../components/library/checkbox.md`.

## Accessibility and compliance

- The label is programmatically tied to the input and is always visible; a placeholder is
  never the only label (WCAG 2.1 AA; European Accessibility Act). See
  `../compliance/accessibility.md`.
- Required by default; mark only the optional fields with "(optional)", never asterisks.
- Consent is never pre-ticked and never phrased as a double negative (no dark patterns);
  legal wording is adapted to plain language without changing its meaning, and anything
  touching money, risk, or personal data follows `../compliance/`.

## Eval hooks

- Every input has a visible label in; no field is named by a placeholder alone.
- Label in: short noun, sentence case, no ending period/colon/question mark.
- Label out: descriptive or interrogative, no ending period or colon; never repeats the
  label in verbatim.
- Legend: short, no ending period or colon; does not restate the group's labels.
- Helper text: not a question, about three lines, prefers one sentence, no call to action.
- Placeholder: on a form field, a format example only, never essential information; a guide-phrase placeholder is allowed only on search / marketing surfaces (see the exception above).
- No duplicated confirmation fields (password, email).
