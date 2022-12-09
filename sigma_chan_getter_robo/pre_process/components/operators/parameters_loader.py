# coding: utf-8

import json

from sigma_chan_getter_robo.data_structure.parameters import Parameters


def load_parameters(parameters_str: str) -> Parameters:

    parameters_dict = json.loads(parameters_str)

    return Parameters(**parameters_dict)
