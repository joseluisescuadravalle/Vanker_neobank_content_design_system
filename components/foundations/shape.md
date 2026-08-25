# Shape

**Status: normative.**

**Decided:** "Rounded" corners. Friendly and modern, still composed. Interactive
elements at 12px, cards at 16px, with a consistent radius scale below.

## Radius scale

| Token | Value | Use |
| --- | --- | --- |
| `radius.none` | 0 | Full-bleed edges, dividers |
| `radius.xs` | 6px | Small badges, inner elements |
| `radius.sm` | 8px | Thumbnails, small tiles |
| `radius.md` | 12px | Buttons, inputs, interactive elements |
| `radius.lg` | 16px | Cards |
| `radius.xl` | 20px | Sheets, modals |
| `radius.2xl` | 28px | Bottom-sheet top edge, large surfaces |
| `radius.full` | 999px | Pills, chips, tags, toggles, avatars |

## Component mapping

| Element | Token |
| --- | --- |
| Button, CTA | `radius.md` (12px) |
| Text field, input | `radius.md` (12px) |
| Card | `radius.lg` (16px) |
| Sheet, modal | `radius.xl` (20px); bottom sheets round the top corners at `radius.2xl` |
| Chip, tag, badge | `radius.full` |
| Avatar, toggle | `radius.full` |
| Image thumbnail | `radius.sm` (8px) |

## Borders and focus

| Token | Value | Use |
| --- | --- | --- |
| `border.width.hairline` | 1px | Dividers, input outlines, card borders |
| `border.width.strong` | 2px | Selected state, emphasis |
| `focus.ring.width` | 2px | Keyboard focus indicator |
| `focus.ring.color` | `color.accent` (`#DB2777`) | Focus indicator color |
| `focus.ring.offset` | 2px | Gap between element and ring |

## Usage rules

- One radius per element type; do not mix radii on the same component.
- When an element nests inside another, use one step smaller so corners sit concentric
  (for example a `radius.sm` thumbnail inside a `radius.lg` card).
- Pills (`radius.full`) are for chips, tags, toggles, and avatars only, never for cards
  or large surfaces.

## Accessibility

- Corner radius is a stylistic choice, not an accessibility feature. Accessibility comes
  from touch-target size (see `spacing.md`), contrast (see `color.md`), and a visible
  focus indicator.
- Every interactive element shows the focus ring on keyboard navigation. Never remove
  the focus indicator without replacing it with an equally visible one.

## Machine-readable tokens

```json
{
  "radius": {
    "none": 0, "xs": 6, "sm": 8, "md": 12, "lg": 16, "xl": 20, "2xl": 28, "full": 999
  },
  "border": { "width": { "hairline": 1, "strong": 2 } },
  "focus":  { "ring": { "width": 2, "color": "#DB2777", "offset": 2 } }
}
```
