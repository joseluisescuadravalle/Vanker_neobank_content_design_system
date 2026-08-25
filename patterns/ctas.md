# Calls to action (CTAs)

**Status: normative (rules) + example (samples).**

Buttons and links that start an action. The label must tell the person exactly what
happens when they tap it.

## Rules

- Lead with a verb. Say the specific action, not "OK", "Submit", or "Continue" when a
  clearer verb exists.
- Match the label to the outcome. "Send €{amount}" beats "Confirm" on a payment button.
- Keep it short: an action verb phrase, 3 words maximum.
- A button label is only the action. Never put a message, status, notification, or toast text in a button.
- Sentence case, no ending period, no emoji.
- One primary action per screen. Secondary actions are lower emphasis.
- Be honest about consequence. A destructive action says so ("Delete space"), it never
  hides behind a vague word.

## Primary vs secondary

- **Primary:** the main, positive path. Specific verb.
- **Secondary:** the way out or the lesser action. Neutral: "Cancel", "Not now", "Back".

## Examples

| Context | Primary (Do) | Avoid |
| --- | --- | --- |
| Send money | Send €{amount} | Confirm |
| Add a card | Add card | Submit |
| Create a space | Create space | OK |
| Confirm identity | Confirm identity | Proceed |
| Move money to a space | Move €{amount} | Continue |
| Freeze a lost card | Freeze card | Manage |
| Delete a space | Delete space | Remove |
| Dismiss a promo | Not now | Cancel |

## Eval hooks

- Label starts with a verb, except neutral secondaries ("Cancel", "Not now", "Back").
- 3 words or fewer.
- No ending punctuation, no emoji.
- Money actions state the amount where it is known.
