# Select (dropdown)

**Status: normative.**

An input for choosing one value from a short, predefined list. Distinct from a *menu*
dropdown, which triggers actions. It reuses the text field's styling and label model (see
`text-field.md` and `../../patterns/forms.md`).

## Slots

- **Label** (required): the same label model as the text field. A **label in** names the
  field ("Document type"); a **label out** is added only when the choice needs a
  descriptive or interrogative phrase a short label cannot carry. Sentence case, no ending
  period. Adapt the microcopy to whichever label you use, and do not let it repeat the
  options. Optional fields add "(optional)".
- **Prompt** (default): the placeholder shown before a choice, "Choose an option", in muted
  text (`color.text-tertiary`). It disappears once a value is chosen and never stands in for
  the label.
- **Options** (2 to 5): the predefined choices, in minimal words (1 to 3). They are
  **parallel** (same grammatical form), sentence case, **no ending punctuation**, mutually
  exclusive, in a logical order (alphabetical, by frequency, or a meaningful order). The
  options **do not repeat the label's verb**: label "Profession" with options "Employee /
  Self-employed / Student", not label "What do you do?" with options "I am self-employed /
  I work for a company / I am a student".
- **Selected value**: once chosen, it replaces the prompt and shows in `color.text-primary`
  (ink), like an entered value.

## Rules

- **At most 5 options.** If there are more, a dropdown is the wrong component: use a
  searchable select or another pattern (a long dropdown is hard to scan and reach on mobile).
- Options say the least needed to be clear; no ending punctuation, no emoji.
- The label is always visible, so the field is identified even before a choice.
- Do not restate the label in the options, and do not use an empty label ("Choose an
  option") as the field's only name.

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
(`../foundations/iconography.md`) indicating it opens. Focus shows the fuchsia ring.

## Accessibility

- A native `select` or an accessible listbox: operable by keyboard, the label
  programmatically associated, and the options and the current selection announced.
- The chevron is decorative; the accessible name comes from the label.
- Minimum 44px tap target.

## Machine-readable spec

```json
{
  "select": {
    "label": { "model": "label-in + optional label-out (see text-field)", "style": "short noun, sentence case, no period", "always-visible": true, "no-repeat-in-options": true },
    "prompt": { "text": "Choose an option", "color": "color.text-tertiary", "never-a-label": true },
    "options": { "max": 5, "words": "1-3", "punctuation": "none", "parallel": true, "no-verb-repeat": true },
    "selected": { "color": "color.text-primary" },
    "states": ["default", "open", "selected", "disabled", "error"],
    "error": "field-validation (see patterns/errors.md)",
    "reuses": "text-field styling",
    "a11y": { "role": "listbox-or-select", "label-associated": true, "min-target": 44 }
  }
}
```
