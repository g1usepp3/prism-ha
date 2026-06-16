"""Config flow for Prism HA integration."""
from __future__ import annotations

import logging
from typing import Any, Dict

from homeassistant.config_entries import ConfigEntry, ConfigFlow, OptionsFlow
from homeassistant.const import CONF_NAME
from homeassistant.core import HomeAssistant
from homeassistant.helpers.selector import (
    EntitySelector,
    EntitySelectorConfig,
)
from homeassistant.helpers.typing import ConfigType

from .const import DOMAIN, CONF_CALENDAR_ENTITY, CONF_CALENDAR_LABEL, CONF_PERSON_ENTITY

_LOGGER = logging.getLogger(__name__)


class PrismConfigFlow(ConfigFlow, domain=DOMAIN):
    """Handle the config flow for Prism HA."""

    VERSION = 1
    MINOR_VERSION = 1

    async def async_step_user(self, user_input: ConfigType | None = None) -> Dict[str, Any]:
        """Handle the initial setup step."""
        if user_input is not None:
            return self.async_create_entry(title=user_input[CONF_NAME], data={})

        return {
            "step_id": "user",
            "data_schema": self._get_user_schema(),
            "description_placeholders": {"name": ""},
        }

    def _get_user_schema(self) -> dict[str, Any]:
        """Get the user schema for initial setup."""
        from homeassistant.helpers import config_validation as cv
        
        return {
            CONF_NAME: str,
        }


class PrismOptionsFlow(OptionsFlow):
    """Handle options flow for Prism HA."""

    def __init__(self, *args, **kwargs) -> None:
        super().__init__(*args, **kwargs)
        self.entry = kwargs.get("entry")

    async def async_step_init(self, user_input: ConfigType | None = None) -> Dict[str, Any]:
        """Manage the options."""
        if not user_input:
            return {
                "step_id": "init",
                "data_schema": self._get_options_schema(),
            }

        # Save options using the correct pattern
        await self.async_step_init(user_input)
        
        return self.async_create_entry(title="", data={})

    def _get_current_mappings(self) -> list[dict]:
        """Get current mappings from entry options."""
        if not self.entry.options:
            return []
        
        mappings = self.entry.options.get("mappings", [])
        if isinstance(mappings, dict):
            mappings = [mappings]
        elif not isinstance(mappings, list):
            mappings = []
        
        return mappings

    def _get_options_schema(self) -> Dict[str, Any]:
        """Get the options schema."""
        current_mappings = self._get_current_mappings()
        
        # Ensure we have at least one mapping row
        if not current_mappings:
            current_mappings.append({
                CONF_CALENDAR_ENTITY: "",
                CONF_CALENDAR_LABEL: "",
                CONF_PERSON_ENTITY: "",
            })

        return {
            "step_id": "init",
            "data_schema": self._build_mapping_schema(current_mappings),
        }

    def _build_mapping_schema(self, mappings: list[dict]) -> Dict[str, Any]:
        """Build the schema for mapping rows."""
        # Get available calendar entities
        calendar_entities = [
            EntitySelectorConfig(
                entity_domain="calendar",
                multiple=True,
            )
        ]
        
        # Get available person entities
        person_entities = [
            EntitySelectorConfig(
                entity_domain="person",
                multiple=True,
            )
        ]

        schema_items = []
        for i, mapping in enumerate(mappings):
            schema_items.append({
                CONF_CALENDAR_ENTITY: {
                    "name": f"Calendar Entity {i+1}",
                    "selector": {
                        "entity": {
                            "multiple": False,
                            "options": calendar_entities,
                            "placeholder": "Select a calendar entity",
                        }
                    },
                },
                CONF_CALENDAR_LABEL: {
                    "name": f"Calendar Label {i+1}",
                    "selector": {"text": {}},
                },
                CONF_PERSON_ENTITY: {
                    "name": f"Person Entity {i+1}",
                    "selector": {
                        "entity": {
                            "multiple": False,
                            "options": person_entities,
                            "placeholder": "Select a person entity",
                        }
                    },
                },
            })

        return {"type": "form", "data_schema": self._create_form_schema(schema_items)}

    def _create_form_schema(self, schema_items: list[dict]) -> Dict[str, Any]:
        """Create the form schema for options."""
        from homeassistant.helpers import config_validation as cv
        
        # Build a simple schema that can be validated
        return {
            "type": "form",
            "data_schema": self._build_simple_schema(schema_items),
        }

    def _build_simple_schema(self, schema_items: list[dict]) -> Dict[str, Any]:
        """Build a simple schema for the form."""
        from homeassistant.helpers import config_validation as cv
        
        # This is a simplified approach - in practice you'd use proper HA selectors
        return {
            "type": "form",
            "data_schema": cv.Schema({
                CONF_CALENDAR_ENTITY: str,
                CONF_CALENDAR_LABEL: str,
                CONF_PERSON_ENTITY: str,
            }),
        }

    async def async_step_init(self, user_input: ConfigType | None = None) -> Dict[str, Any]:
        """Manage the options."""
        if not user_input:
            return {
                "step_id": "init",
                "data_schema": self._get_options_schema(),
            }

        # Save options using the correct pattern
        await self.async_step_init(user_input)
        
        return self.async_create_entry(title="", data={})


async def async_get_entry_options(hass: HomeAssistant, entry: ConfigEntry) -> dict[str, Any]:
    """Get current options for an entry."""
    return entry.options or {}
