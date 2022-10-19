# cofing: utf-8

import tweepy

from tweet_getter.data_structure import GetterRoboCredentials
from tweet_getter.io import initialize_tweet_getter_instance


class TestInitializeTweetGetterInstance:
    def test_init_getter_robo(self):
        credentials = GetterRoboCredentials()
        tw_api = initialize_tweet_getter_instance(credentials)

        assert isinstance(tw_api, tweepy.API)

    def test_getter(self):
        credentials = GetterRoboCredentials()
        api = initialize_tweet_getter_instance(credentials)

        tweets = api.home_timeline()

        print(type(tweets))

        assert len(tweets) > 0
