# Voice

**Status: normative.**

This document defines Vanker's voice: the consistent personality behind every word,
in every surface, at every moment. Voice does not change. How it flexes by situation
is covered in `tone.md`.

Vanker's mission: to put the technological advances that optimize personal finance at
the service of everyone, whatever their age or background.

## Who Vanker sounds like

Vanker sounds like a clever, modern, well-informed friend who happens to be brilliant
with money and genuinely wants to make your life easier. It is fresh and current, but
calm and trustworthy. It explains anything you do not understand without ever making
you feel behind. It is a bank for everyone, so it never excludes anyone with jargon,
hype, or cleverness for its own sake.

Two reference points calibrate the writing: **Apple** (effortless plain-language
clarity, calm confidence, nothing wasted) and **Revolut / N26** (sleek, modern,
tech-premium, precise and minimal).

## The four principles

### 1. Clarity first
Everyone understands Vanker on the first read. Short sentences, one idea at a time,
plain words over financial jargon. When a technical term is unavoidable, explain it in
plain language, and expand every acronym the first time, for example KYC (Know Your
Customer).
- **Do:** "Your card is on its way. It usually arrives in 3 to 5 working days."
- **Not:** "Your card issuance request has been provisioned and is pending fulfillment."

### 2. On your side
Vanker is empathetic and helpful. It reassures before it instructs, never blames the
person, and always makes the next step obvious. Money is emotional; Vanker is calm and
kind about it.
- **Do:** "That payment did not go through. Your money is safe. Let us try again."
- **Not:** "Transaction failed. Invalid input."

### 3. Confidently modern
Vanker is intelligent, current, and comfortable with technology, but it never shows
off. It puts advanced tools in simple words. Smart, not smug.
- **Do:** "We spotted a payment that looks unusual, so we paused it to check with you."
- **Not:** "Our proprietary ML fraud engine flagged an anomalous transaction vector."

### 4. Calm and trustworthy
Vanker's register is composed. It uses natural contractions and avoids hype,
exclamation marks, and pressure. It is a bank: people trust it with their money, and
the tone earns that trust. Personality and light humor appear only in marketing and
promotional copy; everywhere else Vanker is warm but serious.
- **Do:** "You've reached the target for your Travel space."
- **Not:** "WOW! You totally smashed it!!"

## Register (how the words are set)

- **Person:** Vanker speaks as "we". It addresses the person as "you".
- **Contractions:** yes. Natural contractions are part of Vanker's warm, plain voice,
  including negative ones ("don't", "couldn't", "we're", "you'll"), everywhere — not only
  in marketing. The one guardrail: spell out the negative ("do not", "cannot") where a
  misread of the contraction could cause harm, since "don't" can be misread as "do" by
  someone scanning. That is two cases, not a whole register: a **security or safety
  instruction**, and any sentence stating **whether money moved** ("We could not send your
  payment", "We do not know yet whether it went through"). An error is not automatically
  one of them: "This page doesn't exist" and "We couldn't find that transaction" keep the
  contraction. See `../patterns/system-errors.md`.
- **Emoji:** none, with a single exception: 1-2 emoji in the title of a non-critical push
  notification (never in security, fraud, or money-movement push, and never in a body). See
  `../patterns/notifications.md`. The modern feel otherwise comes from clarity and design.
- **Humor:** only in marketing and promotional surfaces, and even there, light and
  occasional. Never in errors, money movement, security, onboarding, or compliance.
- **Reading level:** plain English aimed at roughly CEFR B1 to B2, for a wide audience
  of all ages. Short sentences. One idea per sentence where possible.
- **Acronyms:** expanded on first use, except widely-understood ones (IBAN, PIN, SEPA).
  See `../terminology/glossary.md`.
- **Numbers, money, time:** always concrete and specific ("3 to 5 working days", "a 2 €
  fee"), never vague ("shortly", "a small fee").

## Anti-voice (what Vanker is not)

- Not stuffy or corporate ("Please be advised that...").
- Not slangy or over-familiar ("Heads up, your dough just landed!").
- Not hype or salesy ("revolutionary", "game-changing", "amazing").
- Not cold or robotic ("Error 402.").
- Not condescending ("As you probably already know...").

## Words to avoid

- Hype: revolutionary, amazing, incredible, game-changing, best-in-class, effortless
  (as a claim).
- Jargon without explanation: leverage, utilize, provision, disbursement, remittance.
- Pressure: hurry, last chance, do not miss out, act now.
- Blame: you failed to, you entered the wrong, invalid.
