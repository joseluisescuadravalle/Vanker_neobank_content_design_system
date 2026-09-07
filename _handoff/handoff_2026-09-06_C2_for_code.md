# Handoff for Claude Code: port C2 (`A-NEGATION`, clause-scoped) to `src/lib/assertions.ts`

Date: 6 September 2026. The system side of the divergence report is committed in
`Content_Design_System_AI`. This note carries the one change the app must port to keep
parity; everything else in the report (C3, C1) was the app's own and is done (`f988fc7`).

## What changed in `evals/assertions.py`

`spelled_negation` no longer looks for a negative contraction and a money word anywhere in
the slot. It splits the text into **clauses** and fails only when one clause holds both a
negative contraction and a money noun (`MONEY_OUTCOME`) **or** a money-outcome verb
(`MONEY_VERB`, new).

Acceptance (both are golden cases now):

- passes: `We’ve kept your 250 € transfer to Marta Ruiz, so you won’t need to type it again.`
  (`syserr.contraction-other-clause`)
- fails: `Your payment didn’t go through` (`syserr.contraction-money-verb`)
- still fails: `We couldn’t send your payment` (`syserr.contraction-on-money`)
- still passes: `Your phone is blocking access, so we can’t take the photo here.`
  (`perm.denied-body`; generic verbs like take, move, complete are deliberately NOT money verbs)

## The patterns, verbatim from Python (translate flags: all are case-insensitive)

NEG_CONTRACTION (unchanged):
```
\b(?:could|did|has|have|had|is|are|was|were|wo|ca|would|should)n['’]t\b
```
MONEY_OUTCOME (unchanged):
```
\b(payment|transfer|money|funds|paid|charged|sent it|debited)\b
```
MONEY_VERB (new):
```
\b(?:go|went|gone|get|got)\s+through\b|\b(?:send|sent|arrive[sd]?|charge[sd]?|debit(?:ed)?|refund(?:ed)?|receive[sd]?|pay|paid)\b|\bleft\s+your\s+account\b
```
CLAUSE_SPLIT (new):
```
[,;:.!?]|\s+(?:so|but|and|because|if|while|unless|although|once|until|when)\s+
```

## The logic

```
for clause in CLAUSE_SPLIT.split(text):
    m = NEG_CONTRACTION.search(clause)
    if m and (MONEY_OUTCOME.search(clause) or MONEY_VERB.search(clause)):
        fail("negative contraction ('" + m[0] + "') in a clause about money moving; spell it out ('could not', 'did not')")
pass
```

Note for the TypeScript port: `String.prototype.split` with a regex that has no capture
groups behaves like Python's `re.split` here (the separators are dropped). Keep the
apostrophe class `['’]` so curly and straight both match. `rules.json` does not carry these
patterns (they are code-only, listed under `code_only`), so the port is by hand, and the
four cases above are the parity test.

## Also new on the system side (no port needed)

- `patterns/errors.md` rule on merging facts instead of splitting paragraphs or dropping
  facts (C4), referred to from `system-errors.md` rule 9.
- `skill/vanker-content-design/SKILL.md`: same-run editorial review now fills a per-slot
  voice checklist (subject, we/you, passive and nominalization, stakes) with recorded
  answers (C5).
- `evals/worked-cases/`: the session-expired screen with the before/after outputs (C6).

## Second batch, same day: sentence rule inside `A-PARAGRAPHS` (port needed) and two editorial rules (no port)

`A-PARAGRAPHS` now also checks each sentence of each paragraph: fail when a sentence has
more than 25 words, or more than 2 joins, where a join is `,\s+(?:and|so|but)\b|;`
(case-insensitive). The thresholds and the pattern are in `rules.json` under `sentence`,
so read them from there. Message shapes: "paragraph N: a sentence runs to 27 words (max
25); split it, one fact per sentence" and "paragraph N: a sentence chains 4 clauses; a
sentence carries one fact, or two joined once when the slot would otherwise need a fourth
paragraph". One message per paragraph (first offending sentence), same as the Python.

Parity cases (golden): `syserr.two-clause-merge` passes (two clauses, one join, under 25
words); `syserr.three-clause-chain` fails (three joins); `syserr.long-sentence` fails (33
words). `complaint.answer-no` was trimmed from 27 to 22 words to keep passing; the same
copy in `patterns/complaints.md` was trimmed with it.

Editorial, no code: C4 is now an exception, not a principle ("merge two related facts into a
two-clause sentence only when the slot would otherwise need a fourth paragraph"), and the
body never repeats the title; both in `patterns/errors.md`, the second also in the Clarity
row of `evals/rubric.md`. If the app shows rubric text, the Clarity cell changed.

## Correction, 7 September: three clauses fail, and the modal content model

`max_joins` in `rules.json` (`sentence`) is now **1**: a sentence with two joins has three
clauses and fails. Read the value from `rules.json` rather than hardcoding it; the pattern
and `max_words` (25) are unchanged. The negative golden case `syserr.three-clause-chain`
is now José Luis's sentence: "Something did not work on our side when we tried to send
your 150 €, and no money has left your account, so to continue we need you to confirm your
identity." (fails on words and on clauses). `syserr.two-clause-merge` still passes (one
join). Once this is ported and the four sentence cases pass, retire the app's provisional
gate for long sentences: the rule lives in `A-PARAGRAPHS` now.

`patterns/errors.md` has the modal content model rewritten: title = what happened and its
impact, the only required slot; body optional, adds what the title does not say, one fact
per sentence and per paragraph, one to three paragraphs, never repeats the title (Clarity
in the rubric); actions = the exits, at most two. The JSON block under `shapes.modal`
carries it as data if the app renders slot rules.
