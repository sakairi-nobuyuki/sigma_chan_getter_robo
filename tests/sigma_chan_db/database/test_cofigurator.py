# coding: utf-8

import pytest
from sigma_chan_getter_robo.sigma_chan_db.database import DatabaseEngine
from sigma_chan_getter_robo.data_structure.parameters import Parameters
from sqlalchemy.engine import Engine
from sqlalchemy.orm import Session

class TestDatabaseEngine:
    """Testing SQLAlchemy create engine"""
    def test_init(self, mock_parameters):
        """Testing constructor"""
        assert isinstance(mock_parameters, Parameters)
        parameters = mock_parameters
        parameters.endpoint_url = "192.168.11.10"

        db_engine = DatabaseEngine(mock_parameters)
        print("Test DB configure")
        assert isinstance(db_engine, DatabaseEngine)
        print(">> engine: ", db_engine.engine, type(db_engine.engine))
        assert isinstance(db_engine.engine, Engine)

        print(">> type Base: ", db_engine.base, type(db_engine.base))
        
        

