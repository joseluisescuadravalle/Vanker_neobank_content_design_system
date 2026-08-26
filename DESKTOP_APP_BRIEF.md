# Vanker Content Design System — Desktop App: Kickoff Brief

This document is the handoff to start building a **desktop app** (in Claude Code) that
makes the Vanker content design system usable by different stakeholders on a product
design team. Drop it into the new project as context, and drive the build yourself.

---

## 1. Context: what the system is

**Vanker** is a fictional euro-area neobank. Its **content design system** is a repository
written so that both people and an AI agent can use it to produce the whole digital
experience, on-brand and compliant.

- Repo: `https://github.com/joseluisescuadravalle/Vanker_neobank_content_design_system`
- The system is the **source of truth**. This app is a **client** over it: it reads the
  repo, it does not duplicate its rules.

Brand in one line: graphite `#111827` + fuchsia `#DB2777`; Plus Jakarta Sans (product) and
Space Grotesk (marketing); flat, rounded (12px), calm motion; English copy, euro-area
money format (`150 €`, `2.540,75 €`).

## 2. What is in the repo (the app's data)

| Folder | Holds | The app consumes it for |
| --- | --- | --- |
| `README.md`, `CLAUDE.md`, `DISCLAIMER.md` | Charter and hard rules | Orientation; `CLAUDE.md` is the system prompt for any generator |
| `voice-and-tone/` | `voice.md`, `tone.md` | Reference; generator context |
| `terminology/` | `glossary.md`, `banned-terms.md` | Reference; the linter's word lists |
| `patterns/` | ctas, errors, confirmations, empty-states, notifications | Reference; each ends in **Eval hooks** |
| `components/foundations/` | color, typography, shape, spacing, elevation, iconography, motion | Each has a **machine-readable JSON token block** — the design tokens |
| `components/library/` | 9 components (button, text-field, card, transaction-row, navigation, sheet-modal, banner-toast, empty-state, onboarding-step) | Each has a JSON spec + accessibility + eval hooks |
| `compliance/` | framework + 9 guardrail files | Reference; regulatory checks |
| `evals/` | `assertions.py`, `assertions.md`, `golden-set/cases.jsonl`, `run_golden.py`, `rubric.md`, `judge-prompt.md` | The **linter engine** and the test data |

