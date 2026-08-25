# Notifications

**Status: normative (rules) + example (samples).**

Push notifications and in-app alerts. They are short and arrive uninvited, so every
word counts. Tone follows the stakes (see `../voice-and-tone/tone.md`): money and
security notifications are precise and serious; marketing may show personality.

## Anatomy

- **Title** — the key fact in a few words.
- **Body** — one concise sentence with the useful detail.

## Rules

- Front-load the key fact. People read the first few words only.
- Be specific: money notifications state the amount and who is involved.
- Keep it tight: title around 40 characters or fewer, body around 120 or fewer.
- No emoji, no pressure, no clickbait ("You will not believe...").
- Security and fraud notifications are serious and always include a clear action.
- Marketing notifications may have personality, stay honest, and are easy to ignore.
- Never dress a money or security alert as marketing.

## Variables

`{amount}`, `{sender}`, `{recipient}`, `{merchant}`, `{balance}`

## Examples

**Money received**
- Do: Title "Money in" / Body "You received {amount} € from {sender}."
- Not: "You have got money!"

**Payment sent**
- Do: Title "Payment sent" / Body "{amount} € is on its way to {recipient}."
- Not: "Your transfer has been processed successfully."

**Card payment**
- Do: Title "Card payment" / Body "{amount} € at {merchant}."
- Not: "A transaction occurred on your account."

**Low balance**
- Do: Title "Low balance" / Body "Your current account is down to {balance} €."
- Not: "Uh oh, running low!"

**Security check**
- Do: Title "Confirm it is you" / Body "We paused a payment that looks unusual. Open the app to review it."
- Not: "Suspicious activity detected."

**Space target reached**
- Do: Title "Space funded" / Body "Your Travel space has reached its target."
- Not: "Goal complete!!!"

**Marketing**
- Do: Title "New: smarter savings" / Body "Meet the tools that help your money work harder. Take a look."
- Not: "The savings account that will change your life forever."

## Eval hooks

- Money notifications state the amount.
- Title is short (about 40 characters or fewer).
- Security notifications include a clear action.
- No emoji, no pressure or clickbait terms.
