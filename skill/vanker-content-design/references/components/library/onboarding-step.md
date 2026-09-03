# Onboarding step

**Status: normative.**

One step in a guided flow (account setup, identity checks, first-time setup). It shows
where the person is, explains what this step needs and why, and offers one clear action.
The tone is patient and plain (see `../../voice-and-tone/tone.md`, "Onboarding").

## Anatomy

1. **Progress:** a segmented bar with completed segments in `color.accent` (fuchsia),
   plus a text label ("Step 2 of 4"). Always visible.
2. **Back:** a labeled control from the second step onward; it returns without losing
   entered data.
3. **Icon** (optional, only when it genuinely helps): a plain outline icon in
   `color.accent` (fuchsia) stroke, standalone, no circle. Used as a small leading icon beside the title it saves space, or as a focal illustration at the larger illustration size (see `../foundations/iconography.md`). Skip it
   when it would be decorative filler.
4. **Title:** what the step asks, in plain words ("Confirm your identity").
5. **Description:** why it matters and roughly how long it takes.
6. **Step content:** the field, options, or affordance for this step, as needed.
7. **Primary action:** one verb ("Continue", "Get started"). An optional secondary
   ("Do this later"), low emphasis, only when the step is genuinely optional.

## Content rules

- **Explain the why** in plain language. Never a bare "Complete KYC"; say "Confirm your
  identity" and why it is needed.
- **Expand acronyms** on first use: KYC (Know Your Customer) becomes "confirm your
  identity" in customer copy.
- **Give a time estimate** when the step takes effort ("It takes about two minutes").
- Assume no prior knowledge; never talk down.
- One primary action per step. A skip or defer appears only for truly optional steps, at
  low emphasis.
- Give the title and description generous separation; the screen must feel simple and airy, not crowded. The title-to-body gap is deliberately large (about 80px on a step and about 112px on the welcome screen, roughly double the usual section gap). Keep sentences short and separate the
  reason (the "why") from the practical detail, rather than stacking several sentences in
  one dense paragraph.

## Progress

- An intro or welcome screen, where the person only has to start, is not counted as a
  step and shows no counter. The count begins at the first real step ("Step 1 of 3"). The intro headline may color the brand name in fuchsia ("Welcome to Vanker") as a light brand moment, with the body well separated below.
- Always show how far along the person is; never hide the length of the flow.
- The progress indicator is small and discreet at the top (a thin bar and a quiet "Step X
  of Y"); it orients without dominating the screen.
- The bar is not the only signal: the "Step X of Y" text carries it too, so it does not
  depend on color.

## Accessibility

- The step's progress is announced ("Step 2 of 4"), not shown by color alone.
- On moving to a new step, focus moves to that step's title so screen-reader and keyboard
  users land in the right place.
- Back returns to the previous step with entered data intact.
- Respect `prefers-reduced-motion` on step transitions.

## Machine-readable spec

```json
{
  "onboarding-step": {
    "anatomy": ["progress", "back?", "icon?", "title", "description", "content?", "primary-action", "secondary-action?"],
    "progress": { "style": "segmented", "active-color": "color.accent", "text-label": "Step X of Y", "always-visible": true, "intro-not-counted": true },
    "content": { "explain-why": true, "expand-acronyms": true, "time-estimate": "when effortful", "tone": "patient" },
    "actions": { "primary": "single verb", "secondary": "defer, low-emphasis, optional-steps-only" },
    "a11y": { "progress-announced": true, "focus-to-title-on-step-change": true, "back-preserves-data": true }
  }
}
```

## Eval hooks

- The step explains why it is being asked, in plain language, never a bare acronym.
- Acronyms are expanded on first use ("confirm your identity" rather than "KYC").
- A time estimate appears only when it is measured, and as a range.
- The progress indicator does not count the intro screen (`../../patterns/flow-intro.md`).
- The step never asks for something it does not need yet.
