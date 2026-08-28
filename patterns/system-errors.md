# Connectivity and system errors

**Status: normative (rules) + example (samples).**

What Vanker says when the problem is **ours or the network's**, not the person's: no
connection, our systems failing, planned maintenance, an expired session, content that no
longer exists, and a version of the app that can no longer be used.

`errors.md` sets the anatomy of an error (what happened, reassurance, what to do next) and
the rules for field validation and modal errors. This file is about the six system
situations: which surface each one takes, and what the copy must say.

## The two questions that pick the surface

Before writing a word, answer these in order:

1. **Is the person blocked?** Can they keep using the rest of the app, or is everything
   stopped until this is resolved?
2. **Can they do something about it?** Is there an action that can actually work right now,
   or is the honest answer "wait"?

| Situation | Blocked? | Surface | Actions |
| --- | --- | --- | --- |
| The device is offline | No, cached data is still readable | **Banner**, top of the screen, persistent | None (it resolves itself) |
| An action failed because the device is offline | Only that action | **Modal** (or inline, if the action was inline) | Retry (primary), Cancel |
| Our systems failed (a request did not complete) | Only that action | **Modal** | Retry (primary), Cancel |
| Our systems failed (the screen cannot render) | That screen | **Full screen** | Retry (primary) |
| Planned maintenance | Yes | **Full screen** | None, or Close if the app still opens |
| Session expired | Yes | **Full screen** | Log in (primary) |
| Content not found | That screen | **Full screen** | Go back (primary) |
| Update required | Yes | **Full screen**, blocking | Update (primary) |

Two consequences of the table that are easy to get wrong: **offline is never a modal** (it
blocks nothing on its own, and a modal that traps someone in a lift is a bad citizen), and
**maintenance never offers Retry** (retrying cannot work, and a button that does nothing is
a lie).

## Rules

1. **State what happened to the money, always.** Any system error that interrupts a money
   action says which of the three truths applies, in the first two lines:
   - "No money has left your account."
   - "Your payment is on its way and we will confirm it."
   - "We do not know yet whether it went through, and we will tell you as soon as we do."
   Never leave the money unaccounted for. This is the single most important rule in the
   file.
