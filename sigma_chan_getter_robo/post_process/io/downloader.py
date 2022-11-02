# coding: utf-8

import os
import requests

class Downloader:
    """Download data from internets
    """
    def __init__(self) -> None:
        pass


    def dauso_single_file(self, url: str, file_path: str) -> bool:
        """Download a single file.

        Args:
            url (str): A file url to be downloaded
            file_path (str): A file path to save the file

        Returns:
            bool: True if succeeded, else False
        """
        
        response=requests.get(url)

        if response.status_code != 200:
            print("Failed to get an image.")
            return False
        if not "image" in response.headers["content-type"]:
            print("The file seems not to be an image: ", response.headers["content-type"])
            return False

        dir_path = os.path.dirname(file_path)
        if not os.path.exists(dir_path):
            os.makedirs(dir_path)

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
        
    
