# Empty states

**Status: normative (rules) + example (samples).**

What Vanker shows when there is legitimately nothing here yet: no transactions, no spaces,
no results. A low-stakes, warm moment (see `../voice-and-tone/tone.md`). This file is the
content structure; the component visuals live in `../components/library/empty-state.md`.

## Slots

- **Icon** (required): an illustration icon (large, fuchsia stroke, no circle), decorative
  and `aria-hidden`. It may later become a fuller illustration.
- **Title** (required): a short, plain, positive statement. **No ending period**, never a
  question, no blame, no humor, no emoji. It says what will appear here or what to do, never
  a bare "No data".
- **Body** (required): explains what will appear and why it is worth it, in plain language,
  one or two short sentences. Never generic.
- **CTA** (optional): **by default there is none.** The exception is a **first-use** empty
  state, which may carry a **single primary CTA** (a real first action, verb rules from
  `ctas.md`). No secondary. Never add a CTA to a no-results or all-caught-up state.

## The body and the CTA

- When there **is** a CTA (first use), the body **does not contain the call to action**; the
  action lives in the CTA.
- When there is **no** CTA (no-results, all-caught-up), the body may give brief guidance on
  what to do, since there is no button.

## Variants

| Variant | CTA | Tone |
| --- | --- | --- |
| First use (no data yet) | One primary CTA | Encouraging |
| No results (search / filter) | None | Neutral, not a failure |
| All caught up (nothing pending) | None | Positive |

## Tone and accessibility

- Warm and encouraging; never make the person feel behind or at fault.
- The message is real text, never baked into the image; the layout is centered.

## Examples (slot format)

- **First use:** Icon (savings) / Title "Set money aside" / Body "Spaces help you save for
  what matters, like a trip or a rainy day." / CTA "Create space".
- **No results:** Icon (search) / Title "No transactions match \u201cana\u201d" / Body "We could not find anything
  for that search. Check the spelling or try another word." / (no CTA).
- **All caught up:** Icon (check) / Title "You are all caught up" / Body "New updates from
  Vanker will appear here." / (no CTA).

## Machine-readable spec

```json
{
  "empty-state": {
    "slots": {
      "icon": { "required": true, "decorative": true, "alt": "" },
      "title": { "required": true, "ending-period": false, "is-an-error": false },
      "body": { "required": true, "says-what-will-appear": true },
      "cta": { "required": false, "only-on": "first use" }
    },
    "variants": ["first use", "no results", "all caught up"],
    "no-results-follows": "patterns/search.md",
    "shame": false
  }
}
```

## Eval hooks

- Title has no ending period and is not a question.
- Body is not generic and, in a first-use state, does not contain the CTA.
- A CTA appears only in a first-use state; never in no-results or all-caught-up.
- No emoji, no jokes.
