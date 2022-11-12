# coding: utf-8

import datetime
from typing import Union

from sigma_chan_getter_robo.sigma_chan_db.db_operators import get_latest_tweet_id


def configure_since_id() -> Union[str, bool]:
    latest_tweet_id = get_latest_tweet_id()

    if latest_tweet_id == "hoge":
        return None
    else:
        return latest_tweet_id


def issue_new_job_id() -> str:
    return datetime.datetime.now().strftime("%Y%m%d%H%M%S")
