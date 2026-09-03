# Checkbox

**Status: normative.**

Lets a person mark one or more options, or give consent or agreement. Form-level rules are
in `../../patterns/forms.md`; consent and legal wording follow `../../compliance/`.

## Slots

- **Label** (required): the option or the statement being agreed to, beside the box. A
  concise phrase, but **keep the articles and determiners** — do not clip it to a robotic
  fragment. The person may speak in the **first person** ("I agree to the processing of my
  personal data"). No emoji; a checkbox label is a statement, not a question.
- **Group legend** (optional): when several checkboxes belong together, a legend heads the
  group (see `../../patterns/forms.md`).
- **Helper / link** (optional): a short clarification or a link to the full terms, below
  or within the label ("Read the privacy policy"). Legal detail lives behind the link, not
  in the label.

## Rules

- **No dark patterns.** A consent box is **never pre-ticked**, and the label is never a
  double negative or worded so that leaving it unchecked hides a real choice ("Do not opt
  me out of…"). The person must be able to tell, at a glance, what ticking the box does.
- **Plain language over legalese.** When the box carries legal or regulatory wording, adapt
  it to plain, conversational language **without changing its meaning**; do not invent
  compliant wording (see `CLAUDE.md`, the safety rule).
- **One idea per box.** Do not bundle unrelated consents into a single checkbox (for
  example account terms and marketing) — that is not free, specific consent.
- Concise, but complete: keep the words that make it unambiguous.

## Content examples (slot format)

- ✅ "I agree to the processing of my personal data"
- ✅ "I want to subscribe to the newsletter to receive exclusive offers" (optional, unticked)
- ❌ "I do not want to not receive offers" (double negative / dark pattern)
- ❌ "Terms" (too clipped; name what is being agreed to)

## States

| State | Treatment |
| --- | --- |
| Unchecked | Empty box, `color.border`; default and never pre-ticked for consent |
| Checked | `color.accent` (fuchsia) fill with a check mark |
| Focus | Fuchsia focus ring |
| Error | If a required consent is unchecked, a field validation error below (see `../../patterns/errors.md`) |
| Disabled | `color.surface-subtle`, not operable |

## Accessibility

- The label is programmatically tied to the box (`for` / `id`); tapping the label toggles it.
- State is announced (checked / unchecked), not conveyed by color alone.
- Minimum 44px tap target around the box and label.
- A required-consent error is linked to the group with `aria-describedby`.

## Machine-readable spec

```json
{
  "checkbox": {
    "label": { "required": true, "keep-articles": true, "first-person": "allowed", "question": false, "emoji": false },
    "consent": { "pre-ticked": false, "no-dark-pattern": true, "one-idea-per-box": true, "plain-language": true },
    "states": ["unchecked", "checked", "focus", "error", "disabled"],
    "checked-color": "color.accent",
    "error": "field-validation (see patterns/errors.md)",
    "a11y": { "label-for-id": true, "state-announced": true, "min-target": 44 }
  }
}
```

## Eval hooks

- A checkbox label is a statement, not a question, and carries no emoji.
- Consent boxes are never pre-ticked and never worded as a double negative.
- The label keeps its articles; it is concise but not clipped to a fragment.
- Legal wording is plain-language; unresolved compliance wording is flagged, not invented.
