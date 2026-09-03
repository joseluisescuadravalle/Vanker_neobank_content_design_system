# Notifications (push)

**Status: normative (rules) + example (samples).**

A push notification arrives outside the app, in the OS notification tray, and competes for
attention. It has two slots and **no CTA** (tapping it opens the app).

## Slots

- **Title** (required): very short, **front-loaded** with the key fact. The OS renders it
  bold; that is the platform, not our styling. Guideline: about 40 characters.
- **Body** (required): fits one or two lines when collapsed; commas and an ending period are
  fine. Front-loaded, with the useful detail (amount in European format). Guideline: about
  120 characters. **No emoji in the body.**

No CTA: the action is the tap, which opens the app.

## Emoji (the one exception to the no-emoji rule)

- One or two emoji are allowed **only** in the **title** of a **non-critical** push
  (marketing, celebration, informational).
- **Never** in a security, fraud, or money-movement push (payment sent or received), and
  **never** in the body.
- An emoji is never the only carrier of meaning (a screen reader reads its name); it never
  replaces a word.

## Front-load

Put the key fact in the first few words of both title and body; people read the tray at a
glance.

## Types

| Type | Emoji in title | Tone |
| --- | --- | --- |
| Money in / out | No | Precise |
| Security / fraud | No | Serious |
| Low balance | No | Calm |
| Marketing / celebration / info | Up to 2 | Lighter |

## Examples

- **Money received:** Title "Money in" / Body "You received 150 € from Ana."
- **Payment sent:** Title "Payment sent" / Body "150 € is on its way to Luis García."
- **Security:** Title "Confirm it is you" / Body "We paused a payment that looks unusual. Open the app to review it."
- **Low balance:** Title "Low balance" / Body "Your current account is down to 12 €."
- **Marketing:** Title "Smarter savings ✨" / Body "Meet the tools that help your money work harder."

## The lock screen

A push is read by whoever is looking at the phone, not only by its owner.

- The amount and the counterparty may appear: people expect a bank to tell them, and hiding
  them makes the notification useless.
- **The balance never appears.** "You received 150 €" is fine; "Your balance is now
  2.540,75 €" is not.
- Card details never appear, and no identifier appears unmasked (see `A-MASK`).
- A one-time code may appear, because the notification **is** the channel for it, but that
  push carries nothing else, is never grouped with others, and the code never appears again
  in a later push or inside the app (`../components/library/code-input.md`).

## The tap, the timing, and repetition

- **The tap opens the thing the notification is about**, not the home screen. A push about
  a payment opens that payment. Landing somewhere else makes the person hunt, and it is the
  fastest way to teach them to ignore notifications.
- **Money and security messages send immediately, at any hour.** Everything else respects
  quiet hours and is never sent at night.
- **One event, one notification.** Never send the same event twice, and never send a push
  and then a second push correcting it: if the outcome is not certain, wait for it.
- **The same event tells the same story here, in email, and in the app** — the same amount
  format, the same state vocabulary, the same name. See `emails.md`.

## Machine-readable spec

```json
{
  "push": {
    "slots": { "title": { "max-chars": 40, "front-loaded": true, "emoji": [0, 2] }, "body": { "max-chars": 120, "emoji": false } },
    "cta": false,
    "emoji-allowed-in": "non-critical title only",
    "emoji-never-in": ["security", "fraud", "money movement", "any body"],
    "lock-screen": { "amount": true, "counterparty": true, "balance": false, "card-details": false, "code": "only in a push that carries nothing else" },
    "tap-opens": "the thing it is about",
    "timing": { "money-and-security": "any hour", "everything-else": "respects quiet hours" },
    "one-event-one-notification": true,
    "matches-email-and-in-app": true
  }
}
```

## Eval hooks

- Title front-loads the key fact; about 40 characters or fewer.
- Body about 120 characters or fewer (fits two lines); no emoji in the body.
- Emoji (1-2) only in a non-critical title; never in security, fraud, or money-movement push.
- Money notifications state the amount in European format.
- No push shows the balance, a card detail, or an unmasked identifier.
- A code push carries the code and nothing else.
- The amount, the state vocabulary, and the counterparty name match the email and the
  in-app state for the same event.
