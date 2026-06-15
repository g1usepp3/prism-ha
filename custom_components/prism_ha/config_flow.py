import logging
from homeassistant import config_entries
from voluptuous import Schema, Required
from .const import DOMAIN

_LOGGER = logging.getLogger(__name__)


class PrismConfigFlow(config_entries.ConfigFlow, domain=DOMAIN):
    VERSION = 1
    MINOR_VERSION = 0
    MAJOR_VERSION = 1

    async def async_step_user(self, user_input=None):
        if user_input is not None:
            return self.async_create_entry(
                title=user_input["household_name"],
                data={"household_name": user_input["household_name"]}
            )

        return self.async_show_form(
            step_id="user",
            data_schema=Schema({
                Required("household_name"): str
            })
        )


class PrismOptionsFlow(config_entries.OptionsFlow):
    async def async_step_init(self, user_input=None):
        if user_input is not None:
            return self.async_show_form(
                step_id="add_mapping",
                data_schema=self.build_add_mapping_schema(user_input.get("mappings", []))
            )

        # Get current mappings from config entry
        mappings = user_input or {}
        
        return self.async_show_form(
            step_id="init",
            data_schema=Schema({})
        )

    def build_add_mapping_schema(self, existing_mappings):
        """Build schema for adding a single mapping row."""
        import homeassistant.helpers.config_validation as cv
        
        # Get available calendar entities and person entities from hass
        calendars = self.hass.states.async_entity_ids("calendar")
        persons = self.hass.states.async_entity_ids("person")

        return Schema({
            Required("calendar_entity"): str,
            Required("calendar_label"): str,
            Required("person_entity"): str
        })

    async def async_step_add_mapping(self, user_input=None):
        if user_input is not None:
            # Add the new mapping to the list
            existing_mappings = self._options.get("mappings", [])
            existing_mappings.append(user_input)
            
            return self.async_create_entry(
                title="",
                data={"mappings": existing_mappings}
            )

        return self.async_show_form(
            step_id="add_mapping",
            data_schema=self.build_add_mapping_schema(self._options.get("mappings", []))
        )


async def async_setup_entry(hass, config_entry):
    """Set up Prism HA from a config entry."""
    _LOGGER.debug("Setting up Prism HA for %s", config_entry.entry_id)
    return True
