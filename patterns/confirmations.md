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
- The primary button is a clear action verb ("Send money"); it never repeats the amount, which is already shown in the summary (see `ctas.md`).
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

## Machine-readable spec

```json
{
  "confirmations": {
    "pre-action": {
      "required-when": ["irreversible", "moves money", "lowers protection"],
      "title": { "starts-with-the-action-verb": true, "form": "question", "ending-period": false },
      "body": { "required-when": "irreversible or with consequences", "states-reversibility": true },
      "actions": { "count": 2, "layout": "stacked", "primary-on-top": true, "primary-mirrors-the-title-verb": true }
    },
    "post-action": { "surface": "toast or full screen", "tense": "past", "celebration": "restrained" }
  }
}
```

## Eval hooks

- Pre-action money confirmations state amount, recipient, timing, and fee (or "no fee").
- Destructive confirmations name the consequence and whether it can be undone.
- Post-action confirmations use past tense and include the key detail.
- No emoji, no exclamation-heavy celebration.

## Confirmation dialog: content structure

For a dialog that asks the person to confirm an action before it happens, especially a
destructive one. (When the action needs a data summary before confirming, such as a
payment, use the review sheet described above instead.) It is a set of slots.

### Slots

- **Title** (required): asks the person to confirm the action, **starting with the action
  verb and naming the object**, as a question ("Delete this space?"). Never vague ("Are you
  sure?"), never just the verb ("Delete?").
- **Body** (optional): included **only if the action is irreversible or has consequences**.
  It states the consequence ("You will not be able to get the data back."). It never
  repeats the title and never contains a CTA.
- **Actions** (exactly two, stacked, primary on top):
  - **Primary:** the action verb from the title ("Delete").
  - **Secondary:** the way out ("Cancel").

### Rules

- Exactly two CTAs.
- The primary CTA is the title's verb; the secondary is the exit.
- A destructive dialog does not dismiss on a scrim tap (see
  `../components/library/sheet-modal.md`).

### Example

- Title "Delete this space?" / Body (only if irreversible) "You will not be able to get the
  data back." / **Delete** (primary), **Cancel** (secondary).

### Eval hooks (per slot)

- Title starts with the action verb and is a question, never "Are you sure".
- Body appears only for irreversible or consequential actions, never repeats the title, and
  never contains a CTA.
- Exactly two CTAs; primary uses the title's verb; secondary is the exit.
