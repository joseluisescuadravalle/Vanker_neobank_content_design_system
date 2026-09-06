# Worked case: session expired while a transfer was being typed

**Status: tooling.** The screen behind the divergence report of 6 September 2026 (C1 to
C6), kept here so the three behaviors it exposed can be re-run in one command each. Run
from this folder with the skill's checker, which is the same code as `../assertions.py`:

```bash
python3 ../../skill/vanker-content-design/scripts/check_copy.py --file a-correct.txt
python3 ../../skill/vanker-content-design/scripts/check_copy.py --file c-title-in-body.txt
```

## a-correct.txt: the right screen passes

Title states the fact; body says why, what happened to the money with the fixed sentence,
and that the draft is kept; one action. Before C2 the body failed `A-NEGATION` on
"won't", because the check looked for a contraction and a money word anywhere in the
slot, and "transfer" was in the same sentence. After C2 the check is scoped to the
clause and the clause must carry a money noun or a money-outcome verb: "so you won't need
to type it again" has neither.

```
Before C2:  body (system-error-screen)    FAIL  1 of 20 checks
                A-NEGATION: negative contraction ('won’t') in a sentence about money
After C2:   body (system-error-screen)    ok    20 checks
            No rule broken (3 slots). Meaning not evaluated: read the screen back before delivering.
```

The two sentences that define the boundary are golden cases now:
`syserr.contraction-other-clause` (passes) and `syserr.contraction-money-verb` ("Your
payment didn't go through", must fail).

## c-title-in-body.txt: the title pasted into the body fails on shape

Same copy, with the title repeated as the first sentence of the body. `A-PARAGRAPHS` fails
because paragraph 1 now stacks three facts. This is the C3 lesson for the desktop app: the
check runs on the body slot alone, never on title plus body joined, or every screen would
fail for the wrong reason.

```
body (system-error-screen)    FAIL  1 of 20 checks
    A-PARAGRAPHS: paragraph 1 stacks 3 facts into one block; give each its own paragraph
```

## What the checker does not see here (C4, C5)

The correct screen has four facts (signed out, why, money, draft kept) in a two-paragraph
body: the second paragraph joins two facts with "and" instead of adding a third paragraph
or dropping one. That merge is the editorial rule added in `../../patterns/errors.md`
(Rules) and referred to from `system-errors.md` rule 9, and the voice checklist that a
same-run editorial review must fill (`SKILL.md`, Editorial review, step 3) is what would
catch a body that hides the actor ("access was blocked") where this one says "we signed
you out".
