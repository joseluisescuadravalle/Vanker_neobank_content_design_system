# Biases Vanker may use

**Status: normative (rules) + example (samples).**

Eight biases, one card each. Every card has the same six parts, because the boundary
between a nudge and a dark pattern is not the bias but the way it is used, and a card
without the "where it turns" part is a catalog of tricks. Amounts follow the European
format (see `../terminology/glossary.md`).

**The thesis: the same mechanism that helps a person save is the one that sells them a
subscription they did not want.** Each card names both sides.

## What this is not

| If you are looking for | Go to |
| --- | --- |
| The prohibited patterns and their checks | `../compliance/dark-patterns.md` |
| Which biases a given pattern may use | The **Behavioral lens** block of that file in `../patterns/` |
| How the reviewer scores the use of a bias | `lens.md` |
| The neutral frame for investment, credit and crypto | `../compliance/risk-warnings.md` |

## 1. Default effect

- **Mechanism.** People keep what is already set. The default is the decision most people
  end up with.
- **Where it helps.** Security alerts on, the suggested saving amount pre-filled, the
  safest delivery option selected. The default is the option that protects the person or
  costs them nothing.
- **Where it turns.** A pre-ticked consent, the paid tier preselected, the expensive
  delivery as default. Every consent starts empty (`../components/library/checkbox.md`).
- **Patterns.** forms, notifications, confirmations, cards.
- **Forbidden.** Consents, credit, investment, crypto.
- ✅ Alerts for every card payment are on. You can change this in Settings.
- ❌ Plus is selected for you. Reason: the default favors the product, not the person.
- **Watched by.** `A-DOUBLE-NEGATIVE` and the checkbox spec (code); "Default protects the
  person" in `lens.md` (reviewer).

## 2. Goal gradient

- **Mechanism.** Effort rises as the goal gets close. A visible distance to the end keeps
  people going.
- **Where it helps.** "Step 2 of 3", a saving goal with the amount left, an onboarding
  that says how long it takes.
- **Where it turns.** A fake progress bar, a "you are almost there" with no real steps
  behind it, a countdown. `A-NO-BANNED` rejects "almost there".
- **Patterns.** flow-intro, welcome-carousel, empty-states, success.
- **Forbidden.** Identity verification (nothing accelerates KYC, Know Your Customer);
  anything that leads to a purchase.
- ✅ 120 € to go for your trip to Lisbon.
- ❌ You are almost there, do not stop now. Reason: no real distance shown, and pressure.
- **Watched by.** `A-NO-BANNED`, `A-SCARCITY` (code); "Progress is real" in `lens.md`.

## 3. Gain framing

- **Mechanism.** The same fact reads differently as a gain or as a loss. People act more
  calmly on gains.
- **Where it helps.** Say what the person gets ("keep 3 € a month") rather than what they
  lose without it. The fact stays the same and the disclosure stays complete.
- **Where it turns.** A gain frame that hides the cost, or its mirror: a loss frame used to
  push ("do not lose your rate"). The loss frame is `A-GUILT` territory.
- **Patterns.** ctas, empty-states, notifications, emails.
- **Forbidden.** Risk warnings, credit, investment, crypto: those carry a neutral frame by
  regulation, and a gain frame on a risk is a prohibited claim.
- ✅ Round up your card payments and set the change aside.
- ❌ Stop wasting the change from your card payments. Reason: a loss frame with blame.
- **Watched by.** `A-GUILT`, `A-NO-CLAIMS` (code); "Frame is a gain and the fact is
  complete" in `lens.md`.

## 4. Anchoring in presets

- **Mechanism.** The first number seen becomes the reference for what is reasonable.
- **Where it helps.** Preset amounts that match what people typically do (20, 50, 100),
  so the person does not start from a blank field.
- **Where it turns.** A high anchor that makes a big amount look normal, a "from" price
  whose condition sits elsewhere (`A-PRICE-ASTERISK`), presets on a credit amount.
- **Patterns.** forms (amount input), currency-exchange.
- **Forbidden.** Credit (the anchor would say "borrow more"), investment, crypto.
- ✅ Presets 20 €, 50 €, 100 €, with the field free for any amount.
- ❌ Presets 500 €, 1.000 €, 2.000 € on a first transfer. Reason: the anchor is set for the bank.
- **Watched by.** `A-AMOUNT-VALUE`, `A-PRICE-ASTERISK` (code); "Anchor matches the
  person" in `lens.md`.

## 5. Mental accounting

- **Mechanism.** People treat money differently by the label they give it. Money set
  apart for a purpose is money that does not get spent by accident.
- **Where it helps.** Spaces named by purpose, a balance shown as "available" apart from
  what is set aside, a saving goal with a name.
