# Offers

**Status: normative (rules) + example (samples).**

Copy that proposes something the person did not ask for and may pay for: a paid tier, a
paid feature, a promotional rate, a partner product. It is the one surface in the product
where Vanker's interest and the person's can pull apart, so it is the surface with the
most rules and the fewest words.

**The thesis: an offer is a fair question, not a pitch.** The price is the first thing
seen, the decline is as close as the accept, and the answer is taken as final. Everything
`../compliance/dark-patterns.md` forbids was invented on this screen.

## What this is not

| If you are looking for | Go to |
| --- | --- |
| A confirmation before a money action | `confirmations.md` |
| The pre-login argument for Vanker itself | `welcome-carousel.md` |
| A permission the app needs | `permissions.md` |
| The prohibited practices and their checks | `../compliance/dark-patterns.md` |
| Fee wording and pre-contractual information | `../compliance/disclosures.md` |

## Situations

- **A paid tier or feature** (an upgrade): a contract at a distance, so
  `../compliance/disclosures.md` applies: the fee, what it includes, and the right of
  withdrawal where it applies.
- **A promotional rate**: the rate, its end date as a plain date, and what happens after.
- **A partner product**: who provides it, and that leaving Vanker's screens is about to
  happen.

## Slots

- **Title** (required): names the offer and its price in one line ("Plus for 4 € a
  month"). No question, no verb, no adjective. The price sits in the title so that the
  first thing seen is the true anchor.
- **Body** (required, one to three short paragraphs): what it includes, the condition if
  any, and the one fact that would change the decision (a minimum term, a date, a fee
  after the promotion). Nothing the person would discover later.
- **Primary** (required): the action verb ("Upgrade", "Activate"). Never "Yes", never the
  benefit ("Save more").
- **Decline** (required): one of "Not now", "Cancel", "Back" or "Skip", checked as
  `decline-cta`. Never "Learn more" in its place, never a sentence.

## Rules

1. **The price is in the title.** Reason: whatever is read first becomes the reference,
   and the reference must be the real cost, not the benefit.
2. **The decline costs one tap and sits under the primary, always visible.** Reason: a
   decline behind a scroll, a link, or a second screen is a harder path to say no, which
   Distance Marketing of Financial Services (Directive EU 2023/2673) forbids.
3. **One offer per screen, never inside another task.** No upsell in a confirmation, an
   error, a success screen, or a loading state. Reason: a person in the middle of moving
   money is not deciding about a subscription, and the ending of an action closes, it does
   not sell (see `../behavioral/biases.md`, peak-end).
4. **"Not now" is taken as an answer.** The same offer does not return in the same session,
   and not before a stated interval. Reason: repetition after a decline is nagging;
   documented in `../compliance/dark-patterns.md` and graded by judgment.
5. **The body carries every fact that would change the decision.** Reason: a fact found
   after accepting is a hidden cost, whatever its size.
6. **No scarcity, no crowd, no fear, no asterisk.** Reason: each is a check
   (`A-SCARCITY`, `A-SOCIAL-PROOF`, `A-GUILT`, `A-PRICE-ASTERISK`), and each is the grammar
   of a scam.
7. **A gain frame is allowed; the fact stays complete.** "Keep 3 € a month on international
   transfers" is fine when the price and the condition are on the same screen. Reason: a
   gain frame helps the person weigh the offer; it never replaces the cost.
8. **A partner product says who provides it before the tap.** Reason: the person is
   about to deal with another company under other terms.

## Accessibility

- The decline is in the tab order right after the primary and is announced with the same
  role; nothing about it is smaller in the accessibility tree.
- The price in the title is real text, never only in an image.
- The sheet does not trap the person: scrim tap and swipe dismiss it, as a decline.

## Examples (slot format)

- ✅ Title "Plus for 4 € a month" / Body "Plus includes 5 free international transfers a month and
  a second card. You can cancel any month, and the fee stops the next month." / Primary "Upgrade"
  / Decline "Not now".
- ✅ Title "2% on Spaces until 31 October 2026" / Body "The rate applies to every Space
  from today until 31 October 2026. After that date, the standard rate applies." /
  Primary "Activate" / Decline "Not now".
- ❌ Title "Save more with Plus". Reason: the benefit where the price should be.
- ❌ Body "Only 3 spots left at this rate." Reason: false scarcity (`A-SCARCITY`).
- ❌ Decline "No, I'll keep paying fees". Reason: confirmshaming (`A-CONFIRMSHAME`).
- ❌ Decline "Learn more". Reason: not a decline; the person has no way to say no
  (`A-DECLINE-PRESENT`).
- ❌ An upgrade offer on the screen that confirms a transfer. Reason: an offer inside
  another task (rule 3).

## Machine-readable spec

```json
{
  "offers": {
    "surface": "offer-screen",
    "slots": {
      "title": { "required": true, "names-offer-and-price": true, "question": false, "verb": false },
      "body": { "required": true, "paragraphs-max": 3, "carries-decision-facts": true },
      "primary": { "required": true, "surface": "cta", "verb": true },
      "decline": { "required": true, "surface": "decline-cta", "labels": ["Not now", "Cancel", "Back", "Skip"] }
    },
    "one-per-screen": true,
    "never-inside": ["confirmation", "error", "success", "loading", "system-error"],
    "decline-taken-as-answer": true,
    "gain-frame-allowed": true,
    "partner-named-before-tap": true
  }
}
```

## Behavioral lens

- **Applies.** Target behavior: `decide-freely`.
- **Biases allowed.** Gain framing (rule 7), with the price in the title and the fact
  complete in the body. Anchoring only on the true price: the title is the anchor.
- **Biases forbidden here.** Default effect (nothing preselected, no trial that converts
  by itself), goal gradient (no progress toward a purchase), positive friction on the
  decline (one tap), and the checked ones: scarcity, social proof, fear.
- **What the reviewer scores.** "Serves the declared behavior", "Uses only allowed
  biases", "Frame is a gain and the fact is complete", "Friction protects, never retains".
  Everything else `na`.

## Eval hooks

- Title carries an amount or a rate in the European format (`A-EURO-FORMAT`) and no
  question mark; the reviewer confirms it names the offer.
- Decline is one of the controlled labels (`A-CONFIRMSHAME`) and is present
  (`A-DECLINE-PRESENT`).
- No scarcity, crowd, fear or asterisk (`A-SCARCITY`, `A-SOCIAL-PROOF`, `A-GUILT`,
  `A-PRICE-ASTERISK`).
- An offer never appears inside another task (reviewer; documented, not checked).
- The same offer does not return in the session after a decline (reviewer; documented,
  not checked).
