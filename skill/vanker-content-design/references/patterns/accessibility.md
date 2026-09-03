# Accessibility in content

**Status: normative (rules) + example (samples).**

Most of what makes a screen usable without sight, without a mouse, or without full
attention is decided by **the words**, not by the code that renders them. A screen reader
does not read a layout; it reads a sequence of strings. A person with low vision does not
see an error highlighted in red; they hear a sentence, or they hear nothing. That makes
accessibility a content discipline before it is an engineering one, and this file is the
part that belongs to whoever writes the copy.

The legal frame is in `../compliance/accessibility.md`: the European Accessibility Act
(Directive EU 2019/882), in force since 28 June 2025, requires EN 301 549 / WCAG 2.1 Level
AA. That file says it is the law. This one says what to type.

## The test that settles most arguments

**Read the screen aloud, in order, to someone who cannot see it. If they cannot act, the
copy is not finished.**

It costs thirty seconds and it catches almost everything on this page: the sentence that
points at a color, the button called "OK", the error that names no field, the link called
"here", the paragraph that assumes you can see the thing above it. Nothing here is
theoretical, and none of it needs a tool to find.

## What the copy owns

| Content owns | Design owns | Engineering owns |
| --- | --- | --- |
| The words a screen reader says, and their order | Contrast, spacing, target size | Roles, `aria-*`, focus management |
| The accessible name of every control | The focus ring | Keyboard order and traps |
| The alternative for every image | Whether motion exists at all | `prefers-reduced-motion` |
| Whether meaning survives without color | Whether color carries a hint | The live region's politeness |

The three columns fail together. Content that names a thing precisely gives engineering an
accessible name to attach and design a label worth showing.

## Rules

1. **Never by color alone, and never by position, size or shape alone.** "The fields marked
   in red" is unreadable to a person who cannot see red, cannot see the screen, or is
   looking at it in bright sun. Name the field. WCAG 1.4.1, and the single most common
   content failure there is. Checked by `A-COLOR-ALONE`.
2. **Never refer to a position on the screen.** "The button below", "on the right", "above".
   Layouts mirror in right-to-left languages, reflow at other sizes, and a screen-reader
   user has no left. Name the thing. Checked by `A-LOCALIZABLE` (see
   `../terminology/localization.md`).
3. **Every string is real text.** Never inside an image, never baked into an illustration.
   Text that lives in a picture cannot be resized, translated, selected, searched, or read
   aloud.
4. **Every control has a name that works alone.** A screen reader can list the buttons on a
   screen with no surrounding copy: six buttons called "OK" are six identical rows. The CTA
   rules in `ctas.md` are an accessibility rule before they are a style rule.
5. **Every image has an alternative, and a decorative image is declared decorative.** An
   empty alt is a deliberate answer, not a forgotten field. See `alt-text.md`.
6. **An error is text, it names the field, and it is announced.** "Your street is missing"
   rather than a red border. See `errors.md` and `forms.md`; the error summary exists
   precisely so that a person who cannot scan the form still knows what to fix.
7. **Link text names its destination.** "Read our privacy policy", never "click here". A
   screen reader can list every link on a page: a list of nine "here"s is a maze. See
   `links.md`.
8. **Announce, do not interrupt.** New information arrives in a polite live region and does
   not steal focus; only something that blocks the person is assertive. A toast that grabs
   focus loses the person their place in the form.
9. **Expand acronyms and abbreviations on first use.** A screen reader pronounces "IBAN" as
   a word and "SCA" as three letters, and neither tells anyone what it is. See
   `../terminology/glossary.md`.
10. **Write ranges and figures so they can be read aloud.** "3 to 5 working days", never
    "3-5": next to money, a hyphen is read as a minus sign by people and by software. See
    `../terminology/numbers-and-dates.md`.
11. **One idea per sentence, one fact per paragraph.** Not a stylistic preference: a person
    using a screen reader cannot skim back over a dense block, and a person with reduced
    attention loses the thread in the middle of a clause.
12. **A timeout warns before it expires and offers more time.** Losing a form to a silent
    timer punishes slow typing, which is what an accessibility need often looks like. The
    copy says what happens and what was kept. See `../patterns/auth.md`.
13. **Copy never depends on motion.** If an animation carries the meaning, the meaning is
    gone under `prefers-reduced-motion`. The words carry it, the motion decorates it.

## Examples

| Not this | This | Why |
| --- | --- | --- |
| "Check the fields marked in red." | "Your street and your postcode are missing." | Names the fields. Works with no screen at all. |
| "Tap the button below to continue." | "Tap Continue." | A button has a name; the screen has no below. |
| "Click here to read our privacy policy." | "Read our privacy policy." | The link says where it goes. |
| "Your session will expire soon." (then it does) | "You have 2 minutes left. Stay signed in?" | Warns, and offers the time back. |
| "Arrives in 3-5 working days." | "Arrives in 3 to 5 working days." | A hyphen next to a figure reads as a minus sign. |
| Alt text: "image.png" | Alt text: "Your card, showing the last four digits" | An alternative, not a file name. |

## Accessibility statement

Vanker publishes an accessibility statement describing conformance, known limitations, and
how to report a problem, and it acts on what is reported. The route to report is written in
the same plain language as everything else, and it is not the only route: someone who cannot
use the form must be able to reach a person. See `../compliance/accessibility.md` and
`complaints.md`.

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
