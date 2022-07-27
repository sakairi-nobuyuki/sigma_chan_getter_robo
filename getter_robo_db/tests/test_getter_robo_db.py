# coding: utf-8

import sqlalchemy
import sqlalchemy.ext.declarative



from getter_robo_db import DatabaseOperator

from getter_robo_db import Base, Engine


import pytest

@pytest.mark.db_operation
class TestDatabaseOperator:
    def test_init(self):
        db = DatabaseOperator()

        assert isinstance(db, DatabaseOperator)

#    def test_print_keys(self):
#        db = DatabaseOperation()
#        res_dict = {"type": "hoge", "name": "hoge", "value": 1.0, "source": "fuga"}
#        columns_list = db._get_columns()
        
#        assert len(columns_list) > 0

#        res = db.load_inference_results_model(res_dict)

        #assert isinstance(res, InferenceResultsModel)
        #assert res.type == res_dict["type"]
        #assert res.name == res_dict["name"]


    #def test_insert(self):
    #    db = DatabaseOperation()
    #    res_dict = {"type": "hoge", "name": "hoge", "value": 1.0, "source": "fuga"}
    #    res = db.load_inference_results_model(res_dict)
    #    db.insert(res)

