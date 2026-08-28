# Status label

**Status: normative.**

A small, non-interactive label that names the current state of one object: a transaction, a
card, an identity check, a recurring payment, a space. It is read, never tapped.

A status label is the shortest piece of content in the system and one of the most
consequential: it is often the only thing a person reads before deciding whether their money
arrived. It therefore uses a **closed vocabulary** (a fixed list of terms) rather than free
copy.

## What this is not

| Not this | What it is | Where it lives |
| --- | --- | --- |
| Count badge | The number or dot on a navigation icon ("3") | Not specified yet |
| Chip | An interactive control: filter, choice, or removable input | Not specified yet |
| Banner, toast | A message about an event that just happened | `banner-toast.md` |
| Button | An action | `button.md`, `../../patterns/ctas.md` |

Elsewhere in this repository the word "tag" refers to this component. "Badge" in Vanker means
the count badge only.

## Slots

- **Label** (required, the only text slot): one or two words, taken verbatim from the
  controlled vocabulary below. Never free copy.
- **Leading indicator** (optional): a 6px dot in the tone's full color, or a 16px
  (`icon.sm`) outline icon. Use one or the other, never both, and only when several
  different statuses appear in the same list and the reader needs an anchor faster than
  reading. An icon that repeats what the word already says is noise (see
  `../foundations/iconography.md`).
- **No** trailing icon, chevron, or close (×): those signal that the element can be tapped.

## Rules

1. **The normal state carries no label.** A status label marks an exception. A settled
   transaction, an active card, and a verified account show nothing. If every object is
   labeled, the label stops meaning anything.
2. **Closed vocabulary, one term per state.** Use the exact term from the tables below.
   Never introduce a synonym ("Processing", "In progress", "Rejected"), and never adapt a
   term per screen.
3. **The word carries the meaning; color only reinforces it.** The tone is derived from the
   status by the mapping table, never chosen per screen. The brand accent (fuchsia) is never
   a status tone.
4. **A status label is neither an action nor an explanation.** It names a state in one or two
   words. The reason goes in the body copy or the detail view; the action goes in a button
   (see `CLAUDE.md`, "keep calls to action in buttons").
5. **It is never the only place a consequential fact appears.** "On hold", "Declined",
   "Failed", and "Not approved" always come with an explanation on the same screen or one tap
   away, and with the complaints route where the outcome affects the customer (see
   `../../compliance/complaints.md`).
6. **No numbers, amounts, dates, or counts inside the label.** "Pending", not "Pending ·
   2 days" and not "2 pending". Duration and amounts belong to the row or the detail view.
7. **No compliance or guarantee claims.** "Protected", "Insured", "Safe", and "Guaranteed"
   are not statuses (see `CLAUDE.md`, section 2).
8. **One status label per object.** If two states are true at once, show the one that blocks
   the person's next step.
9. **Sentence case, no ending punctuation, no emoji, no ALL CAPS.** Uppercase micro-text is
   harder to read at 12px and is spelled out letter by letter by some screen readers.

## Controlled vocabulary

Normative. The tone column is fixed; it is not a per-screen decision.

### Transactions and payments

| Label | Tone | Means | Default? |
| --- | --- | --- | --- |
| — | — | Settled and final | Yes: no label |
| `Pending` | warning | Authorized, not settled yet |  |
| `Scheduled` | info | Will be sent on a future date |  |
| `On hold` | warning | Held while we check it; we will say why |  |
| `Declined` | error | Refused by the bank or the card network |  |
| `Failed` | error | Did not go through for a technical reason |  |
| `Canceled` | neutral | Canceled before it was sent |  |
| `Refunded` | success | The money was returned |  |
| `Returned` | neutral | The payment came back to the account |  |

### Cards

| Label | Tone | Means | Default? |
| --- | --- | --- | --- |
| — | — | Active and usable | Yes: no label |
| `Frozen` | info | Paused by the customer, reversible in the app |  |
| `Blocked` | error | Blocked by Vanker for security; needs contact |  |
| `Not activated` | warning | Delivered, waiting for activation |  |
| `Expired` | neutral | Past its expiry date |  |
| `Canceled` | neutral | Permanently canceled |  |

### Identity verification

Customer-facing wording only. The raw acronym KYC (Know Your Customer) never appears in a
status label (see `../../terminology/glossary.md`).

