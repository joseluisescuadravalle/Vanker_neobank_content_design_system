# Logging in

**Status: normative (rules) + example (samples).**

Everything between opening the app and being inside it: the passcode, face or fingerprint,
the tries that run out, a forgotten passcode, a new phone, logging out, and the periodic
re-check the regulation requires.

The code field itself is `../components/library/code-input.md`; what Vanker never asks for
is in `../compliance/security-payments.md`; the expired-session screen is in
`system-errors.md`.

## The rule that governs everything here

**Never tell anyone whether an account exists.**

"There is no account with that email" is a gift: it turns a login screen into a tool for
checking which of a stolen list of addresses bank with Vanker, and it tells a scammer whose
inbox is worth attacking. The rule applies to every screen in this file, and it has one
consequence that feels wrong until you see why:

- The recovery screen says the same thing whether or not the address is ours: **"If there
  is an account for that email, we have sent it a link."**
- A failed login says the attempt was wrong, never which half: **"That passcode was not
  right."** Never "wrong passcode for this account", which confirms the account.
- The response takes the same time either way, and looks identical either way.

The person who really owns the account loses nothing: they check their inbox and the link
is there.

## Getting in

- **Face or fingerprint is a convenience over the passcode, never a replacement.** The
  passcode is always reachable on the same screen, because a fingerprint fails with wet
  hands and a face fails behind a scarf. A screen that offers only biometrics is a lockout
  waiting to happen.
- **Never pressure someone into biometrics.** It is offered once, in its permission screen
  (`permissions.md`), and refusing it costs nothing and is not asked again on the next
  launch.
- **The passcode screen carries no marketing, no promotion, and no news.** It is the door.
- Vanker never asks for the passcode outside its own screens, and says so where a person
  might be tricked (see `../compliance/security-payments.md`).

## Tries and the lock

Copy follows `errors.md`: no blame, no error codes, and the negative spelled out in a
critical instruction.

| Situation | Copy |
| --- | --- |
| Wrong passcode | "That passcode was not right." |
| Wrong, with tries left | "That passcode was not right, and you have 2 more tries." |
| Locked | Title "We locked the app for 30 minutes" · Body "This happens after too many passcode tries, to keep your account safe." · Buttons "Reset passcode" (primary), "Close" |

- **Say how many tries remain**, from the point where it matters (the last two), not from
  the first mistake, which reads as a threat.
- **Never blame.** "You entered the wrong passcode" is banned
  (`../terminology/banned-terms.md`); the passcode was not right, and that is all.
- **The lock always states when it ends**, in plain time, and always offers a way through
  now (resetting the passcode). A lock with no exit and a "contact support" line is a dead
  end, and in a bank a dead end means someone cannot reach their money.
- Never say why a specific try failed, and never confirm any part of it.

## Forgotten passcode

Resetting is a security event, not a form.

- **Screen 1** — "Reset your passcode" · "We will send a code to the phone number on your
  account." · Button "Send code".
- **Screen 2** — the code field (`../components/library/code-input.md`), with its masked
  destination and its security line.
- **Screen 3** — the new passcode, with the rules stated **before** typing, not as errors
  afterwards.
- The old passcode stops working the moment the new one is set, and the copy says so in one
  line.
- Where the account cannot be recovered in the app, the route out is a real one with a
  named channel and a time, never "contact support".

## A new phone

Logging in on a device we have not seen is the highest-risk moment in this file, and it is
also where a real customer is most likely to be stopped. Both matter.

- **Say what is happening, without accusing.** "This looks like a new phone. We will check
  it is you before you log in."
- Verify with a code to the number on the account (`code-input.md`), never with security
  questions, which are guessable and which nobody remembers.
- **Tell the account holder afterwards**, on the devices and channels already trusted: a
  push and an email saying a new device logged in, when, and what to do if it was not them.
  That message names the action and the way to stop it, and never blames.
- If verification fails, the person is not locked out of the world: the same real route out
  as above.

## Logging out, and being logged out

Two different events, and the copy must not blur them.

- **The person logs out.** Not dangerous and not dramatic: a plain confirmation ("Log out
  of Vanker?" with "Log out" and "Cancel"). If logging out clears biometrics or a saved
  device, say that in one line, because it changes what happens next time.
- **We log them out.** Idle timeout or a security event, written as the security measure it
  is: "We logged you out" (see `system-errors.md`), never as a failure and never with an
  error tone.
- After either one, coming back lands on the passcode screen, not on a marketing screen.

## The periodic re-check

Strong Customer Authentication requires a full re-authentication at intervals even for
someone who never logs out (`../compliance/framework.md`).

- **Explain it before it happens** where it can be predicted, and always explain it when it
  does: "We ask for this every few months, to keep your account safe."
- Never present it as a problem, an error, or something the person did.
- Never make it the moment to also ask for something else (a permission, a marketing
  consent, an upsell).

## What this pattern never does

- Never reveals whether an account, an email, or a phone number exists.
- Never says which part of a login was wrong.
- Never offers biometrics as the only way in.
- Never locks someone out with no stated end and no route through.
- Never blames the person for a failed attempt.
- Never puts a promotion, a rating prompt, or a survey on the way in.
- Never asks for a full passcode or code outside its own screens.

## Machine-readable spec

```json
{
  "auth": {
    "enumeration": {
      "reveal-account-existence": false,
      "recovery-response": "If there is an account for that email, we have sent it a link.",
      "identical-response-and-timing": true
    },
    "getting-in": {
      "biometrics": "convenience over the passcode, never a replacement",
      "passcode-always-reachable": true,
      "pressure-to-enable": false,
      "promotions-on-the-door": false
    },
    "tries": {
      "remaining-shown-from": "the last two",
      "blame": false,
      "reveal-which-part-failed": false,
      "lock": { "duration-stated": true, "route-through-now": "reset passcode", "dead-end": false }
    },
    "reset": { "screens": ["send code", "enter code", "new passcode"], "rules-stated-before-typing": true, "old-passcode-invalidated": "stated" },
    "new-device": {
      "accusation": false,
      "verify-with": "code to the number on the account",
      "security-questions": false,
      "notify-trusted-channels": true,
      "failure-has-a-real-route-out": true
    },
    "logout": { "by-person": "plain confirmation", "by-system": "security measure, not a failure", "biometric-side-effect-stated": true },
    "periodic-reauth": { "explained": true, "framed-as-error": false, "bundled-with-other-asks": false }
  }
}
```

## Eval hooks

- No copy states or implies whether an account, email, or phone number exists; the recovery
  message is the conditional one.
- A failed login never says which part was wrong and never blames the person.
- Remaining tries are stated from the last two, in digits.
- A lock states when it ends and offers a way through now.
- Biometrics is never the only route in, and refusing it is never re-asked or pressured.
- A new-device check explains itself without accusing, and the account holder is told
  afterwards on a channel already trusted.
- A person logging out and being logged out are worded differently.
- Nothing else is asked for during a re-authentication.
