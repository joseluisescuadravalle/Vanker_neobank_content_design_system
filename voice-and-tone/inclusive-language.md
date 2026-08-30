# Inclusive language

**Status: normative. Always applied.**

Who Vanker is talking to, and how it avoids deciding who they are. `voice.md` is how the
brand sounds; this is who it sounds like it is talking to.

## The rule the rest of the file applies

**Describe the situation, never label the person.**

A bank labels people more than almost any other product does, and its labels stick. "This
payment was returned" describes something that happened; "you are a defaulter" describes a
person, in a message they did not ask for, about the part of their life they are least in
control of. The first is a fact the person can act on. The second is a verdict.

The test: if the sentence turns a circumstance into an identity, rewrite it.

## Money difficulty

This is where a bank does the most damage with the fewest words, and it is the reason this
file exists.

- **No labels for people in difficulty.** Not "defaulter", "delinquent", "bad credit",
  "risky customer", "the unbanked", "the poor". Name the event: "This direct debit was
  returned", "Your balance is below zero".
- **Never moralize.** Not "you overspent", not "you failed to pay", not "unfortunately you
  did not keep enough in your account". State what happened and what can be done.
- **Never assume the reason.** Someone whose payment failed may be between jobs, may have
  been defrauded, may have moved money on purpose. We do not know, and a message that
  guesses is wrong in the cases that matter most.
- **Do not give financial advice.** A bank telling someone to "try budgeting" inside an
  error message is condescending and outside what it can know. Offer the real options: a
  payment plan, the channel to talk to a person, the deadline that actually applies.
- **No praise and no shame for money behaviour.** "Great job saving!" reads as a
  congratulation to some and a taunt to someone who could not. Report, do not grade.
- **No comparison with other people.** "You saved more than 60% of customers" is a
  compliment at the top and a judgement at the bottom, on something nobody chose to enter.
- **No celebration on hardship screens.** No confetti, no streaks, no gamification anywhere
  near arrears, overdrafts, or a failed payment.
- **Vulnerability changes the flow, never the label.** If a person tells us they are in
  difficulty, the product adapts what it offers. It never displays that back to them as a
  status, and it never repeats it in a later screen where someone else might see it.
- **No fear and no threats.** Consequences are stated only when they are certain, with
  their date (see `../terminology/banned-terms.md` on pressure).

## Gender

- **Never assume gender**, from a name, a title, an account, or a product. No "Mr" or "Mrs"
  unless the person gave it.
- **Singular "they"** for a person whose gender we do not know. Never "he/she", never
  "(s)he", never "he" as a default.
- **No gendered role words**: spokesperson, salesperson, businessperson, workforce. Not
  spokesman, salesman, businessman, manpower.
- **No gendered relationship assumptions**: "your partner", not "your husband" or "your
  wife". A joint account is two people, not a couple.
- Ask for gender only where the law requires it, and say why on the screen that asks.

## Family and household

- **Never assume a family shape.** Not "your family", "your children", "your household"
  unless the person told us. A savings space is not a wedding fund.
- **No "head of household" or "main earner"** unless it is a legal term, used with its
  definition.
- Life events are offered, never assumed: the copy does not congratulate anyone on
  something it inferred.

## Age

- **Age is a figure when a rule needs it, and irrelevant otherwise.** Not "elderly", not
  "seniors", not "the young".
- **Never tie ability to age.** No "simple enough for your grandmother", no "for
  digital natives".

## Disability and health

- **A bank rarely has any reason to mention it.** Where an accessibility feature exists,
  name the feature, not the person: "Larger text", never "For visually impaired users".
- **Never "suffers from", "confined to", "wheelchair-bound", "special needs"**, and never
  "normal users" as the other side of the comparison.
- **No disability as metaphor**: not "blind spot", "tone deaf", "crazy", "insane", "lame",
  "dumb", "paralysed".
- Health information a person gives us is used for the flow that needs it and never
  restated (see `../compliance/data-privacy.md`).

## Origin, name, and status

- **A name or an address is never treated as suspicious in copy.** Identity checks are
  factual and identical for everyone (see `../compliance/identity-kyc.md`).
- **Never "foreign", "alien", or "non-national"** as a description of a person. Where a
  rule depends on residence or nationality, name the rule.
- Names are not "normal" or "strange". Fields accept accents, apostrophes, and any length,
  and the copy never apologizes for them.

## Words with a history

- **"blocked list" and "allowed list"**, never blacklist and whitelist.
- Never "master" and "slave" for anything.
- Never "grandfathered"; say "kept on the old terms".

## Idioms

Idioms exclude anyone who did not grow up with them, and they are the first thing to break
in translation: "ballpark figure", "piece of cake", "touch base". Plain words say the same
thing to more people.

## Eval hooks

- No copy labels a person by their money situation; the event is described instead.
- No moralizing, no financial advice, no praise or shame, and no comparison with other
  customers.
- No gender assumed; singular "they" for an unknown person; no gendered role words.
- No family shape, age, or ability assumed.
- No disability used as a metaphor, and no "normal users".
- "blocked list" and "allowed list", never blacklist and whitelist.
- No idioms.