| Label | Tone | Means | Default? |
| --- | --- | --- | --- |
| — | — | Verified, nothing to do | Yes: no label |
| `In review` | info | We are checking the documents |  |
| `Action needed` | warning | The customer has to do something to continue |  |
| `Verified` | success | Shown only where confirming it matters, for example on a profile screen |  |
| `Expired` | warning | The documents are out of date |  |
| `Not approved` | error | Final negative outcome; never shown without a reason and the complaints route |  |

### Recurring payments (direct debits and subscriptions)

| Label | Tone | Means | Default? |
| --- | --- | --- | --- |
| — | — | Active | Yes: no label |
| `Upcoming` | info | Due within the next few days |  |
| `Paused` | neutral | Temporarily stopped |  |
| `Canceled` | neutral | Ended |  |
| `Failed` | error | The last collection did not go through |  |

### Spaces

| Label | Tone | Means | Default? |
| --- | --- | --- | --- |
| — | — | Open and saving | Yes: no label |
| `Target reached` | success | The space reached its target |  |
| `Paused` | neutral | Automatic transfers are stopped |  |

## Never use these

| Not this | Use this | Why |
| --- | --- | --- |
| Processing, In progress, Awaiting | `Pending` | One term per state. |
| Cancelled | `Canceled` | American spelling baseline. |
| Rejected | `Declined` (a payment) / `Not approved` (a verification) | "Rejected" reads as blame and blurs two different outcomes. |
| Error | `Failed` | "Error" names our problem, not the state of their money. |
| Completed, Done, Successful, Settled, Paid, Active, New | no label | The normal state carries no label. |
| Unverified, Unconfirmed | `In review` or `Action needed` | Says what happens next, not what is missing. |
| Locked | `Frozen` (by the customer) or `Blocked` (by Vanker) | Two different states with two different exits. |
| Inactive | `Not activated` | Names the pending step. |
| Protected, Insured, Safe, Guaranteed | no label | A compliance claim is not a status. |

## Tone to token mapping

| Tone | Background | Dot / icon | Text |
| --- | --- | --- | --- |
| neutral | `color.surface-subtle` | `color.text-secondary` | `color.text-primary` |
| info | `color.info-subtle` | `color.info` | `color.text-primary` |
| success | `color.success-subtle` | `color.success` | `color.text-primary` |
| warning | `color.warning-subtle` | `color.warning` | `color.text-primary` |
| error | `color.error-subtle` | `color.error` | `color.text-primary` |

**Why the text is always graphite:** the tinted background carries the tone, and graphite on
every `-subtle` token clears WCAG AA comfortably in both light and dark mode. Colored text on
a tinted background of the same hue is where status labels usually fail contrast, and the
system has no `warning-text` or `info-text` token to fall back on. Do not invent one.

## Style

| Property | Value |
| --- | --- |
| Type | `caption` (12 / 16, weight 500), sentence case |
| Padding | 2px top and bottom, 8px left and right |
| Height | 20px |
| Radius | `radius.full` (see `../foundations/shape.md`) |
| Dot | 6px, 6px gap before the text |
| Icon (alternative to the dot) | `icon.sm` (16px), 4px gap |
| Max width | Never truncated; if it does not fit, the layout changes, not the label |

## Placement

- **Transaction row:** in the meta line, after the category and time (see
  `transaction-row.md`).
- **Card, list item, detail header:** trailing on the title line, or directly under it.
- **Never** inside a button, inside a heading, or as the only content of a table cell whose
  column header does not say what it describes.

## States and motion

The component itself has no interactive states: it is not focusable, not hoverable, not
pressable. What changes is the status it carries.

- A status change crossfades over `motion.duration.fast` (160ms, ease-out).
- Under `prefers-reduced-motion`, the new label replaces the old one with no transition.
- A status label never animates on its own (no pulsing, no blinking) except the
  loading/progress case, which is a different component.

## Accessibility

- The label is real text, never an image or a bare colored dot. Meaning is never in the color
  alone (see `../foundations/color.md`).
- The status is part of the accessible name of the object it belongs to, not a separate stop:
  "Mercadona, 52,40 euros out, groceries, today at 2:32 pm, pending" — one focus stop, not
  two.
- When the status is the outcome of something the person just did, announce the change with a
  polite live region; do not move focus.
