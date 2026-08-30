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

## Setting text: alignment

Alignment is decided by the **number of lines and the job of the block**, never by taste.

| Block | Alignment |
| --- | --- |
| One or two lines, in a symmetric composition (success screen, empty state, full-screen moment, a short modal title) | **Centered allowed** |
| **Three lines or more** | **Left. No exception** |
| Anything inside a reading flow: forms, lists, details, transaction rows, emails | **Left** |
| Figures in a column (amounts, dates) | **Right**, with tabular numbers |
| Anything | **Never justified** |

**Why the line count decides it.** At every line break the eye jumps back to the start of
the next line. Left-aligned, that point is always at the same horizontal position and the
eye lands without searching. Centered, the start of each line shifts with the length of the
one above, so the eye has to find it before it can read it. On one or two lines that cost is
invisible; from the third it is real and it accumulates. Justified text adds uneven word
spacing on top, which is why WCAG 2.1 (1.4.8) rules it out and why dyslexia style guidance
asks for a ragged right edge.

## Setting text: blocks

**One fact, one paragraph.**

A body that stacks three separate facts into one block forces the person to read all of it
to find the one that matters to them. Splitting it costs nothing and changes how heavy it
looks:

> **Report this card?**
>
> Your money is safe.
>
> This card will stop working for good, and we'll send you a new one.
>
> The replacement is free and usually arrives in 3 to 5 working days.

Same words, three paragraphs, half the weight.

- **One sentence per paragraph.** Two are allowed only when they are tightly linked and both
  short; if the pair runs long, it is two paragraphs.
- **At most three paragraphs in the body of a modal or a sheet.** If it needs four, it is a
  screen, not a modal (see `../library/sheet-modal.md`).
- **Not bullets.** In a modal, a bulleted list reads as terms and conditions, and it chills
  exactly the moment that needs warmth. Bullets belong to reference content, not to a
  message.
- The separation is vertical space (`space.2`), not a blank line of text and not a rule.

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
    "numbers": { "tabular": true },
    "alignment": {
      "centered-allowed-up-to-lines": 2,
      "left-from-lines": 3,
      "reading-flow": "left",
      "figures-in-a-column": "right",
      "justified": false
    },
    "blocks": {
      "sentences-per-paragraph": 1,
      "two-allowed-when": "tightly linked and both short",
      "max-paragraphs-in-a-modal-body": 3,
      "bullets-in-a-modal": false,
      "separator": "space.2"
    }
  }
}
```
