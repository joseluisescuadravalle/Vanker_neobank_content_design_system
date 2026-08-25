# Components

**Status: normative.**

This layer is Vanker's design system: the visual and content specifications for the
interface. It has two parts.

- `foundations/` — the design decisions that cascade into everything (color,
  typography, shape, spacing, elevation, motion). Captured as **design tokens**, so a
  person, an AI agent, and code can all apply them exactly.
- `library/` — the individual components (buttons, fields, cards, rows, navigation,
  sheets, banners), each specified for content, visual style, and states, building on
  the foundations and the `../patterns/` layer.

## Roadmap

Foundations, decided in order:
1. Color
2. Typography
3. Shape and corner radius
4. Spacing and layout
5. Elevation and depth
6. Iconography and imagery
7. Motion

Library, built on the foundations: buttons, text fields and forms, cards (account and
Space), lists and rows (transaction row), navigation (tab bar), sheets and modals,
banners and toasts, empty state, onboarding step.

We build one subsection at a time, decide together, and record each decision here.
