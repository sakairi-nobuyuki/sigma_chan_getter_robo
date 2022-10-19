# coding: utf-8

import tweepy

from sigma_chan_getter_robo.tweet_getter.data_structure import GetterRoboCredentials


def initialize_tweet_getter_instance(credentials: GetterRoboCredentials) -> tweepy.API:
    auth = tweepy.OAuthHandler(credentials.consumer_api_key, credentials.consumer_api_secret_key)
    auth.set_access_token(credentials.access_token, credentials.access_token_secret)

    return tweepy.API(auth, wait_on_rate_limit=True, timeout=600)
