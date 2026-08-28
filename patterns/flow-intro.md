# Flow intro

**Status: normative (rules) + example (samples).**

The single screen that opens a multi-step process inside the product: activating biometric
signing, verifying identity, ordering a card, setting up a direct debit. One screen, one
job — get the person to the first step **prepared**, or let them leave without cost.

This is product, not marketing: the person is already a customer and already inside the
app. The pre-login argument is a different pattern (`welcome-carousel.md`). The individual
steps that follow are `../components/library/onboarding-step.md`.

## The screen's real job

Most abandonment in a multi-step flow does not happen at the step that fails. It happens
at step 3, when the person discovers they need a document that is in a drawer in another
room. **This screen is where that is prevented**, so its body is not a summary: it is a
briefing.

Three facts, in this order, and only the ones that are true:

1. **How many steps.** "Three steps."
2. **How long it takes** — only from measured data, as a range, never invented (the rule in
   `loading.md` applies here too). "About two minutes."
3. **What they need at hand.** The card, the identity document, the phone that receives
   the messages. This is the fact that saves the flow.

## Slots

- **Title** (required): what the feature or service is, in the person's words. One line, no
  ending period. It explains the thing, it does not sell it.
- **Body** (required): the briefing above, in at most three short lines. It may also carry
  one relevant condition or consequence (what happens to their data, what changes after).
- **Steps** (optional): at most three, each a short phrase in the person's words. Where the
  flow has more than three, group them; a list of seven steps is a reason to leave.
- **Primary button**: **"Start"**.
- **Secondary button**: **"Not now"**.
- **This screen is not a step.** The step indicator starts counting after it: the first
  real step is 1 of 3, not 2 of 4.

## The buttons

**"Start", always.** Tapping the primary button does not activate biometric signing, verify
an identity, or order a card: it opens the first step. A label that names the end goal
("Activate biometrics") promises something the tap does not deliver. See the master rule in
`ctas.md`: the label names what happens on tap, and a low-commitment, honest verb beats a
specific one that misdescribes the result.

**"Not now", not "Cancel" and not "Exit".** Nothing has started, so there is nothing to
cancel, and the person is not escaping anything. "Not now" states the truth: they can do
this later. It is also the wording that makes it a real choice rather than a shamed one.

- Never a shaming secondary ("No thanks, I do not want my account to be secure").
- Never remove the secondary to force the flow, unless the flow is genuinely mandatory (a
  regulatory step), and then say so on the screen rather than hiding the exit.
- Stacked, full width, primary on top.

## Rules

- **Explain the value in one line at most**, and only where it is not obvious. This screen
  informs; the argument for the feature belongs earlier, where the person chose it.
- **No fear.** Not "your account is at risk without this". Say what the feature does.
- **State a requirement before it becomes a blocker**, never at the step where it stops
  them.
- **Say what happens with their data** where the flow collects something sensitive (an
  identity document, a selfie, a bank connection), in one plain line, linking to the detail
  (see `../compliance/data-privacy.md`).
- **Say if it can be paused.** "You can finish this later" is worth more than a paragraph
  of reassurance, and if it cannot be paused, say that instead.
- **No progress bar on this screen.** There is no progress yet.

## Example (illustrative)

**Title:** "Sign your payments with your fingerprint"

**Body:** "It takes three steps and about two minutes. You will need your card and the
phone where you receive our messages. You can finish this later if you need to."

**Steps:** "Confirm your identity" · "Register your fingerprint" · "Try it once"

**Buttons:** "Start" (primary) · "Not now" (secondary)

Not this:

- Primary button "Activate biometrics" (the tap does not activate anything).
- "Your account is not protected until you do this" (fear).
- A body that lists seven steps.
- "This will only take a second" (an invented duration).

## Machine-readable spec

```json
{
  "flow-intro": {
    "surface": "in-product",
    "voice": "product",
    "screens": 1,
    "counts-as-step": false,
    "slots": {
      "title": { "required": true, "lines": 1, "ending-period": false, "explains-not-sells": true },
      "body": { "required": true, "max-lines": 3, "must-state": ["step-count", "duration-if-measured", "what-to-have-at-hand"] },
      "steps": { "required": false, "max": 3, "person-words": true },
      "primary": { "label": "Start", "names-what-happens-on-tap": true },
      "secondary": { "label": "Not now", "shaming": false }
    },
    "banned": { "goal-verb-as-primary": true, "fear": true, "invented-duration": true, "progress-bar": true },
    "data-disclosure": "one plain line where the flow collects sensitive data, linked to the detail",
    "pausable-stated": true
  }
}
```

## Eval hooks

- The primary button is "Start": it names what the tap does, never the goal of the flow.
- The secondary is "Not now": no "Cancel", no "Exit", no shaming label.
- The body states the number of steps, the duration only if measured, and what the person
  needs at hand.
- No fear-based framing and no invented duration ("only a second", "in no time").
- The step indicator does not count this screen.
- Where the flow collects sensitive data, one plain line says what happens with it.
