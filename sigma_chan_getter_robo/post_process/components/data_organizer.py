# coding: utf-8

from typing import Any, List, Dict, Union

class DataOrganizer:
    def __init__(self, job_id: str, target_type: str) -> None:
        self.job_id = job_id
        self.target_type = target_type
        if self.target_type not in ["images", "words"]:
            raise NotImplementedError(f"In data organizer, {self.target_type} is not implemented.")

    def __call__(self, **kwds: Any) -> List[str]:
        if self.target_type == "images":
            res = self.__extract_images_urls(kwds)
        elif self.target_type == "words":
            res = self.__extract_words(kwds)

        return res


    def __extract_images_urls(self, input_dict: Dict[str, Dict[str, List[str]]]) -> List[str]:
        url_list = []
        for input in input_dict.values():
            url_list.extend(input["image_url"])

        return url_list
    
    def __extract_words(self, input_dict: Dict[str, Dict[str, List[str]]]) -> List[str]:
        return {input_key: input_value["text"] for input_key, input_value in input_dict.items()}

