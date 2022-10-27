# coding: utf-8

import typer
from sigma_chan_getter_robo.tweet_getter.pipelines.friends_tweets_getter import FriendsTweetsPipeline

app = typer.Typer()

@app.command()
def collect_tweet_data_pipeline(all: str = False):
    ### configure data download
    ### TODO: get since_id from the database

    ### TODO: set max datalength

    friends_tweets = FriendsTweetsPipeline()
    res = friends_tweets.get_all_friends_texts_urls_tweets()

    ### create image url list
    
    ### create summary json
    

    ### store data



if __name__ == "__main__":
    app()
