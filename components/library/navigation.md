# Navigation

**Status: normative.**

Two pieces move people through Vanker: a **bottom tab bar** for top-level navigation and
a **top app bar** for the current screen.

## Bottom tab bar

Primary navigation between the main areas of the app.

- **Destinations:** 3 to 5. Vanker default: Home, Cards, Spaces, Profile.
- **Each tab:** an outline icon (24px) above a label. The label is a single noun in
  sentence case and is **always visible**, never icon-only.
- **Active:** icon and label in `color.accent` (fuchsia), with `aria-current`.
- **Inactive:** `color.text-secondary`.
- One tab is active at a time. Selecting a tab does not lose the other tabs' state.
- Fixed to the bottom, above the device safe-area inset. Height 56px plus the inset.

## Top app bar

The header of the current screen.

- **Standard:** an optional back control (leading), the screen title (centered or
  leading), and up to two trailing action icons.
- **Large title:** for top-level screens, an optional eyebrow line (a greeting) and a
  large screen title (`heading-lg` or `display`). It collapses to the standard bar as
  the screen scrolls.
- **Title:** the screen's name, a short noun in sentence case ("Payment details",
  "Accounts"). It truncates with an ellipsis if long.
- **Back:** a labeled control ("Back") that returns to the previous screen.

## Content rules

- Tab labels are single nouns in sentence case: "Home", "Cards", "Spaces", "Profile".
- App bar titles name the screen, short noun, sentence case.
- No more than two trailing actions in the app bar; further actions go into an overflow
  menu.

## Accessibility

- The tab bar is a tablist; the active tab exposes `aria-current`, and each tab has an
  icon plus a visible label and an accessible name.
- Each tab and each app bar control meets the 44px minimum tap target.
- Back and action icons have accessible labels; icons never stand alone without a name.
- Respect safe-area insets on notched devices; never place a control under the inset.
- Do not signal the active tab by color alone; the visible label and position also carry
  it.

## Machine-readable spec

```json
{
  "navigation": {
    "tab-bar": {
      "destinations": { "min": 3, "max": 5, "default": ["Home", "Cards", "Spaces", "Profile"] },
      "tab": { "icon": "icon.lg", "label": "always-visible", "label-style": "single noun, sentence case" },
      "active": { "color": "color.accent", "aria-current": true },
      "inactive": { "color": "color.text-secondary" },
      "height": 56,
      "safe-area": true
    },
    "app-bar": {
      "variants": ["standard", "large-title"],
      "title": "screen name, short noun, sentence case",
      "trailing-actions-max": 2,
      "back": "labeled"
    },
    "a11y": { "role": "tablist", "min-target": 44, "labeled-icons": true }
  }
}
```
