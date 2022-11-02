# coding: utf-8

import pytest

from sigma_chan_getter_robo.post_process.components.configurator import (
    DatabaseConfigurator,
    LocalStorageCofigurator,
)


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


class TestDatabaseConfigurator:
    @pytest.mark.parametrize("target_type", ["latest", "oldest"])
    def test_init(self, target_type):
        configurator = DatabaseConfigurator("hoge", target_type)

        assert isinstance(configurator, DatabaseConfigurator)

    @pytest.mark.parametrize("target_type", ["latest", "oldest"])
    def test_configure(self, target_type, mock_tweet_getter_dict):
        configurator = DatabaseConfigurator("hoge", target_type)

        if target_type == "latest":
            assert configurator(**mock_tweet_getter_dict) == mock_tweet_getter_dict["max_tweet_id"]
        if target_type == "oldest":
            assert configurator(**mock_tweet_getter_dict) == mock_tweet_getter_dict["min_tweet_id"]
