# coding: utf-8

from sigma_chan_getter_robo.data_structure.parameters import Parameters
from sigma_chan_getter_robo.pre_process.components.operators import load_parameters


def test_load_parameters(mock_parameters_str):
    """Test load_parameters"""
    assert isinstance(mock_parameters_str, str)

    parameters_dict = load_parameters(mock_parameters_str)

    assert isinstance(parameters_dict, Parameters)
