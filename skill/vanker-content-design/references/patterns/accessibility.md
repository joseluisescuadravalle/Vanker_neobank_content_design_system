# Accessibility in content

**Status: normative (rules) + example (samples).**

For someone using a screen reader, an interface isn't a design but a sequence of strings
read out one after another. **Accessibility is measured, for the most part, through the
words**, not the code that renders them. A person with low vision does not see an error
highlighted in red; they hear a sentence, or they hear nothing. That makes accessibility a
content discipline before it is an engineering one, and this file is the part that belongs
to whoever writes the copy.

The legal frame is in `../compliance/accessibility.md`: the European Accessibility Act
(Directive EU 2019/882), in force since 28 June 2025, requires EN 301 549 / WCAG 2.1 Level
AA. That file says it is the law. This one says what to type.

## The test that settles most arguments

**One simple test tells you whether the text on a screen is accessible: read it aloud to
someone who can't see it. If they can't make a decision and move on, the text isn't
finished.**

In a few seconds, with no tools, you'll catch everything that fails: the sentence that
points at a color, the button that only says "OK", the link that says "here", and the
paragraph that assumes you can see the screen.

## What the copy owns

| Content decides | Design decides | Engineering decides |
| --- | --- | --- |
| The words a screen reader says, and their order | Contrast, spacing, and the size of the tap target | Describing every element and its state to a screen reader |
| The accessible name of every control | The focus ring | Never trapping keyboard navigation |
| The alternative for every image | Whether there is motion at all | Respecting the "reduce motion" setting |
| Whether the meaning survives without color | Whether color carries a hint, never the meaning | Announcing what changes without interrupting what the person is doing |

Accessibility isn't one team's job. It's shared between content, design, and engineering,
and the three depend on each other: if one fails, it all fails.

## Rules

1. **Never point at something by color alone, or by position, size, or shape.** "The fields
   marked in red" means nothing to someone who can't see red, can't see the screen, or is
   reading it in bright sunlight. Name the fields. WCAG 1.4.1, and the single most common
   content failure there is. Checked by `A-COLOR-ALONE`.
2. **Never refer to a position on the screen.** "The button below", "on the right". Layouts
   reflow on other screen sizes, and a screen reader user has no left. Name the thing.
   Checked by `A-LOCALIZABLE` (see `../terminology/localization.md`).
3. **Words are always text, never part of an image.** Text painted into an image can't be
   translated, selected, searched, or read by a screen reader.
4. **Every control needs a specific name.** To a screen reader, six buttons called "OK" are
   six identical rows. The CTA rules in `ctas.md` are an accessibility rule before they are
   a style rule. Checked by `A-CTA`.
5. **Every image needs alt text: the label a screen reader reads to explain what the image
   shows.** If the image is decorative, or its information is already in the visible text,
   the alt text is left empty so nothing is repeated. An empty alt is a deliberate answer,
   not a forgotten field. See `alt-text.md`. Checked by `A-ALT`.
6. **An error is shown as text and names the field it refers to.** "Your street is missing"
   rather than a red border. The error summary exists precisely so that a person who can't
   scan the form still knows what to fix. See `errors.md` and `forms.md`. Checked by
   `A-FIELD-ERROR`.
7. **Link text names its destination.** "Read the privacy policy", never "click here". To a
   screen reader, a list of nine "here"s is a maze. See `links.md`. Checked by
   `A-LINK-TEXT`.
8. **Announce, don't interrupt.** New information appears calmly, without cutting off what
   the person is doing. Only something that truly blocks them, like an error that stops them,
   can interrupt. A toast that grabs focus loses the person their place in the form.
9. **Expand acronyms and abbreviations on first use.** A screen reader pronounces "IBAN" as
   a word and "SCA" as three letters, and neither tells anyone what it is. See
   `../terminology/glossary.md`.
10. **Write ranges and figures so they can be read aloud.** "3 to 5 working days", never
    "3-5": next to money, a hyphen is read as a minus sign by people and by software. See
    `../terminology/numbers-and-dates.md`.
11. **One idea per sentence and one fact per paragraph, to avoid cognitive overload.** A
    dense block tires anyone, and a screen reader user can't skip it: they have to hear all
    of it. Checked by `A-PARAGRAPHS`.
12. **A timeout warns first and offers more time.** Losing a form to a silent timer punishes
    anyone who needs to type slowly. The copy says what happens and what was kept. See
    `../patterns/auth.md`.
13. **Copy never depends on motion.** If the meaning lives in an animation, it disappears
    when the person turns on reduced motion (`prefers-reduced-motion`). The words carry it;
    the motion decorates it.

## Examples

| Wrong | Right | Why |
| --- | --- | --- |
| "Check the fields marked in red." | "Your street name and postal code are missing." | It works without a screen. |
| "Tap the button below to continue." | "Tap Continue." | The button has a name. |
| "Click here to read our privacy policy." | "Read the privacy policy." | The link says where it goes. |
| "Your session will expire soon." | "You have 2 minutes left. Do you want to stay logged in?" | It warns and says how much time is left. |
| "Arrives in 3-5 working days." | "Arrives in 3 to 5 working days." | A hyphen next to a figure reads as a minus sign. |

## Behavioral lens

- **Does not apply**: a cross-cutting rule, not a decision the person takes. The reviewer scores it `na`.

See `../behavioral/biases.md` for the cards and `../behavioral/lens.md` for the rubric.

## Eval hooks

- No string identifies something by color alone ("marked in red", "the green button").
- No string refers to a position on the screen.
- Every call to action names its action; no bare "OK" or "Confirm".
- Every link names its destination.
- Every acronym is expanded on first use.
- A range between figures uses "to", never a hyphen.
- A field error names the field and states a fact.
- Alt text exists for every meaningful image; a decorative one carries an empty string on
  purpose.

## Machine-readable spec

```json
{
  "accessibility": {
    "standard": "EN 301 549 / WCAG 2.1 AA",
    "legal-anchor": "compliance/accessibility.md",
    "content-owns": ["screen-reader text and its order", "accessible names", "alternatives", "meaning without color"],
    "rules": {
      "color-alone": false,
      "position-reference": false,
      "text-in-images": false,
      "named-controls": true,
      "alt-required": true,
      "decorative-alt": "empty string, declared",
      "errors": { "as-text": true, "names-the-field": true, "announced": true },
      "link-text": "names the destination",
      "live-region": { "default": "polite", "assertive": "only when it blocks" },
      "acronyms": "expanded on first use",
      "ranges": "to, never a hyphen",
      "density": { "one-idea-per-sentence": true, "one-fact-per-paragraph": true },
      "timeout": { "warns": true, "offers-more-time": true, "states-what-was-kept": true },
      "motion": { "meaning-in-motion": false, "respects-reduced-motion": true }
    },
    "checks": ["A-COLOR-ALONE", "A-LOCALIZABLE", "A-CTA", "A-LINK-TEXT", "A-ALT", "A-ACRONYMS", "A-DATE", "A-FIELD-ERROR", "A-PARAGRAPHS"]
  }
}
```
