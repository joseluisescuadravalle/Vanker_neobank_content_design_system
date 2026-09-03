# Security and payments

**Status: normative within the fiction. Illustrative, not verified.**

Content rules for authentication, payee verification, payment transparency, and fraud.

## Strong Customer Authentication (SCA) (PSD2 / PSR)

- Explain, in plain words, when and why an extra verification step is needed (for
  example a new payee or a higher-value payment).
- Vanker will **never** ask for a full passcode, a one-time code, or card details by
  phone, email, or message. Say so in security copy.
- Do: "To keep your account safe, confirm this payment with your passcode."
- Not: "Enter your full passcode so we can verify you" (in an inbound message).

## Verification of Payee (VoP) (Instant Payments Regulation)

- Before a euro transfer, show the result of matching the name to the account (IBAN):
  a **match**, a **close match** (show the real name), or **no match**.
- On a close match or no match, warn clearly and let the person decide; do not block
  silently and do not auto-confirm.
- Do: "The name does not match this account. Check with the person before you send, as
  we may not be able to recover the money."

## Instant payments and charges

- Offer instant euro transfers and charge no more than for a standard transfer.
- State arrival ("arrives in seconds") honestly.

## Currency conversion

- Show the markup over the European Central Bank (ECB) reference rate before confirming
  (see `disclosures.md`).

## Fraud and scam warnings (PSR)

- Show a contextual warning on higher-risk transfers (a new payee, an unusually large
  amount, a first payment to an account).
- Reinforce that Vanker will never tell someone to move money to a "safe account".
- Be specific and calm; do not blame the person.

## Eval hooks

- Security copy states that Vanker never asks for full codes or passcodes.
- A euro-transfer flow shows a Verification of Payee result before confirmation.
- Higher-risk transfers carry a scam warning; the person can still decide.
