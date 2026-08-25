# Typography

**Status: normative.**

**Decided:** the product interface uses **Plus Jakarta Sans** (calm, legible, warm, for
all ages). **Space Grotesk** is reserved for **marketing and brand display** only. This
mirrors the brand rule that extra personality lives in marketing, not in the product.

## Families

| Token | Value | Use |
| --- | --- | --- |
| `font.family.text` | Plus Jakarta Sans, then system sans fallback | All product UI and body text |
| `font.family.display` | Space Grotesk, then Plus Jakarta Sans fallback | Marketing and brand display only |

Full fallback stack for `text`: `"Plus Jakarta Sans", -apple-system, BlinkMacSystemFont,
"Segoe UI", Roboto, Helvetica, Arial, sans-serif`.

## Weights

| Token | Value |
| --- | --- |
| `font.weight.regular` | 400 |
| `font.weight.medium` | 500 |
| `font.weight.semibold` | 600 |
| `font.weight.bold` | 700 |
| `font.weight.extrabold` | 800 |

## Scale

Sizes in px (mobile-first), with line-height and default weight. Body text is 16 px to
stay comfortable for all ages.

| Role | Size / Line | Weight | Tracking | Use |
| --- | --- | --- | --- | --- |
| `display-lg` | 44 / 48 | 800 | -0.02em | Hero figure (big account balance) |
| `display` | 34 / 40 | 700 | -0.02em | Large headings, onboarding hero |
| `heading-lg` | 28 / 34 | 700 | -0.01em | Screen title (h1) |
| `heading` | 22 / 28 | 700 | normal | Section title (h2) |
| `title` | 18 / 24 | 600 | normal | Card title, list header (h3) |
| `body-lg` | 18 / 28 | 400 | normal | Emphasized body |
| `body` | 16 / 24 | 400 | normal | Default body text |
| `body-sm` | 14 / 20 | 400 | normal | Secondary text, help |
| `caption` | 12 / 16 | 500 | normal | Captions, metadata |
| `overline` | 12 / 16 | 600 | +0.06em | Uppercase labels (use sparingly) |
| `button` | 16 / 20 | 600 | normal | Button and CTA labels |

## Usage rules

- Headings and the hero balance carry the weight; body stays 400 for easy reading.
- **Money and aligned figures use tabular numbers** (`font-feature-settings: "tnum" 1`)
  so digits line up in lists and tables.
- In **marketing**, headings (`display`, `heading-lg`, `heading`) switch to
  `font.family.display` (Space Grotesk). Body stays Plus Jakarta Sans everywhere.
- Do not use Space Grotesk anywhere in the product UI.
- One `display-lg` or `display` per screen at most; more than one competes.

## Accessibility

- Base body is 16 px; never set meaningful text below 12 px.
- Body line-height is 1.5 for comfortable reading.
- Respect the user's system font-scaling (Dynamic Type). Do not cap or disable it; let
  layouts grow.
- Personality never comes at the cost of legibility (see the marketing/product split).

## Machine-readable tokens

```json
{
  "font": {
    "family": {
      "text": "\"Plus Jakarta Sans\", -apple-system, BlinkMacSystemFont, \"Segoe UI\", Roboto, Helvetica, Arial, sans-serif",
      "display": "\"Space Grotesk\", \"Plus Jakarta Sans\", sans-serif"
    },
    "weight": { "regular": 400, "medium": 500, "semibold": 600, "bold": 700, "extrabold": 800 },
    "scale": {
      "display-lg": { "size": 44, "line": 48, "weight": 800, "tracking": "-0.02em" },
      "display":    { "size": 34, "line": 40, "weight": 700, "tracking": "-0.02em" },
      "heading-lg": { "size": 28, "line": 34, "weight": 700, "tracking": "-0.01em" },
      "heading":    { "size": 22, "line": 28, "weight": 700, "tracking": "normal" },
      "title":      { "size": 18, "line": 24, "weight": 600, "tracking": "normal" },
      "body-lg":    { "size": 18, "line": 28, "weight": 400, "tracking": "normal" },
      "body":       { "size": 16, "line": 24, "weight": 400, "tracking": "normal" },
      "body-sm":    { "size": 14, "line": 20, "weight": 400, "tracking": "normal" },
      "caption":    { "size": 12, "line": 16, "weight": 500, "tracking": "normal" },
      "overline":   { "size": 12, "line": 16, "weight": 600, "tracking": "+0.06em" },
      "button":     { "size": 16, "line": 20, "weight": 600, "tracking": "normal" }
    },
    "numbers": { "tabular": true }
  }
}
```
