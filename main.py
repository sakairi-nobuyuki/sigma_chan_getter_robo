# coding: utf-8

import typer

from sigma_chan_getter_robo.post_process import (
    commit_database,
    initialize_bucket,
    save_images_to_bucket,
    save_words,
)
from sigma_chan_getter_robo.pre_process import configure_since_id, issue_new_job_id
from sigma_chan_getter_robo.pre_process.components.operators import load_parameters
from sigma_chan_getter_robo.tweet_getter.pipelines.friends_tweets_getter import (
    FriendsTweetsPipeline,
)

app = typer.Typer()


@app.command("tweet_getter")
def tweet_getter_pipeline(parameters_str: str) -> None:
    # def tweet_getter_pipeline(max_data_length: int = 10000) -> None:
    print("Tweet getter robo")

    parameters = load_parameters(parameters_str)
    print(">> parameters: ", parameters)

    ### configure data download
    since_id = configure_since_id()
    job_id = issue_new_job_id()
    print(f">> job_id: {job_id}\n>> last tweet id: {since_id}")

    try:
        ### get tweet
        print(f">> initializing tweet getter pipeline")
        friends_tweets = FriendsTweetsPipeline(parameters.tweet)
        print(f">> getting tweets")
        if since_id is None:
            print(">>   since_id is not found.")
            res = friends_tweets.get_all_friends_texts_urls_tweets(
                #since_id=None, n_max_items=parameters.tweet.max_items
                n_max_items=parameters.tweet.max_items
            )
        else:
            print(f">>    since_id: {since_id}")
            res = friends_tweets.get_all_friends_texts_urls_tweets(
                since_id=since_id, n_max_items=parameters.tweet.max_items
            )

        ### store data
        print(">> post-processing")
        print(">>   initializing bucket: ")
        bucket = initialize_bucket(parameters)
        save_words(job_id, res, bucket)
        save_images_to_bucket(job_id, res, bucket)
    except Exception as e:
        print(">> something was wrong: ", e)
    commit_database(job_id, res, "latest")
    # commit_database(job_id, res, "oldest")
    print(">> Completed")
    return True


if __name__ == "__main__":
    app()
