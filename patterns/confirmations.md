# Confirmations

**Status: normative (rules) + example (samples).**

Copy that asks the person to confirm an action, or tells them it is done. Two moments:
the **pre-action confirmation** (here is what will happen) and the **post-action
confirmation** (it worked).

## Pre-action confirmation

Use before anything with real consequences: moving money, sharing details, or a
destructive action.

Rules:
- State exactly what will happen: what, how much, to whom, when, and any fee.
- No hidden surprises. If there is a fee or a delay, it appears here.
- The primary button restates the action, for example "Send {amount} €" (see `ctas.md`).
- For destructive actions, name the consequence and make the safe choice the easy one.

Examples:
- Do: "You are sending {amount} € to {recipient} by SEPA transfer. It will arrive today. There is no fee."
- Not: "Are you sure you want to continue?"
- Destructive, Do: "Deleting this space will move its {amount} € back to your current account. This cannot be undone."
- Destructive, Not: "Are you sure?"

## Post-action confirmation

Use to close the loop after the action succeeds.

Rules:
- Confirm what happened, in past tense, plainly.
- Include the useful detail: amount, recipient, when it arrives.
- Calm affirmation, not celebration (see `../voice-and-tone/tone.md`, "Success"). No emoji.
- Offer the sensible next step, if there is one, as a low-key option.

Examples:
- Do: "Sent. {amount} € is on its way to {recipient} and should arrive today."
- Not: "Success!!!"
- Do: "Your Travel space is set up. You can add money to it whenever you like."
- Not: "Done."

## Eval hooks

- Pre-action money confirmations state amount, recipient, timing, and fee (or "no fee").
- Destructive confirmations name the consequence and whether it can be undone.
- Post-action confirmations use past tense and include the key detail.
- No emoji, no exclamation-heavy celebration.
