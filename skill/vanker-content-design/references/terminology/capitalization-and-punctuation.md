# Capitalization and punctuation

**Status: normative. Always applied.**

These rules were scattered across eleven files, one clause at a time, and an agent had to
read the whole system to infer them. This is where they live now. Everything here applies
to **customer-facing copy**, not to this documentation.

## Capitalization

**Sentence case, everywhere.** Only the first word is capitalized, plus what is a name in
its own right.

- **Capitalized:** Vanker, Spaces, and any other product or feature name; people's names;
  place names; acronyms (IBAN, SEPA, PIN).
- **Lowercase:** every generic banking noun, even when it feels important — account, card,
  transfer, balance, payment, statement, limit, passcode.
- **Never Title Case.** "Send Money To A Friend" belongs to another brand.
- **Never ALL CAPS in the string.** Where a design calls for uppercase (the `overline` type
  token), the **style** applies it and the copy stays sentence case. Uppercase typed into
  the text is read out letter by letter by some screen readers, breaks when the design
  changes, and cannot be translated.

## The period: it marks a sentence, not a label

This one rule generates most of the table below. If the string is a **label** — something
that names, titles, or tags — it takes no ending period. If it is a **sentence of body
copy**, it takes one, even when it is the only sentence.

| Element | Ending period | Other punctuation |
| --- | --- | --- |
| Button, CTA | **No** | None at all: no comma, colon, question or exclamation mark |
| Label in | **No** | No colon, no question mark |
| Label out | **No** | A question mark is allowed; a colon is not |
| Legend | **No** | No colon |
| Placeholder | **No** | Format only (`DD/MM/YYYY`) |
| Helper text | **Yes** | Never a question |
| Field error | **Yes** | Never "?" or "!" |
| Error summary title | **No** | — |
| Modal or sheet title | **No** | A question mark is allowed ("Report this card?") |
| Modal or sheet body | **Yes** | One fact per paragraph |
| Toast | **No** | Never "?" or "!" |
| Banner title | **No** | — |
| Banner description | **Yes** | — |
| Status label | **No** | Nothing at all |
| Accordion header | **No** | A question mark is allowed |
| Toggle label | **No** | Nothing at all |
| Push title | **No** | — |
| Push body | **Yes** | — |
| Email subject and preheader | **No** | No question bait |
| Carousel headline | **No** | — |
| Carousel body | **No** | — |
| Counter | **No** | — |
| Tooltip | **Yes** | Complete sentences |
| List item that is a phrase | **No** | — |
| List item that is a sentence | **Yes** | — |

## The rest of the marks

- **Exclamation mark: never.** Not in errors, not in success, not in marketing. Vanker's
  warmth comes from what it says, not from shouting it.
- **Question mark:** only where something is genuinely being asked — a modal title, a label
  out, an accordion header, a permission heading. Never as an attention device in a subject
  line.
- **Semicolon: never.** Two sentences, or a comma.
- **Em dash and en dash: not in product copy.** Use a comma, a full stop, or parentheses.
  They are hard to read at small sizes, they are typed inconsistently, and they complicate
  translation.
- **Ellipsis: never in copy.** Not "Loading…", not to imply more. The only ellipsis a person
  should see is the one the system renders when it truncates a value.
- **Colon:** to introduce a value or a list, never at the end of a label.
- **Ampersand:** only in a tight label where the words do not fit. Never in body copy (see
  `banned-terms.md`).
- **Oxford comma: yes.** "Your name, your address, and your date of birth." American English
  baseline, and it removes a real ambiguity in a list of legal items.
- **Quotation marks and apostrophes: curly** (`’`, `“ ”`), never straight.
- **Latin abbreviations: never.** "for example", not "e.g."; "that is", not "i.e."; and
  nothing ends with "etc." — either the list is complete or it says what the rest are.
- **Ranges take "to", never a hyphen.** "3 to 5 working days", never "3-5". In a bank a
  hyphen between figures reads as a minus sign, and a minus sign next to money means
  something.
- **The minus sign is the real minus (−), not a hyphen**, wherever it marks money going out
  (see `../components/library/transaction-row.md`).
- **Percentages have no space:** `0,5%`.

## Documented but not automatically checked

Two rules here are deliberately not in `../evals/assertions.py`, and it is better to say so
than to let someone assume they are covered:

| Rule | Why not |
| --- | --- |
| Curly quotes and apostrophes | It is a rendering and tooling concern as much as a copy one; flagging every straight apostrophe would drown the real findings |
| Sentence case in every string | Only Title Case is detectable with confidence; a two-word string with one proper noun is indistinguishable from a mistake |

Everything else on this page is enforced by `A-PUNCTUATION`, `A-CASE`, or the per-surface
checks listed in `../evals/assertions.md`.

## Eval hooks

- No exclamation mark anywhere in customer copy.
- No semicolon, em dash, en dash, or ellipsis in product copy.
- No "e.g.", "i.e." or "etc.".
- A range uses "to", never a hyphen between figures.
- No Title Case, and no ALL CAPS typed into a string.
- The ending period follows the label-or-sentence rule for the element.
