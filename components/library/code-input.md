# Code input

**Status: normative.**

The field where a person enters the single-use code Vanker sent them, to confirm their
identity or to authorize a payment (Strong Customer Authentication, SCA). It is the most
security-sensitive input in the product and the one most often copied badly from other
apps.

In customer copy this is a **code**, never "OTP" and never "one-time password" (see
`../../terminology/glossary.md`).

## What this is not

| Not this | What it is | Where |
| --- | --- | --- |
| Passcode | The code that unlocks the app, chosen by the person | `text-field.md` |
| PIN | The card PIN | `text-field.md` |
| Password | Account password | `text-field.md` |

Those are secrets the person keeps. A code is a secret **we** send, valid once, for minutes.
That difference drives every rule below.

## One field, not six boxes

Vanker uses **a single input** with visible digit slots drawn behind it. The segmentation is
presentation; the input is one field with one label.

Six separate inputs are the common pattern and they break in four places at once:

- **Autofill.** `autocomplete="one-time-code"` delivers the whole code to one field. Split
  across six inputs, the platform commonly fills only the first, and the person has to type
  the rest from a notification they can no longer see.
- **Paste.** People paste codes. One field takes the paste; six need custom handling that
  fails on the first unexpected format.
- **Screen readers.** Six inputs announce six labels ("edit text, 1 of 6"), and the error is
  attached to nothing in particular. One field announces one name, one value, one error.
- **Editing.** Backspace, caret movement, and correcting the third digit all behave the way
  the platform already taught the person, with no focus-jumping logic to get wrong.

Rule: **never move focus automatically between digit slots**, because there is nothing to
move focus between.

## Slots

- **Heading** (required): what to do, in a person's words. "Enter the code we sent you".
- **Destination line** (required): where the code went, **masked**. "We sent a 6-digit code
  to +34 ··· ··· 123." Never the full phone number or email address (see
  `../../compliance/data-privacy.md`).
- **Label in** (inline variant): "Code". No digits, no "OTP".
- **Code field**: one input, digit slots drawn, digits always visible.
- **Expiry line** (required when the code expires): "The code expires in 5 minutes."
- **Payment context** (required when the code authorizes a payment): the amount and the
  payee, beside the field. See "Dynamic linking" below.
- **Security line** (required): "We will never ask you for this code by phone, email, or
  message."
- **Resend** (button): "Resend code".
- **Error** (conditional): replaces the expiry line.

## Content rules

1. **Say where the code went, masked.** The person needs to know which phone or inbox to
   look at; they do not need us to publish it back to them. `+34 ··· ··· 123`,
   `a···@example.com`.
2. **Say how many digits, before the field.** "a 6-digit code", so the person knows when
   they are done.
3. **Say the expiry once, in plain time.** "The code expires in 5 minutes." Not in the
   label, not in the button, and never as a pressure device.
4. **Never echo the code in the interface.** In-app copy never displays the code, never
   pre-fills it, and never repeats it back after a failure.
5. **The digits stay visible.** A code is not a password: do not mask it with dots. The
   person must be able to check what they typed against the message.
6. **Say what Vanker never does.** The security line is part of this screen, not an
   optional extra: "We will never ask you for this code by phone, email, or message" (see
   `../../compliance/security-payments.md`).
7. **No pressure, no fake urgency.** The expiry is a fact, not a countdown that shouts.
   Never "hurry", never "last chance" (see `../../terminology/banned-terms.md`).
