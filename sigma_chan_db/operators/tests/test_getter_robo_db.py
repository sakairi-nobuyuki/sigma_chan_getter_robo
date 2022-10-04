# coding: utf-8

from database import DatabaseOperator

from database import Base, Engine
from database.models import JobId


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

    def test_get_latest_tweet_id(self) -> str:
        db = DatabaseOperator()
        
        row = db.get_latest_query()

        print("selected db", row)
        print(row.job_id)

        assert row is not None
        
