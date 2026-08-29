# Patterns

**Status: normative (patterns) + example (samples).**

Reusable UX copy patterns that recur across surfaces: calls to action, error
messages, empty states, confirmations, and notifications. Each pattern states the
rule and shows labeled examples.

Contents:
- `ctas.md`, `errors.md`, `system-errors.md`, `loading.md`, `welcome-carousel.md`,
  `flow-intro.md`, `permissions.md`, `auth.md`, `empty-states.md`, `confirmations.md`,
  `notifications.md`, `success.md`, `forms.md`.

`errors.md` holds the anatomy of an error and the rules for field validation and modal
errors. `system-errors.md` covers the situations where the problem is ours or the
network's: offline, our systems failing, maintenance, an expired session, content that no
longer exists, and a required update. `loading.md` covers the waiting itself: which
indicator to show, what to say while it runs, and what to say when it runs long.

Two patterns are often lumped together as "onboarding" and must not be:
`welcome-carousel.md` is the pre-login argument (marketing voice, highest regulatory
exposure), and `flow-intro.md` is the single screen that opens a multi-step process
inside the product (product voice). The steps themselves are
`../components/library/onboarding-step.md`.
