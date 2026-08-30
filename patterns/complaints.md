# Complaints

**Status: normative (rules) + example (samples).**

How a person tells Vanker that something went wrong, and what Vanker says back.

What the regulation requires is in `../compliance/complaints.md`: the route, the 15
working days for a payment complaint (35 in exceptional cases, with the delay explained),
and the free escalation to the national Alternative Dispute Resolution (ADR) body. This
file is the copy.

## The one flow whose incentives are opposed to the person's

Every other flow in this product wants to be completed. This one, in most companies, is
quietly designed to be abandoned: a chatbot before a human, a help centre in the way, a
form that asks for a category nobody knows, a route that only exists inside an app the
person may be locked out of.

Vanker's position is the opposite, and it is measurable:

> **The complaint flow is judged by how easy it is to complete, never by how few
> complaints it receives.**

`CLAUDE.md` (section 2) already forbids discouraging, dismissing, or obstructing a
complaint. Everything below is what that means in words and screens.

## The route

- **Visible where the reason to complain appears**: a failed payment, a declined
  application, a fee, a closed account, a lock (`system-errors.md`, `auth.md`, `cards.md`).
- **At least one channel that does not need the app.** Someone locked out cannot complain
  in the app, and the lockout may be the complaint. A phone number or an email is part of
  the route, not a fallback.
- **Never a gate.** No chatbot to get past, no "have you checked the help centre?", no
  required sign-in where the sign-in is the problem, no category dropdown before the person
  can write.
- **Free text is accepted as it comes.** If we need a category, we sort it and say we did,
  with a way to correct it — the same rule as an automatic category on a payment
  (`charts.md`). Never make the person translate their problem into our taxonomy.
- Never ask for the story twice. What was said in one channel is carried into the next.

## The acknowledgement

Sent immediately, and it carries three things:

| | Example |
| --- | --- |
| **That we have it, and a reference** | "We have your complaint. Your reference is VNK-4821." |
| **When we will answer**, as a date or a stated limit | "We will answer within 15 working days." |
| **What happens next** | "We may call you if we need more detail." |

- **The reference is given now**, on the screen, not promised in an email that may not
  arrive.
- **The timeframe is stated up front**, not on request (`../compliance/complaints.md`).
- **Never a survey, a rating prompt, or an offer** anywhere in this flow.

## The answer

- **Acknowledge before explaining.** The first line is about what happened to the person,
  not about what Vanker did correctly.
- **Never defend.** No "as per our terms", no "you agreed to", no "unfortunately". A
  complaint answered defensively is a complaint that escalates.
- **Say the outcome plainly**, including when it is no: "We are not refunding this payment,
  and here is why."
- **Give the reason in full**, in plain language, and name the fact it rests on.
- **Never close it silently**, and never let it lapse. If we need longer, we say so before
  the limit, with the new date and the reason
  (`../compliance/complaints.md`: 35 working days in exceptional cases).
- **Name the escalation route in the same message**, especially when the answer is no:
  "If you are not happy with this, you can take it to [ADR body] for free." Burying it is
  forbidden.

## Tone

The person may be frightened, out of money, or right. Often more than one.

- **On their side, even when declining** (`../voice-and-tone/tone.md`).
- **No labels and no moralizing.** A complaint often comes from someone in difficulty or
  who has been defrauded; the rules in `../voice-and-tone/inclusive-language.md` apply
  with their full weight.
- **No apology theatre.** One plain "we got this wrong" is worth more than three
  paragraphs of regret, and an apology for something that was not our fault is not an
  apology, it is noise.
- No jokes, no emoji, no brightness.

## Examples

**Acknowledgement**

> We have your complaint. Your reference is VNK-4821.
>
> We will answer within 15 working days. If we need longer, we will tell you before then
> and explain why.

**An answer that is no**

> We are not refunding the 40 € fee, because it was charged for a same-day transfer you
> confirmed on 2 September.
>
> If you are not happy with this, you can take it to the Alternative Dispute Resolution
> (ADR) body for free, and we will help you do it.

**Not this**

- "Unfortunately, as per our terms and conditions, this fee is non-refundable."
- "Please try our help centre first."
- An acknowledgement with no reference and no date.
- A satisfaction survey after a complaint.

## Machine-readable spec

```json
{
  "complaints": {
    "measured-by": "how easy it is to complete, never how few arrive",
    "route": {
      "visible-where-the-reason-appears": true,
      "channel-outside-the-app": "required",
      "gates": { "chatbot": false, "help-centre-first": false, "sign-in-required": false, "category-before-writing": false },
      "free-text-accepted": true,
      "category-is-ours-to-guess": true,
      "ask-for-the-story-twice": false
    },
    "acknowledgement": {
      "immediate": true,
      "reference-given-on-screen": true,
      "timeframe-stated": "15 working days, 35 in exceptional cases",
      "next-step-stated": true,
      "survey-or-offer": false
    },
    "answer": {
      "acknowledge-before-explaining": true,
      "defensive-language": false,
      "outcome-stated-plainly": true,
      "reason-in-full": true,
      "silent-closure": false,
      "extension-announced-before-the-limit": true,
      "escalation-named-in-the-same-message": "ADR body, free"
    },
    "tone": { "on-their-side-when-declining": true, "labels": false, "apology-theatre": false, "emoji": false }
  }
}
```

## Eval hooks

- The route is reachable without the app and without passing a gate.
- An acknowledgement carries a reference on screen and states when the answer will come.
- No defensive language: "as per our terms", "you agreed to", "unfortunately".
- An answer states the outcome plainly, gives its reason in full, and names the free ADR
  escalation route in the same message, including when the answer is no.
- An extension is announced before the limit, with the new date and the reason.
- No survey, rating prompt, or offer appears anywhere in the flow.
- The person is never asked to categorize their own complaint or to tell the story twice.
