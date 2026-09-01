# Assertions (deterministic checks)

**Status: tooling.**

Black-and-white rules a machine can verify, drawn from the "Eval hooks" across the system.
Each has an ID used in `golden-set/cases.jsonl` and implemented in `assertions.py`.

## Format and terminology

| ID | Checks | Source |
| --- | --- | --- |
| `A-NO-EMOJI` | No emoji anywhere | `../voice-and-tone/voice.md` |
| `A-EURO-FORMAT` | € after the amount; dot thousands, comma decimals; no ",00" on round amounts; cents show exactly two decimals, never one | `../terminology/glossary.md` |
| `A-NO-BANNED` | No banned or jargon terms, matched on **word boundaries** so "reach" is not "ACH" and "provisional" is not "provision". Also covers login-as-a-verb and, surface-aware, `&` in body copy | `../terminology/banned-terms.md` |
| `A-COLOR-ALONE` | No string points at something by its color ("marked in red", "the green button"). A color as an attribute of a product ("graphite card") is not a locator and passes | `../patterns/accessibility.md` |
| `A-ATTRIBUTION` | Screen level. A screen reporting a failure names the side it is on (our systems, or the device). A session expiry, maintenance or a missing page is not a failure and is not asked | `../patterns/system-errors.md` |
| `A-REPEATED-CHARS` | No letter repeated three times or more ("Oooh", "Retryyyy"): a typo, or a noise written out. Format placeholders (`DD/MM/YYYY`), hex colors and URLs are exempt by shape | `../terminology/banned-terms.md` |
| `A-ACRONYMS` | Known acronyms are expanded on first use | `../terminology/glossary.md` |
| `A-NUMERALS` | Numbers are digits in body copy and instructions ("3 steps", not "three steps") | `../terminology/glossary.md` |
| `A-PUNCTUATION` | No exclamation mark, semicolon, em or en dash, ellipsis, or Latin abbreviation, and a range takes "to" rather than a hyphen between figures | `../terminology/capitalization-and-punctuation.md` |
| `A-CASE` | No Title Case and no ALL CAPS typed into a string. Five exemptions, all by shape: the first word of a sentence, the first word after a slot break, a repeated proper noun, a format placeholder, an acronym expansion, and a named entity the compliance files require in full ("Deposit Guarantee Scheme") | `../terminology/capitalization-and-punctuation.md` |
| `A-LINK-TEXT` | Link text names its destination: "here", "click here", "read more", "learn more" and a bare URL all fail | `../patterns/links.md` |
| `A-DATE` | No numeric, ordinal, or month-first dates; no "Yesterday" or "Tomorrow"; no abbreviated figures or "(s)" plurals; no vague timing | `../terminology/numbers-and-dates.md` |
| `A-INCLUSIVE` | No label for a person where an event should be described, no assumed gender, age or ability, no disability as metaphor, no blacklist/whitelist | `../voice-and-tone/inclusive-language.md` |
| `A-ALT` | Alt text: no "image of" prefix, no file name, no generic one-worder, about 125 characters, no amount. An empty string passes: decorative is a deliberate answer | `../patterns/alt-text.md` |
| `A-BADGE` | A count badge carries digits and an optional `+`, never a word, a currency, an amount, or a zero | `../components/library/count-badge.md` |
| `A-CHIP` | A chip label names the value, never the act: no leading verb, up to three words, no ending punctuation | `../components/library/chip.md` |
| `A-SEARCH-PLACEHOLDER` | Names the scope; a bare "Search" fails, since it is the field's only naming | `../patterns/search.md` |
| `A-NO-RESULTS` | Nothing found is an empty state: no bare "No results found", no error or apology language, no blaming the spelling | `../patterns/search.md` |
| `A-DATE-UNAVAILABLE` | A day that cannot be used states why and what happens instead; nothing moves silently | `../components/library/date-field.md` |
| `A-LOCALIZABLE` | Named variables rather than positional ones, no variable glued into a word, and no reference to a position on the screen | `../terminology/localization.md` |
| `A-CATEGORY-GUESS` | Copy that states an automatic category carries the way to correct it in the same breath | `../patterns/charts.md` |
| `A-FX` | A rate is shown with its markup over the ECB reference rate, and no "0% commission" claim where the cost sits in the spread | `../patterns/currency-exchange.md`, `../compliance/disclosures.md` |
| `A-COMPLAINT` | No defensive language, and an acknowledgement carries a reference and the timeframe | `../patterns/complaints.md`, `../compliance/complaints.md` |

