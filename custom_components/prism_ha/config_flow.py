"""Config flow for Prism HA."""

from typing import Any

import voluptuous as vol

from homeassistant.config_entries import ConfigEntry
from homeassistant.data_entry_flow import FlowResult
from homeassistant.helpers.selector import (
    EntitySelector,
    EntitySelectorConfig,
)
from homeassistant.core import HomeAssistant

from .const import DOMAIN


class PrismConfigFlow:
    """Handle the config flow for Prism HA."""

    VERSION = 1

    async def async_step_user(
        self, user_input: dict[str, Any] | None = None
    ) -> FlowResult:
        """Handle the initial step."""
        if user_input is not None:
            return self.async_create_entry(title=DOMAIN, data=user_input)

        return self.async_show_form(
            step_id="user",
            data_schema=vol.Schema({}),
        )


class PrismOptionsFlow:
    """Handle options flow for Prism HA."""

    def __init__(self, *args: Any, **kwargs: Any) -> None:
        super().__init__(*args, **kwargs)
        self.config_entry = kwargs.get("config_entry")

    async def async_step_init(
        self, user_input: dict[str, Any] | None = None
    ) -> FlowResult:
        """Manage the options."""
        if user_input is not None:
            return self.async_create_entry(title="", data=user_input)

        current_mappings = self._get_current_mappings()
        schema_items = [
            {
                "name": f"Mapping {i + 1}",
                "schema": vol.Schema(
                    {
                        vol.Required("calendar_entity", default=""): EntitySelector(
                            EntitySelectorConfig(domain="calendar")
                        ),
                        vol.Optional("calendar_label", default="Calendar"): str,
                        vol.Optional("person_entity", default=""): EntitySelector(
                            EntitySelectorConfig(domain="person")
                        ),
                    }
                ),
            }
            for i in range(len(current_mappings))
        ]

        return self.async_show_form(
            step_id="init",
            data_schema=self._build_options_schema(schema_items),
            defaults={
                "mappings": [
                    {
                        "calendar_entity": mapping.get("calendar_entity"),
                        "calendar_label": mapping.get("calendar_label"),
                        "person_entity": mapping.get("person_entity"),
                    }
                    for mapping in current_mappings
                ]
            },
        )

    def _get_current_mappings(self) -> list[dict]:
        """Get current mappings from config entry."""
        options = self.config_entry.options or {}
        return options.get("mappings", [])

    def _build_options_schema(
        self, schema_items: list[dict]
    ) -> vol.Schema:
        """Build the options schema with mapping rows."""
        mapping_fields = []
        for item in schema_items:
            mapping_fields.extend(item["schema"].schema)

        return vol.Schema(
            {
                vol.Required("mappings"): [vol.Schema(mapping_fields)],
            }
        )


async def async_get_options_flow(config_entry: ConfigEntry) -> PrismOptionsFlow:
    """Get the options flow for this handler."""
    return PrismOptionsFlow(config_entry=config_entry)
