# coding: utf-8


from sigma_chan_getter_robo.tweet_getter.components.operators import *
from sigma_chan_getter_robo.tweet_getter.data_structure import GetterRoboCredentials
from sigma_chan_getter_robo.tweet_getter.io import initialize_tweet_getter_instance


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

        friends_id_list = get_friends_id_list(api)

        print(friends_id_list)

        assert len(friends_id_list) > 0
