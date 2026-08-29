# Accordion

**Status: normative.**

A list of headers that expand to show their content. Used for help content, for the detail
behind something already summarized, and for long reference text nobody reads end to end.

An accordion hides content behind a tap, so it shares the tooltip's problem (see
`tooltip.md`) with one important difference: **the header stays visible in the page**. It
is in the reading order, it can be found, focused, linked to, and read out. That is why an
accordion may carry things a tooltip never can — a long explanation, a link, a button — and
why it still may not carry the thing the person needs in order to decide.

## When it is right, and when it is hiding

| Content | Accordion? |
| --- | --- |
| A question most people do not have | **Yes** |
| The detail behind a total that is already visible (how a fee is made up) | **Yes** |
| Long reference or legal text, secondary to the decision | **Yes** |
| A fee, rate, limit, or condition that decides the action | **No.** It is visible, on the screen |
| A required disclosure or risk warning for that surface | **No.** See `../../compliance/disclosures.md` |
| Something most people need | **No.** If most people open it, it was never optional |
| An error, or the reason a control is disabled | **No.** See `../../patterns/errors.md` |
| A step of a flow | **No.** That is a flow (`../../patterns/flow-intro.md`) |

The test is the same one the tooltip uses, one notch softer: **if the person never opens
it, can they still decide correctly?** If not, it is not collapsible.

The reconciliation that makes this workable in a bank: **the total is visible, the
breakdown may collapse.** "You pay 3 € to send this transfer" stays on the screen; "How
this is calculated" can be an accordion.

## Headers

The header is the whole component. If it does not predict what is inside, people either
never open it or open all of them, and both are failures.

- **It names its content exactly**, in the words the person would use. For help content it
  is their question ("Why do I need to confirm my identity?"); elsewhere it is a noun
  phrase ("How the fee is calculated").
- **Up to about eight words.** One line on a phone.
- **Parallel within a group**: all questions, or all noun phrases. Never mixed.
- **Never generic.** "More information", "Details", "Other", "Read more", "Learn more" and
  "Info" are not headers: they describe the act of opening, not the content.
- Sentence case. A question takes a question mark; a noun phrase takes no ending
  punctuation.
- **No count, no badge, no promise.** Not "3 things you should know".

## Behavior

- **Several panels can be open at once**, and opening one never closes another. Closing
  content the person did not ask to close moves the page under their finger and loses their
  place.
- All panels start **closed**, unless the person arrived from a link or a search result
  pointing at one: that panel opens and takes focus.
- The whole header row is the control (text, chevron, and the space between), at least 44px
  tall, with the chevron rotating to show the state.
- Content inside may include lists, links, and buttons. A **button** is allowed because the
  panel is a container, not body copy; an inline call to action inside a sentence is not
  (see `CLAUDE.md`).
- **Never nested.** An accordion inside an accordion is a filing cabinet; if the content
  needs two levels, it needs a screen.
- The panel does not close on scroll, on blur, or on a timer.

## Motion

- Height and opacity over `motion.duration.base` (160ms), `motion.easing.standard`.
- Under `prefers-reduced-motion`, the panel appears and disappears with no transition.
- The chevron rotation follows the same duration; nothing bounces.

## Accessibility

- Each header is a `button` inside a heading element of the level the page structure calls
  for, so screen readers can jump between headers.
- The button carries `aria-expanded`, and the panel is linked with `aria-controls`; the
  panel is a `region` labelled by its header.
- **Collapsed content is really collapsed** (`hidden`), so it is not read out of order —
  and, because browser find-in-page cannot reach it, the page's own search must open the
  panel it matched rather than reporting nothing.
- Focus never moves when a panel opens: the person keeps their place on the header.
- The state is announced by `aria-expanded`, never by the chevron alone.

## Content examples

- ✅ "Why do I need to confirm my identity?"
- ✅ "How the fee is calculated"
- ✅ "What happens if I close my account"
- ❌ "More information" (describes opening, not content)
- ❌ "Details"
- ❌ An accordion holding the only mention of a 2 € fee on the transfer screen.
- ❌ A collapsed risk warning.

## Machine-readable spec

```json
{
  "accordion": {
    "collapsible-test": "if the person never opens it, can they still decide correctly?",
    "allowed": ["uncommon questions", "detail behind a visible total", "secondary reference text"],
    "forbidden": ["deciding fee, rate, limit or condition", "required disclosure", "risk warning", "error", "disabled reason", "flow step", "content most people need"],
    "header": {
      "predicts-content": true,
      "max-words": 8,
      "form": ["question", "noun-phrase"],
      "parallel-within-group": true,
      "banned": ["more information", "details", "other", "read more", "learn more", "info", "additional information"],
      "case": "sentence",
      "count-or-badge": false
    },
    "behavior": {
      "multiple-open": true,
      "opening-one-closes-another": false,
      "default": "all closed",
      "deep-link-opens-and-focuses": true,
      "target-height": 44,
      "nested": false,
      "closes-on-scroll-or-timer": false
    },
    "content": { "lists": true, "links": true, "buttons": true, "inline-cta-in-prose": false },
    "motion": { "duration": "motion.duration.base", "easing": "motion.easing.standard", "reduced-motion": "none" },
    "a11y": { "header-role": "button", "in-heading": true, "aria-expanded": true, "aria-controls": true, "panel-role": "region", "collapsed-is-hidden": true, "in-page-search-opens-panel": true, "focus-stays-on-header": true }
  }
}
```

## Eval hooks

- The header names its content and is never "More information", "Details", "Read more",
  "Learn more", "Other", or "Info".
- Headers within one group are parallel: all questions or all noun phrases.
- No fee, rate, limit, condition, disclosure, or risk warning that affects the decision sits
  inside a collapsed panel; a total stays visible even when its breakdown collapses.
- Opening one panel never closes another, and panels are never nested.
- The panel's prose contains no inline call to action; an action inside it is a button.
- A panel reached from a link or a search result opens and takes focus.
