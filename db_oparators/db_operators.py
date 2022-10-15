# coding: utf-8

import typer
from database import DatabaseOperator

app = typer.Typer()


@app.command("insert")
def insert_tweet_id(tweet_id: str) -> None:
    db = DatabaseOperator()

    tweet_ids = db.create_job_id_data(tweet_id)

    db.insert(tweet_ids)


@app.command("get-latest-query")
def get_latest_tweet_id() -> str:
    db = DatabaseOperator()

    tweet_id = db.get_latest_query().tweet_id

    return tweet_id


if __name__ == "__main__":
    app()
