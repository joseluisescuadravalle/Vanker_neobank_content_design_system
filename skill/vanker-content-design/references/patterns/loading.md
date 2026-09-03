# Waiting: loading, progress, and skeletons

**Status: normative (rules) + example (samples).**

What Vanker shows and says while something is happening. In a bank, waiting is rarely
neutral: the person is often waiting to find out what happened to their money, and the
wrong indicator turns a two-second delay into a fear that a payment vanished.

Motion tokens are in `../components/foundations/motion.md`; the copy that follows a failed
wait is in `system-errors.md`.

## Choose the indicator by the wait, not by habit

| Wait | What the person is doing | Show |
| --- | --- | --- |
| Under 1 second | Anything | **Nothing.** A spinner that flashes for 300ms is worse than the wait it covers |
| 1 to 3 seconds, content whose shape we know | Reading a list or a screen | **Skeleton** of the real layout |
| 1 to 3 seconds, an action they triggered | Waiting on a button | **Inline spinner in the button**, the button non-interactive |
| 3 to 10 seconds | Waiting on us | **A status message that says what is happening** ("Checking your details") |
| Over 10 seconds, or unknown | Waiting on a process | **A progress screen** with the steps, and permission to leave |
| Determinate work (upload, export) | Watching a task finish | **A progress bar** with a real percentage |

**Only a device-bound wait may ask the person to stay.** An upload, a camera capture, or
anything that lives in the phone rather than on the server can legitimately say "Keep this
screen open while we upload it." Nothing that moves money ever can (see below).

Two rules that fall out of the table: **never show a spinner for a wait we can skeleton**
(a skeleton tells the person what is coming; a spinner tells them only that we are busy),
and **never show a bar for a duration we cannot measure**. A fake percentage is a lie with
a progress animation on top.

## Waiting for money

This is the case the rest of the system exists for, and it is **one screen in two states**,
not two separate designs. The threshold between them is about **10 seconds**.

### The in-flight label is the button's own verb, conjugated

When a button is pressed, its label goes into the present participle and keeps its words:

| Button | In flight |
| --- | --- |
| "Send money" | "Sending money" |
| "Confirm payment" | "Confirming payment" |
| "Add money" | "Adding money" |

Never a new sentence written for the occasion ("Sending your payment"), and never
"Loading". The person reads the same words before and after they tap, and nobody has to
invent the waiting copy.

### State 1 — in flight (0 to about 10 seconds)

The button keeps its conjugated label with a spinner beside it. Nothing else on the screen
changes: no message, no overlay, no title change.

**The button is no longer a button; it is a status wearing a button's shape.** It must be
non-operable and announced as busy (`aria-busy`, `aria-disabled`). If it keeps looking
pressable, someone impatient taps it expecting to retry, and a second transfer is the worst
failure this product can produce.

### State 2 — the wait runs long (after about 10 seconds)

Stop waiting silently and say what is true. Two things are added, and **nothing moves**:

1. **A message above the buttons.** The spinner stays exactly where the person's eye
   already is, on the button they pressed, because it is the proof that the system is still
   working.
2. **A secondary button, `Close`.** It releases whoever wants to leave, without pushing out
   whoever prefers to watch.

**When the process continues without the app open** — the normal case, because an order
that depends on a screen staying open is an architecture problem, not a copy problem:

> This is taking longer than usual. Your money has not left your account yet, and we will
> notify you.
>
> `Sending money` (spinner, not operable)
> `Close` (secondary)

**There is no second variant.** A money order never depends on the screen staying open: once
it is submitted it completes on the server, and `Close` always appears. If an implementation
needs the screen to stay open to finish sending money, that is a defect to fix, not a screen
to write, and this system does not provide wording for it.

### The rules behind those two screens

1. **Never confirm before it is true.** Optimistic interfaces are fine for a filter or a
   favorite. A transfer never says "Sent" until it is confirmed; the state between tapping
   and confirmation is its own state, and it is named with the button's own verb.
