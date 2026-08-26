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

- **Overall pass** requires: every applicable dimension >= 1, **Compliance = 2**, and a
  total of at least 12 of 14 (for surfaces where all dimensions apply).
- Compliance and Tone fit are never allowed to be 0 on a pass. A single 0 on either is an
  automatic fail, however good the rest.

## Use

Run the judge only on candidates that already passed the deterministic assertions (the
cheap gate). Feed the judge the case, the candidate, and the rubric via `judge-prompt.md`.
