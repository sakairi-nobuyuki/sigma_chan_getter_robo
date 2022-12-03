# coding: utf-8


from sqlalchemy import create_engine
from sqlalchemy.engine import Engine
from sqlalchemy.ext.declarative import declarative_base
from sqlalchemy.orm import scoped_session, sessionmaker

from sigma_chan_getter_robo.data_structure.parameters import Parameters



class DatabaseEngine:
    def __init__(self, parameters: Parameters):
        self.parameters = self.__validate_parameters(parameters)
        self.engine = self.__create_engine(parameters)
        self.session = scoped_session(sessionmaker(autocommit=False, autoflush=False, bind=self.engine))

        self.base = declarative_base()
        self.base.query = self.session.query_property()
        
    @classmethod
    def __create_engine(cls, parameters: Parameters) -> Engine:

        db_parameters = parameters.database
        db_url = f"{db_parameters.type}://{db_parameters.user_name}:{db_parameters.passwd}@{parameters.endpoint_url}:{db_parameters.port}/{db_parameters.database_name}?charset=utf8"

        if not isinstance(db_url, str):
            raise TypeError(f"DB URL is type is not string: {type(db_url)}")
        
        engine = create_engine(db_url, encoding="utf-8", echo=True)

        if not isinstance(engine, Engine):
            raise TypeError(f"Engine creation is failed: {type(engine)}")

        return engine

    @classmethod
    def __validate_parameters(cls, parameters: Parameters) -> Parameters:
        """Validating the parameter is its type is correct.

        Args:
            parameters (Parameters): Parameters
        """
        if not isinstance(parameters, Parameters):
            raise TypeError(f"prameters in DatabaseEngine is not that of Parameters: {parameters}")

        return parameters
        