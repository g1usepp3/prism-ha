# Prism HA Project Map

## Main Paths
- `/app` -> Prism HA git repo
- `/ha-config` -> Home Assistant sandbox config
- `/app/custom_components/prism_ha` -> custom integration code
- `/app/www/prism-ha` -> repo-managed frontend/static assets intended for Home Assistant
- `/ha-config/configuration.yaml` -> Home Assistant main YAML config
- `/ha-config/.storage` -> Home Assistant internal storage (use carefully)

## Important Repo Areas
- `custom_components/prism_ha/`
  - Home Assistant custom integration
  - expected place for manifest, init, config flow, translations, entities, helpers, etc.
- `www/prism-ha/`
  - frontend/static assets that may support dashboard work
- `.agent/`
  - agent guidance files
- `.aider.conf.yml`
  - Aider startup config for this repo

## Environment Relationship
- Home Assistant dev container reads plugin code from `/app/custom_components/prism_ha` via bind mount.
- Home Assistant dev container reads frontend assets from `/app/www/prism-ha` via bind mount.
- Aider can directly modify both repo files and Home Assistant sandbox config files.

## Source Locations
- `/app` is the Prism HA git repository and primary source for code.
- `/ha-config` is the Home Assistant sandbox configuration directory.
- Do not clone duplicate repos or pull from alternate locations unless explicitly asked.

## Dashboard Work Locations
- Prefer repo-managed reusable assets under `/app` where appropriate.
- Prefer Home Assistant dashboard/config YAML under `/ha-config` for sandbox instance-specific dashboard work.
- If dashboard YAML files are created, keep them in a clear, reviewable location such as `/ha-config/dashboards/` unless the user chooses a different structure.
- Document any required dashboard resource dependencies.

## Development Preference
- Plugin logic and reusable assets belong in `/app`.
- Home Assistant instance-specific configuration belongs in `/ha-config`.
- Use YAML-mode dashboards where possible for versionable, reviewable dashboard work.
