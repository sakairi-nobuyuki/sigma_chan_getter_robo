# coding: utf-8

from typing import Union
import os
from sqlalchemy.orm import sessionmaker
import sqlalchemy
import sqlalchemy.ext.declarative

#from models import InferenceResultsModel
from getter_robo_db.models import JobId
from getter_robo_db.settings import Engine, Base
#from settings import Engine, Base



class DatabaseOperator:
    def __init__(self):
        print("DBDBDBDBDBDBDBDBDBDBDBDBDBDB")
        print("  Creating a sesssion")
        
        self.session = sessionmaker(bind=Engine)()
        
        print("  DB session start.")
        Base.metadata.create_all(bind=Engine)
        print("  Initialized DB.")

    def __del__(self):
        self.session.close()
        print("  DB session closed.")

    def insert(self, res: Base):
        """Insert data to the DB. Data shall be given in the form of DB model."""
        self.session.add(instance=res)
        self.session.commit()


    def _validate_model(self, inp: dict) -> None:
        input_model_key = inp.keys()
        db_model_key = self._get_columns()

        return set(list(input_model_key)+list(["created", "modified", "id"])) == set(db_model_key)

    def _get_columns(self) -> list:
        """Get columns of the table."""
        inspector = sqlalchemy.inspect(Engine)
        columns = inspector.get_columns("inference_results")

        column_name_list = [column["name"] for column in columns]

        return column_name_list
        