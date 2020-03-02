import os
import glob
import datetime
import pickle
import json
from datetime import datetime, timedelta, date
import time
import collections

import pandas as pd 

import tweepy

import morphology_analysis
import AA
import emma_note
import dont_list

FILE_NAME_TW_FEMI_BASE = "twifemi"


class SigmaChanGetterRobo:
    def __init__ (self):
        import config
        
        self.ck = config.tw_api_key["consumer_API_key"]
        self.cs = config.tw_api_key["consumer_API_secret_key"]
        self.at = config.tw_api_key["access_token"]
        self.ats = config.tw_api_key["access_token_secret"]


def twitter_keys ():
    import config

    ck = config.tw_api_key["consumer_API_key"]
    cs = config.tw_api_key["consumer_API_secret_key"]
    at = config.tw_api_key["access_token"]
    ats = config.tw_api_key["access_token_secret"]

    return ck, cs, at, ats

def get_keyword_related_tws (tw_api, keyword):
    print ("keyword is {}".format (keyword))
    tws_dict = {}
    i_tw = 0
    for tweet in tweepy.Cursor (tw_api.search, q = keyword, exclude_replies = True).items():
        time = datetime.datetime.now ()
        time_ymdhms = time.strftime ('%Y%m%d%H%M%S') 
        i_tw += 1
        tws_dict[tweet.id] = {}
        tws_dict[tweet.id]['attribute']   = 'search_{}'.format (keyword)
        tws_dict[tweet.id]['user_name']   = tweet.user.name
        tws_dict[tweet.id]['id']          = tweet.id
        tws_dict[tweet.id]['created_at']  = str (tweet.created_at)
        tws_dict[tweet.id]['text']        = tweet.text.replace('\n','')
        tws_dict[tweet.id]['favorite_count'] = tweet.favorite_count
        tws_dict[tweet.id]['retweet_count']  = tweet.retweet_count
        print ("in dict: {}, {} th tw".format (tws_dict[tweet.id], i_tw))
        if i_tw > 1000:
            break
        #print ("tweet id: {}, tweet text: {}".format (tweet.id, tweet.text))
    return time_ymdhms, tws_dict


def store_keyword_related_tw_data (keyword, file_path_base = None):

    ck, cs, at, ats = twitter_keys ()

    auth = tweepy.OAuthHandler (ck, cs)
    auth.set_access_token (at, ats)

    tw_api = tweepy.API (auth, wait_on_rate_limit = True)

    print ("{}というキーワードのツイートを取ろうとしているよ。".format (keyword))

    tws_dict_list = []
    try:
        time_ymdhms, tws_dict = get_keyword_related_tws (tw_api, keyword)
        print ("{}のツイートをゲットしたよ❤".format (keyword))
    except:
        tws_dict = {}
        print ("取れんかった。すまんかった。")

    if file_path_base == None:
        file_path = 'keyword_{}.dat'.format (time.strftime ('%Y%m%d') )
    else:
        file_path = '{}_{}.dat'.format (file_path_base, time.strftime ('%Y%m%d') )

    try:
        print ("{}なんていうファイルはあるかないかわからないなあ{}".format (file_path, os.path.exists (file_path)))
        if os.path.exists (file_path):
            with open (file_path, 'r', encoding = 'utf-8') as fp_in:
                tws_dict_last = json.load (fp_in)
        else:
            tws_dict_last = {}
    except:
        print ("残念あがら{}なんていうファイルはないなあ{}".format (file_path, os.path.exists (file_path)))
        tws_dict_last = {}

    ####  辞書のupdateではなくて、ツイートのidが被ってたら消す。
    tws_dict.update (tws_dict_last)


    ### pickleで圧縮したい。
    with open (file_path, 'w') as fp_out:
        json.dump (tws_dict, fp_out, indent = 4, ensure_ascii = False)
    return file_path



