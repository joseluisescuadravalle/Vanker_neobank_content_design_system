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
| everything else (error, confirmation, empty-state, notification, onboarding-step, disclosure, risk-warning, security, banner, toast) | `A-NO-EMOJI`, `A-EURO-FORMAT`, `A-NO-BANNED`, `A-NO-CLAIMS`, `A-ACRONYMS` |

The app must select checks by surface. `assertions.run(text, surface="cta")` returns only
the CTA checks; passing an explicit list overrides the surface.
