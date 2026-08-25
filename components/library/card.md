# Card

**Status: normative.**

A surface that groups related content. Vanker cards are flat: a surface with a 1px
border, no shadow (see `../foundations/elevation.md`). This file covers the base
container and the two signature variants, account and Space.

## Base container

| Property | Token |
| --- | --- |
| Background | `color.surface` |
| Border | 1px `color.border` (elevation role `card`) |
| Radius | `radius.lg` (16px) |
| Padding | `space.5` (20px) |

## Variant: account card

The home screen hero. It shows a balance, front and center.

- **Label:** the account name in sentence case ("Current account"), `caption`,
  `color.text-secondary`.
- **Balance:** `display-lg` (40 / 800), tabular numbers, `color.text-primary`.
- **Subtext:** masked IBAN (International Bank Account Number), last 4 digits visible,
  `color.text-secondary`.
- **Trailing menu** (optional): a 20px icon with an accessible label.

## Variant: Space card

Money set aside toward a target (see `../../terminology/glossary.md`).

- **Icon + name:** the Space name (`title`, 700), truncated to one line with an
  ellipsis. The icon is an outline icon or a user-chosen emoji.
- **Progress:** a track (`color.surface-subtle`) with a fuchsia fill (`color.accent`)
  showing saved vs target.
- **Amounts:** always shown as text ("600 € of 1.000 €"), saved amount bold in
  `text-primary`, target in `text-secondary`. Never rely on the bar alone.
- **States:** in progress; funded (`color.success-text` with a check, "Fully funded");
  empty (0 of target, with an "Add money" affordance).

## Interactive cards

When the whole card is tappable (it navigates or opens something):

- It is a real button or link with a clear accessible name (for example "Travel Space,
  600 of 1.000 euros").
- **Pressed:** background shifts to `color.surface-subtle` (or a 0.99 scale) over
  `motion.duration.fast`.
- **Focus:** 2px fuchsia focus ring (`focus.ring`).
- Minimum tap target 44px applies to the card and to any control inside it.

## States

| State | Treatment |
| --- | --- |
| Default | Base container |
| Pressed (interactive) | `surface-subtle` background |
| Selected (optional) | 2px `color.accent` border |
| Loading | Skeleton placeholders for text and amounts, not a spinner |

## Content rules

- All amounts use tabular numbers and are concrete (never "a bit more").
- The balance is the account's current balance; the label names the account.
- Space names are user-provided: truncate to one line, never wrap to three.
- Progress is always stated in text as well as the bar.

## Accessibility

- An interactive card is fully focusable and announces a single, meaningful name.
- Progress is conveyed in text, not by color or bar length alone.
- The menu icon and any inner control each have an accessible label.

## Machine-readable spec

```json
{
  "card": {
    "container": { "bg": "color.surface", "border": "color.border", "radius": "radius.lg", "padding": "space.5" },
    "variants": {
      "account": { "label": "caption/text-secondary", "balance": "display-lg/tabular", "subtext": "masked-iban" },
      "space": {
        "name": "title",
        "progress": { "track": "color.surface-subtle", "fill": "color.accent" },
        "amounts": "text-required",
        "states": ["in-progress", "funded", "empty"]
      }
    },
    "interactive": { "pressed": "color.surface-subtle", "focus": "focus.ring", "min-target": 44 },
    "numbers": "tabular"
  }
}
```
