# Elevation and depth

**Status: normative.**

**Decided:** a **flat** system. Surfaces are separated by borders and surface color, not
by heavy shadows. Shadows are reserved for elements that genuinely float above the
content (menus, sheets, modals, floating actions). This keeps the interface light and
simple.

## Shadow scale (light)

| Token | Value | Use |
| --- | --- | --- |
| `shadow.none` | none | Resting surfaces |
| `shadow.sm` | 0 1px 2px rgba(17,24,39,.04) | Barely-raised, optional |
| `shadow.md` | 0 4px 12px rgba(17,24,39,.08) | Dropdowns, popovers, tooltips |
| `shadow.lg` | 0 8px 24px rgba(17,24,39,.10) | Sheets, modals, menus |
| `shadow.xl` | 0 12px 32px rgba(17,24,39,.12) | Large floating surfaces (rare) |

## Elevation roles

| Role | Treatment (light) | Use |
| --- | --- | --- |
| `base` | Background, no border, no shadow | Page background |
| `card` | Surface + 1px `color.border`, `shadow.none` | Resting cards, list containers |
| `raised` | Surface + `shadow.md`, no border | Dropdowns, popovers, tooltips |
| `overlay` | Surface + `shadow.lg` | Bottom sheets, modals, menus |
| `floating` | Surface or accent + `shadow.md` | Floating action button, toasts |

## Dark mode

Shadows are almost invisible on dark backgrounds, so depth comes from **lighter
surfaces**: the higher the elevation, the lighter the surface. A faint shadow is added
only to overlays.

| Role | Dark surface |
| --- | --- |
| `base` | `#0B0F19` (page background) |
| `card` | `#161B26` + 1px `#2A3140` border |
| `raised` | `#1F2937` |
| `overlay` | `#232C3D` + soft shadow `0 8px 24px rgba(0,0,0,.4)` |

## Usage rules

- Resting cards never use a shadow; they use a hairline border.
- Only one floating element competes for attention at a time.
- Do not stack shadows to fake more depth; move up one role instead.
- Keep elevation meaningful: a higher shadow means the element floats higher and is
  more temporary (a menu over a card, a modal over the page).

## Machine-readable tokens

```json
{
  "shadow": {
    "none": "none",
    "sm": "0 1px 2px rgba(17,24,39,0.04)",
    "md": "0 4px 12px rgba(17,24,39,0.08)",
    "lg": "0 8px 24px rgba(17,24,39,0.10)",
    "xl": "0 12px 32px rgba(17,24,39,0.12)"
  },
  "elevation": {
    "base":     { "border": false, "shadow": "none" },
    "card":     { "border": true,  "shadow": "none" },
    "raised":   { "border": false, "shadow": "md" },
    "overlay":  { "border": false, "shadow": "lg" },
    "floating": { "border": false, "shadow": "md" }
  },
  "surface-dark": {
    "base": "#0B0F19", "card": "#161B26", "raised": "#1F2937", "overlay": "#232C3D"
  }
}
```
