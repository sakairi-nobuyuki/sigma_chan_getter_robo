import os
import tweepy
import datetime
import pickle
import json
import datetime
import time

import AA
import emma_note


def get_tw_data (dancer_name, data_file = None):
    import config

    ck = config.tw_api_key["consumer_API_key"]
    cs = config.tw_api_key["consumer_API_secret_key"]
    at = config.tw_api_key["access_token"]
    ats = config.tw_api_key["access_token_secret"]

    auth = tweepy.OAuthHandler (ck, cs)
    auth.set_access_token (at, ats)

    tw_api = tweepy.API (auth, wait_on_rate_limit = True)



    print ("dancer name is: ", dancer_name)

    tws_dict_list = []
    tws_dict = {}
    for tweet in tweepy.Cursor (tw_api.user_timeline, screen_name = dancer_name, exclude_replies = True).items():
        time = datetime.datetime.now ()
        time_ymdhms = time.strftime ('%Y%m%d%H%M%S') 

        tws_dict[time_ymdhms] = {}
        tws_dict[time_ymdhms]['dancer_name'] = dancer_name
        tws_dict[time_ymdhms]['id']          = tweet.id
        tws_dict[time_ymdhms]['created_at']  = str (tweet.created_at)
        tws_dict[time_ymdhms]['text']        = tweet.text.replace('\n','')
        tws_dict[time_ymdhms]['favorite_count'] = tweet.favorite_count
        tws_dict[time_ymdhms]['retweet_count']  = tweet.retweet_count
        #tws_dict_list.append (tws_dict)



    #print (tws_dict_list)
    print (tws_dict)


    if len (tws_dict) == 0:
        print ("残念ながらあなたのように{}について興味を持ってる人はいなかったみたいです。".format (dancer_name))


    print ("{}なんていうファイルはあるかないかわからないなあ{}".format (file_name, os.path.exists (file_name)))
    try:
        file_name = 'test_{}.dat'.format (dancer_name)
        if os.path.exists (file_name):
            with open (file_name, 'r', encoding = 'utf-8') as fp_in:
                tws_dict_last = json.load (fp_in)
        else:
            tws_dict_last = {}
    except:
        file_name = 'test_{}_1.dat'.format (dancer_name)
        tws_dict_last = {}

    tws_dict.update (tws_dict_last)

    with open (file_name, 'w') as fp_out:
        json.dump (tws_dict, fp_out, indent = 4, ensure_ascii = False)

    
    

if __name__ == '__main__':
    AA.print_tantsubo ()
    
    #print (get_tw_data (keyword))

    for i in range (3):
        for twifemi in emma_note.twifemi_list:
            get_tw_data (twifemi)
            print ("going to sleep")
            time.sleep (61)
