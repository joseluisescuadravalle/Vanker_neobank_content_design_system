# Dark patterns

**Status: normative within the fiction. Illustrative, not verified. See `/DISCLAIMER.md`.**

What Vanker never does to steer a decision, named pattern by pattern, with the signal each
one leaves in the copy and the check that catches it. This is the deterministic half of the
behavioral layer: the prohibitions. The persuasion Vanker does allow (which bias helps the
person, on which pattern, and where it is forbidden) is a matter of judgment and is
documented separately as the behavioral lens, not here.

**The thesis: every dark pattern is also the grammar of a scam.** Urgency, shaming,
hidden cost and fake crowds are exactly what phishing imitates. A bank that uses them in
its own upsell teaches its customers to trust the fakes, so the ban protects the person
twice: from Vanker, and from whoever pretends to be Vanker.

## What this is not

| If you are looking for | Go to |
| --- | --- |
| The banned word list itself (pressure, blame, marketing claims) | `../terminology/banned-terms.md`, which owns the list; this file names the pattern the words belong to |
| Guaranteed returns, "risk-free", "free" with conditions | `risk-warnings.md`, `principles.md` |
| Whether a consent box may be pre-ticked | `../components/library/checkbox.md` (a component state, not a string) |
| The withdrawal function and its ease of use | `disclosures.md` |
| How a fee is worded | `disclosures.md` |
| The legitimate use of a bias (defaults, goal progress, framing) | The behavioral lens, once written; nothing in this file authorizes a nudge |

## The patterns

Each pattern names the bias it exploits, because a rule an agent understands is a rule it
can apply to a case the list never saw. Every card has the same four parts.

### 1. Confirmshaming

- **What it is.** Wording the decline so that saying no costs the person some self-respect
  ("No thanks, I like paying fees").
- **What it exploits.** Loss aversion and self-image.
- **The signal in the copy.** A decline label that leaves the controlled set, speaks in
  the first person, or names a cost or a loss.
- **What Vanker does instead.** Declines with "Not now", "Cancel", "Back" or "Skip",
  nothing else.

### 2. False scarcity and countdowns

- **What it is.** A limit or a clock the product has no reason to have ("Only 3 spots left
  at this rate", "Offer ends in 04:59").
- **What it exploits.** The scarcity heuristic.
- **The signal in the copy.** Scarcity and time-pressure vocabulary, or a countdown. A
  bank's rates, accounts and cards are not seats on a flight.
- **What Vanker does instead.** A real deadline is a date, written plainly (see
  `../terminology/numbers-and-dates.md`), never a countdown.

### 3. Trick questions

- **What it is.** A consent or an option worded so that the natural answer does the
  opposite of what it reads ("Untick this box to not receive offers").
- **What it exploits.** Cognitive load and the default.
- **The signal in the copy.** Two negators in one checkbox or radio label.
- **What Vanker does instead.** Every checkbox and radio label is one positive statement
  about what happens when it is selected.

### 4. Hidden cost

- **What it is.** An asterisk on a figure, a "free*", or a "from 0,99 €" whose condition
  lives somewhere else.
- **What it exploits.** Anchoring: the first number seen is the number remembered.
- **The signal in the copy.** An asterisk next to a figure or to "free"; "from" before an
  amount with no condition in the same sentence.
- **What Vanker does instead.** The exact amount and its condition sit in the same
  sentence, or the sentence does not carry the amount.

### 5. Unsourced social proof

- **What it is.** "Join thousands who already switched", "most people choose Plus".
- **What it exploits.** The bandwagon effect.
- **The signal in the copy.** A crowd without a figure, a source and a date: a claim
  Vanker cannot back.
- **What Vanker does instead.** A number with its source may be used; a crowd without one
  may not.

### 6. Guilt and fear

- **What it is.** Turning loss aversion against the person: "Don't let your savings lose
  value", "You'll regret this", "before it's too late".
- **What it exploits.** Loss aversion.
- **The signal in the copy.** Regret, loss and "too late" vocabulary aimed at the person.
  Three surfaces are exempt by shape, because a real consequence may need naming there:
  `security`, `system-error` and `auth-error`. Marketing and onboarding are not exempt:
  they are where this language appears, and where the regulator looks first.
- **What Vanker does instead.** States the benefit or the fact and lets the person decide.

### 7. No way to say no

- **What it is.** An offer, an upgrade or a consent with a primary action and no decline
  ("Accept" alone, or a decline that only appears after scrolling).
- **What it exploits.** The default.
- **The signal in the copy.** A screen that asks for an acceptance and carries no decline
  from the controlled set.
- **What Vanker does instead.** Every screen that asks the person to accept something
  carries the decline beside it, at the same cost in taps, and the decline never leaves
  the task the person was doing.

## Rules

1. **The decline is one of "Not now", "Cancel", "Back" or "Skip"**: a controlled set makes
   confirmshaming impossible by construction, and it keeps the decline recognizable across
   the product. Reason: a shamed "no" is a decision taken under pressure, and Distance
   Marketing of Financial Services (Directive EU 2023/2673) forbids making the decline
   harder than the accept.
2. **No scarcity or time-pressure vocabulary anywhere in customer copy**: "limited time",
   "only today", "ends soon", "spots left", "only {n} left", "others are viewing", "while
   it lasts", and no countdown ("ends in 2 hours", "in 04:59"; "your card ends in 4321"
   is not one). Reason: none of it is true of a bank product, and the words
   are the ones a scam uses (see `../patterns/emails.md` on urgency and fraud).
3. **No double negative in a checkbox or radio label.** Reason: nobody can tell what an
   unchecked "do not" means, and a consent given by mistake is not consent (see
   `data-privacy.md`).
