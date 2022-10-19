# coding: utf-8

import tweepy

from sigma_chan_getter_robo.tweet_getter.data_structure import GetterRoboCredentials


class TweetGetter:
    def __init__(self, credentials: GetterRoboCredentials):

        auth = tweepy.OAuthHandler(
            credentials.consumer_api_key, credentials.consumer_api_secret_key
        )
        auth.set_access_token(credentials.access_token, credentials.access_token_secret)
