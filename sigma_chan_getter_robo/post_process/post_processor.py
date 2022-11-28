# coding: utf-8

import json
import os

from sigma_chan_getter_robo.post_process.components import (
    DatabaseConfigurator,
    DataOrganizer,
    LocalStorageCofigurator,
)
from sigma_chan_getter_robo.post_process.io import S3Storage
from sigma_chan_getter_robo.post_process.pipeline.warehouse import ImageStore
from sigma_chan_getter_robo.sigma_chan_db.db_operators import insert_tweet_id


def save_images_to_bucket(job_id: str, res_dict: dict, bucket: S3Storage) -> bool:
    images_organizer = DataOrganizer(job_id, "images")
    images_list = images_organizer(**res_dict)
    image_store = ImageStore(job_id)

    image_store.store_to_bucket(images_list, bucket)


def save_images(job_id: str, res_dict: dict) -> bool:
    images_organizer = DataOrganizer(job_id, "images")
    images_list = images_organizer(**res_dict)
    image_store = ImageStore(job_id)

    image_store.store(images_list)

    return True


def save_words(job_id: str, res_dict: dict, bucket: S3Storage) -> bool:
    words_organizer = DataOrganizer(job_id, "words")
    words_cofingurator = LocalStorageCofigurator(job_id, "words")
    json_path = words_cofingurator()
    # print("res_dict: ", res_dict)
    res_json = words_organizer(**res_dict)
    res_json_str = json.dumps(res_json)
    bucket.save_data(res_json_str.encode("utf-8"), json_path)

    #    dir_path = os.path.dirname(json_path)

    #    if not os.path.exists(dir_path):
    #        os.makedirs(dir_path)
    #    with open(json_path, "w", encoding="utf-8") as f_out:
    #        json.dump(res_json, f_out, ensure_ascii=False, indent=4)

    return True


def commit_database(job_id: str, res_dict: dict, oldest_latest: str) -> bool:
    db_configurator = DatabaseConfigurator(job_id, oldest_latest)
    tweet_id = db_configurator(**res_dict)

    insert_tweet_id(tweet_id)

    return True


def initialize_bucket(
    type: str = "",
    project_name: str = "",
    bucket_name: str = "",
    endpoint_url: str = "",
    access_id: str = "",
    access_key: str = "",
    region_name: str = "",
) -> S3Storage:
    """Initialize S3 bucket. In this time, using minio.

    Returns:
        S3Storage: initialized instance
    """
    # s3 = S3Storage("s3", "", "getter-robo", "http://localhost:9000/", "sigma-chan", "sigma-chan-dayo", "")
    s3 = S3Storage(
        "s3", "", "getter-robo", "http://192.168.11.10:9000/", "sigma-chan", "sigma-chan-dayo", ""
    )

    return s3
