# Count badge

**Status: normative.**

The small number, or dot, sitting on a navigation icon or at the end of a row: three
messages, two cards waiting to be activated, something new in a screen the person has not
opened.

This is not a status label (`status-label.md`), which names the state of an object and
carries no digits. A badge carries **only** a count.

## A badge is a debt

Every badge asks to be cleared. That is its whole power, and the reason it is so easy to
abuse:

- **Only badge something the person can act on and would want to.** A badge on a screen
  that holds nothing for them is a bill for a debt they do not owe.
- **Never badge marketing.** "New!" on a promotion borrows the language of "something of
  yours is waiting" for something nobody asked for. It is the fastest way to teach people
  that badges are noise, and once they learn it, the badge that mattered is gone too.
- **A badge clears when the thing behind it has been dealt with**, not when the screen was
  opened. A badge that comes back without a new event trains people to ignore all of them.
- **Zero is never shown.** No `0` badge, no empty circle: nothing to clear means no badge.

## Number or dot

| Show | When |
| --- | --- |
| **The number** | The count changes what the person does or expects: 3 messages, 2 payments to confirm |
| **A dot** | Something is new but the number would not change anything, or we do not know it |

- **The count is capped**: `9+` on a tab or navigation icon, `99+` in a list row where there
  is space. Never a five-digit number squeezed into a circle.
- **Nothing but digits and the plus.** No currency, no words, no "new", no punctuation, no
  emoji.
- **Never a money amount.** A badge counts things; an amount is text on the screen.

## Style

- Fill `color.accent` (fuchsia) with `color.on-primary` text, `radius.full`, minimum 16px,
  `caption` type in tabular numbers.
- **Not red.** In this system the semantic colors mean one thing each and are never
  decorative (see `../foundations/color.md`): three unread messages are not an error. The
  accent is the brand's emphasis color and this is exactly the small moment it is for.
- The dot is 8px, same fill, no text.
- It sits at the top-right of the icon it marks, overlapping it, never pushing the layout.

## Accessibility

- **The badge is part of the accessible name of the thing it marks**, never a separate
  announcement: "Cards, 3 new", not an icon called "Cards" followed by a stray "3".
- **The dot needs a word too.** A dot conveys "new" by shape and position alone, so its
  accessible name says it: "Messages, new".
- The count updates in a **polite** live region when it changes while the person is on the
  screen; it never interrupts.
- Never rely on the badge alone to tell someone something needs attention: the screen it
  points to says what it is.

## Machine-readable spec

```json
{
  "count-badge": {
    "carries": "a count only",
    "content": { "digits-only": true, "plus-cap": true, "words": false, "currency": false, "amount": false, "emoji": false },
    "cap": { "icon": "9+", "row": "99+" },
    "zero": "no badge",
    "dot-when": "something is new but the number would not change what the person does",
    "never-badge": ["marketing", "screens with nothing to act on"],
    "clears-on": "the thing being dealt with, not the screen being opened",
    "style": { "fill": "color.accent", "text": "color.on-primary", "radius": "radius.full", "min-size": 16, "dot-size": 8, "semantic-red": false },
    "a11y": { "part-of-parent-name": true, "dot-has-a-name": true, "live-region": "polite", "sole-signal": false }
  }
}
```

## Eval hooks

- A badge contains digits and an optional `+`, and nothing else: no words, no currency, no
  amount, no emoji.
- No badge shows zero.
- The count is capped (`9+`, `99+`) rather than shown in full.
- A badge is never used for marketing or for a screen with nothing to act on.
- The badge is announced as part of the name of what it marks, and a dot has a word.
