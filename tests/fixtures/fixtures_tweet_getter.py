# coding: utf-8

import pytest


@pytest.mark.fixture
def mock_tweet_getter_dict() -> dict:
    return {
        "friend_1": {
            "text": ["w_11", "w_12", "w_13"],
            "image_url": ["url_11", "url_12", "url_13"]
        },
        "friend_2": {
            "text": ["w_21", "w_22", "w_23"],
            "image_url": ["url_21", "url_22", "url_23"]
        },
        "friend_3": {
            "text": ["w_31", "w_32", "w_33"],
            "image_url": ["url_31", "url_32", "url_33"]
        }
    }