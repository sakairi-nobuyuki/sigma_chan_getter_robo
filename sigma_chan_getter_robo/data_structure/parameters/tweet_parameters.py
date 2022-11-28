# coding: utf-8

from typing import Optional

from pydantic import BaseModel, PositiveFloat, PositiveInt


class TweetParameters(BaseModel):
    """Model of the parameters of the tweet retrieval.
    
    Attributes: 
        max_items: PositiveInt: Max numbers of tweets get from one user ID.
        sleep_time: PositiveFloat: Sleep time to avoid access deny.
    """
    max_items: PositiveInt = 100
    sleep_time: PositiveFloat = 1.0
