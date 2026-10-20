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

## 1. Status quo

- **Mechanism.** People tend not to change what is given to them.
- **Where it helps.** On security alerts on by default, the suggested saving amount already
  included, the safest delivery option already selected. The default option is the one that
  protects the person or the one that avoids costs.
- **Where it turns.** On a pre-ticked consent, a preselected payment plan, the expensive
  delivery set as default. Every consent must be shown without being selected beforehand.
- **Patterns where it applies.** Forms, Notifications, Confirmations, Cards.
- **Forbidden in.** Consents, credit flows, investment and crypto.
- **Watched by.** An automatic check detects double negatives and the reviewer confirms that
  the option selected by default protects the person.
- ✅ Alerts for every card payment are on. You can change this in Settings.
- ❌ Plus is selected for you. Reason: the default selection favors the product, not the
  person.

## 2. Goal gradient

- **Mechanism.** A person keeps their motivation better if they know all the steps of a
  process and where they are in it. Effort rises as the goal gets close.
- **Where it helps.** In examples like "Step 2 of 3", a saving goal with the amount left, an
  onboarding that says how long it takes.
- **Where it turns.** In a fake progress bar, in an "almost there" with no real steps behind
  it, in a countdown.
- **Patterns where it applies.** Flow-intro, Welcome-carousel, Empty-states, Success.
- **Forbidden in.** Identity verification (nothing accelerates KYC, Know Your Customer) and
  anywhere that leads to a purchase.
- **Watched by.** An automatic check detects countdowns and "almost there" phrases with no
  real steps behind them and the reviewer confirms that the progress shown is real.
- ✅ 120 € to go for your trip to Lisbon.
- ❌ You are almost there, do not stop now. Reason: no real distance shown and it pressures.

## 3. Gain framing

- **Mechanism.** The same fact reads differently as a gain or as a loss. People act more
  calmly on gains.
- **Where it helps.** Say what the person gains ("keep 3 € a month") rather than what they
  lose. The fact is the same and the disclosure stays complete.
- **Where it turns.** When the benefit hides a cost, or when it is flipped and the fear of
  losing something is used to push a decision ("Don't lose your rate").
- **Patterns where it applies.** Ctas, Empty-states, Notifications, Emails.
- **Forbidden in.** Risk warnings, credit, investment and crypto (they carry a neutral frame
  by regulation; a gain frame on a risk is a prohibited claim).
- **Watched by.** An automatic check detects fear, guilt and promises a bank cannot keep and
  the reviewer confirms that the benefit hides no cost.
- ✅ Round up your card payments and set the change aside.
- ❌ Stop wasting the change from your card payments. Reason: a loss frame with blame.

## 4. Anchoring effect

- **Mechanism.** The first number seen becomes the reference for what is reasonable.
- **Where it helps.** In preset amounts that match what people typically do, so the person
  does not start from a blank field.
- **Where it turns.** In a high anchor that makes a big amount look normal, in a "from" price
  whose condition sits elsewhere, in presets for a credit amount.
- **Patterns where it applies.** Forms (amount input), Currency-exchange.
- **Forbidden in.** Credit flows (the anchor would say "borrow more"), investment and crypto.
- **Watched by.** An automatic check detects prices with an asterisk or with "from" and no
  condition and the reviewer confirms that the preset amounts match what the person typically
  does.
- ✅ Presets 20 €, 50 € and 100 €, with the field free for any amount.
- ❌ Presets 500 €, 1.000 € and 2.000 € on a first transfer. Reason: the anchor is set for
  the bank.

## 5. Mental accounting

- **Mechanism.** People treat money differently by where it comes from or the label they
  give it. Money set apart for a purpose is money that does not get spent by accident.
- **Where it helps.** By naming each "Space" by its purpose ("Travel", "Emergencies"),
  because money with a destination is harder to spend on something else. And by showing the
  available balance apart from what is saved, so you can see what is spendable without
  touching savings.
- **Where it turns.** Almost never. The risk is putting a money label on something that is
  not money ("your rewards balance"), because it is valued as if it were euros even though it
  cannot be used the same way.