## Voice and patterns

| ID | Checks | Source |
| --- | --- | --- |
| `A-CTA` | Button label: 3 words max (aim for one), no numbers/amounts, no punctuation, no emoji, not a bare generic ("OK", "Confirm"), and one action per label (no "or", "and", "then") | `../patterns/ctas.md`, `../components/library/button.md` |
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
| `A-ACCORDION-HEADER` | An accordion header names its content: up to about eight words, no ending period, no count, and never "More information", "Details", "Read more" or "Info" | `../components/library/accordion.md` |
| `A-TOGGLE-LABEL` | A toggle label is a noun phrase or a state, never an action verb ("Freeze card"), never a negative, and never carries "On" or "Off" | `../components/library/toggle.md` |
| `A-ENUMERATION` | No copy states or implies whether an account, email, or phone number exists | `../patterns/auth.md` |
| `A-REVERSIBILITY` | A card action says in its own copy whether it can be undone | `../patterns/cards.md` |
| `A-CREDENTIALS` | Outside the app (email, push), nothing asks for a passcode, PIN, card details, or a code | `../patterns/emails.md`, `../compliance/security-payments.md` |
| `A-SUBJECT` | Transactional subject: front-loaded, about 50 characters, no emoji, no question bait, no ALL CAPS, no fake "Re:" | `../patterns/emails.md` |
| `A-PREHEADER` | Preheader adds information, is never empty and never "View in browser" | `../patterns/emails.md` |
| `A-PARAGRAPHS` | **Block level:** one fact per paragraph (two sentences only when short and linked), at most three paragraphs in a modal body | `../components/foundations/typography.md` |

One character, one complaint. `A-SYSTEM-ERROR` and `A-NO-RESULTS` used to re-check the
exclamation mark that `A-PUNCTUATION` already rejects, so the panel printed the same defect
twice under two names. The clause was removed from both, and `system-error-title` gained
`A-PUNCTUATION`, which its hand-written surface list had simply never included.

