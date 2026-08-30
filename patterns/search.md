# Search

**Status: normative (rules) + example (samples).**

The field, what it suggests, what it returns, and what it says when it returns nothing.

Field mechanics are inherited from `../components/library/text-field.md`; the placeholder
exception that this pattern depends on is defined in `forms.md`; the no-results screen is
an empty state (`empty-states.md`), never an error.

## Searching money is not searching content

Everything below follows from one difference: what a person searches for here is their own
money, and what they are usually trying to do is **confirm something happened**. "Did that
transfer to Ana go through?" is a question about facts, asked by someone who may already be
worried.

- **A result must be identifiable without opening it**: the counterparty, the date, and the
  amount, in the row (see `../components/library/transaction-row.md`).
- **Never correct the query silently.** A "did you mean" is offered, never applied. On money
  data, a search that quietly returns results for a different word is worse than no results:
  the person concludes something happened when it did not.
- **Never fuzzy-match an IBAN, a card number, or an amount.** Those are exact by nature, and
  an approximate match on an identifier is a wrong answer wearing the clothes of a right
  one.

## The field

- **No visible label.** This is the exception `forms.md` carves out, and it holds only here:
  a search field is self-evident, and the placeholder does the naming.
- **The accessible name is still required**: "Search transactions". The magnifier icon is
  not a name, and a field whose only name is an icon is unusable with a screen reader.
- **The placeholder names the scope**, which is the most useful thing it can do: "Search
  transactions", "Search transactions, people, and Spaces". A bare "Search" wastes the one
  chance to say what can be found here.
- **A clear control** ("Clear search") appears once there is text, with its own 44px target.
- Submitting is not required: results update as the person types, and Enter also works.
- The typed text is never replaced, reformatted, or reordered while the person types.

## Suggestions

- Suggestions are **offered below the field**, never written into it.
- They are labeled as what they are (recent, or a match), so nobody mistakes a suggestion
  for a result.
- **The list never reorders under the finger.** A suggestion that moves as new results
  arrive is how a person taps the wrong one.
- The number of suggestions is announced politely; focus stays in the field.

## Recent searches

A recent-search list in a bank can be revealing: a name, a company, a debt. It is not
neutral history.

- There is always a visible way to **clear recent searches**, and clearing is immediate.
- Recent searches never appear on a locked or shared screen, and never in a notification.
- They are suggestions, never results, and they are labeled "Recent".

## Results

- **Echo the query, in the person's own words**, so they can see what was actually searched,
  typos included. That is how someone corrects themselves without being corrected.
- Say **how many** and **in what**: "12 transactions for 'ana'".
- Never re-rank by anything the person cannot see. Order by relevance or by date, and say
  which.
- **No trending or popular searches.** What other customers look for is not a suggestion a
  bank makes.

## Nothing found

This is an empty state, not an error: no red, no error icon, no apology, and above all no
suggestion that the person typed it wrong.

**Say what was searched, where, and the way out:**

> **No transactions match "ana"**
>
> Try a different word, or search in all of your accounts.

- **Name the scope that produced the emptiness.** The most common dead end in a banking app
  is a search that finds nothing because a filter is still on from ten minutes ago:
  > **No transactions match "ana" in the last 30 days**
  >
  > `Clear the date filter`
- **The way out is a button**, not an instruction buried in the sentence (see `CLAUDE.md`).
- **Distinguish nothing found from nothing yet.** Searching an account with no transactions
  is a different screen from searching and finding none: the first says the account is new,
  the second says the query matched nothing.
- Never "No results found." on its own: it answers nothing and offers nothing.

## Accessibility

- The field is a `searchbox` with a real accessible name.
- The result count is announced in a **polite** live region as it settles, not on every
  keystroke.
- Results are a list with a heading; the person can move to them from the field without
  losing what they typed.
- The clear control is a button with its own name and its own target.

## Machine-readable spec

```json
{
  "search": {
    "money-not-content": {
      "result-identifiable-without-opening": ["counterparty", "date", "amount"],
      "silent-correction": false,
      "fuzzy-match-identifiers": false
    },
    "field": {
      "visible-label": false,
      "accessible-name": "required",
      "placeholder": "names the scope",
      "bare-search-placeholder": false,
      "clear-control": { "name": "Clear search", "min-target": 44 },
      "submit-required": false,
      "rewrites-typed-text": false
    },
    "suggestions": { "written-into-field": false, "labeled": true, "reorders-under-finger": false, "announce": "polite" },
    "recent": { "clearable": true, "on-locked-or-shared-screen": false, "labeled": "Recent" },
    "results": { "echoes-query": true, "states-count-and-scope": true, "order-stated": true, "trending": false },
    "no-results": {
      "is": "empty-state",
      "error-styling": false,
      "blames-spelling": false,
      "states-scope": true,
      "way-out": "button",
      "distinct-from-no-data-yet": true
    },
    "a11y": { "role": "searchbox", "count-live-region": "polite", "results-are-a-list": true }
  }
}
```

## Eval hooks

- The placeholder names the scope; a bare "Search" fails.
- The field has an accessible name even though it has no visible label.
- Results echo the query in the person's own words and state the count and the scope.
- No query is silently corrected, and no identifier is fuzzy-matched.
- A no-results screen names what was searched and the scope, offers the way out in a button,
  and never uses error styling or blames the spelling.
- "No results found." on its own fails.
- Nothing found and nothing yet are different screens.
- Recent searches are labeled, clearable, and never shown on a locked or shared screen.
