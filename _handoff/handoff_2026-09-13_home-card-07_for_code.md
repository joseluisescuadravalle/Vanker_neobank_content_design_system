# Handoff for Claude Code: home card "07 Behavioral design"

Date: 13 September 2026 (night). The behavioral layer is complete in the system
(`compliance/dark-patterns.md`, `behavioral/`, `patterns/offers.md`, the lens blocks), in
the checker (7 checks, 2 surfaces) and in the Review column (Behavioral review panel).
This note adds the home card that documents it. Follow the existing cards (01 to 05) for
layout, navigation and how a card renders system files; nothing here changes that.

## The card

- Number and title: **07 Behavioral design**. Same style as 01 to 05 (06 stays the pink
  checker card). Card copy, one line: "The persuasion Vanker allows, and the dark patterns
  it never uses." No em dash, no exclamation, sentence case.
- It opens a section with four parts, in this order, each read from the system at request
  time (never pasted into the app):
  1. **The ladder.** Three steps as the system states them: rules (correct), editorial
     review (good), behavioral lens (effective). Source: `behavioral/README.md`, section
     "How the review is ordered", and `behavioral/lens.md`, first paragraph.
  2. **What Vanker never does.** `compliance/dark-patterns.md`: the seven patterns, each
     with its check id. A short line under the heading: "Checked by code on every string."
  3. **What Vanker may use.** `behavioral/biases.md`: the eight cards. Render each card's
     six parts as the file has them; the ✅ and ❌ examples stay visible, they are the point.
     Add the "Deliberately left out" list at the end, it answers the question people ask
     first.
  4. **Where it applies.** A table from the Behavioral lens blocks of `patterns/*.md`:
     pattern, applies or does not, target behaviors, a link to the pattern. Build it at
     request time from the blocks (same parser as the panel). 10 apply, 13 do not.
- A closing line linking to the checker: "Try it: open the Offer (sheet) in the Content
  checker and run the Behavioral review." (a link, named by destination, see
  `patterns/links.md`).

## Copy rules for the app's own strings

The app's interface strings follow the system: no em or en dash, no exclamation mark, no
semicolon, sentence case, acronyms expanded on first use. Run the new strings through the
checker's body checks before committing; the "What the review read" line already had to be
fixed once today for a dash.

## Acceptance

| Case | Expected |
| --- | --- |
| Home | Seven cards; 07 after 05, 06 stays the pink checker |
| 07, part 2 | Seven dark patterns with ids `A-CONFIRMSHAME` to `A-DECLINE-PRESENT` |
| 07, part 3 | Eight bias cards with both examples, then "Deliberately left out" |
| 07, part 4 | 23 rows (10 apply, 13 do not), each linking to its pattern |
| Edit `behavioral/biases.md` in the system, reload | The change shows without a rebuild |

## Out of scope

The `success` surface gap, the in-app notification title surface, "structure" vs "pattern
fit", and the inline lists of the 62 older checks: separate cleanups, not this handoff.