- The element is not focusable and is never marked up as a link or a button.
- Text on background meets WCAG AA 4.5:1; the dot, as a non-text indicator, meets 3:1.

## Content examples

Normative pairs (the label alone, and what accompanies it):

- ✅ `Pending` in a transaction row, with "It should arrive by tomorrow" in the detail view.
- ✅ `Action needed` on the verification card, with a button labeled "Confirm identity".
- ✅ `Not approved`, with the reason and a link to the complaints route.
- ❌ "Pending 2 days" (a duration inside the label).
- ❌ "Processing" (a synonym for `Pending`).
- ❌ "Your card is frozen." (a sentence, with punctuation; the label is `Frozen`).
- ❌ "PENDING" (all caps).
- ❌ A yellow dot with no word.

## Machine-readable spec

```json
{
  "status-label": {
    "interactive": false,
    "focusable": false,
    "slots": {
      "label": { "required": true, "source": "controlled-vocabulary", "max-words": 2, "case": "sentence", "punctuation": false, "emoji": false, "digits": false },
      "indicator": { "required": false, "one-of": ["dot", "icon"], "dot-size": 6, "icon-size": 16 }
    },
    "default-state": "no-label",
    "max-per-object": 1,
    "vocabulary": {
      "transaction": ["Pending", "Scheduled", "On hold", "Declined", "Failed", "Canceled", "Refunded", "Returned"],
      "card": ["Frozen", "Blocked", "Not activated", "Expired", "Canceled"],
      "verification": ["In review", "Action needed", "Verified", "Expired", "Not approved"],
      "recurring-payment": ["Upcoming", "Paused", "Canceled", "Failed"],
      "space": ["Target reached", "Paused"]
    },
    "tone-map": {
      "Pending": "warning", "Scheduled": "info", "On hold": "warning", "Declined": "error",
      "Failed": "error", "Canceled": "neutral", "Refunded": "success", "Returned": "neutral",
      "Frozen": "info", "Blocked": "error", "Not activated": "warning", "Expired": "neutral",
      "In review": "info", "Action needed": "warning", "Verified": "success", "Not approved": "error",
      "Upcoming": "info", "Paused": "neutral", "Target reached": "success"
    },
    "tone-tokens": {
      "neutral": { "bg": "color.surface-subtle", "dot": "color.text-secondary", "text": "color.text-primary" },
      "info":    { "bg": "color.info-subtle",    "dot": "color.info",           "text": "color.text-primary" },
      "success": { "bg": "color.success-subtle", "dot": "color.success",        "text": "color.text-primary" },
      "warning": { "bg": "color.warning-subtle", "dot": "color.warning",        "text": "color.text-primary" },
      "error":   { "bg": "color.error-subtle",   "dot": "color.error",          "text": "color.text-primary" }
    },
    "forbidden-tone": "color.accent",
    "banned-labels": {
      "Processing": "Pending", "In progress": "Pending", "Awaiting": "Pending",
      "Cancelled": "Canceled", "Rejected": "Declined | Not approved", "Error": "Failed",
      "Completed": "no-label", "Done": "no-label", "Successful": "no-label", "Settled": "no-label",
      "Paid": "no-label", "Active": "no-label", "New": "no-label",
      "Unverified": "In review | Action needed", "Locked": "Frozen | Blocked",
      "Inactive": "Not activated", "Protected": "no-label", "Insured": "no-label", "Guaranteed": "no-label"
    },
    "style": { "type": "caption", "height": 20, "padding": [2, 8], "radius": "radius.full", "truncate": false },
    "motion": { "change": "motion.duration.fast", "reduced-motion": "none", "idle-animation": false },
    "a11y": { "text-not-color": true, "part-of-parent-name": true, "focusable": false, "live-region": "polite", "contrast": { "text": 4.5, "indicator": 3.0 } }
  }
}
```

## Eval hooks

- The label is one or two words, sentence case, with no ending punctuation, emoji, digits, or
  ALL CAPS.
- The label is a term from the controlled vocabulary; synonyms and free copy fail.
- A default state (settled, active, verified in place, completed) carries no status label.
- No amount, date, duration, or count appears inside the label.
- No compliance or guarantee claim is used as a status.
- The brand accent is never used as a status tone.
- A negative outcome (`Declined`, `Failed`, `On hold`, `Not approved`) is accompanied by an
  explanation, and by the complaints route where the outcome affects the customer.
