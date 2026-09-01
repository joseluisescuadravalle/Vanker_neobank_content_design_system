# Chip

**Status: normative.**

A small, rounded, **interactive** control that carries a value: a filter, a choice among a
few, or something the person added and can remove.

It looks like a status label and is nothing like one. The difference is the whole reason
they are separate files:

| | Chip | Status label |
| --- | --- | --- |
| Interactive | **Yes** | No |
| Who sets it | The person | The system |
| Vocabulary | Open: it carries a value | Closed: a controlled term |
| Figures | Allowed, because the figure is the value | Never |

A chip is also not a button (a button performs an action) and not a toggle (a toggle is a
setting that applies immediately, see `toggle.md`).

## The three kinds

- **Filter chip:** turns a filter on or off. Several can be on at once.
- **Choice chip:** picks one value from a few, like a compact radio group. Use a
  `radio-group.md` when the options need explaining, and a `dropdown.md` when there are more
  than about six.
- **Input chip:** a value the person added, with a remove control: a recipient, a tag, a
  category they chose.

## The label

- **It names the value, not the act.** "Date", not "Filter by date". "Groceries", not
  "Show groceries".
- **Never a verb.** A verb makes it look like a button, and tapping a chip must never
  navigate or submit (see `../../patterns/ctas.md`).
- One to three words, sentence case, no ending punctuation, no emoji.
- **A figure is allowed when the figure is the value**: "Over 100 €", "Last 30 days". This
  is the one control in the system where an amount belongs, because the amount is what the
  person is choosing, not what they are being asked to do.
- Parallel within a row: all nouns, or all ranges. Never mixed.

## Behavior

- **Selected state is a fill and a check, never color alone**: `color.accent-subtle`
  background with `color.text-primary`, plus a check mark (see
  `../foundations/color.md`).
- **Chips are never the only route to something.** A row of chips scrolls sideways and the
  ones off-screen are invisible; anything essential is also reachable another way.
- **When filters are applied, the screen says so in text**, not only through the state of
  chips that may be scrolled out of view: "3 filters applied", with a way to clear them.
- Choosing a chip never submits a form and never opens a screen.
- An input chip's remove control names its value: "Remove Ana", never a bare "Remove".
- Minimum 44px tap target, including the remove control, which is its own target.

## Accessibility

- A filter chip is a toggle button (`aria-pressed`), a choice chip is a radio in a group,
  and an input chip is a button with a nested remove button. The role matches what it does.
- The selected state is programmatic, never inferred from the fill.
- A horizontal row is reachable by keyboard, and reaching the end is possible without a
  pointer.
- The number of results after a filter changes is announced politely.

## Machine-readable spec

```json
{
  "chip": {
    "interactive": true,
    "kinds": ["filter", "choice", "input"],
    "not": ["status-label", "button", "toggle"],
    "label": {
      "names-the-value": true, "verb": false, "words": [1, 3], "case": "sentence",
      "ending-punctuation": false, "emoji": false,
      "figures": "allowed, because the figure is the value",
      "parallel-within-row": true
    },
    "selected": { "fill": "color.accent-subtle", "check": true, "color-alone": false },
    "sole-route": false,
    "applied-filters-stated-in-text": true,
    "submits-or-navigates": false,
    "remove-control": { "names-the-value": true, "own-target": true },
    "a11y": { "filter": "toggle button with aria-pressed", "choice": "radio in a group", "input": "button with a nested remove button", "min-target": 44, "results-announced": "polite" }
  }
}
```

## Eval hooks

- A chip label names the value, never the act, and never begins with a verb.
- One to three words, sentence case, no ending punctuation, no emoji.
- A figure is allowed only where the figure is the value being chosen.
- Chips in a row are parallel: all nouns or all ranges.
- Applied filters are stated in text, not only by the state of chips that may be off-screen.
- A remove control names the value it removes.
