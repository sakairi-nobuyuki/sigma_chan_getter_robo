# coding: utf-8

import pytest
from sigma_chan_getter_robo.post_process.components import DataOrganizer

class TestDataOrganizer:
    @pytest.mark.parametrize("target_type", ["images", "words"])
    def test_init(self, target_type):
        organizer = DataOrganizer("hoge", target_type)

        assert isinstance(organizer, DataOrganizer)
        assert organizer.target_type == target_type

    @pytest.mark.parametrize("target_type", ["images", "words"])
    def test_image_organize(self, target_type, mock_tweet_getter_dict):
    
        organizer = DataOrganizer("hoge", target_type)

        res = organizer(**mock_tweet_getter_dict)
        if target_type == "images":
            assert isinstance(res, list)
            assert len(res) == 9
        if target_type == "words":
            assert isinstance(res, dict)
            assert len(res) == 3
