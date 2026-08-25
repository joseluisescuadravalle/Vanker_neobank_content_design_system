# Motion

**Status: normative.**

**Decided:** "Calm and quick" motion. Fast, decisive, unobtrusive. Motion confirms that
something happened; it never decorates or entertains. A livelier, springy character is
allowed in marketing only.

## Duration

| Token | Value | Use |
| --- | --- | --- |
| `motion.duration.instant` | 0ms | No animation |
| `motion.duration.fast` | 120ms | Micro-interactions: button press, toggle, checkbox |
| `motion.duration.base` | 160ms | Default: fades, small moves, state changes |
| `motion.duration.moderate` | 240ms | Sheets, modals, page transitions |
| `motion.duration.slow` | 320ms | Large or emphasized moves (rare) |

## Easing

| Token | Value | Use |
| --- | --- | --- |
| `motion.easing.standard` | cubic-bezier(0.2, 0, 0, 1) | Entering and moving (decelerate) |
| `motion.easing.exit` | cubic-bezier(0.4, 0, 1, 1) | Leaving (accelerate out) |
| `motion.easing.inout` | cubic-bezier(0.4, 0, 0.2, 1) | Moving within the screen |

## Principles

- Motion has a job: confirm an action, show a relationship, or guide attention. If it
  does none of these, remove it.
- Move a short distance. Big travel reads slow and draws attention.
- Elements enter with `standard` easing and leave a little faster with `exit` easing.
- One meaningful thing moves at a time; avoid competing animations.

## Accessibility (required)

- Respect `prefers-reduced-motion`. When the user has asked their system for less
  motion, replace movement (translate, scale, spring) with an instant change or a
  simple opacity fade of 100ms or less. This is mandatory, not optional.
- Never convey information through motion alone.

## Marketing

Marketing may use a livelier, springy character (a longer duration with a slight
overshoot) for hero and campaign moments. The product stays calm and quick.

## Machine-readable tokens

```json
{
  "motion": {
    "duration": { "instant": 0, "fast": 120, "base": 160, "moderate": 240, "slow": 320 },
    "easing": {
      "standard": "cubic-bezier(0.2, 0, 0, 1)",
      "exit": "cubic-bezier(0.4, 0, 1, 1)",
      "inout": "cubic-bezier(0.4, 0, 0.2, 1)"
    },
    "reduced-motion": "replace movement with opacity fade <= 100ms"
  }
}
```
