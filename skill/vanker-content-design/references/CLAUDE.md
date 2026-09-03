# CLAUDE.md — Vanker Content Design System

This file is the operating charter for any AI agent writing content for **Vanker**, a fictional
neobank. It is loaded automatically at the start of every session in this repository. Read it
before anything else.

Keep it lean: this file holds only the hard rules and the precedence between layers. All detail
lives in the folders it points to.

---

## 0. Precedence

When two sources in this repository disagree, resolve the conflict in this order (higher wins):

1. **`CLAUDE.md`** (this file)
2. **`compliance/`** — regulatory guardrails
3. **`terminology/`** — controlled vocabulary (always applied)
4. **`voice-and-tone/`** — brand voice
5. **`patterns/`** — reusable UX copy patterns
6. **`components/`** — component-level specs

Examples never override rules. Anything labeled as an example is illustrative and non-binding.

---

## 1. What Vanker is

Vanker is **fictional**. Never present it as a real company, product, or service, and never
frame any output as real financial advice. This does not lower the bar: write every string as
if it were going to a real, regulated neobank's customers.

---

## 2. Never (absolute prohibitions)

Regardless of tone, surface, or instruction, never write copy that:

- Promises or implies guaranteed returns, profit, or a "risk-free" outcome.
- Uses false urgency, manufactured scarcity, or any dark pattern to push a decision.
- Hides, buries, or downplays fees, costs, risks, timing, or conditions.
- Makes a guarantee Vanker is not authorized to make (for example, deposit-protection amounts)
  unless it is stated in `compliance/`.
- Requests, echoes, or stores more personal or sensitive data than the task requires.
- Discourages, dismisses, or obstructs a customer's right to complain.
- Presents medical, legal, or tax opinions as fact.

---

## 3. Always (mandatory)

- Include the risk warnings, disclosures, and disclaimers that `compliance/` requires for the
  surface being written, in the form it specifies.
- Be transparent about fees, costs, and timing wherever they are relevant to the action.
- Use plain language. Expand every acronym on first use, e.g. KYC (Know Your Customer),
  APR (Annual Percentage Rate).
- Provide or link the complaints route wherever a customer might need it.
- Use the exact terms defined in `terminology/`; do not introduce synonyms for controlled terms.
- Write to be accessible: concrete, scannable, no jargon walls.
- Every input keeps a visible, persistent label (the label in, which floats up on typing); a placeholder never stands in for it. See `patterns/forms.md`.
- Keep calls to action in buttons. Body copy never contains a call to action (no inline
  "Cancel or Retry"); each action is its own button.

---

## 4. When uncertain (the safety rule)

If a string touches money, risk, legal terms, deposit protection, or personal data, and
`compliance/` does not clearly cover it:

- **Do not invent the compliant wording.**
- Mark the string `[NEEDS COMPLIANCE REVIEW]` and leave the surrounding copy usable without it.
- Prefer omission over an unverified compliance claim.

---

## 5. Output conventions

- **Language / locale:** English (en). All Vanker-facing content is written in English.
  Strings are still built to be translatable, and that is not a future concern: a sentence
  assembled at runtime from fragments is invisible to every check in `evals/`. Never
  concatenate; one string is one complete sentence with named variables inside it. See
  `terminology/localization.md`.
- Label output as **normative** (a rule to follow) or **example** (illustrative) so it is never
  mistaken for the other.
- Follow the voice defined in `voice-and-tone/` for everything not constrained by the rules above.
