# Assertions (deterministic checks)

**Status: tooling.**

Black-and-white rules a machine can verify, drawn from the "Eval hooks" across the system.
Each has an ID used in `golden-set/cases.jsonl` and implemented in `assertions.py`.

## Format and terminology

| ID | Checks | Source |
| --- | --- | --- |
| `A-NO-EMOJI` | No emoji anywhere | `../voice-and-tone/voice.md` |
| `A-EURO-FORMAT` | € after the amount; dot thousands, comma decimals; no ",00" on round amounts; cents show exactly two decimals, never one | `../terminology/glossary.md` |
| `A-NO-BANNED` | No banned or jargon terms | `../terminology/banned-terms.md` |
| `A-ACRONYMS` | Known acronyms are expanded on first use | `../terminology/glossary.md` |
| `A-NUMERALS` | Numbers are digits in body copy and instructions ("3 steps", not "three steps") | `../terminology/glossary.md` |

## Voice and patterns

| ID | Checks | Source |
| --- | --- | --- |
| `A-CTA` | Button label: 3 words max (aim for one), no numbers/amounts, no punctuation, no emoji, not a bare generic ("OK", "Confirm") | `../patterns/ctas.md`, `../components/library/button.md` |
| `A-NO-INLINE-CTA` | Body copy contains no inline call to action ("Cancel or Retry"); actions belong in buttons | `CLAUDE.md`, `../patterns/errors.md` |
| `A-FIELD-ERROR` | Field validation error: one sentence, ends with a period, no ?/!, not generic | `../patterns/errors.md`, `../components/library/text-field.md` |
| `A-PUSH-TITLE` | Push title: at most 2 emoji (non-critical push only), about 40 chars | `../patterns/notifications.md` |
| `A-PUSH-BODY` | Push body: about 120 chars (two lines) | `../patterns/notifications.md` |
| `A-TOAST` | Toast message: no ending period, no ?/!, no emoji, short (~50 chars) | `../components/library/banner-toast.md` |
| `A-OPTION` | Dropdown option: a few words, no ending punctuation, no emoji | `../components/library/dropdown.md` |

## Forms (field text)

| ID | Checks | Source |
| --- | --- | --- |
| `A-LABEL-IN` | Label in: short noun, sentence case, no ending period/colon/question mark, aim 1-3 words, no asterisk and no "(required)" | `../patterns/forms.md`, `../components/library/text-field.md` |
| `A-LABEL-OUT` | Label out: descriptive or interrogative, no ending period or colon | `../patterns/forms.md`, `../components/library/text-field.md` |
| `A-LEGEND` | Legend: short, no ending period or colon, no emoji | `../patterns/forms.md` |
| `A-HELPER` | Helper text: not a question, ~3 lines, prefers one sentence, no emoji | `../patterns/forms.md`, `../components/library/text-field.md` |
| `A-CHECKBOX` | Checkbox label: a statement not a question, no emoji | `../components/library/checkbox.md` |
| `A-RADIO` | Radio option: one line, no ending punctuation, no emoji | `../components/library/radio-group.md` |

## Status

| ID | Checks | Source |
| --- | --- | --- |
| `A-STATUS` | Status label: one or two words from the controlled vocabulary, sentence case, no ending punctuation, no digits, no emoji, no ALL CAPS; flags synonyms ("Processing") and default states that should carry no label ("Completed") | `../components/library/status-label.md` |

## Money

| ID | Checks | Source |
| --- | --- | --- |
| `A-AMOUNT-VALUE` | A rendered amount or a preset: the figure and `€` only, European format, either no decimals or exactly two, no `,00` on a round amount, no words, no emoji | `../components/library/amount-input.md`, `../terminology/glossary.md` |
| `A-AMOUNT-LABEL` | The visible label of an amount field: short noun, no currency symbol or word, no digits | `../components/library/amount-input.md` |

## Security and data minimization

