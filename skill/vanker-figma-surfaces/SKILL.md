---
name: vanker-figma-surfaces
description: Build a Vanker screen or surface in Figma from a prompt, with the right copy and the right components. Use this skill whenever the user asks to create, draw, mock up or put in Figma any Vanker surface (an error modal, a sheet, a banner, a toast, an empty state, a form field, a button, a full screen), even if they only say "in Figma" or "make the screen". It pairs with vanker-content-design (which writes and checks the copy) and uses the Figma MCP tools (use_figma) on the Vanker Design System file. Also use it to update an existing Vanker surface in Figma or to add a new component to the library.
---

# Vanker surfaces in Figma

You are assembling screens for Vanker, a fictional euro-area neobank, in the Figma file
**Vanker Design System**. The file holds the system's tokens as variables, its text and
effect styles, and a component library generated from `components/library/`. Your job is
to turn a request into a surface on the **Surfaces** page, using library instances, never
loose rectangles, and with copy that has passed the content system's checks.

Two rules govern everything:

1. **The copy comes from the content skill, not from you.** Before touching Figma, run the
   `vanker-content-design` skill on the request to get every string (title, body, button
   labels, field labels, helper text) in its delivery format, already checked. Paste those
   strings into the components verbatim. If the content skill marks something
   `[NEEDS COMPLIANCE REVIEW]`, keep the marker visible in the design.
