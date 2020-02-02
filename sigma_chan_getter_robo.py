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

    print (q)

    for tw in tweepy.Cursor (tw_api.search, q = q, count = 100, tweet_mode = 'extended').items ():
        #print (tw.full_text)
        tws_list.append (tw.full_text + '\n')

        file_name = 'test.dat'

    if len (tws_list) == 0:
        print ("残念ながらあなたのように{}について興味を持ってる人はいなかったみたいです。".format (q))

    with open (file_name, 'w', encoding = 'utf-8') as fp_out:
        fp_out.writelines (tws_list)

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


def print_tantsubo ():
    print ('GESUGESUGESUGESUGESUGESUGESUGESUGESUGESU')
    print ('GE                                    SU')
    print ('GE         GESUGESUGESUG              SU')
    print ('GE     GESUG             GESU         SU')
    print ('GE    SUG    UGE    ESU    UGE        SU')
    print ('GE     UGESUG          G ESU          SU')
    print ('GE     UG SUGESUGESUGESUGESU          SU')
    print ('GE    SU SU   ESUGESUG  UGESU         SU')
    print ('GE   ESU                  ESUG        SU')
    print ('GE  GEU  ESUG         SU ES  EU       SU')
    print ('GE UG SU      SUG SUGE   E   ES       SU')
    print ('GE UG  UGE             GE    ESU      SU')
    print ('GE UG    ESUG    E UGE    SU   UG     SU')
    print ('GE U ES        UGES      ES     G     SU')
    print ('GE U    GESU         ESU      SUG     SU')
    print ('GE  G       GESUGES         GES       SU')
    print ('GESUGESUGESUGESUGESUGESUGESUGESUGESUGESU')
    print ('GESUGESUGESUGESUGESUGESUGESUGESUGESUGESU')
                                                            

    






    
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
