# coding: utf-8

from cmath import inf
import tweepy


def get_tweets_by_keyword(tw_api: tweepy.API, keyword: str, n_max_items: int = inf):
    return tweepy.Cursor (tw_api.search_tweets, q = keyword, exclude_replies = True).items(n_max_items)


def get_tweets_by_dancer_name(tw_api: tweepy.API, dancer_name: str, n_max_items: int = inf):
    return tweepy.Cursor (tw_api.user_timeline, screen_name = dancer_name, exclude_replies = True).items(n_max_items)
