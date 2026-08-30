# Currency exchange

**Status: normative (rules) + example (samples).**

Sending money in another currency, converting between currencies, and paying with the card
abroad.

What the regulation requires is in `../compliance/disclosures.md` (the markup over the
European Central Bank (ECB) reference rate, under the Cross-border Payments Regulation);
this file is what the screens say.

## The price is not the fee. It is inside the rate

Everywhere else in this product, a cost is a fee: an amount, stated exactly, before the
person commits. Here the cost can be hidden inside a number that looks like a fact about
the world. A rate of `1 € = 1,0745 USD` reads as the price of the dollar, not as our
margin, and nobody converts a spread into euros in their head.

So this pattern has one job:

> **Make the cost visible as a cost, in euros, next to the rate that produced it.**

## Before confirming, three things, always

Not one of them replaces another:

| | Example |
| --- | --- |
| **The rate we are using** | "1 € = 1,0745 USD" |
| **The markup over the ECB reference rate** | "Our markup: 0,5% over the ECB rate" |
| **What it costs, in euros** | "This conversion costs you 0,54 €" |

- **A rate alone is not a disclosure.** A screen showing only the rate has told the person
  nothing they can act on.
- **A transfer fee, where there is one, is separate** and stated exactly. Never folded into
  the conversion so the total looks like one number.
- **"0% commission" is banned when the cost is in the spread.** So are "no commission",
  "commission-free", and "no hidden fees" as a claim. Hiding a cost inside a rate and then
  advertising the absence of a fee is the dark pattern this file exists to prevent, and
  `CLAUDE.md` (section 2) already forbids it.

## Both sides of the exchange

- **Show what is sent and what arrives**: "You send 100 €" and "Ana receives 107,45 USD".
- **Say when the received amount is an estimate, and why.** Where an intermediary or the
  receiving bank can deduct, the final amount is not ours to promise: "Ana receives about
  107,45 USD. Their bank may deduct a fee we cannot see."
- **Never present an estimate as exact**, and never promise a credited amount we do not
  control (see `../compliance/principles.md`).
- Foreign amounts carry their currency code after the figure ("107,45 USD"), with the same
  separators as the euro format (`../terminology/numbers-and-dates.md`). The currency is
  named in full on first mention where it may be unfamiliar.

## The rate expires

- **Say how long the rate holds**, plainly: "This rate holds for 60 seconds."
- **Never a countdown that pressures.** It is a fact about the quote, not a reason to hurry
  (`../terminology/banned-terms.md`).
- **Never requote silently.** If the rate moves before confirmation, stop, show the new
  rate and the difference, and ask again. A payment that goes out at a rate the person
  never saw is the worst outcome this flow can produce.
- After it lapses, the copy says what happened and offers a fresh quote; it does not simply
  refresh the number under the person's finger.

## Markets close

- **Say when a conversion will not happen now.** Currency markets are closed at weekends
  and on some holidays: "Currency markets are closed until Monday, so this will convert on
  6 September."
- Where a weekend rate carries a wider margin, say that **before** the person commits, not
  in the receipt.
- The date rules apply: a concrete date, never "later" (`../terminology/numbers-and-dates.md`).

## Card payments abroad

- The conversion happens when the payment settles, so the amount can differ from the one
  shown at the terminal. Say so where the person will see both: "Converted when the payment
  settled, at 1 € = 1,0745 USD."
- Where the merchant offered to convert instead (dynamic currency conversion), the copy
  names it plainly and states that paying in the local currency is usually cheaper. This is
  information, not advice about their money.

## Examples

**Before confirming**

> You send 100 €
>
> Ana receives about 107,45 USD
>
> 1 € = 1,0745 USD. Our markup: 0,5% over the ECB rate.
>
> This conversion costs you 0,54 €. Their bank may deduct a fee we cannot see.

**Not this**

- "1 € = 1,0745 USD" alone.
- "0% commission on your first transfer."
- "Ana receives 107,45 USD" where an intermediary can deduct.
- A rate that refreshes under the person's finger.

## Machine-readable spec

```json
{
  "currency-exchange": {
    "thesis": "the cost is inside the rate; make it visible as a cost, in euros",
    "before-confirming": ["rate used", "markup over the ECB reference rate", "cost in euros"],
    "rate-alone-is-not-a-disclosure": true,
    "transfer-fee": "separate and exact",
    "banned-claims": ["0% commission", "no commission", "commission-free", "no hidden fees"],
    "both-sides": { "sent": true, "received": true, "estimate-stated": true, "promise-credited-amount": false },
    "foreign-amount": { "code-after-figure": true, "separators": "as the euro format", "named-on-first-mention": true },
    "quote": { "validity-stated": true, "pressuring-countdown": false, "silent-requote": false, "on-lapse": "say so and offer a fresh quote" },
    "markets-closed": { "stated-before-committing": true, "concrete-date": true, "wider-weekend-margin-stated": true },
    "card-abroad": { "converted-at-settlement-stated": true, "dynamic-currency-conversion-named": true }
  }
}
```

## Eval hooks

- A screen showing a rate also shows the markup over the ECB reference rate and the cost in
  euros; a rate alone fails.
- "0% commission", "no commission", "commission-free" and "no hidden fees" fail wherever the
  cost sits in the spread.
- Both sides of the exchange are shown, and a received amount that depends on an
  intermediary is stated as an estimate with the reason.
- The quote's validity is stated as a fact, never as a countdown that pressures, and the
  rate is never requoted silently.
- A conversion that cannot happen now says when it will, with a concrete date.
- A card payment abroad says the conversion happened at settlement and at what rate.
