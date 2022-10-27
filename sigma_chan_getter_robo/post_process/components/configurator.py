# coding: utf-8

import os
from abc import ABCMeta, abstractmethod
from typing import Any, Callable, Union
from pathlib import Path

class PostprocessConfigurator(metaclass=ABCMeta):
    @abstractmethod
    def __init__(self, job_id: str, target_type: str) -> None:
        self.job_id = job_id
        self.target_type = target_type
        

    @abstractmethod
    def __call__(self, *args: Any, **kwds: Any) -> Any:
        pass



class LocalStorageCofigurator(PostprocessConfigurator):
    def __init__(self, job_id: str, target_type: str) -> None:
        super().__init__(job_id, target_type)
        
        if self.target_type == "images":
            print("Images store configurator: ")
            self.data_dir_path = os.path.join(self.__get_data_storage_path(), "images")
            
            self.configure = self.__configure_image_file_path
        elif self.target_type == "words":
            print("Words store configurator: ")
            self.data_dir_path = os.path.join(self.__get_data_storage_path(), "words")
            self.configure = self.__configure_json_file_path
        else:
            raise NotImplementedError(f"{target_type} is not implemented.")

        print(">> base data dir: ", self.data_dir_path)

    def __call__(self, *args: Any, **kwds: Any) -> Any:
        return self.configure(*args)


    def __configure_json_file_path(self, *args: Any) -> str:
        return os.path.join(self.data_dir_path, "words.json")


    def __configure_image_file_path(self, *args: Any) -> Union[str, bool]:
        if len(args) > 1:
            print(f"Warining: The length of image file is {len(args)}. It should be 1.")

        url = args[0]
        file_name = os.path.basename(url)
        file_extention = file_name.split(".")[-1]

        if file_extention not in ["jpg", "jpeg", "png", "JPEG", "JPG"]:
            return False

        return os.path.join(self.data_dir_path, file_name)

    def __get_data_storage_path(self):
        return os.path.join(str(Path(os.path.abspath(__file__)).parent.parent.parent.parent), self.job_id)

    
        
    
class DatabaseConfigurator(PostprocessConfigurator):
    def __init__(self, job_id: str, target_type: str) -> None:
        print("Post process database configurator:")
        super().__init__(job_id, target_type)
        if self.target_type == "latest":
            print(">> Latest tweet id.")
            self.configure = self.__select_latest_tweet_id
        elif self.target_type == "oldest":
            print(">> Oldest tweet id.")
            self.configure = self.__select_oldest_tweet_id

    def __call__(self, *args: Any, **kwds: Any) -> Any:
        
        return self.configure(**kwds)

    def __select_latest_tweet_id(self, *args: Any, **kwds: dict) -> str:
        
        return kwds["max_tweet_id"]

    def __select_oldest_tweet_id(self, *args: Any, **kwds: dict) -> str:
        
        return kwds["min_tweet_id"]