# Prism HA Agent Rules

## Mission
Build Prism HA as a Home Assistant custom integration and dashboard experience that brings a Prism-style UX to Home Assistant data and workflows.

## Primary Goals
- Build and maintain the custom integration under `/app/custom_components/prism_ha`.
- Use Home Assistant entities and integrations where possible instead of reinventing native HA concepts.
- Support a Prism-style Lovelace/dashboard experience on top of Home Assistant data.
- Keep changes compatible with the sandbox dev environment mounted at `/ha-config`.

## Environment
- `/app` is the Prism HA git repo.
- `/ha-config` is the Home Assistant dev config directory.
- The running Home Assistant test instance mounts plugin code from `/app/custom_components/prism_ha`.
- The running Home Assistant test instance mounts frontend assets from `/app/www/prism-ha`.

## Rules
- Prefer editing repo files in `/app` over ad hoc edits elsewhere.
- Treat `/ha-config` as the live Home Assistant sandbox environment.
- Prefer YAML dashboards and normal YAML config files over direct `.storage` edits.
- Avoid editing `.storage` unless there is no practical YAML-based alternative.
- Keep changes small, reviewable, and testable.
- Do not delete unrelated user work.
- Do not change ports, hostnames, or Ollama settings unless explicitly asked.
- Keep `prism_ha` as the integration domain unless explicitly asked to rename it.
- Favor Home Assistant config flow setup over long-term YAML-only setup.
- Reuse Home Assistant primitives for calendar, todo, shopping, weather, person, and device data.
- Put custom Prism behavior in the integration layer, not in fragile dashboard-only hacks.
- Prefer existing strong Home Assistant cards/plugins when they can achieve the desired Prism HA experience cleanly.
- Do not build a custom frontend widget by default if a well-supported existing Lovelace card can do the job.
- When recommending dashboard work, explicitly call out dependencies on HACS/custom cards/resources.

## Git and Publishing Rules
- The git repo at `/app` is the working source of truth.
- Do not run `git pull`, `git fetch`, `git merge`, `git rebase`, or `git push` unless explicitly asked.
- Do not change remotes or branches unless explicitly asked.
- It is fine to inspect `git status`, `git diff`, and existing tracked files.
- Prefer making changes locally and summarizing them for review.
- If publishing is requested, state which branch and remote will be used before taking action.

## Coding Expectations
- Follow Home Assistant custom integration conventions.
- Keep Python code simple, async where appropriate, and minimal.
- Keep frontend work modular and compatible with Lovelace/Home Assistant delivery paths.
- Update documentation when architecture or setup changes materially.

## Safety
- Before changing many files, explain the intended plan.
- Before touching `/ha-config/.storage`, explain why it is necessary.
- Prefer creating new YAML dashboard files in `/ha-config` or repo-managed assets over rewriting HA internal state.