2. **Say whose side it is on, and do not guess.** If the device reports no connection, say
   so plainly ("Your phone is offline"). If our systems failed, own it ("We could not reach
   our systems"). Never blame the person's connection for our outage, and never claim our
   fault for their tunnel.
3. **Never "something went wrong".** We almost always know more than that: offline is not a
   server failure, maintenance is not a crash, an expired session is not an error at all.
   Reserve the vague fallback for the genuinely unknown, and even then say "on our side".
4. **No visible error codes.** A discreet support reference line is allowed, below the
   actions (see `errors.md`).
5. **Never lose what the person typed.** A system error does not discard a form, an amount,
   or a draft; when the person comes back, it is still there, and the copy says so where it
   is not obvious.
6. **Only offer an action that can work.** Retry when retrying can succeed. When the honest
   answer is waiting, say how long, or say we will tell them.
7. **Do not shout, do not joke.** No "Oops", no exclamation marks, no emoji, no mascot
   apologizing. Calm and specific (see `../voice-and-tone/tone.md`).
8. **Contractions are the default; the negation is spelled out where a misreading costs
   money.** Vanker uses contractions everywhere, negatives included (see
   `../voice-and-tone/voice.md`). On these screens the exception is narrow and specific:

   | Spell it out | Contract freely |
   | --- | --- |
   | Any sentence saying whether money moved ("We could not send your payment", "We do not know yet whether it went through") | Everything else on the screen |
   | Any security or fraud instruction ("do not close the app", "we will never ask you for this code") | Connection, navigation, and content statements ("Your phone isn't online", "This page doesn't exist") |
   | Any sentence whose misreading changes what the person does with their money | Descriptions, explanations, reassurance that carries no negation |

   The test is not "is this an error?" but "if the reader's eye skips the `n't`, do they walk
   away believing the opposite about their money?" A payment that did not go through read as
   one that did is the exact harm this rule exists for.
9. **Do not appear too fast.** A connection blip is not an error. Wait about two seconds
   before showing the offline banner, and remove it as soon as the connection is back,
   without a success toast.

## The six situations

### 1. Offline

A persistent banner, warning tone, at the top of the screen. It says what is still
possible, because in a bank most of what people do is look.

- **Title:** "Your phone is offline"
- **Description:** "You can still see your balance and recent transactions. New payments
  will work again when you are back online."
- **Action:** none.
- Never a modal. Never a full screen. It resolves itself.

### 2. An action failed because there is no connection

- **Title:** "We could not send your payment"
- **Body:** "Your phone lost its connection, and no money has left your account."
- **Actions:** "Retry" (primary), "Cancel" (secondary).

### 3. Our systems failed

When the request did not complete and we do not know its outcome, say exactly that. Do not
promise it failed.

- **Title:** "We could not complete your payment"
- **Body:** "Something did not work on our side. We do not know yet whether the payment went
  through, and we will tell you as soon as we do."
- **Actions:** "Close". A reference line below: "Reference VNK-4821".
- When we do know the money did not move, say so and offer "Retry".

### 4. Planned maintenance

- **Title:** "Vanker is down for maintenance"
- **Body:** "We are making some changes and will be back at 6:00 am. Your money is safe."
- **Actions:** none, or "Close" if the app still opens.
- If the end time is unknown, say so plainly ("We will be back as soon as we can") rather
  than inventing one.
- Announce planned maintenance in advance, in the app, before the window.

### 5. Session expired

Not a failure: a security measure, and it is written as one.

- **Title:** "We logged you out"
- **Body:** "We do this after a while without activity, to keep your account safe. Your
  money is safe, and nothing you were doing has been lost."
- **Action:** "Log in" (primary).
- Where the person was doing something, bring them back to it after logging in, and say so.

### 6. Content not found and update required

**Content not found** (a deleted space, a link to a transaction that no longer exists):

- **Title:** "This page doesn't exist"
- **Body:** "The link may be old, or it may have been deleted."
- **Action:** "Go back" (primary).
- **Name the thing when we know what it was.** "That space no longer exists" and "We
  couldn't find that transaction" beat the generic page message every time; the generic one
  is the fallback for a link we cannot resolve. No money moved and nothing is at risk here,
  so the contraction stays.

**Update required** — blocking, and only when the old version genuinely cannot keep working
(a change it can no longer talk to, a regulatory requirement, a security fix), never to push
a feature:

- **Title:** "Update Vanker to continue"
- **Body:** "This version is too old to work with our systems. Update the app to keep using
  your account."
- **Action:** "Update" (primary).
- Say why, in one line. A blocking screen without a reason reads as a demand.
- **Do not dramatize.** An old version is usually just old. Never tell someone their app is
  unsafe, or imply their account is at risk, unless that is literally true and confirmed:
  a false alarm about their own money is a real cost, and it teaches people to distrust the
  warnings that matter.

## What not to write

| Not this | Why |
| --- | --- |
| "Oops! Something went wrong." | Vague, cheerful, and unhelpful in a bank. |
| "Error 500. Please try again later." | An error code the person cannot use. |
| "Check your internet connection." (when our systems are down) | Blames the person for our outage. |
| "Your payment failed." (when we do not know) | Claims an outcome we have not confirmed. |
| "We are experiencing technical difficulties." | Corporate distance; say what it means for them. |
| "This version is no longer secure." (when it is only old) | A false alarm about the person's own money. |
| A Retry button on a maintenance screen | An action that cannot work. |
| An offline modal | Blocks an app that still works. |

## Eval hooks

- A system error that mentions a payment, a transfer, or money states what happened to the
  money.
- No visible error code in the message; a reference line, when present, is a separate,
  discreet element.
- The copy names the side the problem is on, and does not blame the person's connection for
  our failure.
- "Something went wrong", "Oops", and "unexpected error" do not appear.
- The actions offered can actually work: no Retry on maintenance, no modal for offline.
- No emoji, no exclamation marks, no jokes.
- A sentence stating whether money moved spells out the negative ("could not", "do not"),
  while the rest of the screen uses contractions normally.
- A forced update states a factual reason and does not claim the current version is unsafe
  unless that is confirmed.

## Machine-readable spec

```json
{
  "system-errors": {
    "surface-by-situation": {
      "offline": { "blocking": false, "surface": "banner", "tone": "warning", "actions": [] },
      "action-failed-offline": { "blocking": "action", "surface": "modal", "actions": ["Retry", "Cancel"] },
      "server-error-request": { "blocking": "action", "surface": "modal", "actions": ["Retry", "Cancel"] },
      "server-error-screen": { "blocking": "screen", "surface": "full-screen", "actions": ["Retry"] },
      "maintenance": { "blocking": true, "surface": "full-screen", "actions": [], "retry": false },
      "session-expired": { "blocking": true, "surface": "full-screen", "actions": ["Log in"] },
      "not-found": { "blocking": "screen", "surface": "full-screen", "actions": ["Go back"] },
      "update-required": { "blocking": true, "surface": "full-screen", "actions": ["Update"], "reason-required": true }
    },
    "money-statement": {
      "required-when": "the error interrupts a money action",
      "one-of": ["not-left", "on-its-way", "outcome-unknown"]
    },
    "rules": {
      "attribution": "name the side: device or our systems",
      "vague-fallback": false,
      "visible-error-code": false,
      "reference-line": "allowed, tertiary",
      "preserves-input": true,
      "offer-only-workable-actions": true,
      "offline-banner-delay-ms": 2000,
      "exclamation": false,
      "emoji": false,
      "contractions": "default",
      "spell-out-negation-when": ["money-outcome", "security-instruction"],
      "update-required-alarm": false
    }
  }
}
```