2. **Instances, not drawings.** Every element on a surface is an instance of a library
   component, or a plain auto-layout frame that only positions instances. If a component
   the surface needs does not exist yet, say so and offer to build it (see "Adding a
   component"); do not fake it with rectangles.

## The file

- File key: `9sr6gsJLZ2eHV4XBfH8D27` (https://www.figma.com/design/9sr6gsJLZ2eHV4XBfH8D27)
- Pages: Cover, Foundations, Button, Text field, Status label, Banner & Toast,
  Sheet & Modal, Empty state, Surfaces. New surfaces go on **Surfaces**.
- Variables: collections Primitives, Color (modes Light and Dark), Spacing, Radius.
  Semantic names match the system: `color/primary`, `color/text-secondary`,
  `color/error-subtle`, `space/4`, `radius/md`. Never hardcode a hex or a pixel value that
  has a variable.
- Text styles: `product/heading`, `product/body`, `product/body-sm`, `product/caption`,
  `product/button`, and the rest of the scale; `marketing/*` only for brand pages.

Before every write, load the `figma-use` skill (it is mandatory for `use_figma`), and start
each script with `await figma.setCurrentPageAsync(page)` on the Surfaces page.

## Component map

Look components up **by name** at run time, never by a remembered node id: ids change if
someone rebuilds the library. Read their property keys from
`componentPropertyDefinitions` on the component set, because Figma appends a suffix
(`Label#3:0`) that you cannot guess.

| Surface (content skill id) | Figma component | Variants | Properties |
| --- | --- | --- | --- |
| `cta`, `button` | `Button` (page Button) | Style: Primary, Accent, Secondary, Tertiary, Destructive; Size: Large, Medium; State: Default, Pressed, Disabled | Label |
| `error`, `confirmation`, `card-action`, `system-error-screen` in a dialog | `Sheet / Modal` (page Sheet & Modal) | Type: Sheet, Modal | Title, Body; nested Button instances `primary` and `cancel` carry their own Label |
| `banner` | `Banner` (page Banner & Toast) | Variant: Info, Success, Warning, Error | Title, Description, Show description, Show action; nested Button instance `action` carries its Label |
| `toast` | `Toast` (page Banner & Toast) | none | Message, Action, Show action |
| `empty-state`, `no-results` | `Empty state` (page Empty state) | Kind: First use, No results, All caught up | Title, Description, Show action; nested Button `primary-action` |
| `label-in`, `helper-text`, `field-error` | `Text field` (page Text field) | State: Empty, Focus, Filled, Error, Disabled | Label, Value, Helper, Show helper |
| `status-label`, `status`, `badge` | `Status label` (page Status label) | Tone: Neutral, Info, Success, Warning, Error; Indicator: None, Dot | Label |
| `checkbox` | `Checkbox` (page Checkbox) | State: Unchecked, Checked, Error, Disabled | Label |
| `radio-option`, `legend` | `Radio option` and `Radio group` (page Radio group) | Option State: Unselected, Selected, Error, Disabled | Option: Label; Group: Legend, with three nested `option-N` instances (add or remove to change the count) |
| `toggle-label`, `toggle-description` | `Toggle` (page Toggle) | State: Off, On, Disabled | Label, Description, Show description |
| `chip`, `preset-amount` | `Chip` (page Chip) | Kind: Filter, Input; Selected: Off, On | Label |
| `dropdown-option`, `option` (the field itself) | `Dropdown` (page Dropdown) | State: Default, Selected, Error, Disabled | Label, Value, Helper, Show helper |
| account or space summary | `Card` (page Card) | Variant: Account, Space | Title, Value (Account only), Subtext |
| transaction list item, `category` | `Transaction row` (page Transaction row) | Direction: Incoming, Outgoing; State: Settled, Pending, Failed, Scheduled | Name, Meta, Amount (include the sign: `+150 €` or `−150 €` with U+2212) |
| tab bar, app bar | `Tab bar` and `App bar` (page Navigation) | Tab bar Active: Home, Cards, Spaces, Profile; App bar Variant: Standard, Large title | App bar: Title, Show back |
| `amount-value`, `amount-label`, `fx-quote` context | `Amount input` (page Amount input) | Variant: Hero, Inline; State: Default, Error | Question or label, Value, Context line; Hero has three nested Chip `preset` instances |
| `code-screen`, `auth`, `auth-error` | `Code input` (page Code input) | State: Default, Error | Heading, Destination, Message; nested Button `resend` |
| `date-unavailable`, date parts | `Date field` (page Date field) | State: Default, Filled, Error | Legend, Echo or error |
| `counter`, free text | `Textarea` (page Textarea) | State: Empty, Filled, Near limit, Error | Label, Value, Helper, Counter |
| `accordion-header`, `accordion-body` | `Accordion` (page Accordion) | State: Closed, Open | Header, Panel |
| `tooltip`, `tooltip-trigger` | `Tooltip` and `Tooltip trigger` (page Tooltip) | none | Tooltip: Body |
| `count-badge` | `Count badge` (page Count badge) | Kind: Count, Dot | Count |
| `onboarding-step`, `flow-intro-body` | `Onboarding step` (page Onboarding step) | none, full screen 375 × 812 | Step label, Title, Description, Show back, Show secondary; nested Buttons `primary` and `secondary`; `content` slot for step-specific controls |

Not built yet (say so if the surface needs them): an iconography library. Every icon in
the file is a placeholder (a circle or a simple vector); do not draw new icons on a surface.

## How to build a surface

1. **Get the copy.** Run `vanker-content-design` on the request. Keep its output; it is
   also the text of the caption you will place next to the surface.
2. **Choose the container.** A full screen is a 375 × 812 frame named
   `Surface / <what it is>`, filled with `color/background`, corner radius 40, clipping
   content. A dialog sits on that frame above a `scrim` rectangle (fill `color/primary`,
   node opacity 0.4). A single component (a banner, a toast, a field) goes alone on a
   375-wide auto-layout frame named the same way, filled with `color/background`, padded
   with `space/4`, hugging its height. Place new surfaces to the right of the last one,
   with 100 px between them, and the `Prompt` caption above at the same x.
3. **Find the components.** One read-only `use_figma` that returns, for each component
   set you need, its id, its variant names and its property keys:

   ```js
   const page = figma.root.children.find(p => p.name === 'Sheet & Modal');
   await figma.setCurrentPageAsync(page);
   const set = page.findOne(n => n.type === 'COMPONENT_SET' && n.name === 'Sheet / Modal');
   return { id: set.id, variants: set.children.map(c => c.name), props: Object.keys(set.componentPropertyDefinitions) };
   ```

   Do one such call per page you need (page context resets between calls, and a script
   switches page at most once).
4. **Assemble.** Switch to Surfaces, create the frame, create instances with
   `variant.createInstance()`, append them to auto-layout frames, then set text and
   booleans with `instance.setProperties({ 'Title#7:0': '...', 'Body#7:3': '...' })` using
   the keys from step 3. Nested buttons: find the child instance by name (`primary`,
   `cancel`, `primary-action`) and call `setProperties({ 'Label#3:0': 'Try again' })` with
   the Button set's key. Swap a variant with `setProperties({ Style: 'Destructive' })`.
   Multi-paragraph bodies keep their blank lines (`\n\n`): the layout depends on them.
5. **Place the caption.** An auto-layout frame named `Prompt` above the surface, with the
   request in one line and the sentence "Copy written with the vanker-content-design
   skill and checked by its deterministic checks." Keep the prompt: the screen is an
   artifact of the course and the prompt is its provenance.
6. **Look at it.** `await frame.screenshot()` or `get_screenshot`, and fix what is wrong
   before answering: text clipped, a button not full width, a body with its paragraphs
   collapsed, a color that is not a variable.
7. **Answer** with the link to the node
   (`https://www.figma.com/design/9sr6gsJLZ2eHV4XBfH8D27?node-id=<id with a dash>`), the
   copy you placed, and anything the content skill flagged. Do not describe the design in
   prose the user can see in Figma.

## Adding a component

When a surface needs a component the library lacks, build it on its own page from the
JSON block and the rules in `components/library/<name>.md`, following the
`figma-generate-library` skill: variants from the states in the spec, every fill, stroke,
radius and padding bound to a variable, text on a text style, a TEXT property for every
slot the content skill can write, a description on the set that names the source file, and
a documentation frame on the page. Then add it to the map above and rerun the surface.

## When the library is wrong

If an instance clips its text, shows a hardcoded fill, or cannot take the copy the content
skill produced, the defect is in the component, not in the surface. Fix it on the
component's page (the variants, not the instance), rerun the surface, and say what you
fixed in the answer. Overriding it on the instance hides the defect for the next person.
The one exception is a task that explicitly forbids touching the library: then override
the instance and report the defect as a finding.

## What not to do

- No hex colors, no raw pixel spacing where a variable exists, no fonts other than the
  file's text styles.
- No copy invented in Figma. If the user changes a string in the chat, run it through the
  content skill again before placing it.
- No em dashes, exclamation marks, emoji or Title Case in any string, even in captions and
  layer names that read as copy.
- No detaching instances. If a component does not fit, the component is wrong: fix it on
  its page.