- **Where it turns.** Almost never; the one risk is a label that hides a cost ("your
  rewards balance" that is not money). Vanker names what it is.
- **Patterns.** empty-states, cards, success.
- **Forbidden.** None.
- ✅ Set money aside for what matters most, like a trip or a rainy day.
- ❌ Your Vanker points are waiting for you. Reason: a label for something that is not money.
- **Watched by.** `A-NO-BANNED` (code); "Label names real money" in `lens.md`.

## 6. Positive friction

- **Mechanism.** One extra step slows the fast, automatic decision. Where the action is
  irreversible or expensive, that pause protects.
- **Where it helps.** A confirmation before deleting a Space with money in it, before a
  large transfer to a new payee, before freezing a card. The step names the consequence.
- **Where it turns.** Friction on the way out: cancelling, withdrawing, complaining,
  closing the account. There it is sludge, and Distance Marketing of Financial Services
  (Directive EU 2023/2673) requires the way out to be as easy as the way in.
- **Patterns.** confirmations, cards. (On sign-in the extra step is security, owned by
  `../compliance/security-payments.md`, not a nudge.)
- **Forbidden.** Cancel, withdraw, complain, close: one tap, no extra step, no
  "are you sure" that argues.
- ✅ Delete this Space and move its 340 € to your main account
- ❌ Are you sure you want to give up your savings habit? Reason: the step argues instead of
  naming the consequence.
- **Watched by.** `A-REVERSIBILITY`, `A-DECLINE-PRESENT` (code); "Friction protects, never
  retains" in `lens.md`; asymmetric friction across a flow is documented but not checked.

## 7. Implementation intentions

- **Mechanism.** A plan with a when and a how much gets done far more often than an
  intention without them.
- **Where it helps.** After a first saving, offer a day and an amount ("every 1st, 50 €");
  a reminder that names the moment rather than "remember to save".
- **Where it turns.** A plan the person did not set, a recurring charge dressed as a plan,
  a reminder that repeats after a "Not now" (nagging; documented, not checked).
- **Patterns.** success, notifications, empty-states.
- **Forbidden.** None, as long as the person sets both the day and the amount.
- ✅ Save 50 € on the 1st of every month. You can pause it any time.
- ❌ We have set up monthly saving for you. Reason: the person did not set it.
- **Watched by.** `A-DATE` (code); "The person set the plan" in `lens.md`.

## 8. Peak-end

- **Mechanism.** People remember an experience by its most intense moment and by how it
  ended, not by its average.
- **Where it helps.** A success screen that states the outcome plainly, a complaint closed
  with the resolution and the person's name for it, an error that ends with what happens
  next. The last line is the one that stays.
- **Where it turns.** A celebration that outweighs the action (a shout, an exclamation mark, confetti
  in words), an ending that sells ("now upgrade to Plus") instead of closing.
- **Patterns.** success, welcome-carousel. (Complaints, system errors and loading fix
  their ending by rule in their own files; the reviewer scores them `na`.)
- **Forbidden.** None; the limit is `../voice-and-tone/voice.md`: warm, not loud.
- ✅ Your 250 € transfer to Marta Ruiz has arrived.
- ❌ Transfer sent. Want to send more with Plus? Reason: the ending sells instead of closing.
- **Watched by.** `A-NO-EMOJI`, `A-PUNCTUATION` (code); "The ending closes" in `lens.md`.

## Deliberately left out

- **Loss aversion as a push.** It is `A-GUILT` everywhere except a real security risk,
  where naming the loss is a fact, not a nudge.
- **Endowment.** "Your Space" before the person has one reads as a trial in disguise.
- **Fresh start.** Real, but it is product timing, not copy.
- **Choice overload.** Covered as a design rule in `../patterns/forms.md` and the pattern
  files; not a lens.
- **Scarcity, social proof without a source, fear.** Prohibited in
  `../compliance/dark-patterns.md`.

```json
{
  "biases": [
    { "id": "default-effect", "patterns": ["forms", "notifications", "confirmations", "cards"], "forbidden": ["consents", "credit", "investment", "crypto"], "measure": "default-protects" },
    { "id": "goal-gradient", "patterns": ["flow-intro", "welcome-carousel", "empty-states", "success"], "forbidden": ["kyc", "purchase"], "measure": "progress-real" },
    { "id": "gain-framing", "patterns": ["ctas", "empty-states", "notifications", "emails"], "forbidden": ["risk-warnings", "credit", "investment", "crypto"], "measure": "frame-gain-complete" },
    { "id": "anchoring", "patterns": ["forms", "currency-exchange"], "forbidden": ["credit", "investment", "crypto"], "measure": "anchor-matches-person" },
    { "id": "mental-accounting", "patterns": ["empty-states", "cards", "success"], "forbidden": [], "measure": "label-real-money" },
    { "id": "positive-friction", "patterns": ["confirmations", "cards"], "forbidden": ["cancel", "withdraw", "complain", "close"], "measure": "friction-protects" },
    { "id": "implementation-intentions", "patterns": ["success", "notifications", "empty-states"], "forbidden": [], "measure": "person-set-plan" },
    { "id": "peak-end", "patterns": ["success", "welcome-carousel"], "forbidden": [], "measure": "ending-closes" }
  ],
  "left-out": ["loss-aversion-push", "endowment", "fresh-start", "choice-overload"],
  "neutral-zones": ["investment", "credit", "crypto", "kyc"]
}
```

## Eval hooks

- No bias outside the patterns listed on its card, and none in a neutral zone (reviewer).
- Every consent starts empty; a default favors the person (code: checkbox spec; reviewer).
- A progress statement carries a real step or amount (reviewer).
- A gain frame keeps the disclosure complete (code: `A-NO-CLAIMS`, `A-PRICE-ASTERISK`;
  reviewer).
- A plan names a day and an amount the person chose (reviewer).
- The last line of a success, a complaint answer or an error closes, it does not sell
  (reviewer).