4. **No asterisk on a figure or on "free", and no "from" before an amount unless the
   condition is in the same sentence.** Reason: the footnote is where the cost hides, and
   `disclosures.md` requires every fee exact and up front.
5. **No crowd without a source**: "most people", "join thousands", "join millions",
   "everyone is", "customers like you". Reason: it is a factual claim about other people,
   and Vanker cannot make claims it cannot show.
6. **No guilt or fear framing in any surface except security, system-error and
   auth-error**: "you'll regret", "don't let", "lose out", "before it's too late", "you're
   missing", "don't miss". Reason: fear is pressure, and `../voice-and-tone/voice.md` sets
   Vanker as warm but serious, without pressure, everywhere outside a real risk.
7. **A screen that asks for acceptance carries a decline** (screen level). Reason: the
   right to decide is the person's, and an accept without a decline is a default dressed
   as a choice.
8. **What this file does not check, it says so.** Asymmetric friction (more steps to cancel
   than to sign up), nagging (the same offer repeated after a "Not now"), preselecting
   the more expensive option, and sludge in the complaints route are real dark patterns
   that no single string reveals. They are documented here so nobody assumes they are
   covered, and they are graded by judgment, not by code.

## Accessibility

- A shamed decline is read aloud by a screen reader with the same weight as the accept;
  the controlled set keeps the choice neutral in every modality.
- A countdown announced as a live region interrupts a screen reader every second. Rule 2
  removes the countdown; if a date exists, it is static text.
- The decline is in the tab order right after the primary, never after the fold.

## Content examples

**Decline label (tertiary button)**

- ✅ Not now
- ❌ No, I'll keep paying fees. Reason: first person and a cost in the decline (confirmshaming).
- ❌ I don't want to save. Reason: the decline names a loss.

**Offer body**

- ✅ Plus costs 4 € a month and includes 5 free international transfers.
- ❌ Only 3 spots left at this rate. Reason: scarcity a bank does not have.
- ❌ Free* international transfers. Reason: the cost hides behind the asterisk.
- ❌ From 0,99 € a month. Reason: "from" without its condition in the same sentence.
- ❌ Join thousands who already switched to Plus. Reason: a crowd without a source.
- ❌ Don't let your savings lose value. Reason: fear framing outside a real risk.

**Consent label (checkbox)**

- ✅ Send me offers from Vanker by email
- ❌ Untick this box to not receive offers. Reason: double negative; the natural reading does the opposite.

**Offer screen (title, body and buttons together)**

- ✅ Title "Plus for 4 € a month" (the price is the anchor, see `../patterns/offers.md`), body with what it includes, primary "Upgrade", tertiary "Not now".
- ❌ The same screen with "Upgrade" as the only button. Reason: no way to say no.

**Security warning (exempt from rule 6)**

- ✅ Someone tried to sign in from a new device. If it was not you, lock your card now. Reason: a real consequence, on an exempt surface.

```json
{
  "dark-patterns": {
    "decline-labels": ["Not now", "Cancel", "Back", "Skip"],
    "decline-forbidden": { "first-person": true, "cost-or-loss": true },
    "scarcity-terms": ["limited time", "only today", "ends soon", "spots left", "only {n} left", "others are viewing", "while it lasts"],
    "countdown": true,
    "double-negative": { "checkbox": false, "radio": false },
    "hidden-cost": { "asterisk-on-figure": false, "asterisk-on-free": false, "from-without-condition": false },
    "social-proof-terms": ["most people", "join thousands", "join millions", "everyone is", "customers like you"],
    "guilt-terms": ["you'll regret", "you will regret", "don't let", "lose out", "before it's too late", "you're missing", "don't miss"],
    "guilt-exempt-surfaces": ["security", "system-error", "auth-error"],
    "offer-screen": { "decline-required": true, "same-tap-cost": true, "decline-stays-in-task": true },
    "not-checked": ["asymmetric-friction", "nagging", "expensive-default", "complaints-sludge"]
  }
}
```

## Eval hooks

| ID | Checks | Surfaces |
| --- | --- | --- |
| `A-CONFIRMSHAME` | A decline label is one of the controlled set; any first-person pronoun, cost or loss word fails | `decline-cta` (new surface) |
| `A-SCARCITY` | No scarcity or time-pressure term, on word boundaries | universal (appended to every surface) |
| `A-DOUBLE-NEGATIVE` | No "not" or "never" together with "un-", "no" or "without" in the same label | `checkbox`, `radio-option` |
| `A-PRICE-ASTERISK` | No `*` attached to a figure or to "free"; "from" directly before an amount needs "if", "when", "for" or "with" in the same sentence | every body-type surface, `email-body`, `banner`, `carousel-body` |
| `A-SOCIAL-PROOF` | No unsourced crowd term | universal |
| `A-GUILT` | No guilt or fear term; skipped on `security`, `system-error`, `auth-error` | universal minus the exempt three |
| `A-DECLINE-PRESENT` | Screen level: an `offer-screen` with a primary CTA carries a decline CTA from the controlled set | `offer-screen` (new surface) |

Documented but not checked (rule 8): asymmetric friction, nagging, the expensive default,
complaints sludge. They belong to the behavioral lens and the editorial review, and they
are listed under the same heading in `../evals/assertions.md`.

`A-SCARCITY` and `A-GUILT` extend the pressure family that `A-NO-BANNED` already rejects
("hurry", "act now", "last chance", "miss out", "urgent", "final notice"). They are separate
checks, not more rows in the banned list, so the panel names the pattern ("false scarcity")
rather than the word, which is what teaches the writer.
