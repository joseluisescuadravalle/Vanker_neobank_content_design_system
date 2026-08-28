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
| euro, € | The currency | Symbol after the amount, with a space: 150 €. |
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
| code | The single-use code we send to confirm identity or a payment | Say "code" or "verification code", and "a 6-digit code" where the length helps. Never "OTP", "one-time password", or "token". |
| two-factor authentication (2FA) | The extra login step | Expand on first mention. |

## People and address

| Term | Use it for | Notes |
| --- | --- | --- |
| we | Vanker | Vanker always speaks as "we". |
| you | The customer | |
| Hi [First name] | Greeting when the name is known | Fall back to "Hi there" when it is not. |

## Money format

- The euro symbol goes **after** the amount, with a space (European convention):
  `150 €`, `52,40 €`. Never before the amount.
- Thousands are separated by a dot, decimals by a comma: `2.540,75 €`.
- **Show decimals only when the amount has cents.** A round amount shows no decimals
  (`150 €`, `2.540 €`), never `150,00 €`. With cents, show exactly two (`52,40 €`,
  `10,10 €`), never one (`10,1 €`). Cents are never present by default.
- The one exception is an amount a person is **still typing** in an amount input: it shows
  exactly what was typed (`10,1`) and is normalized on blur. See
  `../components/library/amount-input.md`.
- Placeholders follow the same order: `{amount} €`.
- Amounts always use tabular numbers (see `../components/foundations/typography.md`).

## Time and date format

- Clock times use the 12-hour format with a space and lowercase am/pm: `2:32 pm`,
  `9:00 am`. Transaction times are always shown.
- Date headers read "Today", "Yesterday", then day month year: `5 May 2026`.

## Acronyms

- Expand an acronym on first use, in parentheses: KYC (Know Your Customer).
- **Always expand:** KYC, APR (Annual Percentage Rate), VoP (Verification of Payee), SCA
  (Strong Customer Authentication), CVV (Card Verification Value), BIC (Bank Identifier
  Code), 2FA (two-factor authentication).
- **Widely understood, no expansion needed:** IBAN, PIN, SEPA.
- In customer copy, prefer the plain phrase over the acronym where possible ("confirm your
  identity", not "KYC").
