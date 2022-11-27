# coding: utf-8

import os
import time
from typing import List

import requests

class Downloader:
    """Download data from internets"""

    def __init__(self) -> None:
        pass

    def dauso_single_object(self, url: str) -> bytes:
        """Download a single file.

        Args:
            url (str): A file url to be downloaded
            file_path (str): A file path to save the file

        Returns:
            bytes: Downloaded object
        """
        response = self.__get_with_retry(url, 10, [500, 502, 503])
        #response = requests.get(url)

        if response.status_code != 200:
            print("Failed to get an image.")
            return False
        if not "image" in response.headers["content-type"]:
            print("The file seems not to be an image: ", response.headers["content-type"])
            return False
        return response.content
        
    
    def dauso_single_file(self, url: str, file_path: str) -> bool:
        """Download a single file.

        Args:
            url (str): A file url to be downloaded
            file_path (str): A file path to save the file

        Returns:
            bool: True if succeeded, else False
        """

        #response = requests.get(url)
        response = self.__get_with_retry(url, 10, [500, 502, 503])

        if response.status_code != 200:
            print("Failed to get an image.")
            return False
        if not "image" in response.headers["content-type"]:
            print("The file seems not to be an image: ", response.headers["content-type"])
            return False

        dir_path = os.path.dirname(file_path)
        if not os.path.exists(dir_path):
            os.makedirs(dir_path)

        if not (isinstance(response.content, bytes) or isinstance(response.content, bytearray)): 
            return False

        with open(file_path, "wb") as f_out:
            f_out.write(response.content)

        if os.path.exists(file_path):
            print("Saved :", file_path)
            return True

        return False

    def configure_file_path_from_url(self, url: str):

        file_name = url.split("/")[-1]
        file_path = os.path.join(self.dir_path, file_name)

        return file_path


    def __get_with_retry(self, url: str, max_retry: int, errors: List[str]):
        for i_try in range(max_retry):
            response = requests.get(url)
            if i_try < max_retry:
                if response.status_code in errors:
                    time.sleep(60.0)
                    continue
            return response
