# coding: utf-8


from tweet_getter.components.operators import *
from tweet_getter.io import initialize_tweet_getter_instance
from tweet_getter.data_structure import GetterRoboCredentials


class TestGetterFunctions:
    def test_getters(self):
        credentials = GetterRoboCredentials()
        api = initialize_tweet_getter_instance(credentials)

        for item in get_tweets_by_keyword(api, "おじさん"):
            print(item.text)

        for item in get_tweets_by_dancer_name(api, ""):
            print(item.text)