| ID | Checks | Source |
| --- | --- | --- |
| `A-MASK` | No full email address and no long run of digits in copy: phone numbers, IBANs, and cards are masked, and a code is never echoed back. Amounts are exempt | `../compliance/data-privacy.md`, `../components/library/code-input.md` |
| `A-NEGATION` | A sentence about whether money moved spells out the negative ("could not"), instead of contracting it | `../voice-and-tone/voice.md`, `../patterns/system-errors.md` |
| `A-SYSTEM-ERROR` | One slot of a system error: no visible error code, no exclamation mark | `../patterns/system-errors.md` |
| `A-MONEY-ACCOUNTED` | **Screen level:** an error that mentions money says what happened to it (nothing left, on its way, or outcome not known yet) | `../patterns/system-errors.md`, `../patterns/errors.md` |
| `A-LOADING` | A waiting status line: present participle, short, no ending period, no exclamation, not a bare "Loading" or "Processing" | `../patterns/loading.md` |
| `A-SKELETON` | A skeleton placeholder carries no text, no digits, and no currency symbol | `../patterns/loading.md` |

## Onboarding

| ID | Checks | Source |
| --- | --- | --- |
| `A-CARD-HEADLINE` | Welcome-card headline: one line, about six words, no ending punctuation, no emoji | `../patterns/welcome-carousel.md` |
| `A-CARD-BODY` | Welcome-card body: at most two short lines, one sentence, no ending period, and no figures (a rate or a price needs a disclosure the card cannot carry) | `../patterns/welcome-carousel.md` |
| `A-INTRO-CTA` | Flow-intro buttons are "Start" and "Not now"; a goal verb ("Activate biometrics") is rejected because the tap only opens the first step | `../patterns/flow-intro.md`, `../patterns/ctas.md` |
| `A-PERMISSION` | Permission-priming body: no "we need access" framing, the person is the subject, and it carries the sentence stating what Vanker will not do with the permission | `../patterns/permissions.md` |
| `A-TOOLTIP` | Tooltip body: one or two sentences, about 160 characters, ends with a period, and carries no figure, no call to action, and no link | `../components/library/tooltip.md` |
| `A-TOOLTIP-TRIGGER` | The trigger's accessible name is the question the tooltip answers, never "info" or "?" | `../components/library/tooltip.md` |
| `A-COUNTER` | A character counter reads "{n} characters left", never a ratio | `../components/library/textarea.md` |
| `A-ERROR-SUMMARY` | The title above a failed submit says what to do, with no blame, no "error", and no count | `../patterns/forms.md` |

`A-NO-BANNED` also rejects the vague-failure phrases ("something went wrong", "oops",
"unexpected error", "technical difficulties") the vague-waiting ones ("please wait",
"almost there", "just a moment", "hang tight", "working on it") and the marketing claims
("the best", "the cheapest", "the fastest", "free forever", "no strings attached").

**A-MONEY-ACCOUNTED is the first screen-level check in the system.** Every other assertion
grades one slot; this one grades the title and the body together, because the title states
the failure and the body carries the reassurance. Running it on a title alone would fail
every correct screen. Use the `system-error-screen` surface with the slots joined.

`A-NO-BANNED` also rejects "OTP", "one-time password", and "token": in customer copy the
single-use code is a **code** (see `../terminology/glossary.md`).

`A-NO-BANNED` also covers the vague-fee phrases forbidden by `../compliance/disclosures.md`
("a small fee", "low fees", "fees may apply"): a fee is an exact amount or the service is free.

## Compliance

| ID | Checks | Source |
| --- | --- | --- |
| `A-NO-CLAIMS` | No prohibited claims ("guaranteed", "risk-free", etc.) | `../compliance/principles.md`, `../compliance/risk-warnings.md` |

## Extending

Add a check as a function in `assertions.py`, register it with a new ID, and reference that
ID from the golden-set cases. The catalog is meant to grow as the system does; not every
rule is code-checkable (those live in `rubric.md`).

