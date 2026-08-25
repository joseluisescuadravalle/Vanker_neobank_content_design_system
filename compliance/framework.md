# Regulatory framework (register)

**Status: normative within the fiction. Illustrative, not verified.**

The European regulations relevant to an online euro-area bank, and the content obligation
each creates for Vanker. Dates reflect the position as of 2026; confirm the current state
before any real use.

| Regulation | What it is | Content obligation for Vanker | Lands in |
| --- | --- | --- | --- |
| **PSD2** → **PSD3 + PSR** (Payment Services Directive 3 / Payment Services Regulation) | The core payments rulebook. PSD2 is in force; PSD3 and the PSR are expected to apply around 2026 to 2027 (roughly 21 months after entry into force, with Verification of Payee at about 27 months). | Strong Customer Authentication messaging; transparency of terms, charges, and execution times; fraud protection and payee matching; complaints handling. | `security-payments`, `disclosures`, `complaints` |
| **Instant Payments Regulation** (EU 2024/886) | Instant euro credit transfers. | Offer instant transfers; charge no more than for standard transfers; show Verification of Payee (VoP) results before sending (euro area from 9 October 2025). | `security-payments` |
| **Payment Accounts Directive** (PAD, 2014/92/EU) | Fee transparency and account access. | Provide a Fee Information Document (FID) before opening and a Statement of Fees each year; use standardized fee terms; support switching. | `disclosures` |
| **Deposit Guarantee Schemes Directive** (DGSD, 2014/49/EU) | Deposit protection. | State that eligible deposits are protected up to 100.000 € per depositor, per bank, by the Deposit Guarantee Scheme (DGS); provide the Depositor Information Sheet. | `disclosures`, `risk-warnings` |
| **Cross-border Payments Regulation** (EU 2021/1230) | Currency conversion transparency. | Show currency conversion charges as a percentage markup over the latest European Central Bank (ECB) reference rate. | `disclosures`, `security-payments` |
| **Consumer Credit Directive 2** (CCD2, EU 2023/2225) | Consumer credit, including overdrafts and Buy Now Pay Later. Applies from 20 November 2026. *(conditional)* | Standardized pre-contractual information, the Annual Percentage Rate (APR), the total amount payable, creditworthiness checks, and a 14-day right of withdrawal. | `disclosures`, `risk-warnings` |
| **Distance Marketing of Financial Services** (Directive EU 2023/2673) | Online sign-up to financial services. Withdrawal function required from June 2026. | Pre-contractual information, a 14-day right of withdrawal, a working online withdrawal function ("withdrawal button"), and no dark patterns. | `disclosures`, `principles` |
| **AML package: AMLR** (EU 2024/1624) + **AMLD6** + **AMLA** | Anti-money-laundering single rulebook. Core rules apply from around 10 July 2027. | Identity verification (Know Your Customer, KYC) and ongoing checks, explained in plain, non-accusatory language. | `identity-kyc` |
| **GDPR** (EU 2016/679) + **ePrivacy** (2002/58/EC) | Data protection and tracking. | A clear privacy notice, a valid lawful basis or consent, tracking consent, and easy exercise of data rights. | `data-privacy` |
| **European Accessibility Act** (Directive EU 2019/882) | Accessibility of banking services. In force from 28 June 2025. | Digital services meet EN 301 549 / WCAG 2.1 Level AA; publish an accessibility statement and a way to report issues. | `accessibility` |
| **eIDAS / eIDAS2** (910/2014, amended by EU 2024/1183) | Electronic identity and the EU Digital Identity Wallet. | Accept and explain electronic identification, including the EU Digital Identity Wallet. | `identity-kyc` |
| **Unfair Commercial Practices Directive** (2005/29/EC) | Fair, non-misleading practices. | No misleading or aggressive copy; transparency of the real offer. | `principles` |
| **MiCA** (EU 2023/1114) | Markets in Crypto-Assets. *(conditional)* | Prominent risk warnings, "not covered by the Deposit Guarantee Scheme", and the required crypto-asset information. | `risk-warnings` |
| **MiFID II** (2014/65/EU) | Investment services. *(conditional)* | Appropriateness or suitability, risk warnings, and costs-and-charges disclosure. | `risk-warnings`, `disclosures` |
| **DORA** (EU 2022/2554) | Digital operational resilience. | Mostly internal; customer-facing only for clear, timely incident and outage communication. | `principles` |
