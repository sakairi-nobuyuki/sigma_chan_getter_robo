import os
import tweepy
import datetime
import pickle
import json
import datetime
import time

import AA
import emma_note

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

def get_tw_data (dancer_name, data_file = None):

    ck, cs, at, ats = twitter_keys ()

    auth = tweepy.OAuthHandler (ck, cs)
    auth.set_access_token (at, ats)

    tw_api = tweepy.API (auth, wait_on_rate_limit = True)

    print ("{}という踊り子さんのツイートを取ろうとしているよ。".format (dancer_name))

    tws_dict_list = []

#    time_ymdhms, tws_dict = get_gomikasu_tws (tw_api, dancer_name)
#    print ("ゴミカスのツイートだよ❤：{}", tws_dict)
    
 
    
    try:
        time_ymdhms, tws_dict = get_gomikasu_tws (tw_api, dancer_name)
        print ("ゴミカスのツイートをゲットしたよ❤")
    except:
        tws_dict = {}
        print ("ゴミカスのツイート取れんかった。すまんかった。")


    #file_name = 'test_{}.dat'.format (dancer_name)
    file_name = 'twifemi.dat'
    try:
        print ("{}なんていうファイルはあるかないかわからないなあ{}".format (file_name, os.path.exists (file_name)))
        if os.path.exists (file_name):
            with open (file_name, 'r', encoding = 'utf-8') as fp_in:
                tws_dict_last = json.load (fp_in)
        else:
            tws_dict_last = {}
    except:
        file_name = 'test_{}_1.dat'.format (dancer_name)
        print ("{}なんていうファイルはあるかないかわからないなあ{}".format (file_name, os.path.exists (file_name)))
        tws_dict_last = {}

    ####  辞書のupdateではなくて、ツイートのidが被ってたら消す。
    tws_dict.update (tws_dict_last)


    ### pickleで圧縮したい。
    with open (file_name, 'w') as fp_out:
        json.dump (tws_dict, fp_out, indent = 4, ensure_ascii = False)
    

if __name__ == '__main__':
    AA.print_tantsubo ()
    
    #print (get_tw_data (keyword))

    for i in range (10):
        for twifemi in emma_note.twifemi_list:
            get_tw_data (twifemi)
            print ("going to sleep")
            time.sleep (261)

            ### 1日ikkaiMeCabで形態素解析をして、その度数分布を作る。

            
