# coding: utf-8

from typing import Optional

from pydantic import BaseModel


class StorageParameters(BaseModel):
    """Model of the parameters of the storage.

    Attributes:
        port: str: Connection port of the storage.
        type: str: Storage type. Only S3 is available now.
        access_id: str: Access ID of the storage.
        accecc_key: str: Access key of the storage.
        project: str: Project name in your environment. It is an optional parameters.
        bucket: str: Bucket name.

    Args:
        BaseModel (_type_): _description_
    """

    port: str = "9000"
    type: str = "s3"
    access_id: str
    access_key: str
    project: str = Optional[str]
    bucket: str
