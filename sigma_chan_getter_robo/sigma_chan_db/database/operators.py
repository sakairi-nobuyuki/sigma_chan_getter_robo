# coding: utf-8

import datetime
import os
from typing import Dict, Union

import sqlalchemy
import sqlalchemy.ext.declarative
from sqlalchemy.orm import sessionmaker

from sigma_chan_getter_robo.sigma_chan_db.database.models import JobId
from sigma_chan_getter_robo.sigma_chan_db.database.settings import Base, Engine


class DatabaseOperator:
    def __init__(self):
        print("DB operation")
        print("  Creating a sesssion")
        self.engine = Engine
        self.session = sessionmaker(bind=self.engine)()
        
        print("  DB session start.")
        Base.metadata.create_all(bind=self.engine)
        print("  Initialized DB.")

    def create_job_id_data(self, tweet_id: str, job_id: str = None) -> JobId:
        date_time_now = datetime.datetime.now()
        if job_id is not None:
            return JobId(
                job_id = date_time_now.strftime('%Y%m%d%H%M%S'), 
                tweet_id = tweet_id, 
                created_at = date_time_now.strftime('%Y-%m-%d %H:%M:%S'), 
                modified_at = date_time_now.strftime('%Y-%m-%d %H:%M:%S'))
        else:
            return JobId(
                job_id = date_time_now.strftime('%Y%m%d%H%M%S'), 
                tweet_id = tweet_id, 
                created_at = date_time_now.strftime('%Y-%m-%d %H:%M:%S'), 
                modified_at = date_time_now.strftime('%Y-%m-%d %H:%M:%S'))

    def __del__(self):
        self.session.close()
        print("  DB session closed.")
        self.engine.dispose()
        print("  DB engine disposed.")

    def insert(self, res: Base):
        """Insert data to the DB. Data shall be given in the form of DB model."""
        self.session.add(instance=res)
        self.session.commit()

    def get_latest_query(self) -> str:
        """Get latest tweet id in the table"""
        query = self._get_latest_query_in_job_id()

        return query

    def _get_latest_query_in_job_id(self) -> str:

        latest_row = self.session.query(JobId).order_by(JobId.job_id.desc()).first()

        return latest_row


    def _validate_model(self, inp: dict) -> None:
        input_model_key = inp.keys()
        db_model_key = self._get_columns()

        return set(list(input_model_key)+list(["created", "modified", "id"])) == set(db_model_key)

    def _get_columns(self) -> list:
        """Get columns of the table."""
        inspector = sqlalchemy.inspect(self.engine)
        columns = inspector.get_columns("job_id")

        column_name_list = [column["name"] for column in columns]

        return column_name_list
        