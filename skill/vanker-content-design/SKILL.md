---
name: vanker-content-design
description: Write, rewrite, or review any customer-facing copy for Vanker, the fictional euro-area neobank, using its content design system (voice, terminology, patterns, component specs, compliance guardrails) and self-check every string with the system's own deterministic checks before delivering. Use this skill whenever the user asks for UX copy, microcopy, error messages, empty states, notifications, push or email text, onboarding steps, button labels, field labels, tooltips, risk warnings, disclosures, or any string for a Vanker screen, even if they do not say "Vanker content design system" or "on-brand". Also use it to review or fix existing Vanker copy, and to answer "does this string follow the system" questions.
---

# Vanker content design skill

Vanker is a fictional neobank written in English for a euro-area audience. This skill turns
its content design system into working instructions: you write **with** the rules loaded,
then run the same code that would otherwise judge you afterwards. The system lives in
`references/` (a generated copy of the repository) and the checks in `scripts/`.

One idea governs everything here: **a string that passes every check can still be wrong.**
The checks catch shape (a banned word, a misplaced euro sign, an exclamation mark). Only
you catch meaning (a title that says the payment failed above a body that says it is on
its way). Do both, in that order.

## Precedence

When two sources disagree, the higher one wins:

1. `references/CLAUDE.md` (the charter)
2. `references/compliance/`
3. `references/terminology/` (always applied)
4. `references/voice-and-tone/`
5. `references/patterns/`
6. `references/components/`

Examples never override rules. Anything labeled "example" is illustrative.

## The hard rules (always in force)

Never write copy that promises or implies guaranteed returns or a risk-free outcome; uses
urgency, scarcity, or any dark pattern; hides or downplays fees, costs, risks, timing, or
conditions; makes a guarantee Vanker is not authorized to make (deposit protection amounts
included) unless `references/compliance/` states it; asks for or echoes more personal data
than the task needs; discourages a complaint; or presents medical, legal, or tax opinion as
fact.

Always: include the disclosures and risk warnings `references/compliance/` requires for the
surface, in the form it specifies; be explicit about fees and timing wherever they matter;
use the exact controlled terms from `references/terminology/glossary.md`; expand every
acronym on first use ("KYC (Know Your Customer)"); keep every call to action in a button
(body copy never says "Cancel or retry"); one button, one action; keep every input's
visible label (a placeholder never replaces it).

**The safety rule.** If a string touches money, risk, legal terms, deposit protection, or
personal data and `references/compliance/` does not clearly cover it, do not invent the
compliant wording. Mark it `[NEEDS COMPLIANCE REVIEW]` and keep the surrounding copy usable
without it. Omission beats an unverified claim.

## Conventions that apply to every string

These are the rules people get wrong most often. Each is enforced by a check, so a slip
costs you a rerun, not a customer.

- **English text, European figures.** Money: `150 €`, `2.540,75 €`, `10,10 €`. The symbol
  goes after the amount with a space, thousands take a dot, decimals a comma, and a round
  amount has no `,00`. Percentages: `0,5%`, always with what they apply to and over what
  period. An agent that "fixes" these to American convention is introducing a bug.
- **Dates** are day month year, written out: `4 September 2026`. Never numeric, never
  ordinal, never month-first. Only "Today" is relative; anything with a consequence gets an
  absolute date, not "in 3 days".
- **Times** are 12-hour, space, lowercase: `2:32 pm`. Waits are measured ranges in working
  days when a bank being open matters: "3 to 5 working days". Never "soon", "shortly",
  "in a moment".
- **Digits, not words**, for counts and steps: "3 steps", "Step 2 of 3".
- **American English** spelling ("color", "canceled", "email"), with Oxford comma and curly
  quotes.
- **Sentence case everywhere.** Capitalize Vanker, Spaces, and named features; every
  generic banking noun stays lowercase. Never Title Case, never ALL CAPS.
- **Punctuation that never appears:** exclamation marks, semicolons, ellipses, em or en
  dashes, Latin abbreviations ("e.g."), emoji. Ranges take "to", not a hyphen. The minus
  sign is `−`, not a hyphen.
