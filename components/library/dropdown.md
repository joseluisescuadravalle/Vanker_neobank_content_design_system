# Select (dropdown)

**Status: normative.**

An input for choosing one value from a short, predefined list. Distinct from a *menu*
dropdown, which triggers actions. It reuses the text field's styling and label convention.

## Slots

- **Label** (required, outside the field): a short noun in sentence case that names the
  data, clear and concise, never a question, **no ending period**. Optional fields add
  "(optional)". Always visible (see `text-field.md`).
- **Prompt** (default): the placeholder shown before a choice, "Choose an option", in muted
  text (`color.text-tertiary`). It disappears once a value is chosen.
- **Options** (2 to 5): the predefined choices, in minimal words (1 to 3). They are
  **parallel** (same grammatical form), sentence case, **no ending punctuation**, mutually
  exclusive, in a logical order (alphabetical, by frequency, or a meaningful order).
- **Selected value**: once chosen, it replaces the prompt and shows in `color.text-primary`
  (ink), like an entered value.

## Rules

- **At most 5 options.** If there are more, a dropdown is the wrong component: use a
  searchable select or another pattern (a long dropdown is hard to scan and reach on mobile).
- Options say the least needed to be clear; no ending punctuation, no emoji.
- The label is always visible, so the field is identified even before a choice.

## States

| State | Treatment |
| --- | --- |
| Default | Prompt "Choose an option" in muted text; chevron on the right |
| Open | The options list; the current choice marked |
| Selected | The chosen option in ink, replacing the prompt |
| Disabled | `color.surface-subtle`, not operable |
| Error | If required and left unselected, a field validation error below (see `../../patterns/errors.md`, "Field validation"), for example "Choose an option to continue." |

## Visual

Reuses the text field: outlined, `radius.md` (12px), 48px tall, with a chevron
(`icon.md`) indicating it opens. Focus shows the 2px fuchsia ring.

## Accessibility

- A native `select` or an accessible listbox: operable by keyboard, the label
  programmatically associated, and the options and the current selection announced.
- The chevron is decorative; the accessible name comes from the label.
- Minimum 44px tap target.

## Machine-readable spec

```json
{
  "select": {
    "label": { "style": "short noun, sentence case, no period", "always-visible": true },
    "prompt": { "text": "Choose an option", "color": "color.text-tertiary" },
    "options": { "max": 5, "words": "1-3", "punctuation": "none", "parallel": true },
    "selected": { "color": "color.text-primary" },
    "states": ["default", "open", "selected", "disabled", "error"],
    "error": "field-validation (see patterns/errors.md)",
    "reuses": "text-field styling",
    "a11y": { "role": "listbox-or-select", "label-associated": true, "min-target": 44 }
  }
}
```
