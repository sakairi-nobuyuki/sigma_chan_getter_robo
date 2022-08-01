# coding: utf-8

import sqlalchemy
import sqlalchemy.ext.declarative



from getter_robo_db import DatabaseOperator

from getter_robo_db import Base, Engine
from getter_robo_db.models import JobId


import pytest

@pytest.mark.db_operation
class TestDatabaseOperator:
    def test_init(self):
        db = DatabaseOperator()

        assert isinstance(db, DatabaseOperator)

    def test_print_keys(self):
        db = DatabaseOperator()
        columns_list = db._get_columns()
        
        print("  table columns: ", columns_list)

        assert len(columns_list) > 0

        tweet_ids = db.create_job_id_data("hoge")

        assert isinstance(tweet_ids, JobId)
        assert tweet_ids.tweet_id == "hoge"


    def test_insert(self):
        db = DatabaseOperator()
        tweet_ids = db.create_job_id_data("hoge")

        db.insert(tweet_ids)

