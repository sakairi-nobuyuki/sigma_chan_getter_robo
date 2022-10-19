# coding: utf-8

import typer

from sigma_chan_getter_robo.tweet_getter.pipelines.friends_tweets_getter import FriendsTweetsPipeline

app = typer.Typer()


@app.command()
def get_friends_tweet(type: str):
    friends_tweets = FriendsTweetsPipeline()

    if type == "text":
        friends_tweets.get_all_friends_texts_tweets()
    elif type == "image_url":
        friends_tweets.get_all_friends_image_url()
    else:
        raise NotImplementedError(f"In get friends tweet getter, {type} is not implemented.")
