# coding: utf-8
import dataclasses
from glob import glob
import json
import os
from pathlib import Path

@dataclasses.dataclass
class GetterRoboCredentials:

    consumer_api_key: str
    consumer_api_secret_key: str
    access_token: str
    access_token_secret: str

    def __init__(self):
        root_dir = Path(os.path.abspath(__file__)).parent.parent.parent.parent
        
        key_path = os.path.join(root_dir, ".key/credentials.json")

        if not os.path.exists(key_path):
            raise FileNotFoundError(f"Credential file is not found.")

        with open(key_path) as f_in:
            credentials_dict = json.load(f_in)

        self.consumer_api_key = credentials_dict["consumer_API_key"]
        self.consumer_api_secret_key = credentials_dict["consumer_API_secret_key"]
        self.access_token = credentials_dict["access_token"]
        self.access_token_secret = credentials_dict["access_token_secret"]
