# Alt text

**Status: normative (rules) + example (samples).**

The text that stands in for anything that is not text: icons, illustrations, photographs,
charts, card artwork, QR codes. It is copy, it is translated like copy, and it is written
by whoever writes the copy, not left to whoever implements the screen.

The legal frame is in `../compliance/accessibility.md`; the icon rules are in
`../components/foundations/iconography.md`.

## The question that decides everything

**Not "what is in the image", but "what would this person miss if the image were not
there?"**

The same photograph needs different alt text on different screens, because its job changes.
A picture of a card on the card screen carries nothing the surrounding text does not
already say; the same picture in a help article about spotting a cloned card carries the
whole point. Alt text describes the **function in this context**, never the pixels.

## The four kinds

### 1. Decorative — empty alt

Most illustrations in this product are decorative, because the heading beside them already
says everything.

- The alt attribute is **present and empty** (`alt=""`), so the image is skipped. Leaving
  the attribute out entirely makes some screen readers read the file name aloud, which is
  how a person ends up hearing "empty dash state dash illustration two dot p n g".
- **If the text next to it already carries the meaning, the image is decorative.** Repeating
  it makes the person hear it twice.

### 2. A meaningful icon — name the function, not the picture

- The alt is what the control **does**: "Delete space", not "bin". "Freeze card", not
  "snowflake".
- **An icon next to a visible text label is decorative.** The label already speaks; giving
  both a name makes the screen reader say it twice.
- A status icon carries the status in words: the icon beside a `Failed` label is decorative,
  because the label is text (see `../components/library/status-label.md`).

### 3. An informative image — one sentence, no prefix

- Describe what the image tells the person, in one sentence, in the same voice as the rest
  of the screen.
- **Never "image of", "picture of", "photo of", "icon of", "graphic of".** The screen reader
  already announces that it is an image; the prefix spends the first two seconds saying
  nothing.
- About 125 characters. If it needs more, the description is not alt text: it is content,
  and it belongs on the screen where everyone can read it.

### 4. A chart — the takeaway, plus the data as text

This is the case a bank gets wrong most often, because a spending breakdown is a picture of
someone's money.

- The alt names **what the chart shows and what it shows about it**: "Spending by category
  this month, with groceries the largest."
- **The figures live in text or a table**, reachable by everyone. No alt sentence can
  substitute for the data, and a person using a screen reader is entitled to the numbers,
  not to a summary of them.
- Never put a figure only in the image. If it matters, it is text on the screen.

## Rules for a bank

- **Money is never only in an image, and never only in alt text.** An amount shown in a
  graphic is also real text on the screen.
- **Card artwork is decorative.** The last digits, the status, and the card name are text
  (see `../patterns/cards.md`).
- **Alt text never reveals what masking hides.** A card number visible in a screenshot is a
  leak whether it is in the picture or in its description (see `A-MASK`).
- **A QR code's alt gives the alternative route**, not the encoded content: "QR code to open
  Vanker on your phone. You can also open the app and choose Add money."
- **Screenshots in help content describe the step**, not the pixels: "The Cards screen, with
  the Frozen switch turned on."

## Writing rules

- Sentence case. A short label takes no ending period; a full sentence takes one (see
  `../terminology/capitalization-and-punctuation.md`).
- No emoji, no file names, no dimensions, no "click here".
- Do not repeat the caption or the adjacent heading word for word.
- Alt text is translated with everything else, so no idioms and no wordplay
  (`../voice-and-tone/inclusive-language.md`).
- Write it when you write the screen. Alt text added later is alt text written by someone
  who no longer knows what the image was for.

## Examples

| Context | Alt |
| --- | --- |
| Illustration above "No transactions yet" | `""` (decorative: the heading says it) |
| Icon-only button that freezes a card | "Freeze card" |
| Icon beside the visible label "Frozen" | `""` (the label speaks) |
| Chart of monthly spending | "Spending by category this month, with groceries the largest." |
| Card artwork on the card screen | `""` |
| Help screenshot of the frozen state | "The Cards screen, with the Frozen switch turned on." |

Not this:

- "Image of a graph showing spending"
- "empty-state-illustration-2.png"
- "Chart" (says nothing)
- "Your balance is 2.540,75 €" as the only place that figure exists

## Machine-readable spec

```json
{
  "alt-text": {
    "question": "what would the person miss if the image were not there",
    "kinds": {
      "decorative": { "alt": "", "attribute-present": true, "when": "the adjacent text already carries the meaning" },
      "icon": { "alt": "the function of the control", "decorative-when": "a visible text label is beside it" },
      "informative": { "alt": "one sentence", "max-chars": 125, "prefix": false },
      "chart": { "alt": "what it shows and the takeaway", "data-as-text": "required" }
    },
    "banned-prefixes": ["image of", "picture of", "photo of", "icon of", "graphic of"],
    "bank": {
      "money-only-in-image": false,
      "card-artwork": "decorative",
      "reveals-masked-data": false,
      "qr-code": "the alternative route, not the encoded content"
    },
    "writing": { "case": "sentence", "emoji": false, "file-names": false, "duplicates-adjacent-text": false, "translated": true }
  }
}
```

## Eval hooks

- No alt text begins with "image of", "picture of", "photo of", "icon of", or "graphic of".
- An icon's alt names the function, not the shape, and an icon beside a visible label is
  decorative.
- Alt text is about 125 characters at most; longer descriptions are content on the screen.
- No file name, no dimensions, no emoji in alt text.
- No amount, card number, or masked identifier appears only in an image or only in its alt.
- A chart's data is available as text, not only as a described picture.
