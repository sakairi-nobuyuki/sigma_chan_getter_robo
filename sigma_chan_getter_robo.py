import tweepy
import datetime
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

    tws_list = []

    print ("dancer name is: ", dancer_name)

    for tweet in tweepy.Cursor (tw_api.user_timeline, screen_name = dancer_name, exclude_replies = True).items():
        tws_list.append([tweet.id, tweet.created_at, tweet.text.replace('\n',''), tweet.favorite_count, tweet.retweet_count])

    print (tws_list)


    if len (tws_list) == 0:
        print ("残念ながらあなたのように{}について興味を持ってる人はいなかったみたいです。".format (q))

    file_name = 'test_{}.dat'.format (dancer_name)

    with open (file_name, 'a', encoding = 'utf-8') as fp_out:
        fp_out.writelines (tws_list)

    #print (tws_list)
    

if __name__ == '__main__':
    AA.print_tantsubo ()
    
    #print (get_tw_data (keyword))

    for i in range (3):
        for twifemi in emma_note.twifemi_list:
            get_tw_data (twifemi)
            print ("going to sleep")
            time.sleep (61)
