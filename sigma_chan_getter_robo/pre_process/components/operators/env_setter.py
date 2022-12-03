# coding: utf-8

from sigma_chan_getter_robo.data_structure.parameters import Parameters
import os

def set_environmental_variables(parameters: Parameters) -> bool:
    """Setting environ variables.

    Args:
        parameters (Parameters): Parameters 

    Returns:
        bool: True if succeeded, else False.
    """
    os.environ["GETTER_DB_TYPE"] = parameters.database.type
    os.environ["GETTER_DB_USER_NAME"] = parameters.database.user_name
    os.environ["GETTER_DB_PASSWD"] = parameters.database.passwd
    os.environ["GETTER_DB_HOST"] = parameters.endpoint_url
    os.environ["GETTER_DB_NAME"] = parameters.database.database_name

    return True

