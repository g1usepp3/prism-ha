# Prism HA UI References

## Purpose
This file defines the visual and implementation guidance for Prism HA dashboard work.

Prism HA should feel like Prism in overall UX, but it should remain Home Assistant-native where practical by reusing strong existing Lovelace cards, HACS components, and dashboard tools instead of rebuilding everything from scratch.

## Core UI Goal
Build a Home Assistant dashboard experience that feels like Prism:
- calm, polished, family-friendly
- clear hierarchy
- tile-driven layout
- easy to scan
- strong calendar visibility
- useful everyday widgets
- visually cohesive across widgets

Prism HA is not trying to replace Home Assistant’s architecture. It is trying to provide a Prism-like experience on top of Home Assistant data and workflows.

## Prism As Reference
Use Prism as the UX and layout reference target:
- overall information hierarchy
- spacing rhythm
- dashboard composition
- family-oriented usability
- balance of utility and visual polish

If Prism reference files or screenshots are provided, treat them as design references unless explicitly told to directly reuse code or assets.

## Preferred Dashboard Strategy
Prefer composing strong existing Home Assistant dashboard components first.

Default order of preference:
1. Reuse installed/custom Lovelace cards if they fit the need.
2. Combine cards with styling/layout tools to achieve a Prism-like result.
3. Add Prism HA integration data/mapping so existing cards become more useful.
4. Build custom Prism HA frontend pieces only when the desired experience cannot be achieved cleanly with existing cards.

Do not invent custom cards by default if an existing card can achieve the desired result with reasonable configuration.

## Installed / Preferred Card Stack
The current environment already includes or strongly prefers the following dashboard tools and cards:

- Bubble Card
- button-card
- card-mod
- layout-card
- Config Template Card
- Mushroom
- Atomic Calendar Revive
- Week Planner Card
- Better Moment Card
- Weather Card
- browser_mod
- ICS Calendar (iCalendar)

These should be considered first when designing Prism HA dashboard experiences.

## Widget Guidance

### Tile and Widget Surfaces
Bubble Card is a preferred primitive for tile-like dashboard elements.

Use it when possible for:
- summary tiles
- room/home tiles
- quick actions
- simple status widgets
- high-level Prism-style dashboard blocks

button-card, card-mod, and layout-card may be used to refine layout and styling around Bubble Card or other core cards.

### Calendar
The calendar experience is a major part of Prism HA.

Desired direction:
- family-friendly schedule view
- strong readability
- clear person/calendar association
- useful visual grouping
- color-coded user/calendar context

The Skylight Calendar Card concept is a strong reference direction for the desired calendar experience.

Prism HA should support:
- calendar entity selection
- calendar-to-user/person mapping
- display color mapping or override
- dashboard-friendly calendar presentation

Do not rush into building a final custom calendar widget if the data model is not ready.

### Weather / Time / Context
Weather, date/time, and household context should feel polished but should usually reuse existing cards unless a strong Prism-specific reason exists to do otherwise.

### Chores / Checklists / Shopping
These are likely areas where Prism HA may eventually need more custom behavior and custom UI composition because the logic and gamification requirements are more Prism-specific.

Even there, first evaluate whether strong existing cards can be composed effectively before building custom frontend components.

## Dashboard Composition Rules
- Prefer a small set of reusable visual patterns.
- Keep the dashboard easy to scan from a tablet or wall display perspective.
- Avoid overloading the screen with too many competing card styles.
- Prefer a cohesive system over a “plugin zoo” appearance.
- Reuse a few strong cards consistently rather than many unrelated cards inconsistently.
- Use layout-card and card-mod to improve cohesion where needed.
- Favor practical, reviewable YAML/dashboard composition over fragile ad hoc UI tricks.

## Dependency Rules
When recommending dashboard implementations:
- Prefer already installed cards first.
- If a new dependency is needed, explicitly say so.
- Distinguish between:
  - already installed / available
  - recommended to add
  - optional nice-to-have
- Document required HACS or resource dependencies for anything that becomes part of the Prism HA dashboard approach.

Do not silently assume a card is present if it has not been confirmed.

## Deployment Guidance
Prism HA dashboard plans should include deployment awareness.

That means:
- note which cards/resources are required
- note which pieces belong in repo-managed files
- note which pieces belong in Home Assistant dashboard YAML
- note any HACS/resource prerequisites
- prefer reproducible setup over undocumented UI-only manual edits

## Custom UI Threshold
Custom Prism HA frontend pieces are justified when one or more of these is true:
- existing cards cannot express the needed Prism interaction cleanly
- the widget requires Prism-specific logic and presentation tightly coupled together
- consistency across the dashboard cannot be achieved reasonably through composition alone
- the user explicitly asks for a dedicated custom Prism HA card or panel

## Working Expectation
Whenever proposing dashboard work, explain:
1. what existing cards/plugins should be reused
2. what Prism HA integration data must be exposed
3. what YAML/dashboard files will be created or edited
4. what dependencies must exist in Home Assistant
5. what, if anything, truly needs custom frontend code
