# coding: utf-8

from tweet_getter.pipelines.friends_tweets_getter import FriendsTweetsPipeline
import pytest


class TestFriendsTweetsPipeline:
    @pytest.mark.skip
    def test_init(self):
        friends_tweets = FriendsTweetsPipeline()
        friends_tweets.get_all_friends_texts_tweets()


    def test_img_tw(self):
        friends_tweets = FriendsTweetsPipeline()
        friends_tweets.get_all_friends_image_url()
