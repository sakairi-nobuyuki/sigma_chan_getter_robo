# coding: utf-8

from typing import Optional

from pydantic import BaseModel


class StorageParameters(BaseModel):
    port: str = "9000"
    type: str = "s3"
    access_id: str
    access_key: str
    project: str = Optional[str]
    bucket: str
