# Prism HA Tasks

## Current Objective
Establish a clean development workflow where Aider can:
1. Edit the Prism HA custom integration in `/app`.
2. Edit the Home Assistant sandbox config in `/ha-config`.
3. Help build dashboard and UI assets for the Home Assistant dev environment.

## Near-Term Tasks
- Verify and complete the minimal `prism_ha` custom integration scaffold.
- Ensure `manifest.json`, `__init__.py`, `config_flow.py`, `strings.json`, and translations are correct.
- Confirm the integration can be loaded and tested in the dev Home Assistant instance.
- Decide which setup remains temporary in YAML and which moves to config flow.
- Define the first Prism HA data model for entity mappings.

## After Scaffold
- Add config flow selectors for key entity mappings, such as calendars, weather, todo/shopping, and people.
- Define where Prism-specific state lives.
- Create a first useful dashboard experience in Home Assistant.
- Prefer YAML-based dashboard definitions in the dev environment where practical.

## Dashboard Direction
The desired outcome is a Lovelace/Home Assistant dashboard that feels like Prism, using Home Assistant data plus custom Prism logic.

Possible feature areas:
- widgets
- calendar integration
- chores
- gamified chores
- checklists
- shopping lists
- family/home status
- weather and routines

## Working Style
- Tackle one milestone at a time.
- Keep the repo and dev HA environment in sync.
- Summarize what to restart or reload after changes.