2. **The money clause is not optional.** After ten seconds of spinner the first fear is not
   "when will they tell me", it is "has it gone, and has it gone twice". One clause answers
   it: "Your money has not left your account yet." Where we truly do not know, say that
   instead ("We do not know yet whether it went through"), never a guess.
3. **The `Close` button carries the permission to leave.** Do not also write "you can close
   this screen" in the message: the action lives in the button (see `CLAUDE.md`), and that
   is the sentence that was making the message three lines long.
4. **Two lines, not three.** State 2 is read by someone who is already worried. The reason
   it appeared, the money, and the promise to tell them: nothing else fits and nothing else
   is needed.
5. **Closing never cancels.** `Close` leaves the screen; it does not stop the payment, and
   nothing in the copy may suggest it does. Where an action can still be stopped, that is a
   different button and it says "Cancel".
6. **Never lose the state.** Coming back to the screen mid-process shows the process, not a
   blank form or a fresh start.

## Skeletons

A skeleton is a grey outline of the layout that is about to appear. It sets expectations,
so it has to be honest.

- **Mirror the real layout**: the same rows, the same number of lines, the same rhythm. A
  skeleton that does not match what arrives is a small betrayal repeated on every load.
- **Never put content inside a skeleton.** No text, and above all **no digits, no amounts,
  no currency**. A shimmering `1.234,56 €` that resolves into a different number is the
  worst thing this system could ship.
- **Three to five rows is enough.** Do not fill the viewport with placeholder rows.
- **The shimmer respects `prefers-reduced-motion`**: replace the sweep with a static tint
  (see `../components/foundations/motion.md`).
- **A skeleton is not an empty state.** If the list arrives empty, the skeleton is replaced
  by the empty state (see `empty-states.md`), never by an eternal skeleton.
- Use a skeleton only where the shape is predictable. For an unknown shape, use a status
  message.

## Copy rules

- **Say what is happening, in the first person plural, as it happens**: "Checking your
  details", "Setting up your account", "Sending your payment". Not "Loading", not
  "Processing", not "Working on it".
- **No ending period** on a status line; it is a label, not a sentence.
- **Never "Please wait".** It asks for patience instead of giving information, and there is
  nothing else the person could do.
- **No jokes and no rotating messages.** A carousel of witty lines while someone waits for
  a transfer is a fintech habit Vanker does not have (see `../voice-and-tone/voice.md`).
- **Give a duration only when it is real**, from measured data, and as a range: "about 30
  seconds", "3 to 5 working days". Never "just a moment", never "almost there".
