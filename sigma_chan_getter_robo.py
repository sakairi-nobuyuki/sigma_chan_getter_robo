import os
import pandas as pd
import tweepy
import datetime



def get_tw_data (keyword, data_file = None):
    import config

    ck = config.tw_api_key["consumer_API_key"]
    cs = config.tw_api_key["consumer_API_secret_key"]
    at = config.tw_api_key["access_token"]
    ats = config.tw_api_key["access_token_secret"]

    auth = tweepy.OAuthHandler (ck, cs)
    auth.set_access_token (at, ats)

    tw_api = tweepy.API (auth, wait_on_rate_limit = True)

    q = keyword

    tws_list = []
    
    q = q + ' -filter:retweets'
    print (q)
    getter_res = pd.DataFrame (columns = ['user_id', 'user_name', 'user_screen_name', 'user_profile_image_url', \
        'tweet_id', 'tweet_full_text', 'tweet_fav_count', 'tweet_ceated_at'])
    
    tws = tweepy.Cursor (tw_api.search, q = q, tweet_mode = 'extended').items ()        
    #tweepy.Cursor (tw_api.search, q = q, count = 10, tweet_mode = 'extended').items ()        
    #for tw in tweepy.Cursor (tw_api.search, q = q, count = 10, tweet_mode = 'extended').items ():
    for tw in tws:
        #getter_res.append ({
        #    'user_id': tw.user.id, 
        #    'user_name': tw.user.name, 
        #    'user_screen_name': tw.user.screen_name, 
        #    'user_profile_image_url': tw.user.profile_image_url.replace ('_normal', ''), 
        #    'tweet_id': tw.id, 
        #    'tweet_full_text': tw.full_text, 
        #    'tweet_fav_count': tw.favorite_count, 
        #    #'tweet_ceated_at': tw.created_at + timedelta (hours=+9)})
        #    'tweet_ceated_at': tw.created_at}, ignore_index = True)
        getter_append_sr = pd.Series ([tw.user.id, tw.user.name, tw.user.screen_name, tw.user.profile_image_url.replace ('_normal', ''), \
            tw.id, tw.full_text, tw.favorite_count, tw.created_at], index = getter_res.columns)
        getter_res = getter_res.append (getter_append_sr, ignore_index = True)
        print (tw.full_text)
        print ("Series to append: ", getter_append_sr)
        print ("getter result:    ", getter_res)
        tws_list.append (tw.full_text + '\n')
    print (getter_res)

    

    if len (tws_list) == 0:
        print ("残念ながらあなたのように{}について興味を持ってる人はいなかったみたいです。".format (q))
    
    print ("ゲットしました。datに保存します。")
    
    file_name = 'test.dat'

    getter_res.to_csv (file_name, encoding='utf-8')
    #with open (file_name, 'w', encoding = 'utf-8') as fp_out:
    #    fp_out.writelines (tws_list)

    #print (tws_list)

def print_gesudana ():
    print ('XXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXX')
    print ('XX                                                           XX')
    print ('XX    GGG   EEEE   SSS  U   U DDD      A     N    N     A    XX')
    print ('XX   G   G  E     S   S U   U D  D    A A    NN   N    A A   XX')
    print ('XX   G      EEE    SS   U   U D   D   A  A   N N  N    A A   XX')
    print ('XX   G GGG  E        S  U   U D   D  A    A  N  N N   A   A  XX')
    print ('XX   G   G  E     S   S U   U D  D   AAAAAA  N   NN   AAAAA  XX')
    print ('XX    GGG   EEEEE  SSS   UUU  DDD   A      A N    N  A     A XX')
    print ('XX                                                           XX')
    print ('XXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXX')

def get_keyword_to_search ():    
    print ('どんなクソ共のツイートをしりたいのかな？：')
    keyword = input ('$ ')
    
    return keyword
    

if __name__ == '__main__':
    print_gesudana ()

    keyword = get_keyword_to_search ()

    if keyword == None:
        print ("キーワード入ってないっすよ？")
        exit ()
    else:
        print ("本当に {} について調べるんですね？あんまリクエスト送ると怒られるっすよ？".format (keyword))
        print ("yes/noで答えてください。")
        yes_no = input ('$ ')
        if yes_no == 'no':
            print ('ヲチャとしてそれでいいんですか？')
            exit ()
        elif yes_no == 'yes':
            print ('{}についてヲチしたいだなんてほんと下衆ですね。'.format (keyword))
        else:
            print ('{}ってなんですか？yes/noで聞いてるんだから、聞かれた通りに答えてください。'.format (yes_no))
            exit ()

     
    print (get_tw_data (keyword))
