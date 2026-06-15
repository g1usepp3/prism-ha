import logging
from homeassistant import config_entries
from homeassistant.helpers import selector
from homeassistant.helpers.config_validation import cv, Schema, Required
from . import DOMAIN

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
            return self.async_create_entry(title="", data=user_input)

        return self.async_show_form(
            step_id="init",
            data_schema=Schema({
                Required("calendar_entity"): str,
                Required("person_name"): str,
                "color_override": str
            })
        )


async def async_setup_entry(hass, config_entry):
    """Set up Prism HA from a config entry."""
    _LOGGER.debug("Setting up Prism HA for %s", config_entry.entry_id)
    return True
