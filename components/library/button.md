# Button

**Status: normative.**

The primary interactive control. A button triggers an action, and its label is an action
verb only (see `../../patterns/ctas.md`). Every value below comes from the foundations.

## Variants (most to least emphasis)

| Variant | Style | Use |
| --- | --- | --- |
| Primary | Graphite fill, white text | The single main action on a screen |
| Accent | Fuchsia fill, white text | One standout brand action (for example "Add money"). Used sparingly, never for destructive actions |
| Secondary | Surface fill, 1px border, graphite text | A secondary action beside the primary |
| Tertiary | No fill, graphite text | Low-emphasis actions ("Not now", "Cancel", "Back") |
| Destructive | Error fill, white text | Confirming a destructive action ("Delete space") |

Rule: one Primary **or** one Accent per screen, never both competing as main actions.

## Anatomy

- **Label** (required): an action verb, 3 words maximum (aim for one), no messages.
- **Leading icon** (optional): 20px (`icon.md`), 8px gap (`space.2`), inherits text color.
- **Full width** (optional): stretches to the container; the label stays centered.

## Sizes

| Token | Height | Padding (h) | Type | Use |
| --- | --- | --- | --- | --- |
| `lg` | 52px | 24px | `button` (16) | Prominent, often full-width CTAs |
| `md` | 48px | 20px | `button` (16) | Default |
| `sm` | 40px | 16px | `body-sm` (14) | Compact contexts (keep a 44px tap area) |

## States

| State | Treatment |
| --- | --- |
| Default | Variant colors above |
| Pressed | Scale 0.97 over `motion.duration.fast` (120ms); Primary also darkens to `color.primary-pressed` |
| Focus (keyboard) | 2px fuchsia focus ring (`focus.ring`), 2px offset |
| Disabled | `color.surface-subtle` fill, `color.text-tertiary` label, no pointer, `aria-disabled` |
| Loading | Spinner replaces or precedes the label; the button is non-interactive and announces a busy status |

## Content rules

- The label is an action verb phrase, 3 words maximum (aim for one).
- Never put an amount, a message, a status, a notification, or toast text in a button.
- Match the label to the outcome ("Send money", not "Confirm"). Never put an amount in the label. See `../../patterns/ctas.md`.

## Accessibility

- Minimum tap target 44px; the default 48px height meets it. Small buttons keep a 44px
  tap area through padding and spacing.
- Focus is always visible on keyboard navigation.
- Never signal meaning by color alone: a destructive button also reads as destructive in
  its label, and the disabled state is shown by more than color.
- Loading sets an accessible busy status; disabled sets `aria-disabled`.

## Machine-readable spec

Values reference foundation tokens by name, so the button never hard-codes what the
foundations already define.

```json
{
  "button": {
    "variants": {
      "primary":     { "bg": "color.primary", "text": "color.on-primary", "border": null },
      "accent":      { "bg": "color.accent",  "text": "color.on-accent",  "border": null },
      "secondary":   { "bg": "color.surface", "text": "color.text-primary", "border": "color.border" },
      "tertiary":    { "bg": "transparent",   "text": "color.text-primary", "border": null },
      "destructive": { "bg": "color.error",   "text": "#FFFFFF", "border": null }
    },
    "size": {
      "lg": { "height": 52, "padding-x": 24, "type": "button" },
      "md": { "height": 48, "padding-x": 20, "type": "button" },
      "sm": { "height": 40, "padding-x": 16, "type": "body-sm" }
    },
    "radius": "radius.md",
    "icon": { "size": "icon.md", "gap": "space.2" },
    "press": { "scale": 0.97, "duration": "motion.duration.fast", "easing": "motion.easing.standard" },
    "focus": "focus.ring",
    "content": { "label": "action verb, max 3 words", "forbid": ["number", "amount", "punctuation", "emoji", "message", "status", "notification", "toast"] }
  }
}
```
