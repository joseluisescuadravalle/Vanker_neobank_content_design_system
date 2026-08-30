# Calls to action (CTAs)

**Status: normative (rules) + example (samples).**

A CTA is a button or link the person taps to trigger an action. Its label is an **action
verb** (or short verb phrase) that names the action that happens on tap. Nothing else.

## The master rule: name what happens on tap

The label describes **the immediate result of the tap**, not the goal of the process the
tap begins. This is the rule the others serve, and it is the one most often broken by
labels that look admirably specific.

On the screen that opens the biometric-signing setup, tapping the primary button does not
activate anything: it opens the first step. So the label is **"Start"**, never "Activate"
or "Activate biometrics". The activation happens three screens later, and a button that
promises it is writing a cheque the tap cannot cash.

The same test catches a banner button that only navigates ("Verify" when the person lands
on an explanation, not on verification), and a "Send" that opens a review screen.

**When a label looks like it over-promises, check the heading first.** The heading and the
CTA are one unit: the heading names the action the person is about to take, and the button
repeats its verb. This is the rule already used in confirmations ("Delete the selection?" →
"Delete"), and it resolves most apparent conflicts without an exception.

A permission screen shows it. "Turn on camera" looks like it over-promises under a heading
that reads "Use your camera to check your ID", because the tap does not use any camera. Under
the heading "Turn on your camera to check your ID" it is exactly right: turning the camera on
is what this screen is for, and taking the photo happens on the next one. The fix was the
heading, not the button.

Where the object does not fit inside three words, the button keeps the verb and drops to a
pronoun ("Turn it on"), which still agrees with the heading.

**Specificity must be true, not maximal.** Where a specific verb describes the tap, use it
("Send money", "Delete space"). Where it would misdescribe it, the plainer verb is the
correct answer, and a low-commitment "Start" is better content design than an "Activate"
that lies. This is also why "Start" is not treated as one of the banned generic labels: it
is precise about what the tap does.

## Rules

- **Action verb.** The label is an action verb describing what happens on tap ("Send",
  "Cancel", "Delete", "Send money now").
- **Length.** Aim for a single word; **three words maximum**. Include only the words the
  action needs, never filler ("Kindly", "Please").
- **No numbers or amounts.** Never. The amount belongs on the screen, not on the button.
- **No punctuation.** No period, comma, colon, exclamation mark, or question mark,
  anywhere in the label.
- **No emoji.**
- **Acronyms are allowed.** Do not expand an acronym in a CTA; expanding it would break the
  length. This is the one place the "expand acronyms" rule does not apply.
- **No filler or prohibited terms.** A clean action verb never carries hype or
  prohibited-claim words; if one appears, the label is wrong.
- **Consistent with the heading.** In a confirmation, the CTA mirrors the heading's action.
  Heading "Delete the selection?" -> buttons "Delete" and "Cancel". Heading "Confirm
  payment" -> "Confirm payment".
- **Case.** Sentence case.

## Button or link

A button changes something; a link takes the person somewhere. A button that only navigates
overstates its weight, and a link that changes something breaks the expectation that links
are safe and reversible. See `links.md`.

## Primary vs secondary

- **Primary:** the action, a specific verb. Generic words ("OK", "Submit", "Continue",
  "Confirm", "Done", "Next", "Proceed") are never a primary action on their own.
- **Secondary or dismissive:** "Cancel", "Back", "Not now".
- One primary action per screen.

## What does NOT apply to a CTA

A CTA is a tight action-verb phrase, so the body-copy checks are **not** run on it:

- **Money format** (a CTA has no amounts at all).
- **Banned or jargon terms** as a separate rule (the length and action-verb rule already
  rejects filler like "kindly").
- **Acronym expansion** (an acronym may stay short inside the three-word limit).

Only the CTA rules above apply, plus "no emoji".

## Examples

| Context | Do | Avoid |
| --- | --- | --- |
| Send a payment | Send money | Send 150 € |
| Confirm a payment (sheet "Confirm payment") | Confirm payment | OK |
| Delete a space (dialog "Delete this space?") | Delete space | Remove |
| Create a space | Create space | Submit |
| Dismiss a promo | Not now | Cancel |
| Open a multi-step setup flow | Start | Activate biometrics |
| Open a screen that explains verification | Verify identity (only if the tap starts it) | Verify (when it only navigates) |

Bad CTA: "Kindly utilize your risk-free KYC €150 now". It fails **as a CTA** because it is
far over three words, contains a number, and carries filler. The reason is the CTA
structure, not "banned term" or "money format".

## Eval hooks

- The label names what happens on tap, not the goal of the flow it opens.
- The label repeats the verb of its heading; where they disagree, the heading is checked first.
- Three words or fewer; ideally one.
- No numbers or amounts.
- No punctuation (period, comma, colon, exclamation, question mark); no emoji.
- Not a bare generic word ("OK", "Continue", ...) as a primary action.
- In confirmations, matches the heading's action.
- The body-copy checks (money format, banned terms, acronym expansion) are NOT applied to
  CTAs.