`A-NO-BANNED` also rejects the vague-failure phrases ("something went wrong", "oops",
"unexpected error", "technical difficulties") the vague-waiting ones ("please wait",
"almost there", "just a moment", "hang tight", "working on it"), the marketing claims
("the best", "the cheapest", "the fastest", "free forever", "no strings attached") the
blame phrases from `../terminology/banned-terms.md` ("you entered the wrong", "you failed
to", "you forgot to", "invalid") and the pressure words ("urgent", "act now", "last
chance", "hurry", "miss out", "final notice"), which are the grammar of fraud.

`A-PARAGRAPHS` is the first check that grades the **shape of a block** rather than the
words in it: it reads the paragraph breaks in the candidate, so a candidate for a modal or
sheet body must carry its real line breaks.

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

## Rules that are documented but not checked

`../terminology/capitalization-and-punctuation.md` names two rules that are deliberately not
implemented: curly quotes, and sentence case beyond Title Case detection. Both would produce
more noise than findings, and a noisy check teaches people to ignore it. They are listed
there so nobody assumes they are covered.

## Keeping the term list honest

`../terminology/banned-terms.md` is the source of truth and `assertions.py` implements it.
They drifted twice without anyone noticing, in both directions, and each gap was found by
accident when a bad string passed a check.

`python terms_sync.py` compares the two and fails on any difference. Run it whenever either
file changes, alongside `run_golden.py`.

The inclusive-language list is deliberately **not** part of that sync: it has its own source
file (`../voice-and-tone/inclusive-language.md`), its own check, and its own replacement
message per term, because "use this instead" is the whole point of that list.

## What a PASS means (and what it does not)

A green result from this file means one thing: **no rule in the catalog was broken**. It is
not a statement that the copy is good, and it is not a statement that the copy makes sense.

The distinction has a practical edge, found by breaking four fields on purpose:

| Broken copy | Caught by | Why |
| --- | --- | --- |
| "Retryyyy" | `A-REPEATED-CHARS` | A shape. Code sees it without understanding it. |
| "Oooh." | `A-REPEATED-CHARS`, `A-NO-BANNED` | Same shape, plus a listed word. |
| "Yeah." | `A-NO-BANNED` | A listed word. |
| "Cancel or die" | `A-CTA` | Two actions in one label is a shape too. |
| "We have sent your money." on a screen where nothing was sent | **nothing here** | The sentence is well formed. Only the judge, holding the intent, can see that it is false. |

Three of those four are shapes, and a shape is exactly what deterministic code is for. The
fourth is not, and no list of words will ever reach it. That is the boundary between the two
layers, and it is why an interface that shows **PASS** after running only this file is
over-claiming: the honest label is "no rule broken", with the judge verdict reported
separately, or "not evaluated" when the judge has not run.

## Extending

Add a check as a function in `assertions.py`, register it with a new ID, and reference that
ID from the golden-set cases. The catalog is meant to grow as the system does; not every
rule is code-checkable (those live in `rubric.md`).

## Checks that apply to every surface

`A-NO-BANNED`, `A-NO-CLAIMS`, `A-INCLUSIVE`, `A-LOCALIZABLE`, `A-REPEATED-CHARS` and `A-COLOR-ALONE` are appended to **every** surface list
automatically. Surface lists are hand-written, so a cross-cutting check added later would
otherwise reach only the surfaces someone remembered to update — which is exactly how the
inclusive-language check first missed `helper-text`.

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
| `accordion-header` | `A-ACCORDION-HEADER`, banned/claims, numerals |
| `accordion-body` | The body checks |
| `link` | `A-LINK-TEXT`, banned/claims, case, punctuation |
| `alt-text` | `A-ALT`, case, punctuation, `A-MASK`. An empty candidate is the decorative case and passes |
| `count-badge` | `A-BADGE` only |
| `chip` | `A-CHIP`, case |
| `search-placeholder` | `A-SEARCH-PLACEHOLDER`, case, punctuation |
| `no-results` | `A-NO-RESULTS`, case, punctuation, no inline CTA |
| `date-unavailable` | `A-DATE-UNAVAILABLE`, `A-DATE`, banned, punctuation, case |
| `category` | `A-CATEGORY-GUESS`, case, punctuation, banned |
| `chart-copy` | The body checks plus `A-CATEGORY-GUESS` |
| `fx-quote` | The body checks plus `A-FX` |
| `complaint-acknowledgement`, `complaint-answer` | The body checks plus `A-COMPLAINT` |
| `toggle-label` | `A-TOGGLE-LABEL`, no emoji, banned/claims |
| `toggle-description` | The body checks |
| `auth` | The body checks plus `A-ENUMERATION` |
| `auth-error` | The field-error checks plus `A-ENUMERATION` |
| `card-action` | The body checks plus `A-REVERSIBILITY` |
| `email-subject` | `A-SUBJECT`, banned/claims, `A-MASK`, money format, `A-CREDENTIALS` |
| `email-preheader` | `A-PREHEADER`, banned/claims, `A-MASK`, money format |
| `email-body` | The body checks plus `A-CREDENTIALS` |
| everything else (error, confirmation, empty-state, onboarding-step, disclosure, risk-warning, security, banner) | `A-NO-EMOJI`, `A-EURO-FORMAT`, `A-NO-BANNED`, `A-NO-CLAIMS`, `A-ACRONYMS`, `A-MASK` |

The app must select checks by surface. `assertions.run(text, surface="cta")` returns only
the CTA checks; passing an explicit list overrides the surface.
