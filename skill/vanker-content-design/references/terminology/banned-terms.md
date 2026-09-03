# Banned terms

**Status: normative. Always applied.**

Words and phrases Vanker does not use, with what to use instead and why. This
formalizes the "words to avoid" in `../voice-and-tone/voice.md` and adds
terminology-level rules. It is written to be checkable, so these can become automated
assertions in `../evals/`.

## Hype and marketing inflation

| Avoid | Use instead | Why |
| --- | --- | --- |
| revolutionary, game-changing, incredible, amazing | describe the concrete benefit | Vanker earns trust with clarity, not hype. |
| best-in-class, world-class, cutting-edge | say what it actually does | Empty claims. |
| seamless, effortless (as a claim) | show it is simple, do not assert it | Overused and often untrue. |

## Pressure

| Avoid | Use instead | Why |
| --- | --- | --- |
| hurry, act now, last chance, do not miss out | a plain, honest deadline if one truly exists | Vanker never pressures a money decision. |
| urgent, final notice | state the date plainly and give the real route | Urgency is the grammar of fraud, and a bank that uses it teaches people to trust the fakes. See `../patterns/emails.md`. |

## Blame

| Avoid | Use instead | Why |
| --- | --- | --- |
| you failed to, you entered the wrong, you forgot to, invalid | neutral phrasing ("that did not work", "that code was not right") | Never blame the person. |

## Jargon and corporate filler

| Avoid | Use instead | Why |
| --- | --- | --- |
| utilize | use | Plainer. |
| leverage (as a verb) | use, make the most of | Corporate jargon. |
| provision, disbursement, remittance | plain equivalents (set up, payment, transfer) | Excludes non-experts. |
| OTP, one-time password, token | code, verification code | Nobody outside the industry calls it that. See `../components/library/code-input.md`. |
| please be advised, kindly, at your earliest convenience | plain, direct wording | Stuffy and cold. |
| in order to | to | Wordy. |

## Vague where the person needs a fact

Added by the patterns; each replaces something the person actually needs.

| Avoid | Use instead | Why |
| --- | --- | --- |
| something went wrong, oops, unexpected error, technical difficulties | say what happened and whose side it is on | We almost always know more than that. See `../patterns/system-errors.md`. |
| please wait, almost there, just a moment, hang tight, working on it | say what is happening ("Checking your details") | Asking for patience instead of giving information. See `../patterns/loading.md`. |
| a small fee, low fees, fees may apply | the exact amount, or "free" | A fee is exact or the service is free. See `../compliance/disclosures.md`. |

## Claims a regulated bank cannot evidence

| Avoid | Use instead | Why |
| --- | --- | --- |
| the best, the cheapest, the fastest | say what it actually does | Unevidenced superlatives, and the highest-exposure copy in the app is the pre-login carousel. See `../patterns/welcome-carousel.md`. |
| free forever, no strings attached | state the condition, or do not say it | A bare free claim is a hidden condition. |

## Spelling and formatting (American English)

| Avoid | Use instead | Why |
| --- | --- | --- |
| optimise, colour, personalise, cancelled | optimize, color, personalize, canceled | American spelling baseline. |
| e-mail | email | |
| login / log-in (as a verb) | log in (verb); login only as a noun | |
| & in body copy | and | Ampersand only in tight labels. |

## Vocabulary that does not fit the market

| Avoid | Use instead | Why |
| --- | --- | --- |
| checking account | current account | Vanker is a euro-area bank. |
| routing number, ACH, sort code | IBAN, SEPA | Wrong market. |

## Noises

An interjection is a sound, not information. It adds nothing a person can act on, and in a
screen about money it reads as a nervous laugh: the copy sounds like it is apologizing for
news it has not yet given. A written-out noise also breaks every downstream surface (a
screen reader says it out loud, a translator has nothing to translate, a subject line wastes
its first characters on it).

| Avoid | Use instead | Why |
| --- | --- | --- |
| oh, ooh, aah, ugh, huh, aha, phew, yikes | nothing, or the fact itself | Filler dressed as empathy. Say what happened. |
| yeah, yay, wow, hey, woohoo, hurray, hooray | plain confirmation ("Money sent") | Enthusiasm the person does not share, in a product that holds their salary. |

A letter repeated three times or more ("Oooh", "Retryyyy") is checked separately by
`A-REPEATED-CHARS`, because it is a shape rather than a word: it catches both the noise and
the typo, including ones nobody thought to list.

## Always

- Expand every acronym on first use (see `glossary.md`).
- Never use emoji (see `../voice-and-tone/voice.md`).

## Not in this file

Inclusive language has its own file and its own check: see
`../voice-and-tone/inclusive-language.md` and `A-INCLUSIVE`. It is kept separate because
each of its terms carries a replacement and a reason that belong with the rule, not in a
flat list of words to avoid.

## Keeping this file and the checks in sync

This file is the source of truth; `../evals/assertions.py` implements it. They drifted twice
without anyone noticing, in both directions: rules documented here that were never checked,
and terms added by a pattern that were never written down here.

`python terms_sync.py` (from `../evals/`) compares the two and fails on any difference. Run
it whenever either file changes.

Three rules here cannot be a word in a list, so the checker implements them with their own
logic and the sync script knows to skip them:

| Rule | How it is checked |
| --- | --- |
| login / log-in as a verb | A pattern around the word, since "login" is legitimate as a noun |
| `&` in body copy | Surface-aware: allowed in a tight label, never in body copy |
| Acronym expansion | `A-ACRONYMS`, its own check |
| A letter repeated 3+ times | `A-REPEATED-CHARS`, a shape not a word. Format placeholders (`DD/MM/YYYY`), hex colors and URLs are exempt by shape |
| One button, one action | `A-CTA` rejects `or`, `and` and `then` in a label |
