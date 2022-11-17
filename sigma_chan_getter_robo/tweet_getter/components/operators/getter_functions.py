# coding: utf-8

from cmath import inf
from typing import Any, Dict, List

import tweepy


def get_tweets_by_keyword(tw_api: tweepy.API, keyword: str, n_max_items: int = inf):

    return tweepy.Cursor(tw_api.search_tweets, q=keyword, exclude_replies=True).items(n_max_items)


def get_tweets_by_dancer_name(tw_api: tweepy.API, dancer_name: str, n_max_items: int = inf):

    return tweepy.Cursor(
        tw_api.user_timeline, screen_name=dancer_name, exclude_replies=True
    ).items(n_max_items)


def get_tweets_by_dancer_id(
    tw_api: tweepy.API, user_id: str, n_max_items: int = inf, since_id: str = None
) -> tweepy.cursor.ItemIterator:

    res_iterator = tweepy.Cursor(
        tw_api.user_timeline,
        user_id=user_id,
        exclude_replies=True,
        tweet_mode="extended",
        #include_entities=True,
        since_id=since_id,
    ).items(n_max_items)
    return res_iterator


def get_friends(tw_api: tweepy.API, n_max_items: int = inf):
    return tweepy.Cursor(tw_api.get_friends).items(n_max_items)


def get_friends_id_list(tw_api: tweepy.API, n_max_items: int = inf):
    return [friend.id for friend in get_friends(tw_api, n_max_items)]
