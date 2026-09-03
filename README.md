# Vanker Content Design System

> Content design system for **Vanker**, a fictional neobank, built to be consumed by AI agents:
> voice and tone rules, UX copy patterns, component-level content specs, terminology and a
> regulatory guardrail layer so a model can draft the whole digital experience on-brand.

**Vanker is fictional.** Nothing here is real financial advice or a real product. See `DISCLAIMER.md`.

## What this is

A machine-readable content design system: the single source of truth an AI agent needs to
write any piece of Vanker's digital experience (onboarding, transactions, cards, support,
notifications, legal copy) so that every string is on-brand and compliant with the applicable
regulatory framework.

It is not a style guide for humans to skim. It is a structured, normative reference designed
to be loaded as context by a language model and applied consistently at scale.

## How to use it

**If you are an AI agent (start here):**
1. Read `CLAUDE.md` first. It holds the hard rules that override everything else (what you must
   never write, terminology, source hierarchy when documents conflict).
2. Load the voice and tone layer, then the UX copy patterns, then the component-level specs
   for the surface you are writing.
3. Before finalizing any copy, check it against the regulatory guardrail layer (transparency,
   risk warnings, complaints, KYC (Know Your Customer)).
4. When two sources disagree, follow the source hierarchy defined in `CLAUDE.md`.

**If you are a person:**
- Read this README, then `CLAUDE.md`, then browse the folder that matches your task.
- Normative content (rules the agent must follow) and examples (illustrative, non-binding)
  are labeled separately. Do not treat examples as rules.

## Repository structure

_(to be completed as the system grows)_

- `CLAUDE.md` — hard rules and source hierarchy, read first by any agent.
- `DISCLAIMER.md` — fictional-brand and no-financial-advice notice.
- `voice-and-tone/` — brand voice, tone modulation by context.
- `patterns/` — reusable UX copy patterns (buttons, errors, empty states, confirmations).
- `components/` — component-level content specs.
- `terminology/` — glossary and controlled vocabulary.
- `compliance/` — regulatory guardrail layer.
- `skill/`: the system packaged as a Claude skill, generated from the folders above by
  `evals/build_skill.py`. Install it to write with the rules instead of being judged by them.

## Sources & references

_(links pending — to be added as sources are confirmed)_

- Brand foundations: _TBD_
- Regulatory framework references: _TBD_
- Related design system / component library: _TBD_

## Status

Work in progress. Structure and content are evolving; expect breaking changes to file layout
until a first stable version is tagged.

## Adding to this system

`CONTRIBUTING.md` is the guide: where a new piece goes, the shape every file follows,
how a rule becomes a check, and the traps this system has already walked into.
`evals/check_structure.py` enforces the shape.
