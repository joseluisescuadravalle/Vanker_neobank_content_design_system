# Transactional email

**Status: normative (rules) + example (samples).**

The email Vanker sends because something happened: a payment, a receipt, a security event,
a document. Marketing email is a different thing and is never mixed with this one.

Push notifications are in `notifications.md`; what Vanker never asks for is in
`../compliance/security-payments.md`.

## One event, three surfaces, one truth

A single payment produces a push, an email, and a state inside the app. **They must tell
the same story with the same words**, because the person will see two of them within
seconds of each other and any difference reads as a second event, or as a fake.

| Surface | Payment sent to Luis García |
| --- | --- |
| Push | Title "Payment sent" · Body "150 € is on its way to Luis García." |
| Email | Subject "Payment sent to Luis García" · Preheader "150 €, arriving today" |
| In app | The transaction row, with no status label once it settles |

- **The same amount, in the same format** (`150 €`, never `150,00 €` in one and `150 €` in
  another).
- **The same name for the state**, from the controlled vocabulary in
  `../components/library/status-label.md`. If the app says `Pending`, the email does not
  say "processing".
- **The same counterparty name**, spelled the same way.
- Never send two surfaces that contradict each other on timing ("arriving today" against
  "3 to 5 working days").

## What makes a bank's email different

It is a **permanent record**, it is **forwardable**, and it lands in an inbox where several
convincing fakes of it already exist. Three consequences:

1. **It is the most impersonated object in the person's life.** Everything below about
   phishing follows from that.
2. **It will be read months later**, out of context, possibly by an accountant or a lawyer.
   It must make sense on its own: what happened, when, how much, to whom.
3. **It cannot be edited after sending.** Anything uncertain waits for certainty; there is
   no "we will update this email".

## Anti-phishing rules

These are not tone preferences. They are what lets a person tell our email from a fake.

- **Vanker never asks for a passcode, a PIN, card details, or a one-time code by email**,
  and every transactional email says so in its footer.
- **No link ever leads to a page asking for those.** A link may open the app or a Vanker
  page, and that page never asks for the passcode.
- **No urgency, ever.** "Your account will be closed in 24 hours" is the grammar of fraud.
  If something genuinely has a deadline, state the date plainly and give the real route.
- **Include a detail an attacker does not have**, masked: the person's name and, where it
  helps, the masked identifier (`···· 4321`). Never the full card number, full IBAN, or
  full phone number (see `A-MASK`).
- **The sender is always Vanker**, never a person's name, and the address never changes
  between messages.
- Never attach an executable, never ask the person to enable anything, and send statements
  as an attachment only where that is what the person asked for.

## Structure

- **Subject** (required): the event, front-loaded, about 50 characters. It is read on a lock
  screen, so it follows the same privacy rules as a push title. No emoji in a transactional
  email, no question bait ("Did you make this payment?" as an attention device), no ALL
  CAPS, no "Re:" or "Fwd:" imitation.
- **Preheader** (required): the line the inbox shows after the subject. It **adds
  information, never repeats the subject**, and it is never left to fill itself with "View
  in browser" or the first words of the HTML.
- **Greeting**: "Hi [First name]", falling back to "Hi there"
  (`../terminology/glossary.md`).
- **The fact, first**: what happened, in one sentence, with the amount and the counterparty.
  Everything else is detail below it.
- **Detail block**: the amount, the date and time, the counterparty, the reference, the
  account it came from or went to. Masked where it identifies.
- **One action, one button**, when there is one. Same rules as any CTA (`ctas.md`): the
  label names what happens on tap. Most transactional emails need none.
- **Footer**: how to tell a real Vanker email, the complaints route
  (`../compliance/complaints.md`), and the entity information the regulation requires.

## Transactional or marketing: never both

A receipt is not a promotion. Mixing them makes a message that a person cannot unsubscribe
from carry content they never consented to, which is both a bad experience and a
compliance problem (`../compliance/data-privacy.md`).

| | Transactional | Marketing |
| --- | --- | --- |
| Sent because | Something happened to their money or their account | We have something to say |
| Consent | Not required: it is part of the service | Required, and revocable |
| Unsubscribe link | **No** (you cannot unsubscribe from a receipt) | **Yes**, honoured immediately |
| Promotions inside | **Never** | Yes |
| Timing | Immediately | Never at night, never during a security event |

- Never put an offer, a referral, or a product cross-sell inside a transactional email.
- Never send marketing while a security or fraud message is unresolved.

## Examples

**Payment sent**

- Subject: "Payment sent to Luis García"
- Preheader: "150 €, arriving today"
- First line: "Your payment of 150 € to Luis García is on its way."

**New device logged in** (security)

- Subject: "A new phone logged in to your account"
- Preheader: "Today at 2:32 pm, from Madrid"
- First line: "Someone logged in to your Vanker account from a phone we have not seen
  before."

**Not this**

- Subject: "URGENT: verify your account now" (urgency, and the grammar of fraud)
- Subject: "Did you make this payment? 🤔" (question bait and an emoji in a security email)
- Preheader: "View in browser"
- A receipt with "While you are here, meet our new savings space" at the bottom.

## Machine-readable spec

```json
{
  "transactional-email": {
    "consistency": {
      "one-event-one-truth": true,
      "same-amount-format": true,
      "same-state-vocabulary": "components/library/status-label.md",
      "same-counterparty-name": true,
      "no-contradictory-timing": true
    },
    "anti-phishing": {
      "asks-for-credentials": false,
      "links-to-credential-pages": false,
      "urgency": false,
      "includes-masked-known-detail": true,
      "sender": "Vanker",
      "footer-states-what-we-never-ask": true
    },
    "structure": {
      "subject": { "front-loaded": true, "max-chars": 50, "emoji": false, "question-bait": false, "all-caps": false },
      "preheader": { "required": true, "repeats-subject": false, "max-chars": 90, "auto-filled": false },
      "greeting": "Hi {first_name} / Hi there",
      "first-line": "what happened, with amount and counterparty",
      "detail-block": ["amount", "date and time", "counterparty", "reference", "account"],
      "actions": { "max": 1, "rules": "patterns/ctas.md" },
      "footer": ["how to spot a real email", "complaints route", "entity information"]
    },
    "transactional-vs-marketing": {
      "mixing": false,
      "unsubscribe-in-transactional": false,
      "promotions-in-transactional": false,
      "marketing-during-security-event": false,
      "transactional-timing": "immediately"
    }
  }
}
```

## Eval hooks

- The subject front-loads the event, stays around 50 characters, and carries no emoji, no
  question bait, and no urgency.
- The preheader adds information and never repeats the subject or reads "View in browser".
- No email asks for a passcode, PIN, card details, or a code, and none links to a page that
  would.
- Identifiers are masked; the full card number, IBAN, or phone number never appears.
- The amount, the state vocabulary, the counterparty name, and the timing match the push and
  the in-app state for the same event.
- No transactional email carries a promotion, and no receipt carries an unsubscribe link.
- The footer states how to recognize a real Vanker email and the complaints route.
