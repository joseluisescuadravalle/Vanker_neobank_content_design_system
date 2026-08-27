# Empty state

**Status: normative.**

What a screen or section shows when there is legitimately nothing yet: no transactions,
no spaces, no search results. It gives this component form to the pattern in
`../../patterns/empty-states.md`.

A failed load is **not** an empty state. If data could not load, show an error with a
retry (see `banner-toast.md` and `../../patterns/errors.md`), not "nothing here".

## Anatomy

1. **Icon** (required): a single **illustration** icon (larger, see
   `../foundations/iconography.md`), `color.accent` (fuchsia) stroke, standalone, no circle
   (it works as the illustration of the empty state).
2. **Title:** a short line naming what belongs here or what to do ("Set money aside").
3. **Description:** one or two plain lines: what will appear, and why it is worth it.
4. **Primary action** (only when there is a clear first step): a button following
   `button.md` and `../../patterns/ctas.md` ("Create space").

Centered, with generous vertical spacing (`space.8`).

## Variants

| Variant | Action | Tone |
| --- | --- | --- |
| First use (no data yet) | A primary CTA to create the first item | Encouraging |
| No results (search / filter) | None, or a "Clear filters" secondary | Neutral, not a failure |
| All caught up (nothing pending) | None | Positive, a good thing |

## Content rules

- Say what will appear here or what to do; never just "Nothing here" or "No data".
- Include a first step only when one genuinely exists. Do not add a CTA to a
  no-results or all-caught-up state.
- Never make the person feel behind or at fault.
- No emoji, no jokes (personality is marketing only).
- A no-results state suggests adjusting the search; it does not read as an error.

## Visual

- Icon at illustration size (about 56px), `color.accent` (fuchsia) stroke, no circle, for
  icons. A semantic state keeps its semantic color: an all-caught-up tick is
  `color.success` on `color.success-subtle`.
- Title `title` (18 / 700); description `body-sm`, `color.text-secondary`.
- Primary button as defined in `button.md`. One action at most.

## Accessibility

- The message is real text, never baked into an image; the icon is decorative
  (`aria-hidden`).
- When the empty state replaces a list, the region announces its state so a screen
  reader user knows the list is empty and why.
- The CTA is a real, focusable button with an accessible name.

## Machine-readable spec

```json
{
  "empty-state": {
    "anatomy": ["icon?", "title", "description", "primary-action?"],
    "variants": {
      "first-use": { "action": "primary-cta", "tone": "encouraging" },
      "no-results": { "action": "none-or-clear-filters", "tone": "neutral" },
      "all-caught-up": { "action": "none", "tone": "positive" }
    },
    "icon": { "size": 56, "role": "illustration", "color": "color.accent", "container": "none", "decorative": true, "semantic-exception": "success tick uses color.success" },
    "not-for": "failed-load (use an error with retry)",
    "content": { "forbid": ["emoji", "jokes", "blame", "bare-no-data"] }
  }
}
```
