# coding: utf-8

import pytest
from sigma_chan_getter_robo.data_structure.parameters import Parameters

@pytest.fixture
def mock_parameters_dict():
    """Mock parameters in dict for parameters test"""
    return dict(
        endpoint_url="192.168.1.10",
        storage=dict(access_id="sigma_chan", access_key="sigma_chan_dayo", bucket="sigma_chan"),
        database=dict(),
        tweet=dict(),
    )


@pytest.fixture
def mock_parameters_str():
    """Mock parameters for getter-robo in string."""
    parameters_str = '{"endpoint_url": "192.168.1.1", "storage": {"access_id": "sigma_chan", "access_key": "sigma_chan_dayo", "bucket": "getter_robo"}}'
    return parameters_str

@pytest.fixture
def mock_parameters():
    """Mock parameters as an instance of Parameters"""
    return Parameters(**dict(
        endpoint_url="192.168.1.10",
        storage=dict(access_id="sigma_chan", access_key="sigma_chan_dayo", bucket="sigma_chan"),
        database=dict(),
        tweet=dict(),
    ))
