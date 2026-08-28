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

Two rules that fall out of the table: **never show a spinner for a wait we can skeleton**
(a skeleton tells the person what is coming; a spinner tells them only that we are busy),
and **never show a bar for a duration we cannot measure**. A fake percentage is a lie with
a progress animation on top.

## Waiting for money

This is the case the rest of the system exists for.

1. **Never confirm before it is true.** Optimistic interfaces are fine for a filter or a
   favorite. A transfer never says "Sent" until it is confirmed. The state between tapping
   and confirmation is its own state, and it is named honestly: "Sending".
2. **When the wait runs long, stop spinning and start talking.** After about 10 seconds,
   replace the indicator with the truth: "This is taking longer than usual. Your money has
   not left your account yet, and we will tell you as soon as we know." The negative is
   spelled out, because it is a statement about money (see `../voice-and-tone/voice.md`).
3. **Let the person leave.** For anything that continues without the app open (a transfer
   being processed, documents in review), say so: "You can close the app. We will notify
   you when it is done." A person trapped watching a spinner assumes their money is
   trapped too.
4. **Never lose the state.** Coming back to a screen mid-process shows the process, not a
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
- ✅ "Sending your payment"
- ✅ "This is taking longer than usual. Your money has not left your account yet, and we
  will tell you as soon as we know."
- ✅ "You can close the app. We will notify you when it is done."
- ❌ "Please wait..."
- ❌ "Loading..."
- ❌ "Almost there!"
- ❌ "Hang tight, we are crunching the numbers"
- ❌ A skeleton row showing `1.234,56 €`
- ❌ "Sent" before the transfer is confirmed

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
      "in-flight-state": "Sending",
      "long-wait-threshold-s": 10,
      "long-wait-message": "This is taking longer than usual. Your money has not left your account yet, and we will tell you as soon as we know.",
      "leaving-allowed-message": "You can close the app. We will notify you when it is done.",
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
  period.
- "Please wait", "Loading...", "Almost there", "Just a moment", and "Hang tight" fail.
- A skeleton placeholder contains no text, and never a digit or a currency symbol.
- A money wait that runs long states that the money has not moved, with the negative
  spelled out.
- Where the process continues without the app, the copy says the person can leave.
- No percentage appears unless it is measured; an unknown duration is indeterminate.
- No jokes, no rotating messages, no exclamation marks.