- **Banned vocabulary** (the full list is in `references/terminology/banned-terms.md`): hype
  ("seamless", "amazing"), pressure ("hurry", "last chance"), blame ("you failed to",
  "invalid"), corporate filler ("kindly", "please be advised", "in order to"), vague
  failure ("something went wrong", "oops"), vague waiting ("please wait", "almost there"),
  vague money ("a small fee", "fees may apply"), interjections ("oh", "yeah", "wow"),
  British spellings, and vocabulary from other markets ("checking account", "routing
  number"). No letter repeated three times ("Oooh", "Retryyyy").
- **Calls to action** are verbs, three words at most, no punctuation, no figures, never a
  bare "OK", "Submit", or "Continue" when a specific verb exists ("Send 150 €" belongs in
  the body or the amount, the button says "Send").
- **Contractions are welcome** ("you're", "we'll"), except that a negative about money
  is spelled out: "did not go through", "could not complete", never "didn't" or
  "couldn't" in a sentence about whether money moved, because "don't" misread as "do"
  costs someone money.
- **Color never points at anything** ("the red field"): name the thing. No screen, no
  color, sunlight: the person still needs to find it (WCAG 1.4.1).
- **Never blame, never joke, never exclaim.** Vanker sounds like a calm, well-informed
  friend who is brilliant with money. It reassures, then instructs. Money is emotional;
  the copy is not.

## How to write a screen

1. **Name the screen and its slots.** Every string you deliver has a slot name and a
   surface id, because the checks are surface-aware: a push title is held to different
   rules than a banner body. Pick surface ids from the table in `references/INDEX.md`
   (`cta`, `field-error`, `push-title`, `system-error-screen`, `label-in`, `toast`, and so
   on). If no surface fits, use the closest body surface and say so.
2. **Read the component and the pattern before writing.** `references/INDEX.md` maps each
   surface to the files that own it. Read the component file for the anatomy and the
   slots, and the pattern file for the situation (an error, a wait, a confirmation, a
   permission). Both are short and both carry a thesis in their first lines; do not skip
   them because the task looks familiar. The tone modulation for the moment is in
   `references/voice-and-tone/tone.md`.
3. **Read the compliance file when the string touches its territory.** Money movement,
   fees, or FX: `disclosures.md` and `security-payments.md`. Investment, crypto, credit:
   `risk-warnings.md`. Identity, documents, selfies: `identity-kyc.md`. Personal data,
   permissions, masking: `data-privacy.md`. A complaint or anything a person could
   complain about: `complaints.md`. Screen readers, color, alt text: `accessibility.md`.
   Each file says which surfaces require what, verbatim where the wording is fixed.
4. **Write.** Where the system fixes the wording, use it verbatim. A screen that interrupts
   a money action says one of exactly three things about the money ("No money has left
   your account.", "Your payment is on its way and we will confirm it.", "We do not know
   yet whether it went through, and we will tell you as soon as we do."), and a close
   paraphrase ("Nothing has been charged") fails the check because the person under
   stress should meet the same sentence every time. Disclosures and risk warnings work the
   same way. One string is one complete sentence with named variables inside it
   (`{amount}`, `{date}`); never assemble a sentence from fragments at runtime, because a
   concatenated string is invisible to every check and untranslatable. Say what happened,
   whose side the problem is on, where the money is, and what the person can do now, in
   that order, and stop.
5. **Run the checks** on every slot before showing anything:

   ```bash
   python3 scripts/check_copy.py --surface system-error-title "We could not complete your payment"
   python3 scripts/check_copy.py --file screen.txt
   ```

   `--file` takes the delivery format below and checks each slot against its surface.
   Fix every failure and rerun. Never deliver a string that fails, and never argue with a
   check in the output: if a check is wrong, say so separately, as a finding about the
   system.
6. **Read the screen back as one thing.** This is the step the code cannot do. Read
   title, body, and buttons together, aloud if you can, and ask: does the title agree with
   the body? Is it clear whose fault it is (ours, theirs, the network's)? Is the money
   accounted for (charged, refunded, never left)? Does each button do one thing, and is
   the thing it does the thing the body promised? Would a person who cannot see the
   screen, or who is reading it at a bus stop with 1% battery, know what to do? A screen
   that passes the checks and fails this read-back is not finished.
7. **Get the editorial review.** The read-back is your own; the editorial review is
   someone else's, and the difference is the point. See "Editorial review" below. Copy
   that fails it is fixed and reviewed again, at most twice, before delivery.
8. **Deliver** in the format below, with the review verdict on its last line. Add the
   rules you applied only if the user asks or is learning the system; otherwise the copy
   speaks for itself.

## Editorial review (the judge layer)

The system has two layers of evaluation and this skill carries both. The checks are the
cheap gate: they catch shape and run in a second. The editorial review is the judge of
`evals/`: seven dimensions (voice, tone fit, clarity, terminology, pattern fit, compliance,
accessibility) scored 0 to 2 against `references/evals/rubric.md`, with a pass rule that
does not let compliance or tone fail. It exists because a green run means "no rule
broken", not "the copy is good", and because the person who wrote a screen is the worst
judge of whether it reads as one thing.

The rule the repository lives by: **the writer and the reviewer are not the same run.**
A model that just wrote the copy is not a neutral reviewer of it. So:

1. Build the prompt. It lists the files that govern the surfaces (never the whole system)
   and the copy, and nothing of your reasoning:

   ```bash
   python3 scripts/editorial_review.py --file screen.txt --task "<the request, in one line>" > review-prompt.md
   ```

2. Hand it to a reviewer with a clean context. If you can spawn a subagent (an `Agent` or
   `Task` tool is available), give it only `review-prompt.md` and the path to the skill's
   `references/` folder, and tell it to answer with the JSON and nothing else. Do not give
   it the conversation, your notes, or the checker output. Its verdict is **independent**.
3. If you cannot spawn one, do the review yourself as a separate step: read
   `review-prompt.md` as if you had not written the copy, read the listed files again,
   score strictly, and label the verdict **same run** in the delivery, because the reader
   deserves to know the reviewer was not neutral.
4. Act on the verdict. `pass: false` means the copy goes back to step 4 with the `fix`
   applied, then through the checks again, then through the review again. Two rounds at
   most; if it still fails, deliver the best version and say which dimension failed and
   why, rather than sanding the copy until a reviewer stops objecting.
5. Report it. The last line of the delivery is the verdict, in this form:
   `Editorial review: pass, 13 of 14, independent` or
   `Editorial review: fail, 9 of 12, same run (tone_fit 0: jokey in an error)`.

What the review is not: it is not a second opinion on style. A reviewer that objects to a
sentence the system requires verbatim is wrong, and you say so in the delivery instead of
changing the sentence. And it does not replace the checks: never send it copy the checker
rejected. The cheap gate runs first, always.

## Delivery format

Plain text, one slot per line, `slot (surface): text`. A body that needs more than one
paragraph continues on the following lines until the next slot. This is the format
`scripts/check_copy.py --file` reads, so what you show is exactly what was checked.

```
Screen: payment rejected by the acquirer

title (system-error-title): We could not complete your payment
body (system-error-screen): The card network rejected the payment on our side.

No money has left your account.

Check your card details and try again in a few minutes.
primary (cta): Try again
secondary (cta): Close
```

One fact per paragraph, and a blank line between paragraphs: the checks read the shape of
the block, not only its words.

Mark anything the safety rule caught inline: `[NEEDS COMPLIANCE REVIEW]`. Label a string
as **example** when it is illustrative rather than proposed copy. Close with the verdict
line from the editorial review:

```
Editorial review: pass, 14 of 14, independent
```

## What the checks cannot see (and you must)

The deterministic layer is honest about its limits, and so should you be. A green run
means "no rule broken", not "the copy is good". Things only reading catches:

- A title and a body that contradict each other ("We could not complete your payment"
  above "Your payment is on its way").
- Reassurance that is not true for this situation ("Your money is safe" when it has left).
- A button whose verb does not match what the body says happens next.
- A disclosure that is present but placed where nobody reads it.
- Copy that is correct, compliant, and cold. Vanker is on the person's side; the sentence
  after the bad news says what happens to their money before it says what to do.
- The right pattern in the wrong moment: a first-use empty state ("Set money aside") on a
  screen that is simply empty today ("No statement yet. Your first one arrives on 1
  October").

## Reviewing existing copy

When asked to review rather than write, run the checks first and report failures by check
id with the offending words, then do the read-back and report what the code missed. Offer
the corrected string in the delivery format. Do not soften a failure because the original
author is in the room.

## Files in this skill

- `references/INDEX.md`: surface ids, the checks each surface runs, and the component,
  pattern, and compliance files that own it. Start here for any screen.
- `references/CLAUDE.md`, `terminology/`, `voice-and-tone/`, `compliance/`, `patterns/`,
  `components/library/`: the system, copied verbatim from the repository by
  `evals/build_skill.py`. Do not edit them here; edit the source and rebuild.
- `scripts/check_copy.py`: the deterministic checks (62 as of this build), same code as
  `evals/assertions.py` in the repository, with `rules.json` beside it.
- `scripts/editorial_review.py`: writes the editorial review prompt for a delivery-format
  file, choosing the reference files by surface from `references/owners.json`.
- `references/evals/rubric.md` and `references/evals/judge-prompt.md`: the judge layer,
  copied from the repository.
- `references/MANIFEST.json`: the hash of every copied file, so the repository's seventh
  gate (`build_skill.py --check`) can tell when this skill has drifted from the source.
