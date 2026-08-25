# Spacing and layout

**Status: normative.**

**Decided:** an 8-point grid, built on a 4px base unit. Every margin, padding, and gap
is a token from the scale below, never an arbitrary value. This keeps rhythm consistent
and makes layouts predictable for a person, an agent, and code.

## Spacing scale

| Token | Value | Typical use |
| --- | --- | --- |
| `space.0` | 0 | Reset |
| `space.1` | 4px | Tight gaps (icon to label) |
| `space.2` | 8px | Between related items |
| `space.3` | 12px | Inside compact components |
| `space.4` | 16px | Default padding, screen edges |
| `space.5` | 20px | Card padding |
| `space.6` | 24px | Between groups |
| `space.8` | 32px | Between sections |
| `space.10` | 40px | Large section breaks |
| `space.12` | 48px | Screen-level spacing |
| `space.16` | 64px | Hero and empty-state spacing |

Rule: use multiples of 8 for layout (16, 24, 32); the 4px steps (4, 12, 20) are for
fine-tuning inside components.

## Layout

| Token | Value | Use |
| --- | --- | --- |
| `layout.screen-padding` | 16px (mobile), 24px (>= 768px) | Space from the screen edge |
| `layout.gutter` | 16px | Gap between columns and cards |
| `layout.content-max` | 480px | Max width of app content; it stays centered on wider screens |
| `layout.section-gap` | 32px | Vertical gap between major sections |

### Breakpoints

| Token | Value |
| --- | --- |
| `breakpoint.sm` | 480px |
| `breakpoint.md` | 768px |
| `breakpoint.lg` | 1024px |
| `breakpoint.xl` | 1280px |

The product is mobile-first: design for the smallest screen, then let content grow to
`layout.content-max` and add breathing room. Marketing web pages may use a wider max
width.

## Touch targets (accessibility)

| Token | Value | Note |
| --- | --- | --- |
| `target.min` | 44px | Absolute minimum tappable size (WCAG 2.2, Apple HIG) |
| `target.comfortable` | 48px | Default for primary controls (Android-safe) |
| `target.spacing-min` | 8px | Minimum gap between two tappable targets |

- Primary buttons and list rows are at least 48px tall.
- A small icon may look 24px, but its tappable area is still at least 44px.
- Never place two targets closer than 8px.

## Component spacing conventions

| Element | Spacing |
| --- | --- |
| Button | 14px vertical / 20px horizontal padding (height >= 48px) |
| Input field | 12px vertical / 14px horizontal padding (height >= 48px) |
| Card | `space.5` (20px) padding |
| List row | min height 56px, `space.4` (16px) horizontal padding |
| Screen edges | `layout.screen-padding` |
| Between form fields | `space.4` (16px) |
| Between sections | `space.8` (32px) |

## Accessibility

- Keep the minimum touch targets and target spacing even when text scales up.
- Do not compress spacing to fit more on screen; let the layout scroll instead.

## Machine-readable tokens

```json
{
  "space": { "0": 0, "1": 4, "2": 8, "3": 12, "4": 16, "5": 20, "6": 24, "8": 32, "10": 40, "12": 48, "16": 64 },
  "layout": { "screen-padding": { "base": 16, "md": 24 }, "gutter": 16, "content-max": 480, "section-gap": 32 },
  "breakpoint": { "sm": 480, "md": 768, "lg": 1024, "xl": 1280 },
  "target": { "min": 44, "comfortable": 48, "spacing-min": 8 }
}
```