8. **Resend is honest.** If resending is rate-limited, say the wait plainly ("You can ask
   for a new code in 30 seconds") instead of a button that silently does nothing.

## Dynamic linking (payments)

When the code authorizes a payment, Strong Customer Authentication requires the code to be
tied to that specific amount and payee, and the person must see both while they confirm.

- The screen shows the amount and the payee next to the field: "Confirming 150 € to Ana
  Ruiz."
- The amount follows the money format (`../../terminology/glossary.md`), so `150 €`, not
  `150,00 €`.
- If the amount or the payee changes, the code is void and a new one is sent. Say so:
  "The amount changed, so we sent you a new code."

## Errors

Field validation errors: one sentence, ending with a period, specific, never blaming (see
`../../patterns/errors.md`). Negatives are spelled out in security copy ("do not", "cannot").

| Case | Message (normative) |
| --- | --- |
| Wrong code | "That code was not right." |
| Wrong code, attempts left | "That code was not right, and you have 2 more tries." |
| Expired | "That code has expired." |
| Incomplete | "The code has 6 digits." |
| Too many attempts | Not a field error: a full-screen or modal message that says the account is locked, why, and how to get back in (see `../../patterns/errors.md`) |

- **Never say what was wrong with the code.** "That code was not right" is the whole truth
  the person needs; "the third digit is wrong" is a gift to an attacker.
- **Never blame.** "You entered the wrong code" and "Invalid code" are both out (see
  `../../terminology/banned-terms.md`).
- On a wrong code, **clear the field, keep focus in it, and announce the error**, so the
  person can retype immediately without selecting anything.

## States

| State | Treatment |
| --- | --- |
| Empty | Digit slots visible, `color.border`; label in per `text-field.md` |
| Focus | Active slot marked with a 2px `color.accent` underline; focus ring on the field |
| Filled | Digits in `color.text-primary`, tabular numbers, never masked |
| Checking | Field read-only, inline progress, announced politely ("Checking your code") |
| Error | Slots `color.error`, message below, `aria-invalid`, field cleared, focus kept |
| Resend waiting | Resend button disabled with the remaining time stated in text beside it, never only in the button |

## Behavior

- **Auto-submit when the last digit lands** is allowed and expected, but the primary button
  stays visible and operable: paste, autofill, and assistive technology do not always
  trigger the same events.
- Announce the transition to checking in a **polite** live region; do not move focus.
- `inputmode="numeric"`, `autocomplete="one-time-code"`, `type="text"` (not `number`: it
  brings spinners and drops leading zeros).
- Pasting the full code fills the field; a pasted code with spaces or a trailing period is
  cleaned, not rejected.
- The person can always leave the screen and come back without losing the code they were
  sent.

## Accessibility

- One input, one accessible name ("Verification code"), one error tied with
  `aria-describedby`.
- The destination line and the expiry line are tied to the field with `aria-describedby`, so
  they are read with it.
- The code is never announced digit by digit as a password; it is a visible value.
- Errors are announced, carry an icon and text, and never rely on color alone.
- Minimum 44px tap targets; the field is 48px tall.
- The resend countdown is in text, not only in a disabled button's appearance.

## Content examples

- ✅ "We sent a 6-digit code to +34 ··· ··· 123."
- ✅ "The code expires in 5 minutes."
- ✅ "We will never ask you for this code by phone, email, or message."
- ✅ Error: "That code was not right, and you have 2 more tries."
- ❌ "Enter your OTP" (jargon; it is a code).
- ❌ "We sent a code to +34 612 345 123" (the full number).
- ❌ "Invalid code" (blame, and generic).
- ❌ "Hurry, the code expires soon" (pressure).
- ❌ A masked field showing dots instead of the digits.

## Machine-readable spec

```json
{
  "code-input": {
    "term": "code",
    "banned-terms": ["OTP", "one-time password", "token"],
    "structure": { "inputs": 1, "digit-slots": "presentational", "auto-advance-focus": false },
    "slots": {
      "heading": { "required": true },
      "destination": { "required": true, "masked": true, "example": "+34 ··· ··· 123" },
      "label-in": { "variant": "inline", "value": "Code", "digits": false },
      "field": { "required": true, "digits": 6, "masked": false, "numbers": "tabular" },
      "expiry": { "required": "when-expiring", "form": "plain-time", "pressure": false },
      "payment-context": { "required": "when-authorizing-a-payment", "shows": ["amount", "payee"] },
      "security-line": { "required": true, "text": "We will never ask you for this code by phone, email, or message." },
      "resend": { "type": "button", "label": "Resend code", "wait-stated-in-text": true },
      "error": { "sentences": 1, "ends-with-period": true, "reveals-which-digit": false }
    },
    "dynamic-linking": { "required-for-payments": true, "voids-on-change": true, "money-format": "european" },
    "behavior": {
      "auto-submit-on-complete": true,
      "primary-button-always-visible": true,
      "inputmode": "numeric",
      "autocomplete": "one-time-code",
      "input-type": "text",
      "paste": "accepted-and-cleaned",
      "on-error": ["clear-field", "keep-focus", "announce"]
    },
    "messages": {
      "wrong": "That code was not right.",
      "wrong-with-attempts": "That code was not right, and you have {n} more tries.",
      "expired": "That code has expired.",
      "incomplete": "The code has {digits} digits.",
      "resend-wait": "You can ask for a new code in {seconds} seconds."
    },
    "a11y": { "single-name": "Verification code", "describedby": ["destination", "expiry"], "live-region": "polite", "min-target": 44 }
  }
}
```

## Eval hooks

- Customer copy calls it a code: "OTP", "one-time password", and "token" fail.
- A phone number or email address in copy is masked; a full one fails.
- The destination, the number of digits, and the expiry are stated before the field.
- The security line stating that Vanker never asks for the code is present on the screen.
- A payment-authorizing screen shows the amount and the payee, with the amount in European
  format.
- The error never names which digit was wrong, never blames, and is one sentence.
- The resend wait is stated in text, not only implied by a disabled button.
