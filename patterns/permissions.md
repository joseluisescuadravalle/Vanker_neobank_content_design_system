# Permissions

**Status: normative (rules) + example (samples).**

The screen Vanker shows **before** the phone asks for a permission: notifications, camera,
location, contacts, face or fingerprint recognition.

## Why this screen exists

On iOS the real permission dialog can be triggered **once per install**. If the person says
no there, the app cannot ask again — only the phone's settings can change it. Every rule
below follows from that single shot:

- **Ask at the moment of value, never in a welcome sequence.** Notifications asked for on
  first launch, before there is an account to watch, is the shot thrown away.
- **Never ask for a permission the app does not need yet.** The camera is requested at the
  identity check, not at the start of signup (see `../compliance/data-privacy.md`).
- **One permission per screen.** A screen asking for two is asking for neither.

## Structure

- **Heading** (required): **the action the person is about to take**, and what it is for.
  "Turn on your camera to check your ID". Not a description of the app's needs, and never
  "We need access to…".
- **Body** (required): two sentences, in this order.
  1. **What happens with it**, in the person's own actions ("You'll take a photo of your
     ID…"). The person is the one who acts; Vanker does not "take" their photo.
  2. **What we will not do with it.** This is the sentence that earns the permission, and
     the one most apps never write.
- **Primary button**: the heading's verb, repeated. "Turn on camera". Where the object does
  not fit in three words, it drops to a pronoun: "Turn it on" (see `ctas.md`).
- **Secondary button**: "Not now".

There is no line explaining that the phone will ask next. The system dialog is part of the
flow and announces itself; saying so in advance explains nothing.

## Rules

1. **Never imitate the system dialog.** No fake iOS or Android alert, no borrowed
   typography, no "Allow / Don't allow" pair styled as the platform's. A screen pretending
   to be the operating system is a dark pattern, and in a bank it also teaches people that a
   convincing fake dialog is normal.
2. **The refusal is real.** "Not now" carries the same visual weight rules as any secondary
   button: never greyed out to look disabled, never smaller than the tap target, never
   worded to shame ("No thanks, I do not care about security").
3. **Do not ask again on the next launch.** Re-prime only at a new moment of value, at most
   twice in total. After a system-level denial, stop asking entirely and explain where it is
   changed, at the point where the absence is felt.
4. **Never block on a permission.** A denied camera means the identity check offers another
   route, not that the person loses access to their money.
5. **State the limit truthfully.** If a permission is used for more than the stated purpose,
   the copy says so. A "we will not" sentence that is not true is worse than no screen.
6. **No fear.** "Your account is at risk without notifications" is not allowed. Say what the
   permission enables.

## The five screens

Each is a heading, a body, and the two buttons. The second body sentence is mandatory.

### Notifications

- **Heading:** "Turn on notifications to follow your money"
- **Body:** "You'll get a message the moment a payment leaves your account, so you can spot
  anything you don't recognize. We do not use them for marketing."
- **Buttons:** "Turn them on" · "Not now"

### Camera

- **Heading:** "Turn on your camera to check your ID"
- **Body:** "You'll take a photo of your ID and a short video of your face, and we check
  that they match. We do not use your camera at any other time."
- **Buttons:** "Turn on camera" · "Not now"

### Location

- **Heading:** "Turn on location to protect your card"
- **Body:** "You let us compare where a card payment happens with where your phone is, so we
  can spot a card being used somewhere else. We do not track where you go."
- **Buttons:** "Turn on location" · "Not now"

### Contacts

- **Heading:** "Turn on contacts to send money by name"
- **Body:** "You pick a person from your phone instead of typing an IBAN. Your contacts stay
  on your phone, and we do not upload your address book."
- **Buttons:** "Turn on contacts" · "Not now"

### Face or fingerprint

- **Heading:** "Turn on face recognition to open Vanker faster"
- **Body:** "You open the app and confirm payments with your face instead of your passcode.
  Your face stays on your phone, and we never see it."
- **Buttons:** "Turn it on" · "Not now"

## When the permission is denied

Shown where the absence is felt, not as a nag. The routes go in buttons, never in the body
(see `CLAUDE.md`).

- **Title:** "Vanker can't use your camera"
- **Body:** "Your phone is blocking access, so we can't take the photo here."
- **Buttons:** "Open settings" (primary) · "Send a photo" (secondary)

"Open settings" is honest: the tap opens the settings app. The alternative route is a real
alternative, not a consolation.

## Accessibility

- The two buttons are equal in size and target; only color and weight mark the primary.
- The heading is the screen's `h1` and is announced first.
- Nothing on the screen depends on an image or an icon to be understood.
- If the flow continues after the system dialog, focus lands on the next step, not back on
  the priming screen.

## Machine-readable spec

```json
{
  "permissions": {
    "timing": "moment-of-value",
    "one-per-screen": true,
    "ask-at-first-launch": false,
    "slots": {
      "heading": { "required": true, "form": "action-the-person-takes", "we-need": false },
      "body": { "required": true, "sentences": 2, "order": ["what-happens-with-it", "what-we-will-not-do"], "subject-is-the-person": true },
      "primary": { "repeats-heading-verb": true, "pronoun-fallback": "Turn it on" },
      "secondary": { "label": "Not now", "shaming": false, "visually-weakened": false }
    },
    "system-dialog-warning-line": false,
    "imitates-system-dialog": false,
    "re-ask": { "on-next-launch": false, "max-primes": 2, "after-system-denial": "explain-where-to-change-it" },
    "blocking": false,
    "alternative-route-required": true,
    "fear": false,
    "screens": ["notifications", "camera", "location", "contacts", "biometrics"],
    "denied-state": { "routes-in-buttons": true, "primary": "Open settings", "secondary": "alternative route" }
  }
}
```

## Eval hooks

- The heading names the action the person takes, and the primary button repeats its verb.
- The body has two sentences, the second stating what Vanker will not do with the
  permission.
- The person is the subject of what happens ("You'll take a photo"), not Vanker.
- No "we need", no fear, no imitation of the system dialog.
- The secondary is "Not now" and is never shamed or visually weakened.
- A denied permission offers an alternative route, in a button.
