# coding: utf-8

from typing import List, Dict
from tweet_getter.components.operators import get_friends_id_list, get_friends, get_tweets_by_dancer_name, get_tweets_by_dancer_id
from tweet_getter.io import initialize_tweet_getter_instance
from tweet_getter.data_structure import GetterRoboCredentials
import time
import pprint

class FriendsTweetsPipeline:
    def __init__(self) -> None:
        self.api = initialize_tweet_getter_instance(GetterRoboCredentials())
        self.friends = get_friends(self.api)

    def get_all_friends_texts_tweets(self) -> Dict[str, List[str]]:
        return {friend.id: [tweet.text for tweet in get_tweets_by_dancer_id(self.api, friend.id)] for friend in self.friends}
            
    def get_all_friends_image_url(self) -> Dict[str, List[str]]:

        image_url_dict = {}

        for friend in self.friends:
            image_url_dict[friend.id] = []
            for tweet in get_tweets_by_dancer_id(self.api, friend.id):
                
                print(friend.name)

                if "media" in tweet.entities:
                    media = tweet.entities["media"]
                    for medium in media:
                        if medium["type"] == "photo":
                            pprint.pprint(tweet.entities["media"])
                            image_url_dict[friend.id].append(medium["media_url_https"])

                time.sleep(0.1)
        
        return image_url_dict