# Radio group

**Status: normative.**

Lets a person choose **one** option and discard the rest, with all options visible at
once. Use it when the choices are few and worth showing; when the list is long or space is
tight, use a `dropdown.md` instead. Form-level rules are in `../../patterns/forms.md`.

## Slots

- **Legend** (required): the question or label that heads the group and names the choice
  ("How do you file taxes", "Gender"). It is the group's label; see
  `../../patterns/forms.md`. No ending period or colon.
- **Options** (2 to ~5, each required text): the mutually exclusive choices. Each is
  **clearly distinguishable** with no ambiguity, **keeps its pronouns and articles** (do
  not clip them the way a dropdown option is clipped), and fits on **one line**. Sentence
  case, no ending punctuation, no emoji.
- **Helper text** (optional): a short clarification below the group if the choice needs it.

## Rules

- Exactly one option can be selected; the options together must be **exhaustive and
  mutually exclusive** (add a neutral option like "Prefer not to say" when relevant).
- Options are **parallel** in grammar and clearly different from one another; the person
  should never have to guess how two options differ.
- **Keep the words that carry meaning.** Unlike a dropdown option, a radio option may be a
  short phrase or a first-person statement ("I am an individual"), not a bare noun.
- Do not pre-select a consequential option by default when the choice is meaningful; if a
  default is needed, make it the safe, expected one.

## Content examples (slot format)

- Legend "Account type" / options "I am an individual" · "I am a business" ✅
- Legend "Gender" / options "Male" · "Female" · "Prefer not to say" ✅
- Options "Individual" · "Self-employed person who is also…" ❌ (not one line, not parallel)

## States

| State | Treatment |
| --- | --- |
| Unselected | Empty circles, `color.border` |
| Selected | One filled circle, `color.accent` (fuchsia) |
| Focus | Fuchsia focus ring on the focused option |
| Error | If required and none chosen, a field validation error below (see `../../patterns/errors.md`) |
| Disabled | `color.surface-subtle`, not operable |

## Accessibility

- Wrap the options in a group with the legend as its accessible name (`fieldset` /
  `legend` or `role="radiogroup"` + `aria-labelledby`).
- Arrow keys move between options; the selection is announced, not conveyed by color alone.
- Minimum 44px tap target for each option (circle and label).

## Machine-readable spec

```json
{
  "radio-group": {
    "legend": { "required": true, "role": "group-label", "ending-punctuation": "none" },
    "options": {
      "count": "2-5", "one-line": true, "parallel": true, "mutually-exclusive": true,
      "keep-articles-pronouns": true, "punctuation": "none", "emoji": false
    },
    "selected-color": "color.accent",
    "states": ["unselected", "selected", "focus", "error", "disabled"],
    "error": "field-validation (see patterns/errors.md)",
    "a11y": { "role": "radiogroup", "legend-as-name": true, "arrow-key-nav": true, "min-target": 44 }
  }
}
```

## Eval hooks

- Each option fits one line, keeps its articles/pronouns, and has no ending punctuation or
  emoji.
- Options are parallel and mutually exclusive; a neutral option is offered where relevant.
- The group has a legend as its accessible name.
