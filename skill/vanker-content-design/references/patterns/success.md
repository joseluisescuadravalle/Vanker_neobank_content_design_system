# Success messages

**Status: normative (rules) + example (samples).**

A success message confirms that an action the person took **just completed**. It has two
homes, and it is **never a banner**: a persistent status like "Your card is on its way" is
informational (an info banner), not a success.

## Which one

- **Toast** (default): routine, in-flow successes where the person stays where they are
  ("Payment sent", "Space created", "Card frozen", "Changes saved"). Transient. See the toast
  structure in `../components/library/banner-toast.md`.
- **Full-screen success**: the end of an important flow, when the person needs a next
  destination (account signup, identity verified, application submitted, onboarding done).

**Decision:** does the flow end (or is it high-significance) and the person needs somewhere to
go next? Full-screen success. Otherwise, a toast.

## Full-screen success: content structure

### Slots

- **Success mark** (required): a green tick (the success semantic icon). Icon and text carry
  the meaning, never color alone.
- **Title** (required): confirms the completed action, calm and contained (not fireworks),
  **no ending period** ("Your account is ready").
- **Body** (optional): complementary information. If it adds nothing, leave it out.
- **Continue** (optional): a short heading ("How would you like to continue?") and **2 to 4
  next-step options**. They are a menu of next steps, not a primary/secondary decision: the
  most likely next step is the **primary**, the rest are lower emphasis. Each option is a CTA
  of 3 words maximum, verb first ("View my accounts", "Explore products", "Send money").

### Rules

- Contained celebration (see `../voice-and-tone/tone.md`). No emoji (the tick is a drawn icon).
- Exactly one primary among the continue options; the others are lower emphasis.

### Machine-readable spec

```json
{
  "success": {
    "surface-by-stakes": { "routine-in-flow": "toast", "end-of-an-important-flow": "full screen" },
    "toast": { "tense": "past", "ending-period": false, "max-chars": 50 },
    "full-screen": {
      "mark": { "icon": true, "color-alone": false },
      "title": { "confirms-the-action": true, "ending-period": false, "celebration": "restrained" },
      "body": { "optional": true, "omit-if-empty": true },
      "continue": { "options": [2, 4], "each-a-cta": true }
    },
    "confetti-on-money": false,
    "never-before-confirmed": true
  }
}
```

## Behavioral lens

- **Applies.** Target behaviors: `close-well` (every success) and, on a first saving or a
  completed setup, `keep-saving` or `protect-account` through the continue options.
- **Biases allowed.** Peak-end (the title states the outcome; the last line closes),
  implementation intentions as a continue option the person sets ("Save 50 € every 1st"),
  goal gradient when a goal exists ("120 € to go"), mental accounting.
- **Biases forbidden here.** Anything that sells: no offer, no upgrade, no partner product
  on a success screen (`offers.md`, rule 3). No loud celebration (voice). No plan set for
  the person.
- **What the reviewer scores.** "Serves the declared behavior", "Uses only allowed biases",
  "The ending closes", "The person set the plan" when a plan is offered, "Progress is real"
  when progress is shown. The rest `na`.

See `../behavioral/biases.md` for the cards and `../behavioral/lens.md` for the rubric.

## Eval hooks

- Title has no ending period.
- Continue options are CTAs (verb, 3 words max); exactly one is primary.
- No emoji.