- **A percentage is either true or absent.** No smoothing to 99% while the work continues.
- If the wait has steps the person can follow, name them in their words ("Checking your
  card", "Confirming with your bank"), and mark the ones already done.

## Presentation

| Element | Treatment |
| --- | --- |
| Skeleton | `color.surface-subtle` blocks at `radius.sm`, shimmer sweep of about 1.2s, static under reduced motion |
| Button spinner | 16px, `color.on-primary` on a primary button; the label stays if it fits, and is never replaced by "Loading" |
| Status message | `body-sm`, `color.text-secondary`, centered under the element it describes |
| Progress bar | 4px, `radius.full`, `color.accent` fill on `color.surface-subtle`; percentage in tabular numbers beside it |
| Progress screen | Steps as a vertical list; the current step in `color.text-primary`, the done ones marked, the pending ones in `color.text-secondary` |

The spinner is never fuchsia on a dark surface (see `../components/foundations/color.md`).

## Accessibility

- The loading region carries `aria-busy="true"` while it loads, and the status message
  lives in a **polite** live region. Do not move focus when content arrives.
- **Skeletons are decorative**: hide them from screen readers (`aria-hidden`) and announce
  the wait once ("Loading transactions"), never one announcement per placeholder row.
- Announce completion once, in words, for anything the person is waiting on ("Your
  transactions are ready"), not by silently swapping the content.
- A progress bar exposes its value (`role="progressbar"` with the real value), or, when the
  duration is unknown, is marked indeterminate rather than given a made-up number.
- Never convey progress by motion alone.
- Under `prefers-reduced-motion`, spinners and shimmers become static or fade-only.

## Content examples

- ✅ "Checking your details"
- ✅ "Sending money" (the button said "Send money")
- ✅ "This is taking longer than usual. Your money has not left your account yet, and we
  will notify you." with a `Close` button
- ✅ "Keep this screen open while we upload it." (a device-bound wait, not a money wait)
- ❌ "Please wait..."
- ❌ "Loading..."
- ❌ "Almost there!"
- ❌ "Hang tight, we are crunching the numbers"
- ❌ A skeleton row showing `1.234,56 €`
- ❌ "Sending your payment" when the button said "Send money"
- ❌ "Please keep this screen open while we send it." (a money order never depends on it)
- ❌ "Sent" before the transfer is confirmed
- ❌ "You can close this screen and we will notify you" while a `Close` button sits below it

## Machine-readable spec

```json
{
  "loading": {
    "indicator-by-wait": {
      "under-1s": "none",
      "1-3s-known-shape": "skeleton",
      "1-3s-action": "button-spinner",
      "3-10s": "status-message",
      "over-10s-or-unknown": "progress-screen",
      "determinate": "progress-bar"
    },
    "money": {
      "optimistic-confirmation": false,
      "in-flight-label": "the button's own label in the present participle (Send money -> Sending money)",
      "in-flight-button": { "operable": false, "aria-busy": true, "aria-disabled": true, "keeps-spinner-in-state-2": true },
      "states": {
        "in-flight": { "until-s": 10, "indicator": "button-spinner", "message": null },
        "long-wait": { "after-s": 10, "indicator": "stays-on-the-button", "adds": ["message-above-the-buttons", "secondary-Close"], "moves": "nothing", "max-lines": 2 }
      },
      "long-wait-message": "This is taking longer than usual. Your money has not left your account yet, and we will notify you.",
      "keep-screen-open-allowed": false,
      "keep-screen-open-scope": "device-bound waits only (upload, capture), never money",
      "exit-button": { "label": "Close", "level": "secondary", "shown-when": "always, on any money wait past the threshold", "carries-the-permission-to-leave": true, "cancels": false },
      "permission-to-leave-in-prose": false,
      "money-clause-required": true,
      "preserves-state": true
    },
    "skeleton": {
      "mirrors-layout": true,
      "contains-text": false,
      "contains-digits": false,
      "rows": [3, 5],
      "shimmer-ms": 1200,
      "reduced-motion": "static",
      "replaced-by-empty-state-when-empty": true,
      "aria-hidden": true
    },
    "copy": {
      "form": "present-participle-first-person-plural",
      "ending-period": false,
      "banned": ["please wait", "loading...", "almost there", "just a moment", "hang tight"],
      "rotating-messages": false,
      "duration-only-if-measured": true,
      "percentage": "true-or-absent"
    },
    "a11y": {
      "aria-busy": true,
      "live-region": "polite",
      "skeleton-announcement": "once",
      "completion-announced": true,
      "progressbar-value": "real-or-indeterminate",
      "reduced-motion": true
    }
  }
}
```

## Eval hooks

- A waiting message says what is happening, in the present participle, with no ending
  period, and an in-flight button uses its own label conjugated, never a new sentence.
- The in-flight button is not operable and is announced as busy: a second tap must never be
  able to send the money twice.
- "Please wait", "Loading...", "Almost there", "Just a moment", and "Hang tight" fail.
- A skeleton placeholder contains no text, and never a digit or a currency symbol.
- A money wait that runs long states that the money has not moved, with the negative
  spelled out, in at most two lines.
- A money wait past the threshold always offers `Close`, and the message does not repeat the
  permission in prose.
- A money wait never asks the person to keep the screen open; only a device-bound wait (an
  upload, a capture) may.
- Nothing suggests that closing the screen cancels the payment.
- No percentage appears unless it is measured; an unknown duration is indeterminate.
- No jokes, no rotating messages, no exclamation marks.
