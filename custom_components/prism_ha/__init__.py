"""Prism HA integration."""
from __future__ import annotations

import logging
from typing import Any, Dict

from homeassistant.config_entries import ConfigEntry
from homeassistant.core import HomeAssistant
from homeassistant.helpers.typing import ConfigType

from .const import DOMAIN, PLATFORMS

_LOGGER = logging.getLogger(__name__)


async def async_setup(hass: HomeAssistant, config: ConfigType) -> bool:
    """Set up Prism HA from YAML configuration."""
    return True


async def async_setup_entry(hass: HomeAssistant, entry: ConfigEntry) -> bool:
    """Set up Prism HA from a config entry."""
    # Initialize runtime data for the integration
    hass.data.setdefault(DOMAIN, {})
    
    # Get or initialize mappings from options using proper pattern
    if not entry.options:
        await hass.config_entries.async_update_entry(entry, options={})
    
    mappings = entry.options.get("mappings", [])
    
    _LOGGER.debug("Prism HA setup complete with %d mappings", len(mappings))
    
    # Store runtime data for use by other components
    hass.data[DOMAIN]["entry"] = entry
    
    return True


async def async_unload_entry(hass: HomeAssistant, entry: ConfigEntry) -> bool:
    """Unload a config entry."""
    if DOMAIN in hass.data and "entry" in hass.data[DOMAIN]:
        del hass.data[DOMAIN]["entry"]
    
    _LOGGER.debug("Prism HA unloaded")
    
    return True


async def async_reload_entry(hass: HomeAssistant, entry: ConfigEntry) -> bool:
    """Reload a config entry."""
    # Reload logic if needed in the future
    return await async_setup_entry(hass, entry)
