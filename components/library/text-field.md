# Text field

**Status: normative.**

The core input for typed data. A text field is always led by a visible label; guidance
lives in the label and helper text, never in a placeholder alone.

## Anatomy

1. **Label** (required, on top): a short noun in sentence case ("Email address",
   "Amount"). Always visible. Optional fields add "(optional)" in a lighter weight.
2. **Field** (outlined): 1px border, 12px corners, 48px tall.
3. **Leading / trailing icon** (optional): 20px (`icon.md`), for context (a currency
   symbol) or an action (show password, clear).
4. **Helper text** (optional): one short line below, for guidance the user needs before
   acting. Replaced by the error message when there is an error.

## Content rules (Vanker forms)

- **Labels:** short noun, sentence case. Never hide the label or rely on a placeholder
  to name the field.
- **Placeholders:** only a format example (`DD/MM/YYYY`, `you@example.com`), in muted
  text. Most fields have none. A placeholder never carries essential information, because
  it disappears as soon as the person types.
- **Optional vs required:** fields are required by default; mark only the optional ones
  with "(optional)". Do not use asterisks.
- **Helper text:** one short line, plain and specific ("We will use this to sign you
  in"). Not a place for legal text.
- **Error text:** one clear sentence with a specific hint, never blaming the person, shown
  in red with an icon and announced to screen readers, not color alone ("An IBAN must
  contain 24 characters."). See `../../patterns/errors.md` (field validation errors).
- **Character limits:** when a limit matters, show a live counter; do not silently
  truncate.

## Visual and states

| State | Treatment |
| --- | --- |
| Default | Border `color.border`, label `color.text-primary`, helper `color.text-secondary` |
| Focus | Border `color.accent`, 3px fuchsia focus ring; label stays `text-primary` |
| Filled | Same as default, with the value in `color.text-primary` |
| Error | Border `color.error`, trailing error icon, message in `color.error-text`, `aria-invalid` |
| Disabled | `color.surface-subtle` fill, `color.text-tertiary` text, not editable |
| Read-only | Value shown, no strong border, not editable (distinct from disabled) |

Field height 48px, radius `radius.md` (12px), horizontal padding `space.3`/`space.4`,
text `font.scale.body` (16px). 16px prevents mobile browsers from zooming on focus.

## Accessibility

- The label is programmatically tied to the input (`for` / `id`), so it is always
  announced and its tap area also focuses the field.
- Error messages are linked to the field (`aria-describedby`) and never rely on color
  alone; they always include an icon and text.
- Keep the 44px minimum tap target; the 48px height meets it.
- Set the right `type`, `inputmode`, and `autocomplete` (for example `type="email"`,
  `inputmode="numeric"`, `autocomplete="one-time-code"`) so keyboards and autofill help
  everyone.

## Machine-readable spec

```json
{
  "text-field": {
    "height": 48,
    "radius": "radius.md",
    "type": "font.scale.body",
    "label": { "case": "sentence", "style": "short noun", "optional-marker": "(optional)", "required-default": true },
    "placeholder": { "use": "format-example-only", "color": "color.text-tertiary" },
    "states": {
      "default":  { "border": "color.border" },
      "focus":    { "border": "color.accent", "ring": "focus.ring" },
      "error":    { "border": "color.error", "text": "color.error-text", "aria-invalid": true },
      "disabled": { "bg": "color.surface-subtle", "text": "color.text-tertiary" }
    },
    "a11y": { "label-for-id": true, "error-describedby": true, "min-target": 44 }
  }
}
```