- **Patterns where it applies.** Empty-states, Cards, Success.
- **Forbidden in.** None.
- **Watched by.** An automatic check detects banned vocabulary and the reviewer confirms that
  each label names real money ("Travel", not "your points").
- ✅ Set money aside for what matters most to you, like a trip or a rainy day.
- ❌ Your Vanker points are waiting for you. Reason: a label for something that is not money.

## 6. Positive friction

- **Mechanism.** One extra step slows a fast, automatic decision. Where the action is
  irreversible or expensive, that pause protects.
- **Where it helps.** In a confirmation before deleting a Space with money in it, before a
  large transfer to a new payee, before reporting a lost card.
- **Where it turns.** When the extra step is on the way out: cancelling, withdrawing,
  complaining or closing the account. There it no longer protects the person, it retains
  them. On top of that, Distance Marketing of Financial Services (Law 22/2007 and Directive
  EU 2023/2673) requires the way out to be as easy as the way in.
- **Patterns where it applies.** Confirmations, Cards.
- **Forbidden in.** Cancel, withdraw, complain, close actions… There a single click must
  exist, with no extra step, no "are you sure…?" that argues.
- **Watched by.** An automatic check confirms that every irreversible action says so and that
  there is always a way to decline. The reviewer confirms that no extra step slows the way
  out. That cancelling has more steps than signing up is documented, but not checked.
- ✅ Delete this Space and move its 340 € to your main account
- ❌ To cancel Plus, answer this survey first. Reason: a mandatory step on the way out that
  does not protect the person, it only retains them.

## 7. Implementation intentions

- **Mechanism.** A plan with a clear "when" and "how much" gets done far more often than a
  simple intention.
- **Where it helps.** After a first saving, by proposing that the person choose a day and an
  amount to keep saving ("50 € on the 1st of every month"). And in reminders, which name the
  specific moment ("Today is the 1st. Time to move 50 € to Travel") instead of a generic
  "Remember to save".
- **Where it turns.** In a plan the person did not set, in a recurring charge dressed as a
  plan, in a reminder that repeats after a "Not now".
- **Patterns where it applies.** Success, Notifications, Empty-states.
- **Forbidden in.** None, as long as the person sets both the day and the amount.
- **Watched by.** An automatic check reviews the date format and the reviewer confirms that
  the day and the amount were chosen by the person.
- ✅ Save 50 € on the 1st of every month. You can pause it any time.
- ❌ We have set up monthly saving for you. Reason: the person did not set it.

## 8. Peak-end

- **Mechanism.** People remember an experience by its most intense moment and by how it
  ended.
- **Where it helps.** In a success screen that explains the outcome clearly and usefully, in
  a complaint closed with the resolution and the name the person gave it, in an error message
  that ends by stating what happens next.
- **Where it turns.** In a celebration that outweighs the action (a shout, an exclamation
  mark, confetti in words), in an ending that sells ("now upgrade to Plus") instead of
  closing.
- **Patterns where it applies.** Success, Welcome-carousel.
- **Forbidden in.** None. The limit is the brand voice (clear, modern, calm, always on your
  side).
- **Watched by.** An automatic check detects emojis and exclamation marks and the reviewer
  confirms that the last line closes the action instead of selling.
- ✅ Your 250 € transfer to Marta Ruiz has arrived.
- ❌ Transfer sent. Want to send more with Plus? Reason: the ending pushes to keep acting
  instead of closing.

## Deliberately left out

- **Loss aversion as a push.** The system forbids it and detects it on every screen, except
  when there is a real security risk: there, saying what can be lost is informing, not
  pushing.
- **Endowment.** "Your Space" before the person has one reads as a trial in disguise.
- **Fresh start (fresh start effect).** People are more motivated to start something on dates
  that mark a new beginning: a Monday, the 1st, New Year. It works, but it depends on when a
  proposal is shown. That is decided by the product, not the copy.
- **Choice overload.** Covered as a design rule in forms and the pattern files. Not a lens.
- **Scarcity, social proof without a source, fear.** They are prohibited dark patterns.

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
