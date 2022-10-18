# coding: utf-8

import pytest

from tweet_getter.pipelines.friends_tweets_getter import FriendsTweetsPipeline


class TestFriendsTweetsPipeline:
    def test_init(self):
        friends_tweets = FriendsTweetsPipeline()
        friends_tweets.get_all_friends_texts_tweets(n_max_items=10)

    @pytest.mark.skip
    def test_img_tw(self):
        friends_tweets = FriendsTweetsPipeline()
        friends_tweets.get_all_friends_image_url()
