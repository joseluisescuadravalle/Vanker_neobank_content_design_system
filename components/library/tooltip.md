# Tooltip

**Status: normative.**

A small panel that explains one term or one control, opened on purpose by the person and
dismissed the same way.

A tooltip is **the weakest place in the product to put a piece of information**: it is
hidden by default, it needs a deliberate action to appear, it disappears again, and on a
phone it competes with the keyboard and the person's own thumb. That weakness is the whole
specification. Almost nothing qualifies.

## What may never live in a tooltip

Absolute, and it comes from `CLAUDE.md` (section 2) and `../../compliance/disclosures.md`:

- **Anything the person needs in order to complete the action.** If they cannot finish the
  field without it, it is helper text, and helper text is visible.
- **Any fee, cost, rate, limit, or condition that affects the decision.** A fee behind an
  info icon is a hidden fee, whatever the intention.
- **Any disclosure, risk warning, or legal statement** the regulation requires on that
  surface.
- **Any error, or the reason a control is disabled.**
- **Anything about the money in front of the person right now** (an amount, an arrival
  time, an exchange rate).

If the answer to "what happens if they never open it?" is anything other than "nothing",
it does not belong in a tooltip.

## The three tiers

| The information is… | It goes in | Visible? |
| --- | --- | --- |
| Needed to complete the field or the action | **Helper text** (`text-field.md`, `../../patterns/forms.md`) | Always |
| A clarification of one term, useful but optional | **Tooltip** | On request |
| Longer than two lines, or with structure, steps, or a link | **Sheet** (`sheet-modal.md`), opened by a "Learn more" link | On request |

The middle tier is narrow on purpose. **A tooltip that needs a link, a list, or a second
paragraph is a sheet that has not admitted it yet.**

## Anatomy

- **Trigger** (required): a real button carrying an outline info icon (`icon.sm`, 16px)
  next to the term it explains. Minimum 44px tap target. Never a bare icon glyph, never the
  term itself underlined, never the whole label.
- **Panel**: `color.surface` on `elevation.raised` (`shadow.md`), `radius.md`, 12px padding,
  maximum 280px wide, arrow pointing at the trigger.
- **Body**: one or two lines of `body-sm`.
- **Close**: tapping outside, pressing Escape, or tapping the trigger again. A close (×)
  inside the panel is optional and only for the widest panels.

There is no title, no icon inside the panel, no button, and no second tooltip.

## Content rules

1. **The trigger is a question, the tooltip is its answer.** The trigger's accessible name
   is the question the person would ask ("What is a BIC?"), and the panel answers exactly
   that, first sentence first.
2. **One or two sentences, up to about 160 characters.** Complete sentences, ending with a
   period.
3. **Define, do not sell.** A tooltip explains a term; it never promotes a feature, and it
   never contains a call to action (see `CLAUDE.md`).
4. **No links inside.** A link inside a tooltip is unreachable for many people on a phone,
   because the panel closes when they reach for it. If a link is needed, the whole thing is
   a sheet.
5. **No figures.** No amounts, no percentages, no currency: a number that affects a decision
   must be visible on the screen (see the prohibition above).
6. **Plain language, no jargon to explain the jargon.** "A BIC identifies a bank
   internationally, the way an IBAN identifies an account." Not "the ISO 9362 business
   identifier code".
7. **The term stays expanded in the copy anyway.** A tooltip never replaces the rule that
   acronyms are expanded on first use (`../../terminology/glossary.md`); it adds the
   explanation, it does not license the shorthand.

## Never

- **Never a tooltip on a disabled control.** A disabled element does not reliably receive
  taps or focus, so the explanation never opens. If something is disabled, the reason is
  written next to it, in the layout.
- **Never hover-only.** There is no hover on a phone. The trigger opens on tap and on
  keyboard activation; hover may open it on a pointer device, but nothing may depend on it.
- **Never automatic.** A tooltip does not appear on load, on scroll, or on focus, and it
  does not follow the person around the screen.
- **Never as onboarding.** A tour made of tooltips that fire one after another is not this
  component (see `../../patterns/flow-intro.md`).
- **Never carrying an error.** Errors are inline and permanent while they apply (see
  `../../patterns/errors.md`).

## Behavior and motion

- Opens on tap, click, or keyboard activation of the trigger; closes on Escape, on tapping
  outside, or on re-activating the trigger.
- **Stays open while the pointer is on it**, so it can be read and its text selected, and it
  is dismissible without moving the pointer (WCAG 1.4.13).
- Only one tooltip is open at a time.
- On a small screen the panel repositions to stay fully visible; it never gets clipped and
  never covers the field the person is using.
- Fades in over `motion.duration.fast` with no movement or bounce; under
  `prefers-reduced-motion` it appears with no transition.

## Accessibility

- The trigger is a `button` with an accessible name that is the question, not "info" or "?".
- The panel is linked with `aria-describedby`, so its text is read as part of the field it
  describes.
- Escape closes it and returns focus to the trigger.
- Text meets WCAG AA contrast on the panel surface; the arrow is decorative.
- The content of a tooltip is **never** the only way to reach a piece of information: it
  restates or clarifies something the screen already works without.

## Content examples

- ✅ Trigger "What is a BIC?" · Panel "A BIC identifies a bank internationally, the way an
  IBAN identifies an account. Most euro transfers do not need one."
- ✅ Trigger "What is a virtual card?" · Panel "A card that only exists in the app. You can
  use it online and delete it whenever you want."
- ❌ "There is a 2 € fee for this transfer." (a fee must be visible)
- ❌ "Tap here to add money to your space." (a call to action)
- ❌ "Read the full terms" with a link (that is a sheet)
- ❌ A tooltip on a greyed-out button explaining why it is greyed out.

## Machine-readable spec

```json
{
  "tooltip": {
    "weakest-surface": true,
    "forbidden-content": ["needed-to-complete", "fee", "cost", "rate", "limit", "condition", "disclosure", "risk-warning", "error", "disabled-reason", "amount", "arrival-time", "exchange-rate"],
    "tiers": {
      "needed": "helper-text",
      "optional-clarification": "tooltip",
      "longer-or-structured-or-linked": "sheet"
    },
    "trigger": { "element": "button", "icon": "icon.sm", "min-target": 44, "accessible-name": "question", "hover-only": false },
    "panel": { "surface": "color.surface", "elevation": "raised", "radius": "radius.md", "max-width": 280, "padding": 12, "type": "body-sm" },
    "content": { "sentences": [1, 2], "max-chars": 160, "ends-with-period": true, "cta": false, "links": false, "figures": false, "emoji": false },
    "behavior": { "opens-on": ["tap", "click", "keyboard"], "closes-on": ["escape", "outside-tap", "re-activate"], "automatic": false, "one-at-a-time": true, "hoverable": true, "dismissible": true },
    "never": ["on-disabled-control", "hover-only", "as-onboarding-tour", "carrying-an-error", "nested"],
    "motion": { "in": "motion.duration.fast", "movement": false, "reduced-motion": "none" },
    "a11y": { "trigger-role": "button", "describedby": true, "escape-returns-focus": true, "sole-source-of-information": false }
  }
}
```

## Eval hooks

- The tooltip contains no fee, rate, limit, condition, amount, percentage, or currency.
- It is one or two complete sentences, about 160 characters at most, ending with a period.
- It contains no call to action and no link.
- The trigger's accessible name is the question the panel answers, never "info" or "?".
- Nothing needed to complete the action is inside it.
- It is not attached to a disabled control, does not open automatically, and does not
  depend on hover.
