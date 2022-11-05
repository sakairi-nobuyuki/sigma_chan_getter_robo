# coding: utf-8

from abc import ABCMeta, abstractmethod


class AbstractStorage(metaclass=ABCMeta):
    @abstractmethod
    def __init__(
        self,
        type: str,
        project_name: str,
        bucket_name: str,
        endpoint_url: str,
        access_id: str,
        access_key: str,
        region_name: str,
    ) -> None:
        pass

    @abstractmethod
    def save_image(self, image: bytes) -> bool:
        pass

    @abstractmethod
    def save_json(self, src: dict) -> bool:
        pass
