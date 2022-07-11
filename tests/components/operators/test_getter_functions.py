# coding: utf-8


from tweet_getter.components.operators import *
from tweet_getter.io import initialize_tweet_getter_instance
from tweet_getter.data_structure import GetterRoboCredentials


class TestGetterFunctions:
    def test_getters(self):
        credentials = GetterRoboCredentials()
        api = initialize_tweet_getter_instance(credentials)

        assert isinstance(get_tweets_by_keyword(api, "おじさん"), tweepy.cursor.ItemIterator)
        assert isinstance(get_tweets_by_dancer_name(api, ""), tweepy.cursor.ItemIterator)

    def test_get_friends(self):
        credentials = GetterRoboCredentials()
        api = initialize_tweet_getter_instance(credentials)

        friends = get_friends(api)

        assert isinstance(friends, tweepy.cursor.ItemIterator)
        