def get_gomikasu_tws (tw_api, dancer_name):
    tws_dict = {}
    for tweet in tweepy.Cursor (tw_api.user_timeline, screen_name = dancer_name, exclude_replies = True).items():
        time = datetime.datetime.now ()
        time_ymdhms = time.strftime ('%Y%m%d%H%M%S')
        today     = datetime.today ()
        yesterday = today - timedelta (days = 1)
        if str (datetime.strftime (today, '%F')) in str (tweet.created_at) or str (datetime.strftime (yesterday, '%F')) in str (tweet.created_at):
            print ('今日のだからゲット')
        else:
            print ('昔のだからパス', str (time.strftime ('%F')), str (tweet.created_at))
            continue
        tws_dict[tweet.id] = {}
        tws_dict[tweet.id]['attribute']   = 'twifemi'
        tws_dict[tweet.id]['dancer_name'] = dancer_name
        tws_dict[tweet.id]['id']          = tweet.id
        tws_dict[tweet.id]['created_at']  = str (tweet.created_at)
        tws_dict[tweet.id]['text']        = tweet.text.replace('\n','')
        tws_dict[tweet.id]['favorite_count'] = tweet.favorite_count
        tws_dict[tweet.id]['retweet_count']  = tweet.retweet_count

    return time_ymdhms, tws_dict



def store_dancers_tw_data (dancer_name, file_path_base = None):

    ck, cs, at, ats = twitter_keys ()

    auth = tweepy.OAuthHandler (ck, cs)
    auth.set_access_token (at, ats)

    tw_api = tweepy.API (auth, wait_on_rate_limit = True)

    print ("{}という踊り子さんのツイートを取ろうとしているよ。".format (dancer_name))

    tws_dict_list = []
    try:
        time_ymdhms, tws_dict = get_gomikasu_tws (tw_api, dancer_name)
        print ("ゴミカスのツイートをゲットしたよ❤")
    except:
        tws_dict = {}
        print ("ゴミカスのツイート取れんかった。すまんかった。")

    file_path = '{}_{}.dat'.format (file_path_base, time.strftime ('%Y%m%d') )
    try:
        print ("{}なんていうファイルはあるかないかわからないなあ{}".format (file_path, os.path.exists (file_path)))
        if os.path.exists (file_path):
            with open (file_path, 'r', encoding = 'utf-8') as fp_in:
                tws_dict_last = json.load (fp_in)
        else:
            tws_dict_last = {}
    except:
        file_path = 'test_{}_1.dat'.format (dancer_name)
        print ("残念あがら{}なんていうファイルはないなあ{}".format (file_path, os.path.exists (file_path)))
        tws_dict_last = {}

    ####  辞書のupdateではなくて、ツイートのidが被ってたら消す。
    tws_dict.update (tws_dict_last)


    ### pickleで圧縮したい。
    with open (file_path, 'w') as fp_out:
        json.dump (tws_dict, fp_out, indent = 4, ensure_ascii = False)
    return file_path

def get_command_line ():
    import argparse

    parser = argparse.ArgumentParser (description = 'ゴミカスのツイートをゲットして形態素解析するゲスなプログラムだよ。')

    parser.add_argument ('--skip_tweet_get', action = 'store_true')

    args = parser.parse_args ()

    return args

if __name__ == '__main__':
    AA.print_tantsubo ()

    args = get_command_line ()
    ma = morphology_analysis.MorphAnalysis ()
    dl = dont_list.DontList ()
    print (dl.simple)
    #print (get_tw_data (keyword))

    

    out_path_list = []
    for i in range (10):
        if args.skip_tweet_get == True:  break
        for dancer_name in emma_note.twifemi_list:
            out_path = store_dancers_tw_data (dancer_name, FILE_NAME_TW_FEMI_BASE)
            if len (out_path) > 0:  out_path_list.append(out_path)
            print ("going to sleep")
            time.sleep (61)
            
            
    
    out_path_list = []
    for i in range (10):
        if args.skip_tweet_get == True:  break
        for keyword in emma_note.keywords:
            out_path = store_keyword_related_tw_data (keyword)
            if len (out_path) > 0:  out_path_list.append(out_path)
            print ("going to sleep")
            time.sleep (61)

