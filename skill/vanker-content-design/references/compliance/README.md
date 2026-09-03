# Compliance

**Status: normative within the fiction. Illustrative, not verified. See `/DISCLAIMER.md`.**

The regulatory guardrail layer. In the precedence order of `/CLAUDE.md`, this layer sits
directly below `CLAUDE.md` and overrides voice, patterns, and components: when a rule
here conflicts with tone or style, the rule wins.

The text here translates the applicable **European** framework for an online bank into
**content obligations** (what must be said, when, and how). It is written for a fictional
euro-area neobank and has **not** been reviewed by a legal or compliance professional. It
must not be used in a real product without independent review.

## Files

- `framework.md` — the regulatory register: each regulation, what it is, and the content
  obligation it creates. Read this first for the map.
- `principles.md` — cross-cutting content-compliance principles and prohibited practices.
- `disclosures.md` — what must be disclosed, and where (fees, deposit protection, credit,
  currency conversion, contract and withdrawal information).
- `risk-warnings.md` — required risk warnings and prohibited claims.
- `security-payments.md` — authentication (SCA), Verification of Payee, payment
  transparency, fraud and scam warnings.
- `identity-kyc.md` — identity verification (AML / KYC) content.
- `complaints.md` — the right to complain, timelines, and escalation (ombudsman / ADR).
- `data-privacy.md` — data protection (GDPR) and tracking consent.
- `accessibility.md` — the European Accessibility Act obligations.

## Conditional modules

Some rules apply only if Vanker offers the product: **credit / overdraft / BNPL**
(CCD2), **crypto-assets** (MiCA), **investments** (MiFID II). These are marked
"conditional" where they appear.

## How the agent uses this layer

Before finalizing any customer-facing string, check it against this layer. If a string
touches money, risk, credit, deposits, identity, or data and this layer does not clearly
cover it, mark it `[NEEDS COMPLIANCE REVIEW]` and do not invent the wording.
