# coding: utf-8

from pydantic import BaseModel

from sigma_chan_getter_robo.data_structure.parameters import (
    DataBaseParameters,
    StorageParameters,
    TweetParameters,
)


class Parameters(BaseModel):
    """Parameters for getter robo.

    Args:
        BaseModel (_type_): _description_
    """

    endpoint_url: str
    database: DataBaseParameters
    storage: StorageParameters
    tweet: TweetParameters
