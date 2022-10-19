# coding: utf-8

import pytest

from sigma_chan_getter_robo.tweet_getter.pipelines.friends_tweets_getter import FriendsTweetsPipeline


class TestFriendsTweetsPipeline:
    def test_init(self):
        print("initializing pipeline")
        friends_tweets = FriendsTweetsPipeline()
        print("get tweets")
        res = friends_tweets.get_all_friends_texts_tweets()

        print("type of the get_all_friends_texts_tweets: ", type(res))
        print("result of the get_all_friends_texts_tweets: ", res)

    @pytest.mark.skip
    def test_img_tw(self):
        friends_tweets = FriendsTweetsPipeline()
        friends_tweets.get_all_friends_image_url()
