# Calls to action (CTAs)

**Status: normative (rules) + example (samples).**

A CTA is a button or link the person taps to trigger an action. Its label is an **action
verb** (or short verb phrase) that names the action that happens on tap. Nothing else.

## Rules

- **Action verb.** The label is an action verb describing what happens on tap ("Send",
  "Cancel", "Delete", "Send money now").
- **Length.** Aim for a single word; **four words maximum**. Include only the words the
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
- **Acronym expansion** (an acronym may stay short inside the four-word limit).

Only the CTA rules above apply, plus "no emoji".

## Examples

| Context | Do | Avoid |
| --- | --- | --- |
| Send a payment | Send money | Send 150 € |
| Confirm a payment (sheet "Confirm payment") | Confirm payment | OK |
| Delete a space (dialog "Delete this space?") | Delete space | Remove |
| Create a space | Create space | Submit |
| Dismiss a promo | Not now | Cancel |

Bad CTA: "Kindly utilize your risk-free KYC €150 now". It fails **as a CTA** because it is
far over four words, contains a number, and carries filler. The reason is the CTA
structure, not "banned term" or "money format".

## Eval hooks

- Four words or fewer; ideally one.
- No numbers or amounts.
- No punctuation (period, comma, colon, exclamation, question mark); no emoji.
- Not a bare generic word ("OK", "Continue", ...) as a primary action.
- In confirmations, matches the heading's action.
- The body-copy checks (money format, banned terms, acronym expansion) are NOT applied to
  CTAs.
