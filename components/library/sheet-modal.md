# Sheet and modal

**Status: normative.**

Two ways to present focused content over the current screen. Both dim the screen behind
with a scrim and use the `overlay` elevation role.

## When to use which

- **Bottom sheet (default):** contextual actions, confirmations, short forms, option
  lists. It rises from the bottom, within thumb reach. Use it for most mobile flows.
- **Modal dialog:** a focused decision that must be answered before continuing,
  especially destructive or high-consequence ones. It interrupts on purpose.

## Bottom sheet

- **Anatomy:** a grab handle, an optional short title, the content, and the actions
  (primary, then a secondary "Cancel").
- **Shape:** rounded top corners at `radius.2xl` (28px); it meets the bottom edge.
- **Motion:** slides up over `motion.duration.moderate` (240ms) with
  `motion.easing.standard`; leaves with `motion.easing.exit`.
- **Dismiss:** swipe down, tap the scrim, or Cancel.
- **Confirmation content:** summarize the action as rows before confirming (To, Amount,
  Arrives, Fee), then a primary button consistent with the sheet title ("Confirm payment"). See
  `../../patterns/confirmations.md`.

## Modal dialog

- **Anatomy:** a title (a question for decisions), a short body, and an actions row
  (secondary "Cancel", then the primary or destructive action).
- **Shape:** centered card at `radius.xl` (20px), `overlay` shadow.
- **Motion:** fades and scales in from 0.96 over `motion.duration.base`.
- **Destructive content:** name the consequence and whether it can be undone ("Deleting
  Travel will move its 600 € back to your current account. This cannot be undone").

## Dismissal and safety

- A standard sheet or modal dismisses via scrim tap, swipe (sheet), or Cancel.
- A **destructive or critical modal does not dismiss on scrim tap, swipe, or back**. It
  requires an explicit choice, so a stray tap never destroys anything.
- Only one sheet or modal is open at a time.

## Content rules

- Titles are short; decision modals use a question ("Delete this space?").
- The primary button matches the words of the sheet or modal title that names the action ("Confirm payment", "Delete space"); never a bare
  "OK" or "Confirm". See `../../patterns/ctas.md`.
- One primary action. The safe way out ("Cancel") is always present.

## Accessibility

- On open, focus moves into the sheet or modal and is trapped inside; on close, it
  returns to the control that opened it.
- `role="dialog"`, `aria-modal`, labeled by the title; the background is inert.
- Esc closes where a safe Cancel exists; a destructive modal maps Esc and back to Cancel,
  never to the destructive action.
- Respect `prefers-reduced-motion`: replace the slide or scale with a simple fade.
- If the content is tall, it scrolls while the actions stay reachable.

## Machine-readable spec

```json
{
  "sheet-modal": {
    "sheet": {
      "radius": "radius.2xl",
      "motion": { "enter": "motion.duration.moderate", "easing": "motion.easing.standard" },
      "dismiss": ["swipe-down", "scrim", "cancel"]
    },
    "modal": {
      "radius": "radius.xl",
      "elevation": "overlay",
      "motion": { "enter": "motion.duration.base", "effect": "fade-scale-0.96" },
      "dismiss": ["scrim", "cancel"]
    },
    "destructive": { "dismiss-on-scrim": false, "requires-explicit-choice": true },
    "content": { "primary": "matches-title-action", "cancel": "always-present" },
    "a11y": { "role": "dialog", "aria-modal": true, "focus-trap": true, "return-focus": true, "esc": "cancel" }
  }
}
```
