# coding: utf-8

import json
from sigma_chan_getter_robo.post_process.components import DataOrganizer
from sigma_chan_getter_robo.post_process.components import LocalStorageCofigurator
from sigma_chan_getter_robo.post_process.pipeline.warehouse import ImageStore
from sigma_chan_getter_robo.post_process.components import DatabaseConfigurator
from sigma_chan_getter_robo.sigma_chan_db.db_operators import insert_tweet_id

def save_images(job_id: str, res_dict: dict) -> bool:
    images_organizer = DataOrganizer(job_id, "image")
    images_list = images_organizer(res_dict)
    image_store = ImageStore(job_id)
    image_store.store(images_list)    

    return True

def save_words(job_id: str, res_dict: dict) -> bool:
    words_organizer = DataOrganizer(job_id, "words")
    words_cofingurator = LocalStorageCofigurator(job_id, "images")
    json_path = words_cofingurator()
    res_json = words_organizer(res_dict)

    with open(json_path, "w") as f_out:
        json.dump(res_json, f_out, ensure_ascii=True, indent=4)

    return True

def commit_database(job_id: str, res_dict: dict, oldest_latest: str) -> bool:
    db_configurator = DatabaseConfigurator(job_id, oldest_latest)
    tweet_id = db_configurator(res_dict)

    insert_tweet_id(tweet_id)

    return True