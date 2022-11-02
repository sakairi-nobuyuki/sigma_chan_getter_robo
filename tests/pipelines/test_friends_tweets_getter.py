# coding: utf-8

import pytest

from sigma_chan_getter_robo.tweet_getter.pipelines.friends_tweets_getter import (
    FriendsTweetsPipeline,
)


class TestFriendsTweetsPipeline:
    @pytest.mark.skip
    def test_init(self):
        print("initializing pipeline")
        friends_tweets = FriendsTweetsPipeline()
        print("get tweets")
        res = friends_tweets.get_all_friends_texts_tweets()

        print("type of the get_all_friends_texts_tweets: ", type(res))
        print("result of the get_all_friends_texts_tweets: ", res)

    def test_tweet_getter(self):
        print("initializing pipeline")
        friends_tweets = FriendsTweetsPipeline()
        since_id = None
        print(f">> job_id: hoge\n>> last tweet id: {since_id}")
        print("get tweets")
        res = friends_tweets.get_all_friends_texts_urls_tweets(since_id=None, n_max_items=1000)

        print("type of the get_all_friends_texts_tweets: ", type(res))
        print("result of the get_all_friends_texts_tweets: ", res)


    @pytest.mark.skip
    def test_img_tw(self):
        friends_tweets = FriendsTweetsPipeline()
        friends_tweets.get_all_friends_image_url()
