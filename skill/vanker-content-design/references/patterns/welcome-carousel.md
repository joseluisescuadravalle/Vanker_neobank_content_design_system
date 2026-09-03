# Welcome carousel (pre-login)

**Status: normative (rules) + example (samples).**

The first screen of the app for someone who is not logged in: three cards that say what
Vanker is and why it is worth opening an account, with two fixed buttons underneath.

**This is not onboarding.** Nobody is being set up here. It is the product's argument,
addressed to a stranger, so it takes the **marketing voice** (see `../voice-and-tone/`)
and it carries the **highest regulatory exposure of any screen in the app**: everything
said here is a claim made to a prospective customer. The screen that opens a setup flow
inside the product is a different pattern (`flow-intro.md`).

## Structure

- **Three cards.** Not four. Each card carries one benefit and one idea; the fourth card
  is almost always a repeat or a promise that needs a footnote.
- **Two fixed buttons**, below the carousel, that do not move or change between cards:
  **"Join Vanker"** (primary) and **"Log in"** (secondary). Stacked, full width, primary on
  top (see `../components/library/sheet-modal.md`).
- **Page indicator:** three dots, tappable, showing which card is in view.

## Movement

**The carousel never advances on its own.** It moves when the person swipes or taps a dot.

This is not a stylistic preference. Content that moves automatically for more than five
seconds requires a mechanism to pause, stop, or hide it (WCAG 2.2.2), and a bank's first
screen failing that is a poor start. It is also bad content design: an argument that
advances while someone is still reading the first line is an argument nobody finishes.

- Swipe and dot taps only; no timer, no resume-after-idle.
- Motion follows `../components/foundations/motion.md` and is a plain horizontal slide.
- Under `prefers-reduced-motion`, the cards cross-fade instead of sliding.

## Card content

**A headline, and preferably nothing else.**

- **Headline** (required): the whole benefit in one line, up to about six words. Sentence
  case, no ending period, no emoji.
- **Body** (optional, and usually unnecessary): at most two short lines. It exists **only
  to expand the idea already in the headline**. It never introduces a second benefit, a new
  feature, a price, a condition, or a number the headline did not carry. If the body says
  something new, it belongs on its own card or nowhere.
- No call to action inside a card: the two buttons below are the only actions on the
  screen (see `../CLAUDE.md`).

## What this screen may and may not claim

Every line here is marketing copy from a regulated bank to someone who is not yet a
customer. `../compliance/disclosures.md` and `../compliance/principles.md` apply in full,
not as a reminder:

- **No return, profit, or safety promise.** Nothing "guaranteed", nothing "risk-free".
- **"Free" is never bare.** If a service is free, it is free with its condition stated, or
  it is not said here.
- **No price, rate, or fee without the disclosure it requires.** A rate needs its APR
  (Annual Percentage Rate) context; a fee needs its exact amount. If it does not fit on a
  card, it does not go on a card.
- **No deposit-protection claim** except in the exact form `../compliance/disclosures.md`
  allows.
- **No comparison with named competitors**, and no superlative that cannot be evidenced
  ("the best account", "the cheapest transfers").
- **No urgency and no scarcity.** There is no deadline on opening a bank account.
- Personality is allowed here, humor lightly; hype is not (see
  `../terminology/banned-terms.md`).

## Examples (illustrative)

| Card | Headline | Body (only if needed) |
| --- | --- | --- |
| 1 | "See every euro as it moves" | "Payments appear the moment they happen" |
| 2 | "Send money in seconds" | "Any day, at any hour" |
| 3 | "Save without thinking about it" | "Spaces set money aside as you go" |

Buttons: **"Join Vanker"** (primary), **"Log in"** (secondary).

Not this:

- "The best account in Europe" (unevidenced superlative).
- "Free forever, no strings attached" (a bare free claim).
- "Save with 3% and send money in seconds" (two benefits in one card, and a rate with no
  disclosure).
- "Join now before it is too late" (manufactured urgency).

## Accessibility

- The carousel is a list of three items, not a live region: it announces the card in view
  when the person moves it, and nothing when they do not.
- The dots are real controls with an accessible name ("Card 2 of 3") and a 44px target.
- The two buttons sit outside the carousel in the reading order, so they are reachable
  without swiping through the cards.
- Every card is reachable by keyboard and by screen reader in order.
- No information exists only inside a card the person may never see: the buttons and the
  meaning of the screen stand on their own.

## Machine-readable spec

```json
{
  "welcome-carousel": {
    "surface": "pre-login",
    "voice": "marketing",
    "cards": { "count": 3, "one-idea-per-card": true },
    "headline": { "required": true, "max-words": 6, "case": "sentence", "ending-period": false, "emoji": false },
    "body": { "required": false, "max-lines": 2, "expands-headline-only": true, "introduces-new-idea": false, "cta": false },
    "auto-advance": false,
    "advance-by": ["swipe", "dot-tap"],
    "reduced-motion": "cross-fade",
    "buttons": { "fixed": true, "primary": "Join Vanker", "secondary": "Log in", "layout": "stacked-full-width" },
    "indicator": { "type": "dots", "count": 3, "tappable": true, "accessible-name": "Card {n} of {total}" },
    "claims": {
      "returns-or-safety-promise": false,
      "bare-free": false,
      "rate-or-fee-without-disclosure": false,
      "deposit-protection": "only in the compliance-approved form",
      "named-comparisons": false,
      "unevidenced-superlatives": false,
      "urgency-or-scarcity": false
    }
  }
}
```

## Eval hooks

- Exactly three cards, each carrying one idea.
- The headline is one line, up to about six words, sentence case, with no ending period and
  no emoji.
- The body, when present, adds no benefit, feature, price, condition, or number that the
  headline did not carry.
- No call to action inside a card; the two buttons are fixed and do not change between
  cards.
- The carousel does not advance on its own.
- No guaranteed-return, risk-free, bare-free, urgency, scarcity, superlative, or named
  comparison claims.
- A rate or a fee appears only with the disclosure it requires, or not at all.
