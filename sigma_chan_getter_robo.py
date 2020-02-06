import os
import glob
import datetime
import pickle
import json
import datetime
import time

import tweepy

import morphology_analysis
import AA
import emma_note

FILE_NAME_TW_FEMI_BASE = "twifemi"


def get_gomikasu_tws (tw_api, dancer_name):
    tws_dict = {}
    for tweet in tweepy.Cursor (tw_api.user_timeline, screen_name = dancer_name, exclude_replies = True).items():
        time = datetime.datetime.now ()
        time_ymdhms = time.strftime ('%Y%m%d%H%M%S') 

        tws_dict[tweet.id] = {}
        tws_dict[tweet.id]['attribute']   = 'twifemi'
        tws_dict[tweet.id]['dancer_name'] = dancer_name
        tws_dict[tweet.id]['id']          = tweet.id
        tws_dict[tweet.id]['created_at']  = str (tweet.created_at)
        tws_dict[tweet.id]['text']        = tweet.text.replace('\n','')
        tws_dict[tweet.id]['favorite_count'] = tweet.favorite_count
        tws_dict[tweet.id]['retweet_count']  = tweet.retweet_count


    return time_ymdhms, tws_dict

def twitter_keys ():
    import config

    ck = config.tw_api_key["consumer_API_key"]
    cs = config.tw_api_key["consumer_API_secret_key"]
    at = config.tw_api_key["access_token"]
    ats = config.tw_api_key["access_token_secret"]

    return ck, cs, at, ats

def get_tw_data (dancer_name, file_path_base = None):

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

if __name__ == '__main__':
    AA.print_tantsubo ()

    ma = morphology_analysis.MorphAnalysis ()
    #print (get_tw_data (keyword))

    out_path_list = []
#    for i in range (10):
#        for dancer_name in emma_note.twifemi_list:
#            out_path = get_tw_data (dancer_name, FILE_NAME_TW_FEMI_BASE)
#            out_path_list.append[out_path]
#            print ("going to sleep")
#            time.sleep (61)
            
            
    
    ### 1日ikkaiMeCabで形態素解析をして、その度数分布を作る。
    extr_path_list = glob.glob ('./*dat', recursive =True)
    print (extr_path_list)

    aggr_dict = {}
    for extr_path in extr_path_list:
        with open (extr_path, 'r')as fp_in:
            extr_dict = json.load (fp_in)
        
        for extr in extr_dict.values ():
            parsed_text = ma.parse_text (extr['text'])
            for i_str in range (int (parsed_text['length'])):
                print (parsed_text[i_str]['string'], parsed_text[i_str]['POS'])
                aggr_dict[parsed_text[i_str]['string']] = 1
