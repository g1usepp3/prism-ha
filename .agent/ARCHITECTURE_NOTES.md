# Prism HA Architecture Notes

## Product Idea
Prism HA is not a separate smart-home backend. It is a Prism-style experience layered on top of Home Assistant data, entities, and workflows.

## Architectural Principle
Use Home Assistant as the system of record whenever practical:
- calendars from Home Assistant calendar entities
- weather from Home Assistant weather entities
- people/presence from person and device entities
- todos and shopping from Home Assistant-compatible entities/integrations

## Prism HA Responsibility
Prism HA should provide:
- a cohesive setup and mapping layer
- Prism-specific orchestration
- dashboard UX and widget composition guidance
- chore logic, points, streaks, and gamification
- any custom derived state not already modeled well by Home Assistant

## Integration Direction
The integration domain is `prism_ha`.

Expected direction:
- minimal bootstrap now
- config flow setup
- options flow for editable entity mappings
- mapping of selected Home Assistant entities
- optional services/helpers for Prism-specific behavior
- Lovelace-friendly outputs and/or frontend assets

## Dashboard Direction
Short term:
- support the Home Assistant sandbox environment
- prefer editable YAML/dashboard assets when possible
- reuse strong existing Lovelace cards whenever practical

Long term:
- a polished Home Assistant dashboard that visually resembles Prism
- a cohesive family dashboard experience
- potentially custom cards or a stronger frontend layer if needed

## UI Composition Principle
The default assumption is not “build everything custom.”

The preferred order is:
1. reuse existing Home Assistant cards/plugins
2. compose them into a cohesive Prism-like dashboard
3. expose better data/mappings from Prism HA
4. build custom Prism HA frontend only where necessary

## Development Notes
- Keep repo code reusable and clean.
- Keep Home Assistant sandbox changes explicit and reviewable.
- Avoid coupling the entire product to one brittle frontend path too early.
- Separate integration/data-model responsibilities from dashboard composition responsibilities.
