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
    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        self.mappings = self.hass.config_entries.options.get(self.config_entry.entry_id, {}).get("mappings", [])

    async def async_step_init(self, user_input=None):
        """First step - show existing mapping and offer to add one."""
        if user_input is not None:
            return await self.async_step_add_mapping()

        # Show current mappings in description for confirmation
        mapping_list = "\n".join([f"- {m.get('calendar_label')}: {m.get('person_entity')} ({m.get('calendar_entity')})" 
                                  for m in user_input.get("mappings", [])]) or "No mappings configured yet."

        return self.async_show_form(
            step_id="init",
            data_schema=Schema({}),
            description_placeholders={"mappings": mapping_list}
        )

    async def async_step_add_mapping(self, user_input=None):
        """Add a single calendar-person mapping."""
        if user_input is not None:
            # Get current mappings and add new one
            existing_mappings = self.hass.config_entries.options.get(self.config_entry.entry_id, {}).get("mappings", [])
            
            new_mapping = {
                "calendar_entity": user_input["calendar_entity"],
                "calendar_label": user_input["calendar_label"],
                "person_entity": user_input["person_entity"]
            }
            
            existing_mappings.append(new_mapping)
            
            # Save to options
            self.hass.config_entries.async_update_entry(
                self.config_entry, 
                options={**self.config_entry.options, "mappings": existing_mappings}
            )
            
            return self.async_create_entry(
                title="",
                data={"mappings": existing_mappings}
            )

        # Get available entities from hass
        calendars = self.hass.states.async_entity_ids("calendar")
        persons = self.hass.states.async_entity_ids("person")

        # Default to first calendar and person if available
        default_calendar = calendars[0] if calendars else ""
        default_person = persons[0] if persons else ""

        return self.async_show_form(
            step_id="add_mapping",
            data_schema=Schema({
                Required("calendar_entity"): str,
                Required("calendar_label"): str,
                Required("person_entity"): str
            }),
            description_placeholders={
                "calendars": calendars,
                "persons": persons
            },
            defaults={
                "calendar_entity": default_calendar,
                "calendar_label": "",
                "person_entity": default_person
            }
        )


async def async_setup_entry(hass, config_entry):
    """Set up Prism HA from a config entry."""
    _LOGGER.debug("Setting up Prism HA for %s", config_entry.entry_id)
    
    # Initialize mappings if not exists in options
    if "mappings" not in config_entry.options:
        hass.config_entries.async_update_entry(config_entry, options={**config_entry.options, "mappings": []})
    
    return True


async def async_unload_entry(hass, entry):
    """Unload a config entry."""
    _LOGGER.debug("Unloading Prism HA for %s", entry.entry_id)
    return True
