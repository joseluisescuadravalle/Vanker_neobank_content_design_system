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

## Eval hooks

- Title front-loads the key fact; about 40 characters or fewer.
- Body about 120 characters or fewer (fits two lines); no emoji in the body.
- Emoji (1-2) only in a non-critical title; never in security, fraud, or money-movement push.
- Money notifications state the amount in European format.
