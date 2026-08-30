# Cards

**Status: normative (rules) + example (samples).**

Everything a person does with a card once they have one: freezing it, reporting it lost,
activating it, seeing its details and PIN, changing its limits, and replacing or cancelling
it.

The card's state vocabulary is in `../components/library/status-label.md`; the freeze
switch is `../components/library/toggle.md`; what Vanker never asks for is in
`../compliance/security-payments.md`.

## The three actions people confuse

This is the whole design problem of the screen. Three actions sit next to each other, two
of them sound alike, and one of them cannot be undone.

| Action | Who does it | Reversible | Card afterwards |
| --- | --- | --- | --- |
| **Freeze** | The person, instantly | **Yes**, any time | `Frozen`, and it works again on unfreezing |
| **Report lost or stolen** | The person, and we cancel the card | **No** | `Canceled`, and a new card is ordered |
| **Cancel** | The person no longer wants it | **No** | `Canceled`, with no replacement |

Rules that follow, and they are absolute:

1. **Every one of these actions states its reversibility in the copy**, in the same breath
   as the action. "You can unfreeze it any time." / "This card will stop working for good."
   Never leave it to the button colour or to a warning icon.
2. **An irreversible action never looks or reads like a reversible one.** Freezing is a
   switch; reporting and cancelling are actions with a confirmation
   (`confirmations.md`), never switches (see `../components/library/toggle.md`).
3. **Freeze comes first and is reachable in one tap** from the card screen. Someone who has
   just lost a card is frightened and fast, and the safe, reversible action is the one that
   should be easiest to reach.

## Reporting a card lost or stolen

The most stressed moment in the product. The first line is not a form.

**One fact per paragraph**, never one block of four lines (see
`../components/foundations/typography.md`):

> **Report this card?**
>
> Your money is safe.
>
> This card will stop working for good, and we'll send you a new one.
>
> The replacement is free and usually arrives in 3 to 5 working days.

- **Reassure about the money before anything else**, in its own paragraph.
- Then the consequence, in plain words.
- Then the cost, exactly, or the fact that there is none (see
  `../compliance/disclosures.md`), and the delivery time as a measured range, never "soon".
- Buttons: "Report card" (primary), "Cancel" (secondary).
- **Never ask why before acting.** Any question about what happened comes after the card is
  dead, and it is optional.
- Never imply the person was careless.

## Activating a card

- The screen that opens the activation flow is a flow intro (`flow-intro.md`): its primary
  button is "Start", because the tap opens the first step and does not activate anything.
- Where activation genuinely happens on one tap, the button names it: "Activate card".
- Say what activation does in one line, and what stops working if there was an old card.

## Card details and PIN

- The full number, expiry, and CVV (Card Verification Value) are **hidden by default** and
  shown only after authentication (`auth.md`).
- Say the details hide again, and when: "These details hide again in 30 seconds."
- Copying a detail is allowed; say what was copied ("Card number copied"), and never leave
  it on the clipboard longer than the screen is open.
- **Vanker never asks for the PIN inside the app**, and the PIN screen says so. Showing a
  PIN is authenticated like the details; the PIN is never sent by email, message, or push
  (see `../compliance/security-payments.md`).
- No card detail ever appears in a notification, a toast, or a screenshot-friendly summary
  (see `A-MASK` and `../compliance/data-privacy.md`).

## Limits

- A limit is stated with its exact amount and its period: "You can spend up to 1.500 € a
  day with this card."
- **Raising a limit lowers protection**, so it is authenticated before it applies, and the
  switch or field does not move until that succeeds (`../components/library/toggle.md`).
- Lowering a limit applies immediately.
- Never present a limit as a punishment or as our generosity; it is a setting.

## Replacement and delivery

- "Your new card is on its way. It usually arrives in 3 to 5 working days."
- The status label while it travels is `On its way`; once delivered it is `Not activated`
  until the person activates it (`../components/library/status-label.md`).
- Any fee is stated exactly before the person confirms, or the copy says the replacement is
  free.
- Never promise a date we cannot keep. A range from measured data, or nothing.

## Virtual cards

- A virtual card is created and deleted in the app, and the copy says both: "You can delete
  it whenever you want."
- Deleting one is irreversible for that card number, and the copy says so.
- Never suggest a virtual card is more or less protected than a physical one unless that is
  factually true and stated in `../compliance/`.

## What this pattern never does

- Never presents an irreversible card action without saying it is irreversible.
- Never uses a switch for something that cannot be switched back.
- Never blames the person for a lost or stolen card.
- Never shows a card number, CVV, or PIN outside an authenticated screen.
- Never asks for the PIN inside the app.
- Never states a delivery date it cannot keep, or a fee vaguely.

## Machine-readable spec

```json
{
  "cards": {
    "actions": {
      "freeze": { "reversible": true, "control": "toggle", "status": "Frozen", "one-tap-from-card-screen": true },
      "report-lost-or-stolen": { "reversible": false, "control": "action + confirmation", "status": "Canceled", "orders-replacement": true },
      "cancel": { "reversible": false, "control": "action + confirmation", "status": "Canceled", "orders-replacement": false }
    },
    "reversibility-stated-in-copy": true,
    "report-flow": { "reassure-money-first": true, "ask-why": "after, and optional", "blame": false, "fee": "exact or free", "delivery": "measured range" },
    "details": { "hidden-by-default": true, "requires-authentication": true, "auto-hide-stated": true, "in-notifications": false },
    "pin": { "asked-inside-the-app": false, "sent-by-message": false, "requires-authentication": true },
    "limits": { "amount-and-period-stated": true, "raising": "authenticated before it applies", "lowering": "immediate" },
    "replacement": { "status-while-travelling": "On its way", "status-on-arrival": "Not activated", "delivery": "3 to 5 working days, measured", "fee": "exact or free" },
    "virtual": { "delete-is-irreversible": "stated", "protection-claims": "only if in compliance/" }
  }
}
```

## Eval hooks

- Every card action states whether it can be undone, in the same copy as the action.
- An irreversible action is never a switch, and never worded like a reversible one.
- The lost-or-stolen flow reassures about the money before it explains anything else, and
  never asks why before acting.
- A replacement states its fee exactly or says it is free, and gives a measured range rather
  than a date.
- Card numbers, CVV, and PIN never appear outside an authenticated screen, and never in a
  notification.
- The copy never asks the person to type their PIN into the app.
- Limits state their exact amount and period, and raising one is authenticated first.
