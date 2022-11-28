# coding: utf-8

from typing import Optional

from pydantic import BaseModel


class DataBaseParameters(BaseModel):
    port: str = "3306"
    type: str = "mysql"
    user_name: str = "docker"
    passwd: str = "docker"
    database_name: str = "getter_robo"
    encoding: str = "utf-8"