## Surface → checks (important)

Not every check applies to every surface. A **CTA is not body copy**, so it gets only its
own rules; the money-format, banned-terms, and acronym-expansion checks do not run on it.
Apply checks by surface (see `SURFACE_CHECKS` / `checks_for` in `assertions.py`):

| Surface | Checks applied |
| --- | --- |
| `cta`, `button` | `A-CTA`, `A-NO-EMOJI` only |
| `field-error`, `validation` | `A-FIELD-ERROR`, plus the body checks (money format, banned, claims, acronyms) |
| `push-title` | `A-PUSH-TITLE` (emoji allowed, non-critical only), money/banned/claims; no `A-NO-EMOJI` |
| `push-body`, `notification` | `A-PUSH-BODY` plus the body checks (no emoji) |
| `toast` | `A-TOAST`, `A-NO-EMOJI`, plus money/banned/claims |
| `dropdown-option`, `option` | `A-OPTION`, plus banned/claims |
| `label-in` | `A-LABEL-IN`, `A-NO-EMOJI`, banned/claims |
| `label-out` | `A-LABEL-OUT`, `A-NO-EMOJI`, banned/claims, acronyms |
| `legend` | `A-LEGEND`, `A-NO-EMOJI`, banned/claims |
| `helper-text` | `A-HELPER`, `A-NO-EMOJI`, money/banned/claims/acronyms, `A-NO-INLINE-CTA` |
| `placeholder` | `A-NO-EMOJI`, banned/claims (format example only) |
| `checkbox` | `A-CHECKBOX`, `A-NO-EMOJI`, banned/claims |
| `radio-option`, `radio` | `A-RADIO`, banned/claims |
| `status-label`, `status`, `badge`, `tag` | `A-STATUS`, `A-NO-EMOJI`, banned/claims |
| `amount-value`, `preset-amount` | `A-AMOUNT-VALUE`, `A-NO-EMOJI`, banned/claims. **Never `A-CTA`**: a preset amount is a value, not a call to action |
| `amount-label` | `A-AMOUNT-LABEL`, `A-NO-EMOJI`, banned/claims |
| `code-screen` | The body checks, `A-MASK` included: the destination is masked and the code is never echoed |
| `system-error-title`, `system-error` | `A-SYSTEM-ERROR` plus the body checks; no code, no exclamation |
| `system-error-screen` | The body checks plus `A-SYSTEM-ERROR` and `A-MONEY-ACCOUNTED`, run on title and body joined |
| `loading` | `A-LOADING`, banned/claims |
| `loading-screen` | The body checks plus `A-MONEY-ACCOUNTED`, for a long wait that mentions money |
| `skeleton` | `A-SKELETON` only: a skeleton has no copy to check, and that is the point |
| `carousel-headline`, `carousel-body` | Their own check plus banned/claims and no emoji |
| `flow-intro-cta` | `A-INTRO-CTA` plus the CTA checks |
| `flow-intro-body` | The body checks |
| `permission-body` | The body checks plus `A-PERMISSION` |
| `permission-heading` | Banned/claims, no emoji, `A-MASK` |
| `tooltip` | `A-TOOLTIP`, banned/claims, acronyms, numerals |
| `tooltip-trigger` | `A-TOOLTIP-TRIGGER`, no emoji, banned |
| `counter` | `A-COUNTER` only |
| `error-summary-title` | `A-ERROR-SUMMARY`, banned, no emoji |
| everything else (error, confirmation, empty-state, onboarding-step, disclosure, risk-warning, security, banner) | `A-NO-EMOJI`, `A-EURO-FORMAT`, `A-NO-BANNED`, `A-NO-CLAIMS`, `A-ACRONYMS`, `A-MASK` |

The app must select checks by surface. `assertions.run(text, surface="cta")` returns only
the CTA checks; passing an explicit list overrides the surface.
