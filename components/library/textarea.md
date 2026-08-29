# Text area

**Status: normative.**

The multi-line field where a person **composes** something in their own words: the
reference on a transfer, the name of a space, a message to support, feedback. It is not a
taller text field: what changes is that the person is writing, not filling in.

Field mechanics it shares with `text-field.md` (the label model, focus, error styling)
apply here; the form-level rules are in `../../patterns/forms.md`.

## Slots

- **Label in** (required): as in `text-field.md`, floating to the top edge of the box. It
  stays visible while the person writes, which matters more here than anywhere else,
  because the caret can end up far from it.
- **Label out** (optional): where the field needs a question or a qualifier the short label
  cannot carry.
- **Helper text** (optional): what the text is for and who will read it. On a transfer
  reference this is not decoration: "The person receiving the money will see this."
- **Counter** (conditional): see below.
- **Error** (conditional): one sentence, as in `../../patterns/errors.md`.

## Size and behavior

- Three lines tall by default, growing with the content up to about eight, then scrolling
  inside itself. It never grows without limit and never pushes the submit button off the
  screen.
- No resize handle on mobile; on a pointer device, vertical resize only.
- Enter inserts a line break and never submits the form.
- The value survives leaving the screen and coming back (see `../../patterns/loading.md`).

## The counter

**A plain form field has no counter.** A counter belongs here, and only when **both** are
true: the person is composing free text, and there is a **real limit that would cut what
they wrote**.

The clearest case in a bank is the transfer reference: the remittance information in a SEPA
transfer is capped at 140 characters, and silently trimming it changes what the recipient
reads on their statement. A limit that exists only because a database column was declared
that way is not a reason to count in front of a person.

- **It appears near the end, not from the start.** Show it when about 20 characters or 20%
  remain, whichever comes first. A `0/140` on an empty box turns a message into a quota.
- **It counts what is left, in words:** "22 characters left", "0 characters left". Not
  "118/140": the person cares about the room they have, not about arithmetic.
- **At the limit the field stops accepting characters.** It does not truncate afterwards
  and it does not raise an error: the counter at "0 characters left" has already said it.
- Announce it politely and **only at thresholds** (when it appears, and at zero), never on
  every keystroke.
- Where the limit is generous enough that nobody reaches it, there is no counter.

## Content rules

- The label names what the person writes, not the field: "Reference", "Message", "Space
  name".
- **Say who will read it**, in helper text, wherever it is not obvious. This is the rule
  that prevents someone writing "for the divorce lawyer" in a transfer reference their
  ex-partner will see on their statement.
- A placeholder here is a **format example only**, as everywhere in a form; the exception
  for guide phrases is for search and marketing surfaces, not for this
  (`../../patterns/forms.md`).
- Never pre-fill a composed field with suggested wording the person may send without
  reading.
- No character limit invented to shape behavior ("keep it short"): if there is a limit, it
  is technical, and it is stated by the counter.

## States

| State | Treatment |
| --- | --- |
| Empty | Label in centered on the first line; border `color.border` |
| Focus | Border `color.accent`, focus ring; label in floated to the top edge |
| Filled | Label floated, value `color.text-primary`, box grown to fit |
| Near the limit | Counter visible in `color.text-secondary` |
| At the limit | Counter "0 characters left" in `color.text-secondary`; input stops |
| Error | Border `color.error`, message below, `aria-invalid`; the counter stays |
| Disabled | `color.surface-subtle`, not editable, with the reason next to the field |

## Accessibility

- One `textarea` with its label tied by `for` / `id`; the label never disappears.
- The counter is tied to the field with `aria-describedby` and lives in a **polite** live
  region that speaks at thresholds, not per keystroke.
- The helper text saying who will read the content is part of the field's description, not
  a separate visual note.
- Minimum 44px targets around anything interactive; the box itself is at least 96px tall.
- Never trap focus: Tab moves out of the field, it does not insert a tab character.

## Content examples

- ✅ Label "Reference" · Helper "The person receiving the money will see this." · Counter
  "22 characters left"
- ✅ Label "Message" · Helper "Our support team will read this."
- ❌ A counter reading "0/140" on an empty field.
- ❌ "Keep it brief" as a limit.
- ❌ Silently cutting the reference at 140 characters after the person taps send.

## Machine-readable spec

```json
{
  "textarea": {
    "purpose": "composed free text",
    "label-in": { "required": true, "behavior": "floating", "persistent": true },
    "rows": { "default": 3, "max-grow": 8, "then": "scroll" },
    "enter-submits": false,
    "counter": {
      "required-when": ["free-text composition", "a real limit that would cut the content"],
      "appears-at": "20 characters or 20% remaining",
      "format": "{n} characters left",
      "at-limit": "stops accepting input",
      "truncates-silently": false,
      "announce": "polite, at thresholds only"
    },
    "helper": { "states-who-reads-it": true },
    "placeholder": "format-example-only",
    "prefill-suggested-wording": false,
    "states": ["empty", "focus", "filled", "near-limit", "at-limit", "error", "disabled"],
    "a11y": { "label-for-id": true, "counter-describedby": true, "live-region": "polite", "min-height": 96, "tab-moves-out": true }
  }
}
```

## Eval hooks

- A counter exists only where the person composes free text against a real limit, and it is
  written as "{n} characters left", never as a ratio.
- The counter appears near the limit, not from the first character.
- Nothing is silently truncated: at the limit the field stops accepting input.
- Helper text says who will read the content wherever that is not obvious.
- The field is not pre-filled with wording the person might send unread.
- The label names what the person writes, not the field.
