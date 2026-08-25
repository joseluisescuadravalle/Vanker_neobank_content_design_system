# Iconography

**Status: normative.**

**Decided:** an **outline** icon set with rounded joins and a thin, even stroke, on a
24px grid (the Lucide or Phosphor style, both open and free). The selected state turns
**fuchsia**; the icon stays outline. This keeps the interface calm, flat, and on-brand.

## Style

- Outline only, no filled icons in the product. Rounded line caps and joins.
- Stroke weight 1.75px on the 24px grid; it scales proportionally at other sizes.
- One consistent set across the whole product. Do not mix icon families.

## Sizes

| Token | Value | Use |
| --- | --- | --- |
| `icon.sm` | 16px | Inline with `body-sm`, dense UI |
| `icon.md` | 20px | Inline with `body`, inside buttons |
| `icon.lg` | 24px | Navigation, standalone actions (default) |
| `icon.xl` | 32px | Feature moments |
| `icon.illustration` | ~56px | Illustration in empty states and onboarding (fuchsia stroke, no container) |

## Roles

- **UI icons** (16 to 32px): navigation, banners, toasts, buttons, and inline with text.
- **Illustration icons** (about 56px): the focal image in empty states and in some
  onboarding or marketing moments. Fuchsia (`color.accent`) stroke, standalone, no circle.

## Color by state

| State | Color |
| --- | --- |
| Default (supporting) | `color.text-secondary` |
| Default (prominent) | `color.text-primary` |
| Active / selected | `color.accent` (`#DB2777`) |
| Disabled | `color.text-tertiary` |
| On a primary or accent surface | `color.on-primary` / `color.on-accent` |

Icons inherit the current text color by default, so a fuchsia label carries a fuchsia
icon automatically.

## Usage rules

- An icon that carries meaning is paired with a text label, or given a text
  alternative. Never rely on an icon alone to convey a critical action or status.
- Use one icon per meaning, consistently (the same icon always means the same thing).
- Do not recolor icons decoratively; color signals state, not style.

## Accessibility

- The tappable target is at least 44px even when the icon looks 24px (see `spacing.md`).
- Every meaningful icon has an accessible name (for example an `aria-label`), so screen
  readers announce it.
- Do not use color alone to show the active state; the fuchsia is paired with the
  selected label and position.

## Machine-readable tokens

```json
{
  "icon": {
    "style": "outline",
    "stroke": 1.75,
    "grid": 24,
    "size": { "sm": 16, "md": 20, "lg": 24, "xl": 32, "illustration": 56 },
    "color": {
      "default": "#6B7280",
      "prominent": "#111827",
      "active": "#DB2777",
      "disabled": "#9CA3AF"
    }
  }
}
```
