# Transaction row

**Status: normative.**

One entry in a list of transactions. It answers, at a glance: who, how much, in or
out, and is it settled.

## Anatomy

1. **Leading icon:** a category icon (outline, in a neutral circle) or the merchant
   logo when available. 40px.
2. **Name:** the counterparty or merchant (`title`, 600), one line, truncated with an
   ellipsis.
3. **Meta:** category and time, or a status ("Groceries · 14:32", "Subscription").
   `body-sm`, `color.text-secondary`, one line.
4. **Amount:** trailing, right-aligned, tabular numbers, European format.

Rows are grouped under date headers: "Today", "Yesterday", then a full date
("5 May 2026").

## Amount and sign convention

- **Incoming:** a leading plus and `color.success-text` (green): `+150,00 €`.
- **Outgoing:** a leading minus sign (the real minus, not a hyphen) and
  `color.text-primary`: `−52,40 €`.
- The sign carries the meaning; color never carries it alone.

## States

| State | Treatment |
| --- | --- |
| Settled | As above |
| Pending | Amount in `color.text-secondary`; a "Pending" tag (`warning-subtle`) in the meta line |
| Failed / declined | Amount struck through in `color.text-tertiary`; a "Failed" tag (`error-subtle`) |
| Scheduled (optional) | Amount muted; a "Scheduled" tag with the due date |

## Content rules

- **Name:** the real counterparty or merchant. If it is unknown, show the raw
  description rather than inventing a name.
- **Meta:** one line, category and time or a status, never both crammed together.
- **Amounts:** European format (€ after the amount, dot thousands, comma decimals),
  tabular numbers. See `../../terminology/glossary.md`.
- Keep the name and meta each to a single line; the amount is never truncated.

## Interaction

- The whole row is tappable and opens the transaction detail.
- **Pressed:** background `color.surface-subtle` over `motion.duration.fast`.
- **Focus:** 2px fuchsia focus ring (`focus.ring`).
- Row height is at least 64px (comfortably above the 44px tap target).

## Accessibility

- The row is a single focusable control with one meaningful name that combines the
  parts, for example "Mercadona, 52,40 euros out, groceries, today at 14:32".
- In or out is conveyed by the sign and by words for screen readers ("received" /
  "sent"), never by color alone.
- The pending or failed status is announced, not shown by color alone.

## Machine-readable spec

```json
{
  "transaction-row": {
    "anatomy": ["leading-icon", "name", "meta", "amount"],
    "grouping": "by-date-header",
    "amount": {
      "incoming": { "sign": "+", "color": "color.success-text" },
      "outgoing": { "sign": "−", "color": "color.text-primary" },
      "format": "european",
      "numbers": "tabular"
    },
    "states": ["settled", "pending", "failed", "scheduled"],
    "interactive": { "pressed": "color.surface-subtle", "focus": "focus.ring", "min-height": 64 },
    "a11y": { "single-name": true, "sign-and-words": true }
  }
}
```
