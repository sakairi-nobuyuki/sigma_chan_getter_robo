# coding: utf-8

from sigma_chan_getter_robo.pre_process.components.operators import set_environmental_variables
from sigma_chan_getter_robo.data_structure.parameters import Parameters

import os

def test_set_environmental_variables(mock_parameters: Parameters) -> None:
    """Test environmental variables setter

    Args:
        mock_parameters (Parameters): Mock parameters
    """
    
    assert isinstance(mock_parameters, Parameters)

    set_environmental_variables(mock_parameters)

    assert os.getenv("GETTER_DB_TYPE") == mock_parameters.database.type
    assert os.getenv("GETTER_DB_HOST") == mock_parameters.endpoint_url