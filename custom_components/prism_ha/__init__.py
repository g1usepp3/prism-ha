import logging
from homeassistant.core import HomeAssistant
from homeassistant.config_entries import ConfigEntry
from .const import DOMAIN, PLATFORMS

_LOGGER = logging.getLogger(__name__)


async def async_setup(hass: HomeAssistant, config: dict):
    """Set up the Prism HA component."""
    return True


async def async_setup_entry(hass: HomeAssistant, entry: ConfigEntry):
    """Set up Prism HA from a config entry."""
    _LOGGER.debug("Setting up Prism HA for %s", entry.entry_id)

    # Initialize mappings if not exists in options
    if "mappings" not in entry.options:
        hass.config_entries.async_update_entry(entry, options={**entry.options, "mappings": []})

    hass.data.setdefault(DOMAIN, {})
    hass.data[DOMAIN][entry.entry_id] = {
        "household_name": entry.data.get("household_name"),
        "calendars": [],
        "mappings": entry.options.get("mappings", [])
    }

    return True


async def async_unload_entry(hass: HomeAssistant, entry: ConfigEntry):
    """Unload a config entry."""
    _LOGGER.debug("Unloading Prism HA for %s", entry.entry_id)
    return True
