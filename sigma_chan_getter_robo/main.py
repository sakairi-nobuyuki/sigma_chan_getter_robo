# coding: utf-8

import typer

from sigma_chan_getter_robo.post_process import commit_database, save_images, save_words
from sigma_chan_getter_robo.pre_process import configure_since_id, issue_new_job_id
from sigma_chan_getter_robo.tweet_getter.pipelines.friends_tweets_getter import (
    FriendsTweetsPipeline,
)

app = typer.Typer()


@app.command("tweet_getter")
def tweet_getter_pipeline(max_data_length: int = 1000) -> None:
    print("Tweet getter robo")

    ### configure data download
    since_id = configure_since_id()
    job_id = issue_new_job_id()
    print(f">> job_id: {job_id}\n>> last tweet id (since_id): {since_id}")

    ### get tweet
    print(f">> initializing tweet getter pipeline")
    friends_tweets = FriendsTweetsPipeline()
    print(f">> getting tweets")
    res = friends_tweets.get_all_friends_texts_urls_tweets(
        since_id=since_id, n_max_items=max_data_length
    )

    ### store data
    print(">> post-processing")
    save_words(job_id, res)
    save_images(job_id, res)
    commit_database(job_id, res, "oldest")
    print(">> Completed")
    return True


if __name__ == "__main__":
    app()
