# Localization

**Status: normative. Always applied.**

Vanker ships in English today. This file is not about translating it; it is about **how a
string is built**, and those rules matter now, in one language, for a reason that has
nothing to do with translation.

## Why this matters before there is a second language

**A sentence assembled at runtime is invisible to every check we have.**

`A-FIELD-ERROR` counts the sentences in a string. `A-PARAGRAPHS` reads its paragraph
breaks. `A-MONEY-ACCOUNTED` looks for the clause about the money. `A-NO-INLINE-CTA` looks
for a call to action inside prose. All of them read **the string**. Concatenate
`"You have "` + `n` + `" payments"` and there is no string to read: three fragments pass
every check individually and produce a sentence nobody has ever validated.

So the rules below are not preparation for a future translation project. They are what
makes the copy checkable at all, and translation is the second thing they buy.

## Never concatenate

- **One string is one complete sentence**, with the variable inside it:
  `"You have {count} payments to confirm."` Never `"You have " + count + " payments"`.
- **Never build a sentence from a list of fragments**, and never assemble a message from a
  title fragment plus a body fragment at runtime.
- Two sentences that always appear together are still two strings, but each one is whole.

## Variables

- **Named, never positional.** `{amount}`, `{recipient}`, `{count}`. Never `%s`, `%d`,
  `{0}`, `{1}`. A translator has to be able to move a variable to where the sentence needs
  it, and a positional token in a language with different word order is a guess.
- **The name says what it holds**, because the translator sees a spreadsheet and not the
  screen: `{recipient}`, not `{name}`.
- **A variable is never part of a word.** No `{count} payment{s}`: plural rules differ (a
  Slavic language has more forms than English has, and Arabic has six), so the string is
  plural-aware, with a form per rule, not a letter glued on.
- **A variable never spans a sentence boundary**, and never contains markup.
- **Formatting belongs to the formatter, not to the string.** The string carries
  `{amount} €`; how a number is grouped, and where the symbol sits, comes from the locale
  (see `numbers-and-dates.md`, which is the euro-area English rendering, not a universal
  one).

## One key per use

**Never reuse a string because two places happen to read the same in English.**

"Open" is a verb on a button and an adjective in a status; German needs two different
words, and so does Spanish. Every use gets its own key, with a note saying what surface it
is on and what it does. A shared key saves nothing and produces a sentence that is wrong in
one of the two places, in every language but this one.

## Room to grow

- **German runs about 30% longer than English**, Finnish and Russian often more. A layout
  built to the exact width of the English string breaks on the first translation.
- **Text wraps; it does not truncate.** A truncated word in a bank is a truncated amount or
  a truncated name.
- **Our length limits are limits on the English source.** A CTA is three words *in English*;
  the check runs on the source string, and the layout leaves room for a longer translation.
- Never design a button, a tab, or a status label to fit its English label exactly.

## What is not translated, and what must be

| Not translated | Translated, but not freely |
| --- | --- |
| Product and feature names: Vanker, Spaces | The **controlled status vocabulary**: one term per state in every language, decided once, exactly as `../components/library/status-label.md` does for English |
| Regulatory terms with a defined form: IBAN, SEPA, BIC | The **banned-terms replacements**, which are language-specific by definition |
| Amounts, dates and times, which are formatted, not written | Legal and compliance copy, which is translated by someone qualified and never by a model alone (see `../compliance/`) |

A translated status vocabulary is a controlled vocabulary too. Free translation of `Pending`
across three screens produces three words, and the whole point of the vocabulary was that
there is one.

## Direction and position

- **Never refer to a position on the screen**: not "the button on the right", not "tap the
  icon below". Layouts mirror in right-to-left languages, they reflow on other screen sizes,
  and a screen reader user has no left. Name the thing: "Choose Confirm payment".
- In a right-to-left layout the transaction row mirrors, the leading icon becomes trailing,
  and the minus sign keeps its meaning. The copy does not change; the layout does.

## Also translated

Alt text, accessible names, error messages, push and email, and the words inside images if
any exist. Anything a person can read or hear is copy, and copy is translated (see
`../patterns/alt-text.md`).

## Eval hooks

- No concatenation: one string is one complete sentence with its variables inside it.
- Variables are named, never positional, and never glued into a word to make a plural.
- No `%s`, `%d`, `{0}`.
- No reference to a position on the screen ("on the right", "the button below").
- Length limits are read as limits on the English source.
- Product names and regulatory terms are not translated; the status vocabulary is
  translated once, as a controlled vocabulary.
