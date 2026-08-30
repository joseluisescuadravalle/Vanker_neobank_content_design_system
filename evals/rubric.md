# LLM-as-judge rubric

**Status: tooling.**

For the qualities that code cannot check. A judge model scores a candidate string against
these dimensions, using this repository as the reference. Score each dimension 0, 1, or 2.

| Dimension | 0 (fail) | 1 (partial) | 2 (pass) |
| --- | --- | --- | --- |
| **Voice** | Off-brand (hype, cold, or slangy) | Mostly on-brand, slips once | Sounds like Vanker: fresh, clear, calm |
| **Tone fit** | Wrong for the moment (jokey in an error) | Slightly off | Right tone for the stakes (see `../voice-and-tone/tone.md`) |
| **Clarity** | Confusing or jargon-heavy | Understandable with effort | Plain, first-read clear, short sentences |
| **Terminology** | Wrong or invented terms | Minor slip | Uses the controlled vocabulary and format exactly |
| **Pattern fit** | Ignores the pattern | Partial | Follows the pattern (anatomy, rules) for the surface |
| **Compliance** | Missing or wrong required content | Present but weak or buried | Adequate and clear (see `../compliance/`) |
| **Accessibility** | Relies on color alone, unclear errors | Minor issue | Meets the content accessibility rules |

## Scoring

**Not every dimension applies to every surface.** A button has no compliance content of
its own, and a status label has no tone to speak of. Score those `na`; they are left out of
the total rather than counted as a pass.

- **Overall pass** requires all three:
  1. every applicable dimension is at least 1,
  2. Compliance and Tone fit are never 0,
  3. the total is at least **85% of the maximum available** for the applicable dimensions.
- The percentage replaces the old "12 of 14", which silently failed every surface where a
  dimension did not apply: a perfect CTA scored 10 of a possible 10 and was marked down
  against a maximum it could never reach.

## Use

Run the judge only on candidates that already passed the deterministic assertions (the
cheap gate). Feed the judge the case, the candidate, and the rubric via `judge-prompt.md`.
