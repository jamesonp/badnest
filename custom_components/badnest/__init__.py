"""The example integration."""
import voluptuous as vol
from homeassistant.helpers import config_validation as cv

from .api import NestAPI
from .const import (
    DOMAIN,
    CONF_ISSUE_TOKEN,
    CONF_COOKIE,
    CONF_USER_ID,
    CONF_ACCESS_TOKEN,
    CONF_CAMERA_EVENT_IMPORTANT,
    CONF_CAMERA_EVENT_MINUTES,
    CONF_CAMERA_EVENT_TIMEOUT,
)

CONFIG_SCHEMA = vol.Schema(
    {
        DOMAIN: vol.All(
            {
                vol.Required(CONF_USER_ID, default=""): cv.string,
                vol.Required(CONF_ACCESS_TOKEN, default=""): cv.string,
            },
            {
                vol.Required(CONF_ISSUE_TOKEN, default=""): cv.string,
                vol.Required(CONF_COOKIE, default=""): cv.string,
            },
            {
                vol.Optional(CONF_CAMERA_EVENT_IMPORTANT, default=True): cv.boolean,
                vol.Optional(CONF_CAMERA_EVENT_MINUTES, default=120): cv.positive_int,
                vol.Optional(CONF_CAMERA_EVENT_MINUTES, default=1): cv.positive_int,
            },
        )
    },
    extra=vol.ALLOW_EXTRA,
)


def setup(hass, config):
    """Set up the badnest component."""
    if config.get(DOMAIN) is not None:
        user_id = config[DOMAIN].get(CONF_USER_ID)
        access_token = config[DOMAIN].get(CONF_ACCESS_TOKEN)
        issue_token = config[DOMAIN].get(CONF_ISSUE_TOKEN)
        cookie = config[DOMAIN].get(CONF_COOKIE)
        camera_only_important = config[DOMAIN].get(CONF_CAMERA_EVENT_IMPORTANT)
        camera_event_minutes = config[DOMAIN].get(CONF_CAMERA_EVENT_MINUTES)
        camera_event_timeout = config[DOMAIN].get(CONF_CAMERA_EVENT_TIMEOUT)
    else:
        email = None
        password = None
        issue_token = None
        cookie = None
        camera_only_important = True
        camera_event_minutes = 120
        camera_event_timeout = 1

    hass.data[DOMAIN] = {
        "api": NestAPI(
            user_id,
            access_token,
            issue_token,
            cookie,
            camera_only_important,
            camera_event_minutes,
            camera_event_timeout,
        ),
    }

    return True
