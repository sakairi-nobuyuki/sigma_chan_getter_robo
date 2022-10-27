# coding: utf-8

import pytest

from sigma_chan_getter_robo.tweet_getter.pipelines.friends_tweets_getter import (
    FriendsTweetsPipeline,
)


class TestFriendsTweetsPipeline:
    def test_init(self):
        friends_tweets = FriendsTweetsPipeline()
        res = friends_tweets.get_all_friends_texts_urls_tweets(n_max_items=10)

        assert isinstance(res, dict)
        assert len(list(res.keys())) > 2
        assert isinstance(res[list(res.keys())[0]]["text"], list)
        assert isinstance(res[list(res.keys())[0]]["text"][0], str)
        assert isinstance(res[list(res.keys())[0]]["image_url"], list)

    def test_get_tweet_with_since_id(self):
        friends_tweets = FriendsTweetsPipeline()
        res = friends_tweets.get_all_friends_texts_urls_tweets(
            since_id=int((1582389144034349063 + 1574743392546066432) / 2), n_max_items=10
        )

        assert isinstance(res, dict)
        assert len(list(res.keys())) > 2
        assert isinstance(res[list(res.keys())[0]]["text"], list)
        assert isinstance(res[list(res.keys())[0]]["text"][0], str)
        assert isinstance(res[list(res.keys())[0]]["image_url"], list)
        assert int(res["max_tweet_id"]) > 1574743392546066432

    @pytest.mark.skip
    def test_img_tw(self):
        friends_tweets = FriendsTweetsPipeline()
        friends_tweets.get_all_friends_image_url()
