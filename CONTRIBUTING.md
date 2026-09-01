# Adding a piece to this system

**Status: tooling.** How a new component, pattern, or rule gets written, checked, and
wired in. Every file in this repository follows the shape below; until now that convention
lived only in the files themselves.

Read `CLAUDE.md` first: it is the charter and it wins over everything here.

## 1. Decide where it goes

| It is | It goes in | Test |
| --- | --- | --- |
| One UI element with slots and states | `components/library/` | Can you point at it on a screen? |
| A job that spans surfaces: an error, a flow, a search | `patterns/` | Is it something a person is trying to do? |
| How words, figures, or dates are written | `terminology/` | Does it apply to every string, always? |
| A token: color, type, spacing, motion | `components/foundations/` | Is it a value the design refers to by name? |
| What the regulation requires | `compliance/` | Would a regulator ask for it? |
| How it sounds, and who it addresses | `voice-and-tone/` | Is it about register rather than structure? |

**When two folders could hold it, put it where someone would look for it**, and make the
other one link there. That is how `search.md` ended up owning the placeholder exception
that `forms.md` opened, and how the disabled-field rule ended up in `forms.md` rather than
scattered across the three components that needed it.

**When a name covers two different things, split it.** "Status label / badge / chip" was
one roadmap item and is three files, because a non-interactive label, a count, and an
interactive control share nothing but a rounded shape.

## 2. Write the file

Every file has the same anatomy. The order matters: it is the order someone reads in when
they arrive with a question.

1. **Title and `**Status:**`** — `normative`, `normative (rules) + example (samples)`, or
   `tooling`.
2. **What it is, in two sentences**, and then **the thesis**: the one idea the file exists
   for, stated plainly. `tooltip.md` says a tooltip is the weakest surface in the product.
   `count-badge.md` says a badge is a debt. `search.md` says searching money is not
   searching content. A file without a thesis is a list of preferences.
3. **"What this is not"**, wherever confusion is likely, as a table pointing at the file
   that does own it.
4. **Slots** (a component) or **the situations** (a pattern).
5. **Rules**, numbered, each with its reason (see below).
6. **States, behavior, motion** for a component.
7. **Accessibility**, always its own section, never a footnote.
8. **Content examples**, with ✅ and ❌ and a reason for each ❌.
9. **A machine-readable JSON block**, which is what the agent and the copy checker actually
   consume.
10. **Eval hooks**: the rules restated as things that can be verified.

Cross-references are relative paths in backticks, so they resolve from the file.

## 3. The rule about rules

**Every rule states its reason, inside the rule.**

"No em dashes" is forgettable. "No em dashes: they are hard to read at small sizes, they
are typed inconsistently, and they complicate translation" is arguable, and therefore
usable. This matters more here than in a human style guide: **an agent follows a rule it
understands and improvises around one it does not**, and a reviewer cannot tell whether an
edge case is covered unless the rule says what it is protecting.

Two habits that come from the same idea:

- **Write from the failure.** The best rules in this repository name what goes wrong: a
  push that publishes the balance to anyone looking at the phone, a hyphen between figures
  that reads as a minus sign, a shimmering placeholder amount that resolves into a
  different number.
- **State the tension when there is one.** Where a rule fights another rule, say so and
  resolve it in the file. `ctas.md` does it for specificity against honesty; `date-field.md`
  does it for one field against three.

## 4. Wire it into the evals

For each rule you wrote, decide: **code, judge, or neither.**

- **Code**, if it is black and white and can be checked with a low false-positive rate.
- **Judge**, if it needs reading the situation. It goes in `evals/rubric.md` territory and
  is exercised through `judge.py`.
- **Neither**, if it is real but unenforceable. Say so out loud, in the file and in
  `evals/assertions.md` under the documented-but-not-checked section. Silence is how
  someone comes to believe a rule is covered.

**A noisy check is worse than no check**, because it teaches people to ignore the output.
When a new check fires, sweep the existing candidates before you trust it: three of the
first four warnings `A-CASE` produced were bugs in the check, not in the copy.

Then, mechanically:

1. Add the function to `evals/assertions.py` and register its ID in `REGISTRY`.
2. Add the surface to `SURFACE_CHECKS`, or add the check to `UNIVERSAL` if it applies to
   every string.
3. Add two rows to `evals/assertions.md`: one in the check table, one in the surface table.
4. Add golden cases: **at least one that passes and one that must fail per new rule**, and
   an `expect_judge_fail` case for any rule code cannot see.
5. Run all six: `python run_golden.py`, `python run_golden.py --strict`,
   `python terms_sync.py`, `python check_structure.py`, `python check_examples.py`,
   `python export_rules.py` (then `--check`).
6. **Sweep the existing candidates against the new check**, not only the new cases.
7. Update the folder's `README.md` and the handoff note.

## 5. The traps, all of which we walked into

Each of these was found by accident, and each one now has a tool. Read them before adding a
check.

| Trap | What happened | The tool |
| --- | --- | --- |
| A case only runs the assertions it declares | A tooltip with an unexpanded acronym passed for weeks, because the case never declared `A-ACRONYMS` | `run_golden.py --strict` |
| Surface lists are hand-written | A new check reached only the surfaces someone remembered to update | `UNIVERSAL` in `assertions.py` |
| Substring matching | Adding "ACH" would have flagged "reach" and "each"; "provision" flagged "provisional" | Word-boundary matching |
| The document and the code drift | Fourteen documented terms were never checked; nineteen checked terms were never documented | `terms_sync.py` |
| The runner dropped the surface | Every surface-aware check was being evaluated blind | Fixed in `run_golden.py` |
| The judge marking its own homework | The case's `expected` note is the answer key | `judge.py` never puts it in the prompt |
| A second implementation holds its own copy of the rules | The desktop app's TypeScript linter had the word lists pasted in, so three new rules never reached it and it kept passing "Oooh" and "Cancel or die" | `rules.json` plus `export_rules.py --check` |
| The generator reads the answer key | Three of the four generation cases had their answer written verbatim in the reference the generator receives, so they measured retrieval, not writing | A generation case whose answer is nowhere in the docs (`notification.subscription-price-up`) |
| The generator grades itself | The same model wrote the copy and scored it | Every run file records its model; the generator and the judge are different runs |
| A new rule invalidates old examples | The golden set only holds copy someone chose to put in it, so approved examples in the docs kept contradicting rules written after them | `check_examples.py` |
| A green deterministic run reads as "the copy is good" | Four fields with "Oooh", "Yeah", "Retryyyy" and "Cancel or die" all showed PASS; three were shapes the code should have caught, the fourth needs the judge | `A-REPEATED-CHARS`, the CTA one-action rule, and the honest label in `assertions.md` |

## 6. Checklist

- [ ] It is in the folder someone would look in, and the other candidate links to it.
- [ ] It has a thesis, not a list of preferences.
- [ ] Every rule carries its reason.
- [ ] It has slots or situations, accessibility, examples, a JSON block, and eval hooks.
- [ ] Cross-references resolve.
- [ ] New checks are registered, surfaced, and documented in `assertions.md`.
- [ ] Golden cases: at least one pass and one fail per rule.
- [ ] `run_golden.py`, `run_golden.py --strict` and `terms_sync.py` all clean.
- [ ] `check_structure.py` and `check_examples.py` clean.
- [ ] `export_rules.py` re-run and `--check` clean, so the app's checker gets the new rule.
- [ ] Existing candidates swept against the new checks.
- [ ] Rules you chose not to check are written down as such.
- [ ] The folder README and the handoff note are updated.
