# Error messages

**Status: normative (rules) + example (samples).**

What Vanker says when something goes wrong. Errors are where a bank earns or loses
trust, so tone matters most here (see `../voice-and-tone/tone.md`, "Errors and things
going wrong").

## Anatomy

A Vanker error has up to three parts, in this order:

1. **What happened** — plain, specific, no error code.
2. **Reassurance** — especially that money is safe, when money could be involved.
3. **What to do next** — one clear action.

## Rules

- Reassure before you instruct. If money could be affected, say it is safe.
- Never blame the person (see `../terminology/banned-terms.md`, "Blame").
- Be specific about the cause when you know it. Do not say "something went wrong" if
  you know what did.
- One clear next step, and put it in the button, not buried in prose.
- No error codes in the visible message. A reference code may sit in a small secondary
  line for support.
- No jokes, no emoji. Calm and human.

## Variables

`{amount}`, `{recipient}`, `{n}` (attempts left), `{support_ref}`

## Examples

**Payment failed, funds not moved**
- Do: "That payment did not go through, and no money has left your account. Please check your card details and try again."
- Not: "Payment error. Invalid input. Code 402."

**Insufficient funds**
- Do: "You do not have enough in your current account to send €{amount}. Add money or lower the amount to continue."
- Not: "Transaction declined: insufficient funds."

**Connection problem**
- Do: "We could not reach our systems just now. Your money is safe. Please try again in a moment."
- Not: "Network error. Retry."

**Wrong passcode**
- Do: "That passcode was not right. Please try again. After {n} more tries we will lock the app to keep your account safe."
- Not: "Invalid credentials."

**Unknown cause (fallback)**
- Do: "Something did not work on our side, and your money is safe. Please try again. If it keeps happening, contact us and mention {support_ref}."
- Not: "Unexpected error occurred."

## Eval hooks

- No visible error code in the primary message.
- Contains a clear next step (an imperative verb).
- For money-related errors, contains a safety reassurance.
- Contains no banned blame terms.