**Key reusable assets:**
- The **JSON token blocks** in `components/foundations/*.md` (fenced ```json). Parse these
  to power a token viewer / export.
- `evals/assertions.py` — deterministic content checks (no emoji, euro format, banned
  terms, prohibited claims, acronym expansion, CTA rules). This is the linter's logic.
- `evals/golden-set/cases.jsonl` — labeled test cases, including a negative case.
- The **Eval hooks** blocks across patterns/components/compliance — the human-readable
  rules behind the checks.

## 3. Who the app is for (stakeholders and jobs)

- **Content designer** — "When I write copy for a screen, I want the right pattern and a
  way to check my draft, so it is on-brand and compliant without memorizing everything."
- **Product designer** — "When I build a screen, I want the tokens and the component
  content specs, so design and copy match the system."
- **Engineer** — "When I implement, I want the design tokens as JSON/CSS, so I do not
  hardcode values."
- **PM / stakeholder** — "When I review, I want to see the voice and real examples, so I
  can judge whether copy is on-brand."
- **Legal / compliance** — "When I review copy, I want the regulatory guardrails and to
  flag gaps."

## 4. What the app does (features)

1. **Reference browser** — navigable, searchable view of the whole system (voice, tone,
   terminology, patterns, components, compliance). Everyone.
2. **Copy checker (linter)** — paste a string, pick a surface, run the assertions, get
   pass/fail with the reason and a fix. Content designers. *(Reuses `assertions.py`.)*
3. **Token viewer / export** — render the design tokens; copy as JSON or CSS variables.
   Designers and engineers.
4. **Copy generator** — pick a surface + context, generate on-brand, compliant copy using
   `CLAUDE.md` + the relevant files as context (needs a model API key). Content designers.
5. **Evals dashboard** — run the golden set, show pass rates over time. Leads.

## 5. MVP and milestones (build in this order)

Start small and reuse what exists. Each milestone is shippable on its own.

1. **Copy checker (MVP).** The smallest useful thing, and it reuses the assertions. Input
   box + surface picker -> run checks -> show results. Teaches the app skeleton.
2. **Reference browser.** Read and render the repo's markdown, with search.
3. **Token viewer / export.** Parse the JSON blocks; render swatches and type; export.
4. **Copy generator.** Add a model call with `CLAUDE.md` + relevant files as context.
5. **Evals dashboard.** Wrap `run_golden.py`; show pass rates.

## 6. Architecture

The app is a **read-only client** over the content system repo.

- **Data source:** a local clone of the repo (the app reads its files), or the GitHub raw
  files. Prefer a local folder path the user points at.
- **Linter:** port `assertions.py` to TypeScript so the app is self-contained (no Python
  runtime to bundle), OR call the Python file as a sidecar. Porting is cleaner; keep the
  word lists in sync with `terminology/` (or read them from the repo).
- **Generator (later):** the app sends `CLAUDE.md` + the surface's pattern + the relevant
  compliance file to a model, and formats the returned template's variables in code (the
  euro format and data injection are done by code, never by the model).

## 7. Recommended stack

- **Recommended:** **Tauri + React + TypeScript**. Tauri is small, modern, and reads the
  local file system easily (good for pointing at the repo folder). React + TS is well
  supported by Claude Code.
- **Simplest to start:** begin as a **local web app with Vite + React + TypeScript** (no
  desktop packaging yet), get the checker working, then wrap it in Tauri for the desktop
  build. This lets you learn fast and package later.
- Avoid bundling a Python runtime just for the linter; port the checks to TS.

## 8. Constraints the app must honor

- Money shown or generated uses the **European format** (`150 €`, `2.540,75 €`, no `,00`
  on round amounts). Do the formatting in code.
- The checker's rules come from the repo (`terminology/`, the Eval hooks, `assertions.py`),
  not from new rules invented in the app.
- Compliance text is **illustrative** (see `DISCLAIMER.md`); the app must not present it as
  verified legal wording.
- Respect the system's own accessibility rules in the app's UI (it would be odd to build an
  inaccessible tool for an accessible system).

## 9. First milestone in Code — starter prompt

Paste something like this into a new Claude Code project (after cloning the repo next to it,
or noting its path):

> I am building a desktop app that makes my content design system usable by my team. The
> system lives in a repo at [path]. For this first milestone, build a **copy checker**: a
> simple UI where I paste a string and pick a surface (error, cta, confirmation, ...), and
> it runs deterministic content checks and shows pass/fail with the reason and a suggested
> fix. The check logic already exists in `evals/assertions.py` in the repo — port it to
> TypeScript. Start as a local Vite + React + TypeScript web app. Before writing code,
> propose a plan and explain the structure, and build it in small steps, explaining each.

## 10. How to work with Code so you learn (not just delegate)

- Start every milestone by asking Code for a **plan** first, and read it before it codes.
- Build in **small steps**; after each, ask "explain what you did and why".
- **You** own the decisions (stack, scope, product); Code implements and teaches.
- Read the code it writes and ask "why this pattern?" when unsure.
- Keep the content system repo and the app as **separate projects**; the app consumes the
  repo.

## 11. Open decisions (for you and your instructor)

- Local clone vs GitHub API as the data source.
- Port the linter to TS vs call Python as a sidecar.
- Whether the MVP includes the generator (needs a model key and a privacy/cost decision) or
  stays checker + browser first.
- Desktop framework (Tauri vs Electron) and when to package.
- Single-user local tool vs shared/team deployment later.
