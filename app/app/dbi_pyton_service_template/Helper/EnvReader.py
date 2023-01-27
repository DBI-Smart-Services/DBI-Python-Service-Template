"""
This File is part of the Rudi Project

In this File there is a Cached Function that returns a Config Dictionary
which will include all the necessary config values if they arent set in the environment
"""

from dataclasses import dataclass
from functools import cache
from dotenv import load_dotenv
import os

def get_value_for_key(key, default=None):
    """
    Returns the value for a key from the environment.
    If the key is not set in the environment, the default value is returned.

    :param key: The key to get the value for
    :param default: The default value to return if the key is not set in the environment

    :return: The value for the key
    """
    environment_value = os.getenv(key)
    if environment_value:
        return environment_value
    return default

def str_to_bool(data):
    """
    Converts a string to a boolean value

    :param data: The string to convert

    :return: The boolean value
    """
    if data == "True":
        return True
    elif data == "False":
        return False
    else:
        raise ValueError("The value is not a boolean")

@dataclass
class Config:
    """
    Config Class to hold all the Config Values
    """

    def _populate(self):
        # Port of the Application
        self.port = get_value_for_key("PORT", 4000)
        # debug flag
        self.debug = str_to_bool(get_value_for_key("DEBUG", "True"))

def get_system_default_config():
    """
    This Function returns a Dictionary with all the necessary Config Values.
    The Function checks for an env file in the root directory of the project.
    If the file is found, it will be loaded and the values will be set in the
    environment. If the file is not found, the function will return a dictionary
    with the environment variables or default values.

    :return:    A Config Dataclass
    """

    # print environment variables
    config_env = Config()
    config_env._populate()
    return config_env