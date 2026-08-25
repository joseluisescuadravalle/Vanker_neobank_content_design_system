# Glossary

**Status: normative. Always applied.**

The controlled vocabulary of the system. When one of these terms exists for a concept,
use it exactly as written. Do not introduce synonyms. See `banned-terms.md` for words
to avoid.

## Style baseline

- **Spelling:** American English (optimize, color, personalize, center, canceled).
- **Banking vocabulary:** eurozone. Vanker is a euro-area neobank, so it uses "current
  account", "IBAN", and "SEPA transfer", not US-style "checking account", "routing
  number", or "ACH".
- **Capitalization:** feature and product names are capitalized (Vanker, Spaces);
  generic banking nouns are lowercase (account, card, transfer, balance).

## Money and payments

| Term | Use it for | Notes |
| --- | --- | --- |
| euro, € | The currency | Symbol before the amount: 150. € |
| balance | Total money in an account | |
| available balance | Money you can spend right now | Use when it differs from balance. |
| fee | A charge | Always state the exact amount. Never "a small fee". |
| SEPA transfer | A euro bank transfer | Expand on first mention: SEPA (Single Euro Payments Area). |
| SEPA Direct Debit | A recurring pull payment | |
| IBAN | The account number used for transfers | Expand on first mention: IBAN (International Bank Account Number). |
| BIC | The bank identifier | Expand on first mention: BIC (Bank Identifier Code). |

## Accounts and cards

| Term | Use it for | Notes |
| --- | --- | --- |
| Vanker account | The overall account | |
| current account | The everyday euro account | Not "checking account". |
| debit card | The physical card | |
| virtual card | A card that exists only in the app | |
| card details | Number, expiry, security code | Expand the security code on first mention: CVV (Card Verification Value). |

## Spaces (savings)

| Term | Use it for | Notes |
| --- | --- | --- |
| Spaces | The savings feature, as a product name | Capitalized. |
| space | One saving instance | Lowercase: "your Travel space". |
| target | The amount a space aims to reach | Prefer "target" over "goal" to avoid clashing with the feature name. |

## Identity and security

| Term | Use it for | Notes |
| --- | --- | --- |
| verify, verification | Confirming identity | Prefer this in customer copy over the raw acronym. |
| KYC (Know Your Customer) | The identity-check process | Internal-facing; in customer copy prefer "confirm your identity". Always expand. |
| PIN | The card PIN | Expand on first mention: PIN (Personal Identification Number). |
| passcode | The app unlock code | |
| two-factor authentication (2FA) | The extra login step | Expand on first mention. |

## People and address

| Term | Use it for | Notes |
| --- | --- | --- |
| we | Vanker | Vanker always speaks as "we". |
| you | The customer | |
| Hi [First name] | Greeting when the name is known | Fall back to "Hi there" when it is not. |

## Money format

- The euro symbol goes **after** the amount, with a space (European convention):
  `150 €`, `2.540,00 €`. Never before the amount.
- Placeholders follow the same order: `{amount} €`.
- Amounts always use tabular numbers (see `../components/foundations/typography.md`).
- Thousands are separated by a dot, decimals by a comma: `2.540,00 €`.
