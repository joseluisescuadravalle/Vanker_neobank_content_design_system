# The behavioral lens

**Status: tooling + normative (the target behaviors).**

The behavioral lens as a review: what the author declares, what the reviewer scores, and
when it runs. It is the third step of the ladder, after the deterministic checks (correct)
and the editorial review (good): a copy that has not met the rubric is not ready for a
nudge, so the behavioral review unlocks only when the editorial review reports "meets the
rubric".

**The thesis: a nudge is judged against a declared intention, never in the abstract.**
The author states what the screen is for; the reviewer scores whether the copy serves that
behavior with a legitimate bias, and whether it stays out of the forbidden ones. Without
the declaration the review cannot run, and that is deliberate: it makes the intent visible
and reviewable.

## What this is not

| If you are looking for | Go to |
| --- | --- |
| The cards for each bias | `biases.md` |
| The editorial rubric (voice, tone, clarity, ...) | `../evals/rubric.md` |
| The deterministic checks, dark patterns included | `../evals/assertions.md` |
| Which biases a pattern may use | The **Behavioral lens** block in that pattern file |

## Target behaviors

The short list an author picks from. Each pattern's lens block names which of these apply
to it; a pattern that lists none is "does not apply", and the review is skipped.

| Id | Label | What it means | Typical patterns |
| --- | --- | --- | --- |
| `start-saving` | Start saving | Open a first Space or make a first saving | empty-states, success, welcome-carousel |
| `keep-saving` | Keep saving | Set or keep a recurring saving | success, notifications |
| `complete-setup` | Complete a setup | Finish a multi-step setup (alerts, biometrics, a first transfer) | flow-intro, forms |
| `protect-account` | Protect the account | Turn on or keep a protection (alerts, freeze, limits) | notifications, cards, confirmations |
| `confirm-safely` | Confirm safely | Confirm an irreversible or large action with the consequence in view | confirmations, cards |
| `decide-freely` | Decide freely | Accept or decline an offer with the cost in view and the decline at hand | offers |
| `close-well` | Close well | End an action with the outcome stated and nothing sold | success |

The **Label** is the short name an interface shows (two or three words, sentence case, the
id in smaller type beside it); the description is helper text, never the option label. One
allowed behavior is shown as a statement, not as a choice: a control with a single option
is a question with one answer. Two to seven are a radio group, stacked, following
`../patterns/forms.md`; never a dropdown for so few.

## Rubric

Score each measure 0, 1 or 2, or `na` when the declared behavior does not call for it.
The measures are the "watched by" lines of `biases.md`, restated as a scale.

| Measure | 0 | 1 | 2 |
| --- | --- | --- | --- |
| **Serves the declared behavior** | The copy pushes a different behavior (an upsell on a success screen) | Serves it weakly or indirectly | The copy makes the declared behavior the easy, obvious next step |
| **Uses only allowed biases** | A bias the pattern forbids, or any use in a neutral zone | An allowed bias used clumsily | Allowed biases, on the person's side |
| **Default protects the person** | The default favors the product or is a pre-ticked consent | Neutral default where a protective one existed | The default is the protective or free option, and it says so |
| **Progress is real** | Progress claimed with no step or amount behind it | Progress shown vaguely | A real step count or amount left |
| **Frame is a gain and the fact is complete** | Loss frame, or a gain that hides a cost | Gain frame with a weak disclosure | Gain frame with the full fact in the same breath |
| **Anchor matches the person** | Presets set for the bank | Presets plausible but untested | Presets match typical amounts and the field is free |
| **Friction protects, never retains** | A step on the way out, or a step that argues | Consequence named but wordy | One step, the consequence in one line, none on cancel or withdraw |
| **The person set the plan** | A plan or recurrence the person did not choose | Chosen but not both day and amount | Day and amount chosen, pause offered |
| **The ending closes** | The last line sells, celebrates loudly or leaves the outcome unclear | Closes but flat or vague | States the outcome and, where needed, what happens next |

Overall: **pass** when every applicable measure is at least 1, "Uses only allowed biases"
is 2, and the total is at least 85% of the maximum available, the same threshold as the
editorial rubric. "Uses only allowed biases" cannot be 1 on a pass because a forbidden bias
is not a matter of degree.

## Output

The reviewer returns, in this order:

1. The measures with their scores and `na` where they do not apply.
2. The verdict line: `Behavioral lens: pass, N of M applicable, against 85%` or `fail`.
3. **What the behavioral reviewer would change**: judgment, not copy. It names the bias in
   play and the line where it turns, and it never rewrites the string; the rewrite goes
   back through the rules and the editorial review, because any change to the copy
   invalidates both.

## When it runs

- Only after the editorial review reports "meets the rubric". A copy that has not met it
  is reviewed for quality first.
- Only when the author declares a target behavior. No declaration, no review; the panel
  says so.
- Never by default in the Claude skill: the lens is invoked with an explicit ask
  ("apply the behavioral lens", "behavioral review"). The dark-pattern guardrails run
  always, with the other deterministic checks.

## Prompt skeleton

```
You are reviewing a Vanker string with the behavioral lens.
Reference: behavioral/biases.md, behavioral/lens.md, the Behavioral lens block of the
pattern file for this surface, and compliance/dark-patterns.md.
Surface: {surface}. Pattern: {pattern}. Declared target behavior: {behavior}.
Copy: {candidate}
Score each measure of lens.md 0, 1, 2 or na. Then the verdict line. Then "What the
behavioral reviewer would change", as judgment, never as rewritten copy.
```

```json
{
  "behavioral-lens": {
    "unlocks-after": "editorial review meets the rubric",
    "requires": "declared target behavior",
    "target-behaviors": ["start-saving", "keep-saving", "complete-setup", "protect-account", "confirm-safely", "decide-freely", "close-well"],
    "measures": ["serves-declared-behavior", "allowed-biases-only", "default-protects", "progress-real", "frame-gain-complete", "anchor-matches-person", "friction-protects", "person-set-plan", "ending-closes"],
    "pass": { "min-per-measure": 1, "allowed-biases-only": 2, "threshold": 0.85 },
    "output": ["scores", "verdict", "what-the-reviewer-would-change"],
    "rewrites-copy": false,
    "skill-activation": "explicit"
  }
}
```

## Eval hooks

- The review never runs without a declared target behavior (app, skill).
- The review never runs before the editorial review meets the rubric (app).
- "Uses only allowed biases" is 2 on every pass.
- The reviewer output carries no rewritten copy.
