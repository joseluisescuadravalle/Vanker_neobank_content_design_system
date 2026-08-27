# Banner and toast

**Status: normative.**

Two ways to tell the person something without interrupting them. A **toast** is brief
feedback that disappears on its own; a **banner** stays in the layout until the situation
is resolved. Both connect to `../../patterns/notifications.md`.

## When to use which

- **Toast:** confirm that an action just happened ("Payment sent", "Space deleted").
  Transient and non-blocking.
- **Banner:** a persistent, contextual status the person should see and may need to act
  on (a pending verification, a failed sync, an informational notice).

Rule: a toast is never the only place a piece of important information lives, because it
disappears. Anything that must persist or needs an action is a banner (or inline).

## Toast

- **Style:** a graphite, white-text `shadow.lg` pill that **hugs its content** and is
  centered above the tab bar, not full width.
- **Anatomy:** an optional status icon, one short line, and at most one action ("Undo").
- **Action style:** the action is white (`color.on-primary`), emphasized in bold. Never the
  fuchsia accent, which reads poorly on the dark surface.
- **Layout:** the icon and message read as one centered unit; an action sits directly after
  the message with a small gap, never pushed to the far edge. A long message caps the width
  and wraps.
- **Timing:** auto-dismisses after about 4 seconds, or 6 with an action. One toast at a
  time; others queue.
- **Motion:** fades and rises in over `motion.duration.moderate`; respects
  `prefers-reduced-motion`.
- Not for errors that need an action, and not for critical information.

## Banner

- **Variants:** info, success, warning, error, each using its semantic subtle background
  and semantic icon (see `../foundations/color.md`).
- **Anatomy:** a leading semantic icon, a one-line title, an optional plain description,
  an optional action, and an optional close.
- **Placement:** inline at the top of the relevant screen or section, in the flow (it is
  not floating and does not overlay).
- **Persistence:** stays until the situation is resolved or the person dismisses it.
  Informational banners can be dismissed; a banner tied to an action keeps the action.

## Content rules

- **Toast:** past tense, brief ("Payment sent"). The action is a single verb ("Undo").
- **Banner title:** the point in one line ("Verify your identity to raise your limits").
- **Banner description:** the plain detail, one line ("It usually arrives in 3 to 5
  working days").
- **Banner action:** if tapping completes the action, it is a button with an action verb
  ("Verify"). If tapping only takes the person elsewhere to finish it, say so in the label
  or the description, so the button never implies the task finishes here.
- Error banners are specific and say how to fix it, never blaming the person (see
  `../../patterns/errors.md`).
- Never rely on color alone; the icon and text always carry the meaning.

## Accessibility

- Toasts are announced politely (`role="status"`, `aria-live="polite"`), so a screen
  reader reads them without stealing focus.
- Warning and error banners that appear in response to an action use `role="alert"`;
  purely informational banners use `role="status"`.
- The close control and any action have accessible labels and meet the 44px target.
- If a toast carries an action, the same action is reachable elsewhere, since the toast
  will disappear.

## Machine-readable spec

```json
{
  "toast": {
    "style": { "bg": "color.primary", "text": "color.on-primary", "shadow": "shadow.lg" },
    "action": { "color": "color.on-primary", "weight": "bold" },
    "layout": "content-width, centered above tab bar",
    "timing": { "auto-dismiss-s": 4, "with-action-s": 6, "concurrent": 1 },
    "action-max": 1,
    "a11y": { "role": "status", "aria-live": "polite" }
  },
  "banner": {
    "variants": ["info", "success", "warning", "error"],
    "anatomy": ["icon", "title", "description?", "action?", "close?"],
    "placement": "inline-top",
    "persistent": true,
    "a11y": { "role": { "warning-error": "alert", "info-success": "status" }, "color-not-alone": true }
  }
}
```

## Toast: content structure

The content model for a toast (a transient, in-app confirmation). It has one required slot
and one optional action.

### Slots

- **Message** (required): states what just happened, in **past tense and calm** (never a
  celebration): "Payment sent", "Space deleted". One short line (guideline about 50
  characters). **No ending period, no question mark, no exclamation, no emoji.** Maximum
  clarity and concision.
- **Action** (optional, single): a single verb ("Undo"), **white and bold** on the dark pill
  (never the fuchsia accent). Because the toast disappears, the same action is reachable
  elsewhere.

### Rules

- The toast is never the only place important information lives (it auto-dismisses).
- Announced politely; it does not steal focus.

### Eval hooks

- Message has no ending period, no "?" or "!", no emoji.
- One short line (about 50 characters or fewer).

## Banner: content structure

The content model for a banner (a persistent, in-app message in the layout flow).

### Placement

- **Inline in the layout**, in the flow: it pushes content down and never floats or overlays
  (that is a toast or a sheet). It stays until the situation is resolved or dismissed.
- **Screen level** (top of the content, under the header) for something about the whole
  screen, or **section level** (attached to the card or section it is about).

### Slots

- **Icon** (required): the semantic icon for the type (info / success / warning / error),
  in its semantic color. Color is never the only signal; the icon and text carry meaning.
- **Title** (required): the message in one line.
- **Body** (optional): the plain detail, one line. It **never contains the call to action**.
- **Action** (optional): a **button** with a verb. If tapping completes the action, it is a
  button; if it only navigates elsewhere, say so in the label or the body.
- **Close** (optional): for informational or dismissible banners only. A banner that requires
  an action does **not** offer a close.

### Colors (by type)

| Type | Background | Icon / accent |
| --- | --- | --- |
| Info | `color.info-subtle` | `color.info` |
| Success | `color.success-subtle` | `color.success` |
| Warning | `color.warning-subtle` | `color.warning` |
| Error | `color.error-subtle` | `color.error` |

### Eval hooks

- Meaning is carried by icon and text, never color alone.
- Title is one line; the body never contains the CTA; the action is a button.
- A banner that requires an action has no close.
