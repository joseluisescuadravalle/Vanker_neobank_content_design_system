# Toggle

**Status: normative.**

A switch that turns one setting on or off, **immediately**. It is the only control in the
system that changes something the moment it is touched, with no submit and no confirmation
step.

That immediacy is the whole definition, and it is what decides when a toggle is the wrong
control.

## Toggle or checkbox

| | Toggle | Checkbox |
| --- | --- | --- |
| Takes effect | The moment it is touched | When the form is submitted |
| Lives in | A settings list, a detail screen | A form |
| Reversible | Always, instantly | Until submit |
| Consent, agreement, legal acceptance | **Never** | **Always** |

Two rules fall out of this:

- **A toggle never sits in a form that has a submit button.** If the change waits for a
  submit, it is a checkbox, and a switch that looks applied but is not is a lie about the
  person's own settings.
- **Consent is never a toggle.** Agreement to terms or to data processing requires a clear
  affirmative act recorded with the submission, and it belongs in a checkbox (see
  `checkbox.md` and `../../compliance/data-privacy.md`).

## The label names the setting, not the action

The label is a **noun phrase naming what is switched, or the state when it is on**. Verbs
belong to buttons (see `../../patterns/ctas.md`): a switch is not something you press to
make something happen, it is a thing that is on or off.

- ✅ "Face recognition", "Instant notifications", "Card frozen", "Rounding up"
- ❌ "Turn on notifications", "Freeze card", "Enable rounding" — these are buttons, and a
  button that leaves a switch behind confuses what state the person is in
- ❌ "Do not send notifications" — a negative label makes "off" a double negative, and
  nobody can tell what an unchecked "do not" means

Where the natural name is a verb phrase, name the resulting state instead: **"Card
frozen"**, not "Freeze card". It also keeps one vocabulary across the product, because
`Frozen` is already the status label for that card (see `status-label.md`).

- Up to about four words, sentence case, no ending punctuation, no emoji.
- **No "On" or "Off" text beside the switch.** The position is the state; words beside it
  duplicate it and, when a request fails, contradict it. The state is carried to screen
  readers by the control itself.

## The description

One line under the label, when the consequence is not obvious from the name.

- It says **what changes**, in the present ("Payments over 50 € will ask for your face"),
  not what to do.
- **Any cost, limit, or condition goes here, visible**, never behind a tooltip or an
  accordion (see `tooltip.md`).
- No call to action, no link into a flow. If the setting needs a flow to be configured, the
  row is not a toggle: it is a row that opens a screen.

## Immediacy, and the two exceptions

The switch applies at once. Two cases are not exceptions to that rule but to the control
itself:

1. **A change that lowers protection may require authentication first.** Freezing a card is
   safe and applies immediately; unfreezing it, raising a limit, or turning off a security
   step may ask for the passcode or a code (see `code-input.md`). The switch **does not
   move until that succeeds**.
2. **A change that is not instantly reversible is not a toggle.** Closing an account,
   cancelling a card, ending a subscription: those are actions with a confirmation, in a
   button (see `../../patterns/confirmations.md`).

**Never show the new state before it is true.** The switch moves when the change is
confirmed, not when the finger lifts — the same rule as the payment that never says "Sent"
before it is (see `../../patterns/loading.md`). While it is in flight the row shows an
inline progress indicator and the switch is not operable.

## When it fails

- The switch **returns to its previous position**, and the row says why in one line, in
  place: "We couldn't turn this on just now. Please try again in a moment."
- It never snaps back silently, and it never leaves the person believing a security setting
  is on when it is not.
- If the failure touches money or security, the message follows `../../patterns/errors.md`
  and spells out the negative.

## States

| State | Treatment |
| --- | --- |
| Off | Track `color.surface-subtle`, knob `color.surface`, 1px border |
| On | Track `color.accent` (fuchsia), knob white |
| In flight | Switch not operable, inline progress in the row |
| Focus | Fuchsia focus ring around the switch |
| Disabled | `color.text-tertiary`, not operable, with the reason written next to it, never only grey |

Switch 51 × 31px, knob 27px, `radius.full`, whole row tappable with a minimum 44px target.

## Motion

- The knob travels over `motion.duration.fast` (120ms), `motion.easing.inout`; the track
  color crossfades over the same time.
- Under `prefers-reduced-motion` the knob and color change with no transition.
- Nothing bounces, and the row never animates its height.

## Accessibility

- `role="switch"` with `aria-checked`, or a native checkbox styled as a switch: the state is
  programmatic, never inferred from position or color.
- The label is tied to the control, and tapping the label or the row toggles it.
- The state is announced on change ("on" / "off"), and a failure is announced politely with
  the reason.
- The description is linked with `aria-describedby`, so the consequence is read with the
  setting.
- Color is never the only signal of state (position, and the announced value, carry it too).

## Content examples

- ✅ "Instant notifications" · "You'll get a message the moment a payment leaves your
  account"
- ✅ "Card frozen" · "Nobody can pay with this card while it's frozen"
- ✅ "Rounding up" · "We round each payment up to the next euro and move the difference to
  your Savings space"
- ❌ "Turn on notifications" (a button label on a switch)
- ❌ "Do not share my data" (a negative label; and consent is a checkbox)
- ❌ A switch showing "On" text beside it
- ❌ A switch that moves before the change is confirmed

## Machine-readable spec

```json
{
  "toggle": {
    "applies": "immediately",
    "never": ["inside a form with a submit", "for consent or legal agreement", "for an irreversible change"],
    "label": {
      "form": "noun-phrase-or-state",
      "action-verb": false,
      "negative": false,
      "max-words": 4,
      "case": "sentence",
      "ending-punctuation": false,
      "on-off-text": false
    },
    "description": { "required": "when the consequence is not obvious", "tense": "present", "cost-or-limit": "visible here", "cta": false },
    "authentication": { "required-when": "the change lowers protection", "switch-moves-only-on-success": true },
    "optimistic-ui": false,
    "in-flight": { "operable": false, "indicator": "inline" },
    "failure": { "returns-to-previous-position": true, "silent": false, "message-in-row": true },
    "switch": { "width": 51, "height": 31, "knob": 27, "radius": "radius.full", "on": "color.accent", "min-target": 44 },
    "motion": { "duration": "motion.duration.fast", "easing": "motion.easing.inout", "reduced-motion": "none" },
    "a11y": { "role": "switch", "aria-checked": true, "label-tied": true, "row-tappable": true, "state-announced": true, "describedby": true, "color-alone": false }
  }
}
```

## Eval hooks

- The label is a noun phrase or a state, never an action verb and never a negative.
- No "On" or "Off" text sits beside the switch.
- Consent, agreement, and legal acceptance are checkboxes, never toggles.
- No toggle sits in a form with a submit button.
- The description states any cost, limit, or condition in place, with no call to action.
- The switch does not move before the change is confirmed, and a failure returns it to its
  previous position with a reason in the row.
- A change that lowers protection is authenticated before the switch moves.
