# Assertions (deterministic checks)

**Status: tooling.**

Black-and-white rules a machine can verify, drawn from the "Eval hooks" across the system.
Each has an ID used in `golden-set/cases.jsonl` and implemented in `assertions.py`.

## Format and terminology

| ID | Checks | Source |
| --- | --- | --- |
| `A-NO-EMOJI` | No emoji anywhere | `../voice-and-tone/voice.md` |
| `A-EURO-FORMAT` | € after the amount; dot thousands, comma decimals; no ",00" on round amounts | `../terminology/glossary.md` |
| `A-NO-BANNED` | No banned or jargon terms | `../terminology/banned-terms.md` |
| `A-ACRONYMS` | Known acronyms are expanded on first use | `../terminology/glossary.md` |

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
| everything else (error, confirmation, empty-state, onboarding-step, disclosure, risk-warning, security, banner) | `A-NO-EMOJI`, `A-EURO-FORMAT`, `A-NO-BANNED`, `A-NO-CLAIMS`, `A-ACRONYMS` |

The app must select checks by surface. `assertions.run(text, surface="cta")` returns only
the CTA checks; passing an explicit list overrides the surface.
