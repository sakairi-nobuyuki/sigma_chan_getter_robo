# coding: utf-8

from typing import Optional

from pydantic import BaseModel

from sigma_chan_getter_robo.data_structure.parameters import (
    DataBaseParameters,
    StorageParameters,
    TweetParameters,
)


class Parameters(BaseModel):
    """Parameters for getter robo.

    Attributes:
        endpoint_url: Endpoint URL of the local storage and database. It shold be in a form of IPv4.
        database: DataBaseParameters
        storage: StorageParameters
        tweet: TweetParameters

    Args:
        BaseModel (_type_): _description_
    """

    endpoint_url: str
    database: Optional[DataBaseParameters]
    storage: StorageParameters
    tweet: Optional[TweetParameters]
