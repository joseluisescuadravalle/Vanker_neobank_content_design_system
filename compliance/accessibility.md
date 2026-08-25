# Accessibility (European Accessibility Act)

**Status: normative within the fiction. Illustrative, not verified.**

Accessibility is a **legal requirement**, not a nicety. Under the European Accessibility
Act (Directive EU 2019/882), in force from **28 June 2025**, Vanker's digital banking
services must meet **EN 301 549 / WCAG 2.1 Level AA**.

## What this layer requires of content

- Plain, understandable language (see `../voice-and-tone/voice.md`).
- Every meaningful image, icon, and control has a text alternative or accessible name.
- Errors are identified in text, with a clear way to fix them; never signalled by color
  alone (see `../patterns/errors.md`).
- Labels are always present on inputs (see `../components/library/text-field.md`).
- Text resizes and reflows; contrast meets AA (see `../components/foundations/color.md`).
- Media has captions and transcripts.
- Session timeouts warn and allow more time.

## Accessibility statement

- Publish an accessibility statement describing conformance, known limitations, and a
  way for people to report accessibility problems, and act on those reports.

## Relationship to the design system

Most of this is already built into the foundations and the component library (each
component has an accessibility section). This file is the **compliance anchor** that says
those practices are legally required, not optional, and must not be dropped for style.

## Eval hooks

- No information is conveyed by color alone.
- Inputs have visible, associated labels.
- Meaningful icons and images have accessible names.
- Text and error messages are real text, not baked into images.
