# coding: utf-8

from typing import Optional

from pydantic import BaseModel


class DataBaseParameters(BaseModel):
    """Model of parameters of database 

    Attributes:
        port: str: Port number of the connection.
        type: str: Database type. Only MySQL is available now.
        user_name: str: Usename for the database. "docker" is the default username.
        passwd: str: Password for the database. "docker" is the default.
        database_name: str: Database name to use.
        encoding: str: Test encoding in the database.
        tweet_id_registration: str: Whether "oldest" or "latest" tweet id should be registered to the database.

    Args:
        BaseModel (_type_): _description_
    """
    port: str = "3306"
    type: str = "mysql"
    user_name: str = "docker"
    passwd: str = "docker"
    database_name: str = "getter_robo"
    encoding: str = "utf-8"
    tweet_id_registration: str = "oldest"