# coding: utf-8

from typing import Optional
import os
from pydantic import BaseModel, validator

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

    endpoint_url: str = None
    database: Optional[DataBaseParameters]
    storage: StorageParameters
    tweet: Optional[TweetParameters]

    @validator("endpoint_url")
    def __validate_endpoint_url(cls, v):
        endpoint_url = os.getenv("ENDPOINT_URL")
        if endpoint_url is None:
            raise ValueError("Environmental variable 'ENDPONT_URL' is not defined")

        return endpoint_url