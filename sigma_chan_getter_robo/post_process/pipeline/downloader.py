# coding: utf-8

from abc import ABCMeta, abstractmethod
from typing import Any

class Warehouse:
    """Downloading and save file things.
    - Things to be downloaded.
        - Images:
            - jpg, or png files got from internet.
            - each files should be saved into a job_id directory.
            - name of the file is as-is.
        - Words:
            - texts data sorted by each friends. 
            - The file format should be json.
    
    - Directory configuration:

        data --- job_id_1 --- images --- image_1.jpg
              |            |          |- image_2.jpg
              |            |          |- ...
              |            |
              |            |- words --- words.json
              |
              |- job_id_2 --- images --- ...
              |            |- words --- words.json
    
    """
    @abstractmethod
    def __init__(self, job_id: str) -> None:
        self.job_id = job_id
    
    @abstractmethod
    def store(self, src: Any) -> bool:
        pass


class 