# coding: utf-8

import pytest


@pytest.fixture
def mock_parameters_dict():
    """Mock parameters in dict for parameters test"""
    return dict(
        endpoint_url="192.168.1.10",
        storage=dict(access_id="sigma_chan", access_key="sigma_chan_dayo", bucket="sigma_chan"),
        database=dict(), tweet=dict() 
    )
