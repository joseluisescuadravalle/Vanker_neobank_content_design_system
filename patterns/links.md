# Links

**Status: normative (rules) + example (samples).**

Text a person taps to go somewhere. Buttons are in `ctas.md`; this is the other half of the
same decision.

## Link or button

The rule in `ctas.md` says a label names **what happens** on tap. This one says the shape
names **what kind of thing** happens.

| The tap | Shape |
| --- | --- |
| Changes something: money moves, a setting flips, a form is submitted, a card is frozen | **Button** |
| Takes the person somewhere: a screen, a document, a page, a phone call | **Link** |

Two consequences that catch most mistakes:

- **A button that only navigates is lying about its weight.** A banner action that opens an
  explanation is a link, not a "Verify" button (see `../components/library/banner-toast.md`).
- **A link that changes something is worse.** People expect a link to be safe and
  reversible: nothing that moves money is ever a link.

## The text names its destination

**Never "here", "click here", "read more", "learn more", "this link", or "more".**

The reason is not style. Screen reader users navigate by pulling up **a list of the links on
the screen**, with no surrounding sentence. A screen of "here", "here", "read more" is a
list of identical, meaningless entries. The same is true of anyone scanning: the eye stops
on links, and a link that says nothing costs a re-read of the sentence around it.

- ✅ "Read the privacy policy" · "See your fee information" · "Open your statement"
- ❌ "Click here to read the privacy policy" · "Learn more" · "More info"

Rules:

- **Link the shortest phrase that names the destination.** Not the whole sentence, not one
  vague word. Never include the trailing period or a comma in the link.
- **The same destination is always named the same way**, everywhere in the product. Two
  names for one page read as two pages.
- Up to about five words.
- Sentence case, no ending punctuation (see `../terminology/capitalization-and-punctuation.md`).
- **Say when the link leaves.** A link that opens a browser, a document, or a phone call
  says so: "Read the fee information (PDF)", "Call us on the number on your card". A person
  who lands somewhere they did not expect assumes something went wrong.

## Shape, not only color

**A text link carries a shape as well as a color.** Color alone does not identify a link:
WCAG 1.4.1 (Use of Color) is not met by a different shade of the same text, and around 8%
of men cannot rely on hue at all.

- In body copy, a link is **underlined**.
- Where the whole row is the target and a chevron marks it, the chevron is the affordance
  and no underline is needed.
- On the dark toast, the action is white, bold **and underlined** (see
  `../components/library/banner-toast.md`): on graphite, where the message is already
  white, weight alone is not a difference a person can rely on.
- The accent color is never the only signal, and fuchsia is never used as link color on a
  dark surface.

## Where a link may not go

- **Inside a tooltip.** It closes as the person reaches for it (see
  `../components/library/tooltip.md`).
- **Inside a status label, a button, or a toggle label.**
- **Inside the body of an error.** The way out is a button (see `errors.md`).
- **Behind anything that must be seen.** A required disclosure, a fee, or a risk warning is
  on the screen, not one tap away (see `../compliance/disclosures.md`).

## Links in email

An email link is the object phishing imitates most, so it carries two extra rules:

- **Never a bare or shortened URL.** The visible text names the destination; a raw
  `https://…` or a shortener is what a fake looks like.
- **The destination is a Vanker domain**, and the page it opens never asks for a passcode,
  card details, or a code (see `emails.md`).

## Machine-readable spec

```json
{
  "links": {
    "shape-decision": { "changes-something": "button", "navigates": "link", "money": "never a link" },
    "text": {
      "names-destination": true,
      "banned": ["here", "click here", "tap here", "read more", "learn more", "more", "more info", "this link", "link"],
      "max-words": 5,
      "case": "sentence",
      "ending-punctuation": false,
      "includes-trailing-punctuation": false,
      "same-destination-same-name": true,
      "says-when-it-leaves": true
    },
    "affordance": {
      "underline-in-body": true,
      "color-alone": false,
      "chevron-row": "chevron is the affordance",
      "toast-action": "white, bold and underlined"
    },
    "never-inside": ["tooltip", "status-label", "button", "toggle-label", "error body"],
    "never-behind": ["required disclosure", "fee", "risk warning"],
    "email": { "bare-url": false, "shortened-url": false, "domain": "vanker", "destination-asks-for-credentials": false }
  }
}
```

## Eval hooks

- Link text names its destination: "here", "click here", "read more", "learn more", "more",
  and "this link" all fail.
- Link text is up to about five words, sentence case, with no ending punctuation and no
  trailing period inside the link.
- A link that leaves the app or opens a document says so.
- A link is underlined in body copy, or its row carries a chevron; color is never the only
  signal.
- Nothing that moves money is a link, and no required disclosure sits behind one.
- An email never shows a bare or shortened URL as link text.
