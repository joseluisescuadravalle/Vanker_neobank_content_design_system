# Component library

**Status: normative.**

Individual UI components, each specified for content (using `../../patterns/` and
`../../terminology/`), visual style (using `../foundations/`), and states.

Each component file covers: purpose, anatomy, variants, states (default, pressed,
disabled, loading, error), content rules, and accessibility notes.

Components in this library:

- `button.md`
- `text-field.md` — the field label model (label in / label out / legend, placeholder, helper)
- `textarea.md` — composed free text, and the only place a character counter belongs
- `date-field.md` — a date they know is typed, a date they choose is picked
- `dropdown.md` — Select
- `checkbox.md`
- `radio-group.md`
- `card.md`
- `transaction-row.md`
- `status-label.md` — non-interactive state label with a controlled vocabulary
- `count-badge.md` — the number on an icon, and why a badge is a debt
- `chip.md` — the interactive twin of the status label: filter, choice, and input
- `amount-input.md` — the money field (hero and inline), presets, limits, and fees
- `code-input.md` — the single-use code field (Strong Customer Authentication, SCA)
- `tooltip.md` — the weakest surface in the product, and what may never live in it
- `accordion.md` — collapsible content, and the test for what may collapse
- `toggle.md` — the only control that applies immediately, and what that rules out
- `navigation.md`
- `sheet-modal.md`
- `banner-toast.md`
- `empty-state.md`
- `onboarding-step.md`

Form-level guidance (the three principles and the field-text hierarchy) lives in
`../../patterns/forms.md`.
