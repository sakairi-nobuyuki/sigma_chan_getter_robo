# coding: utf-8

from typing import Any, List

from sigma_chan_getter_robo.post_process.components import LocalStorageCofigurator
from sigma_chan_getter_robo.post_process.io import Downloader
from sigma_chan_getter_robo.post_process.pipeline.warehouse import Warehouse
from sigma_chan_getter_robo.post_process.io import S3Storage
import time

class ImageStore(Warehouse):
    """Downloading images"""

    def __init__(self, job_id: str) -> None:
        super().__init__(job_id)
        ### initialize io
        self.downloader = Downloader()
        ### configure
        self.configurator = LocalStorageCofigurator(job_id, "images")

    def store(self, src: List[str]) -> bool:

        for url in src:
            file_path = self.configurator(url)
            if file_path is False:
                continue
            self.downloader.dauso_single_file(url, file_path)
            time.sleep(30.0)

    def store_to_bucket(self, src: List[str], bucket: S3Storage) -> bool:
        for url in src:
            file_path = self.configurator(url)
            if file_path is False:
                continue
            obj = self.downloader.dauso_single_object(url)

            bucket.save_data(obj, file_path)
            time.sleep(30.0)