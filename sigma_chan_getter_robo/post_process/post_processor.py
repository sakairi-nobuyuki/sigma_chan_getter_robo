# coding: utf-8

import json
import os

from sigma_chan_getter_robo.post_process.components import (
    DatabaseConfigurator,
    DataOrganizer,
    LocalStorageCofigurator,
)
from sigma_chan_getter_robo.post_process.pipeline.warehouse import ImageStore
from sigma_chan_getter_robo.sigma_chan_db.db_operators import insert_tweet_id


def save_images(job_id: str, res_dict: dict) -> bool:
    images_organizer = DataOrganizer(job_id, "images")
    images_list = images_organizer(**res_dict)
    image_store = ImageStore(job_id)

    image_store.store(images_list)

    return True


def save_words(job_id: str, res_dict: dict) -> bool:
    words_organizer = DataOrganizer(job_id, "words")
    words_cofingurator = LocalStorageCofigurator(job_id, "words")
    json_path = words_cofingurator()
    # print("res_dict: ", res_dict)
    res_json = words_organizer(**res_dict)
    dir_path = os.path.dirname(json_path)
    if not os.path.exists(dir_path):
        os.makedirs(dir_path)
    with open(json_path, "w", encoding="utf-8") as f_out:
        json.dump(res_json, f_out, ensure_ascii=False, indent=4)

    return True


def commit_database(job_id: str, res_dict: dict, oldest_latest: str) -> bool:
    db_configurator = DatabaseConfigurator(job_id, oldest_latest)
    tweet_id = db_configurator(**res_dict)

    insert_tweet_id(tweet_id)

    return True
