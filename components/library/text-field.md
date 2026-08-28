# Text field

**Status: normative.**

The core input for typed data. A text field is always led by a **visible, persistent
label**; guidance lives in the label and helper text, never in a placeholder alone. The
form-level rules (the three principles, grouping, the field-text hierarchy) are in
`../../patterns/forms.md`; this file is the component.

## Slots

- **Label in** (required): the text inside the empty field that names the data. When the
  person types, it **does not disappear** — it shrinks and floats to the top of the field,
  staying visible above the value ("floating label"). A short noun in sentence case, the
  fewest words possible (aim 1 to 3), no ending period, colon, or question mark. Optional
  fields add "(optional)" in a lighter weight. This is the accessible default: the field is
  never left without a visible name.
- **Label out** (optional): text above the field, used when the data needs a **descriptive
  or interrogative phrase** the short label in cannot carry (a qualifier or a
  disambiguation, not merely a slightly long noun). A question mark is allowed; a period
  and a colon are not. When present, the **label in stays** as the short reference, and the
  two must not repeat the same words.
  - Label out "Combined monthly income of both spouses" · Label in "Monthly income" ✅
  - Label out "Enter your name" · Label in "Name" ❌ (drop the redundant label out)
- **Legend** (for groups): a short word or phrase that heads a group of related fields
  (see `../../patterns/forms.md`). No ending period or colon; does not restate the labels.
- **Field** (outlined): 1px border, 12px corners, 48px tall.
- **Leading / trailing icon** (optional): 20px (`../foundations/iconography.md`), for
  context (a currency symbol) or an action (show password, clear).
- **Placeholder** (optional): a **format example only** ("DD/MM/YYYY", "you@example.com"),
  in muted text. Most fields have none. It never carries essential information, because it
  disappears as soon as the person types, and it never stands in for the label in.
- **Helper text** (optional): one short line below, plain and specific ("We will use this
  to sign you in"). Not a place for legal text or a call to action. Replaced by the error
  message when there is an error.

## Content rules (Vanker forms)

- **Never hide the label** or rely on a placeholder to name the field.
- **Optional vs required:** fields are required by default; mark only the optional ones
  with "(optional)". Do not use asterisks.
- **Error text:** one clear sentence with a specific hint, never blaming the person, shown
  in red with an icon and announced to screen readers, not color alone ("An IBAN must
  contain 24 characters."). See `../../patterns/errors.md` (field validation errors).
- **Character limits:** when a limit matters, show a live counter; do not silently
  truncate.
- **No confirmation fields:** do not duplicate a field to confirm it (password, email);
  use a show/hide toggle instead.

## Visual and states

| State | Treatment |
| --- | --- |
| Empty | Label in centered in the field at body size; border `color.border` |
| Focus | Border `color.accent`, 3px fuchsia focus ring; label in floats up |
| Filled | Label in floated (small) above the value in `color.text-primary` |
| Error | Border `color.error`, trailing error icon, message in `color.error-text`, `aria-invalid` |
| Disabled | `color.surface-subtle` fill, `color.text-tertiary` text, not editable |
| Read-only | Value shown, no strong border, not editable (distinct from disabled) |

Field height 48px, radius `radius.md` (12px), horizontal padding `space.3`/`space.4`,
value text `font.scale.body` (16px). 16px prevents mobile browsers from zooming on focus.

## The floating label (behavior and its risks)

The label in moving up is what keeps the label persistent, but it has two costs to control:

- **Legibility.** In its floated state the label is smaller. It must still meet **WCAG 2.1
  AA contrast** against the field background; do not let the floated label drop to a muted
  tertiary color. For fields carrying money or other critical data, verify the shrunk
  label's contrast explicitly.
- **Motion.** The float is a small transition (`motion` foundation, ~160ms ease-out) and
  must respect **`prefers-reduced-motion`**: when reduced motion is set, the label snaps to
  its floated position without animating.

A placeholder of *format* (for example `DD/MM/YYYY`) may coexist with the floating label
in: they do different jobs (one names the field, one shows the format) and do not compete.

## Accessibility

- The label in is programmatically tied to the input (`for` / `id`), so it is always
  announced and its tap area also focuses the field; it stays visible in every state.
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
    "label-in": { "required": true, "behavior": "floating", "persistent": true, "case": "sentence", "style": "short noun", "words": "1-3", "ending-punctuation": "none", "optional-marker": "(optional)" },
    "label-out": { "required": false, "form": "descriptive-or-interrogative", "ending-period": false, "colon": false, "keeps-label-in": true, "no-verbatim-repeat": true },
    "legend": { "required": false, "scope": "field-group", "ending-punctuation": "none" },
    "placeholder": { "use": "format-example-only", "color": "color.text-tertiary", "never-a-label": true },
    "helper-text": { "lines-max": 3, "question": false, "cta": false },
    "float": { "duration-ms": 160, "respects-reduced-motion": true, "shrunk-label-contrast": "AA" },
    "states": {
      "empty":    { "border": "color.border", "label": "in-field" },
      "focus":    { "border": "color.accent", "ring": "focus.ring", "label": "floated" },
      "filled":   { "label": "floated", "value": "color.text-primary" },
      "error":    { "border": "color.error", "text": "color.error-text", "aria-invalid": true },
      "disabled": { "bg": "color.surface-subtle", "text": "color.text-tertiary" }
    },
    "a11y": { "label-for-id": true, "label-persistent": true, "error-describedby": true, "min-target": 44 }
  }
}
```
