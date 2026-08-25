# Color

**Status: normative.**

**Decided:** direction "Graphite + fuchsia" (a near-black primary with a single fuchsia
accent). Light-first, with a full dark mode. Primary `#111827`, accent `#DB2777`.

## Principles

- **Graphite is primary; fuchsia is the accent.** The near-black primary carries the
  main actions and structure. Fuchsia is the brand pop, used sparingly for emphasis,
  secondary actions, selected states, links, and small brand moments. It never fills
  large areas.
- **Semantic colors mean something fixed** (success, error, warning, info). Never use
  them decoratively, and never use the brand colors to signal state.
- **Every text-on-background pair meets WCAG AA** (4.5:1 for normal text, 3:1 for large
  text and UI). The values below are chosen for this.
- **Never rely on color alone** to convey meaning; pair it with a label or icon.

## Tokens

### Brand

| Token | Light | Dark | Use |
| --- | --- | --- | --- |
| `color.primary` | `#111827` | `#F9FAFB` | Primary actions, key surfaces |
| `color.primary-pressed` | `#000000` | `#E5E7EB` | Pressed / hover of primary |
| `color.on-primary` | `#FFFFFF` | `#111827` | Text and icons on primary |
| `color.accent` | `#DB2777` | `#DB2777` | Brand accent: secondary CTA, highlights, links |
| `color.accent-pressed` | `#BE185D` | `#EC4899` | Pressed / hover of accent |
| `color.accent-subtle` | `#FCE7F3` | `#3B1526` | Tinted accent background |
| `color.on-accent` | `#FFFFFF` | `#FFFFFF` | Text and icons on accent |

### Text

| Token | Light | Dark | Use |
| --- | --- | --- | --- |
| `color.text-primary` | `#111827` | `#F9FAFB` | Main text (ink) |
| `color.text-secondary` | `#6B7280` | `#9CA3AF` | Labels, help text |
| `color.text-tertiary` | `#9CA3AF` | `#6B7280` | Disabled, placeholder |
| `color.text-accent` | `#BE185D` | `#F472B6` | Accent-colored text and links |

### Surfaces

| Token | Light | Dark | Use |
| --- | --- | --- | --- |
| `color.background` | `#F9FAFB` | `#0B0F19` | Page background |
| `color.surface` | `#FFFFFF` | `#161B26` | Cards, sheets |
| `color.surface-subtle` | `#F3F4F6` | `#1F2937` | Secondary fills |
| `color.border` | `#E5E7EB` | `#2A3140` | Dividers, outlines |

### Semantic

| Token | Light | Dark | Use |
| --- | --- | --- | --- |
| `color.success` | `#16A34A` | `#22C55E` | Icons, fills (money in, done) |
| `color.success-text` | `#15803D` | `#4ADE80` | Success text on background |
| `color.success-subtle` | `#DCFCE7` | `#0C2A1A` | Success background |
| `color.error` | `#DC2626` | `#F87171` | Icons, fills, destructive |
| `color.error-text` | `#B91C1C` | `#FCA5A5` | Error text on background |
| `color.error-subtle` | `#FEE2E2` | `#2C1516` | Error background |
| `color.warning` | `#D97706` | `#FBBF24` | Caution |
| `color.warning-subtle` | `#FEF3C7` | `#2A2410` | Warning background |
| `color.info` | `#2563EB` | `#60A5FA` | Neutral information |
| `color.info-subtle` | `#DBEAFE` | `#12203A` | Info background |

## Usage rules

- One primary (graphite) action per screen. Fuchsia carries a secondary brand action,
  selected states, links, and small highlights. Do not fill large areas with fuchsia.
- In dark mode the primary action inverts to a light button with graphite text; the
  accent stays fuchsia.
- For money-in and success text on light backgrounds, use `success-text` (`#15803D`),
  not the brighter `success` fill, so it meets contrast.
- Destructive actions use `error`, never fuchsia.
- The fuchsia accent is for light surfaces. Do not use it as text on the dark toast (or any
  dark surface), where it reads poorly; use white (`on-primary`) there.

## Contrast (AA checks, key pairs)

- White on `primary` `#111827`: 16.1 : 1 (pass)
- White on `accent` `#DB2777`: 4.6 : 1 (pass)
- `text-secondary` `#6B7280` on `background` `#F9FAFB`: 4.7 : 1 (pass)
- `success-text` `#15803D` on white: 5.0 : 1 (pass)
- `error` `#DC2626` on white: 4.8 : 1 (pass)

## Machine-readable tokens

```json
{
  "color": {
    "primary":        { "light": "#111827", "dark": "#F9FAFB" },
    "primary-pressed":{ "light": "#000000", "dark": "#E5E7EB" },
    "on-primary":     { "light": "#FFFFFF", "dark": "#111827" },
    "accent":         { "light": "#DB2777", "dark": "#DB2777" },
    "accent-pressed": { "light": "#BE185D", "dark": "#EC4899" },
    "accent-subtle":  { "light": "#FCE7F3", "dark": "#3B1526" },
    "on-accent":      { "light": "#FFFFFF", "dark": "#FFFFFF" },
    "text-primary":   { "light": "#111827", "dark": "#F9FAFB" },
    "text-secondary": { "light": "#6B7280", "dark": "#9CA3AF" },
    "text-tertiary":  { "light": "#9CA3AF", "dark": "#6B7280" },
    "text-accent":    { "light": "#BE185D", "dark": "#F472B6" },
    "background":     { "light": "#F9FAFB", "dark": "#0B0F19" },
    "surface":        { "light": "#FFFFFF", "dark": "#161B26" },
    "surface-subtle": { "light": "#F3F4F6", "dark": "#1F2937" },
    "border":         { "light": "#E5E7EB", "dark": "#2A3140" },
    "success":        { "light": "#16A34A", "dark": "#22C55E" },
    "success-text":   { "light": "#15803D", "dark": "#4ADE80" },
    "success-subtle": { "light": "#DCFCE7", "dark": "#0C2A1A" },
    "error":          { "light": "#DC2626", "dark": "#F87171" },
    "error-text":     { "light": "#B91C1C", "dark": "#FCA5A5" },
    "error-subtle":   { "light": "#FEE2E2", "dark": "#2C1516" },
    "warning":        { "light": "#D97706", "dark": "#FBBF24" },
    "warning-subtle": { "light": "#FEF3C7", "dark": "#2A2410" },
    "info":           { "light": "#2563EB", "dark": "#60A5FA" },
    "info-subtle":    { "light": "#DBEAFE", "dark": "#12203A" }
  }
}
```
