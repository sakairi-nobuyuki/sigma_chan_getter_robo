# coding: utf-8

from typing import Any
from sigma_chan_getter_robo.post_process.pipeline.warehouse import Warehouse
from sigma_chan_getter_robo.post_process.io import Downloader
from

class ImageStore(Warehouse):
    """Downloading images"""
    def __init__(self, job_id: str) -> None:
        super().__init__(job_id)
        ### initialize io
        
        ### configure


    def store(self, src: Any) -> bool:
        pass