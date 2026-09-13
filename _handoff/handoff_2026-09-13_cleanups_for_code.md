# Handoff for Claude Code: four cleanups

Date: 13 September 2026 (night). None of these is part of the behavioral layer; they are
the loose ends that surfaced while building it. System side is committed.

## 1. Four new surfaces (system: done; app: port)

`rules.json` now carries 71 checks and 78 surfaces. New:

| Surface | Checks | Owner | Gallery |
| --- | --- | --- | --- |
| `success-title` | `A-SUCCESS-TITLE` (no ending punctuation, not a question, no fireworks vocabulary, about 8 words) plus no emoji, money, banned, claims, spelled negation, case, mask | `patterns/success.md` | A full-screen success: mark, title, optional body, 2 to 4 continue options |
| `success-body` | body checks | `patterns/success.md` | same screen |
| `success-option` | CTA checks | `patterns/success.md`, `patterns/ctas.md` | same screen, each option |
| `notification-title` | `A-NOTIFICATION-TITLE` (no emoji, no ending punctuation, about 40 chars) plus no emoji, money, banned, claims, mask, case | `patterns/notifications.md` (new section "The in-app notification") | An in-app notification list item: title + body (`notification`) |

Two checks to port, both read from `rules.json`: `lists.celebration_terms` for
`A-SUCCESS-TITLE`; the length and punctuation rules are in `assertions.md`. Acceptance is
in the golden set: `success.*` and `notification.inapp-*`.

Gallery examples: success "Your account is ready" / options "View my accounts",
"Send money", "Close"; in-app notification "Money in" / "You received 150 € from Ana."
(no-break space before €).

## 2. "structure" becomes "pattern fit"

The editorial review dimensions in the app list "structure" where
`evals/rubric.md` says **Pattern fit** ("Follows the pattern (anatomy, rules) for the
surface"). Rename it everywhere it shows (meter label, verdict reasons, tests). The rubric
is the source; the app does not keep its own dimension names.

## 3. The 62 older checks read their lists from `rules.json`

The 7 dark-pattern checks already do. Move the remaining word lists and patterns
(`banned_terms`, `prohibited_claims`, `not_inclusive`, `must_expand`, `generic_*`,
`title_case_ok`, `proper_nouns`, `ampersand_ok_surfaces`, and the `patterns` block) out of
the TypeScript and into reads of the virtual module, so `parity.test.ts` has nothing left
to compare and can become a test that the module loads. Keep the check logic in
TypeScript; only the data moves.

## 4. Home card 02

"as live tokens" becomes "as live variables" (`A-NO-BANNED` rejects "token"; "variables"
is Figma's word for the same thing).

## Acceptance

| Case | Expected |
| --- | --- |
| Gallery | Two new surfaces: Success (full screen) and In-app notification |
| success-title "Congratulations, you did it!" | FAIL A-SUCCESS-TITLE |
| notification-title "Smarter savings ✨" | FAIL A-NOTIFICATION-TITLE (the push exception stops at the tray) |
| Editorial review meters | "Pattern fit", no "structure" anywhere |
| `parity.test.ts` | No list compared by hand; the module loads and the 71 checks resolve |
| Home card 02 | "as live variables" |
