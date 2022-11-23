# coding: utf-8

import pprint
import time
from cmath import inf
from copy import deepcopy
from typing import Any, Dict, List

import tweepy

from sigma_chan_getter_robo.tweet_getter.components.operators import (
    get_friends,
    get_tweets_by_dancer_id,
)
from sigma_chan_getter_robo.tweet_getter.data_structure import GetterRoboCredentials
from sigma_chan_getter_robo.tweet_getter.io import initialize_tweet_getter_instance


class FriendsTweetsPipeline:
    def __init__(self) -> None:
        self.api = initialize_tweet_getter_instance(GetterRoboCredentials())
        print(">> api: ", self.api)
        self.friends = get_friends(self.api, n_max_items=1000)
        print(">> friends: ", self.friends)
        
    def get_all_friends_texts_urls_tweets(
        self, since_id: str = None, n_max_items: int = inf
    ) -> Dict[str, List[str]]:
        """Get tweets of my friends.

        Args:
            since_id (str, optional): Get tweet posted after the since_id. Defaults to None.

        Returns:
            Dict[str, List[str]]: Tweets of my friends in a list.
            {
                friend_id_1:
                    {
                        "text": [text of tweet_1, text of tweet_2, ...],
                        "image_url":
                            [
                                1st image url of tweet_1, 2nd image url of tweet_1, ...,
                                1st image url of tweet_2, 2nd image url of tweet_2, ...,
                                ...
                            ]
                    },
                friend_id_2:
                    ...,
                max_tweet_id: str: "The latest tweet ID in the getter tweet."
                min_tweet_id: str: "The oldest tweet ID in the getter tweet."
            }
        """
        print(">> Get friends tweets, it's texts and image urls")
        res_dict = {}
        tweet_id_list = []
        
        i_friend = 0
        for friend in self.friends:
        #for i_friend, friend in enumerate(self.friends):            
            print(f">> {i_friend} th friends tweet")
            i_friend += 1
            ### get texts
            res_iterator = get_tweets_by_dancer_id(
                self.api, friend.id, since_id=int(since_id), n_max_items=int(n_max_items)
            )
            text_dict = self.__get_text_dict(res_iterator)
            time.sleep(10.0)

            ### get image urls
            res_iterator = get_tweets_by_dancer_id(
                self.api, friend.id, since_id=since_id, n_max_items=n_max_items
            )
            image_url_dict = self.__get_image_url_dict(res_iterator)

            ### summarize results
            res_dict = self.__summarize_result_dict(
                res_dict,
                self.__flatten_texts_and_image_urls(text_dict, image_url_dict),
                friend.name,
                friend.id,
            )

            ### tweet id
            tweet_id_list.extend(map(int, text_dict.keys()))
            tweet_id_list.extend(map(int, image_url_dict.keys()))

            time.sleep(0.1)

        res_dict["max_tweet_id"] = max(tweet_id_list)
        res_dict["min_tweet_id"] = min(tweet_id_list)
        print(
            ">>  res_dict is: ",
        )
        pprint.pprint(res_dict)


        return res_dict

    def __summarize_result_dict(
        self,
        res_dict: Dict[str, Any],
        friends_tweet_dict: Dict[str, Any],
        friend_name: str,
        friend_id: str,
    ) -> Dict[str, Any]:
        if isinstance(friend_id, int):
            friend_id = str(friend_id)

        res_dict[friend_id] = {}
        res_dict[friend_id]["text"] = friends_tweet_dict["text"]
        res_dict[friend_id]["image_url"] = friends_tweet_dict["image_url"]
        res_dict[friend_id]["friend_name"] = friend_name

        return res_dict

    def __flatten_texts_and_image_urls(
        self, text_dict: Dict[str, str], image_url_dict: Dict[str, List[str]]
    ) -> Dict[str, Any]:
        """Flatten the lists of texts and image urls get by the tweet API regardless to the tweet id.

        Args:x
            text_dict (Dict[str, str]): Tweet text list of a friend
                {
                    tweet_id_1: tweet of tweet_id_1,
                    tweet_id_2: tweet of tweet_id_2,
                    ...
                }
            image_url_dict (Dict[str, List[str]]): Image url list dict of a friend.
                {
                    tweet_id_1: [1st image url of tweet_id_1, 2nd  image url of tweet_id_1 if exists, ...],
                    tweet_id_2: [1st image url of tweet_id_2, 2nd  image url of tweet_id_2 if exists, ...],
                    ...
                }

        Returns:
            Dict[str, Any]:
                {
                    "text": [text of tweet_1, text of tweet_2, ...],
                    "image_url":
                        [
                            1st image url of tweet_1, 2nd image url of tweet_1, ...,
                            1st image url of tweet_2, 2nd image url of tweet_2, ...,
                            ...
                        ]
                }
        """

        text_list = []
        for tweet_id in text_dict.keys():
            text_list.append(text_dict[tweet_id])

        image_urls_list = []
        for tweet_id in image_url_dict.keys():
            image_urls_list.append(image_url_dict[tweet_id])
        # image_urls_list = [image_url for image_url in image_urls for image_urls in image_urls_list]
        image_urls_list = [image_url for image_urls in image_urls_list for image_url in image_urls]

        return dict(text=text_list, image_url=image_urls_list)

    def __get_text_dict(self, res_iterator: tweepy.cursor.ItemIterator) -> Dict[str, str]:
        """Get twett text in dictionary style from the tweet iterator of a friend.

        Args:
            res_iterator (tweepy.cursor.ItemIterator): An iterator of retrieved tweet of a friend.

        Returns:
            Dict[str, str]: _description_

            {
                tweet_id_1: tweet of tweet_id_1,
                tweet_id_2: tweet of tweet_id_2,
                ...
            }
        """

        res_dict = {}
        for res in res_iterator:
            # print(">> res keys: ", res._json.keys())
            # pprint.pprint(res._json)
            if "text" in res._json.keys():
                res_dict[res._json["id_str"]] = res._json["text"]
            if "full_text" in res._json.keys():
                res_dict[res._json["id_str"]] = res._json["full_text"]
        return res_dict

    def __get_image_url_dict(
        self, res_iterator: tweepy.cursor.ItemIterator
    ) -> Dict[str, List[str]]:
        """Get twett text in dictionary style from the tweet iterator of a friend.

        Args:
            res_iterator (tweepy.cursor.ItemIterator): An iterator of retrieved tweet of a friend.

        Returns:
            Dict[str, str]: _description_

            {
                tweet_id_1: [1st image url of tweet_id_1, 2nd  image url of tweet_id_1 if exists, ...],
                tweet_id_2: [1st image url of tweet_id_2, 2nd  image url of tweet_id_2 if exists, ...],
                ...
            }
        """

        res_dict = {}

        for res in res_iterator:
            # print("res json in url image getter: ", res._json)
            if "media" in res.entities:
                #               print("res with media in: ", res._json["id_str"])
                # pprint.pprint(res._json)
                url_list = []

                try:
                    for medium in res.extended_entities["media"]:
                        # print("medius: ", medium)
                        if medium["type"] == "photo":
                            # print(">>  url: ", medium["media_url"])
                            url_list.append(medium["media_url"])

                except:
                    print("something wrong")
                #                print("url list: ", url_list)
                res_dict[res._json["id_str"]] = url_list
        return res_dict
