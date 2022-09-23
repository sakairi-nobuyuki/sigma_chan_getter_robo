# coding: utf-8

from database import DatabaseOperator

import typer

app = typer.Typer()

@app.command("insert")
def insert_tweet_id(tweet_id: str) -> None:
    db = DatabaseOperator()
    
    tweet_ids = db.create_job_id_data(tweet_id)
    
    db.insert(tweet_ids)

@app.command("get_latest")
def get_latest_tweet_id() -> str:
    pass


if __name__ == "__main__":
    app()
    