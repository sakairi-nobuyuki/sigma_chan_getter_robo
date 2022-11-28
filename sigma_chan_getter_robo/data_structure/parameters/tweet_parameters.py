# coding: utf-8

from typing import Optional

from pydantic import BaseModel, PositiveFloat, PositiveInt


class TweetParameters(BaseModel):
    max_items: PositiveInt = 100
    sleep_time: PositiveFloat = 1.0
