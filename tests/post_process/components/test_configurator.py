# coding: utf-8

from sigma_chan_getter_robo.post_process.components.configurator import LocalStorageCofigurator
import pytest


class TestStorageCofigurator:
    @pytest.mark.parametrize("target_type", ["images", "words"])
    def test_init(self, target_type):

        storage = LocalStorageCofigurator("hoge", target_type)

        assert isinstance(storage, LocalStorageCofigurator)
        assert storage.target_type == target_type
        assert storage.job_id == "hoge"

    def test_init_failure(self):

        with pytest.raises(NotImplementedError):
            storage = LocalStorageCofigurator("hoge", "image")

    def test_images_files_configurator(self):
        storage = LocalStorageCofigurator("hoge", "images")

        mock_url = "http://hoge/piyo/fuga.png"

        file_path = storage(mock_url)

        assert file_path.split("/")[-1] == mock_url.split("/")[-1]
        assert file_path.split("/")[-2] != mock_url.split("/")[-2]

    def test_image_files_configuretaor_failure(self):
        storage = LocalStorageCofigurator("hoge", "images")

        mock_url = "http://hoge/piyo/fuga.mov"

        assert storage(mock_url) is False

    def test_words_configurator(self):
        storage = LocalStorageCofigurator("hoge", "words")

        assert storage().split("/")[-1] == "words.json"
