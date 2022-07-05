import math
import re

import MeCab


class MorphAnalysis:
    def __init__ (self):
        self.tagger = MeCab.Tagger ("-d /usr/local/lib/mecab/dic/mecab-ipadic-neologd")
        print ("load dictionary for MeCab")
        self.dont_list = [' ', '#', '(', ')', '.', '/', ':', '://', '@', 'EOS', '（', '）', ',', '.', '、', '。']
        #text = '今日はいい天気だなあ'

    def parse_text_to_words (self, text, exclude_dont_list = False):
        parsed_as_is = self.tagger.parse (text)
        parsed_in_line_list = parsed_as_is.split ('\n')
        if exclude_dont_list:
            words = [parsed_in_line.split ('\t')[0] for parsed_in_line in parsed_in_line_list if parsed_in_line.split ('\t')[0] not in self.dont_list]
            #print ("exclude dont list")
        else:
            words = [parsed_in_line.split ('\t')[0] for parsed_in_line in parsed_in_line_list]
            #print ("include dont list")

        return words
        

    def parse_text_word_and_POS (self, text):
        parsed_as_is = self.tagger.parse (text)

        parsed_in_line_list = parsed_as_is.split ('\n')


        parsed_list = []
        parsed = {}
        parsed['text'] = text

        #print ("text as is: ", text)
        for i_str, parsed_in_line in enumerate (parsed_in_line_list):
            if parsed_in_line == 'EOS':   break
            parsed[i_str]  = {}
            parsed[i_str]['string']    = parsed_in_line.split ('\t')[0]
            parsed[i_str]['POS']       = parsed_in_line.split ('\t')[1].split(',')[0]
            parsed[i_str]['subPOS']    = parsed_in_line.split ('\t')[1].split(',')[1]
        parsed['length'] = i_str
        parsed_list.append (parsed)
            #print (parsed)
            #print (parsed_list)


        return parsed

    def aggrigate_molphed_tweets (self, extr_dict, dont_list):
        fragmented_str = ''
        parsed_text    = {}
        aggr_dict      = {}
        aggr_dict_list = []
        n_keys_in_iter = {}
        i_extr = 0 
        ### JSONの中の項目を読み込んでく。
        for extr in extr_dict.values ():
            #if os.path.exists (out_path): continue
            if len (extr['text'].split ('RT')[0]) == 0:
                print ("こいつらは人の意見に迎合するだけのゴミ野郎です。", extr['text'])
                continue
            parsed_text = ma.parse_text_to_word_and_POS (extr['text'])

            str_list = []
            ### MeCabでツイートをバラす。
            for i_str in range (int (parsed_text['length'])):
                fragmented_str = dont_list.evaluate_simple (parsed_text[i_str]['string'])
                if fragmented_str == None:  continue
                ### dont listになくて、助詞でないやつを抽出。
                #if parsed_text[i_str]['POS'] == '名詞' or parsed_text[i_str]['POS'] == '形容詞' or parsed_text[i_str]['POS'] == '動詞' or parsed_text[i_str]['POS'] == '形容動詞':
                #if parsed_text[i_str]['POS'] == '名詞' or parsed_text[i_str]['POS'] == '形容詞' or parsed_text[i_str]['POS'] == '形容動詞':
                #print ("going to add {} ".format (fragmented_str))
                ### 辞書にないやつは項目追加。
                if fragmented_str not in aggr_dict.keys ():
                    #print ("no {} in key, going to add".format (fragmented_str))
                    aggr_dict[fragmented_str] = {'string': parsed_text[i_str]['string'], 'amount':1, 'POS': parsed_text[i_str]['POS'], 'subPOS': parsed_text[i_str]['subPOS']}
                ### あるやつは数を増やす。
                else:
                    aggr_dict[fragmented_str]['amount'] = int (aggr_dict[fragmented_str]['amount']) + 1

            print ("{}   length of the dict: {}".format (i_extr, len (aggr_dict)))
            n_keys_in_iter[i_extr] = len (aggr_dict)
            i_extr += 1
            aggr_dict_list = sorted (aggr_dict.items(), key = lambda x: x[1]['amount'], reverse = True)
            
            for i_iter, aggr_dict_item in enumerate (aggr_dict_list):
                print (i_iter, aggr_dict_item)
                if i_iter > 20: break
        print ("{} {} finished and going to dump".format (aggr_dict, len (aggr_dict)))

        return aggr_dict_list

    def reduce_RT_url_from_text_to_parse (self, text_to_parse):
        if re.match (r'https:', text_to_parse):
            print ("URL attached text: {}".format (text_to_parse))
            text_to_parse = re.sub (r'(.*)(https://[a-zA-Z/.]+)(.*)', r'\1 \3', text_to_parse)
            print ("URL reduced text:  {}".format (text_to_parse))

        return text_to_parse

    def reduce_TR_notice_from_text_to_parse (self, text_to_parse):
        while (re.match (r'RT @[a-zA-Z0-9_-]+', text_to_parse)):
            #if re.match (r'RT @[a-zA-Z0-9_-]+', text_to_parse):
            print ("RT@ added text: {}".format (text_to_parse))
            text_to_parse = re.sub (r'(.*)(RT @[a-zA-Z0-9_-]+)(.*)', r'\1 \3', text_to_parse)
            print ("RT@ redced text: {}".format (text_to_parse))
        return text_to_parse


if __name__ == '__main__':
    """
    tweet['text']  --MeCab-->  ['word1  POS...', 'word2  POS...', ..., 'word n   POS...'] --> tweet['words']
    --pd.count_values ()--> distribution of words --> tf idf
    """
    import glob
    import json
    import os

    import pandas as pd
    import numpy as np

    import dont_list

    
    ### 1日ikkaiMeCabで形態素解析をして、その度数分布を作る。
    ### 日々のゴミ共のツイートの保存されているJSONのファイルリストを作る。
    extr_path_list = glob.glob ('./twifemi_*dat', recursive =True)
    extr_path_list = [item for item in extr_path_list if 'out.dat' not in item]
    print (extr_path_list)

    ma = MorphAnalysis ()
    dl = dont_list.DontList ()

    aggr_dict = {}
    ### それぞれのJSONファイルから情報を抽出する。
    for extr_path in extr_path_list:
        ### JSONを開く。
        with open (extr_path, 'r')as fp_in:
            extr_dict = json.load (fp_in)

        tf_df        = pd.DataFrame ()
        i_count = 0
        word_dist_series_list = []
        tf_series_list = []
        print ("get tf-idf of {}".format (extr_path))

        for extr in extr_dict.values ():
            if extr['dancer_name'] != '29nikunikuniku':  continue
            date_tmp = extr['created_at'].split (' ') [0].replace ('-', '')

            if date_tmp != extr_path.split ('_') [1]. split ('.') [0]:  
                continue
            else:
                print ("{}は{}のだよ。".format (extr_path, date_tmp))
            print ("tf process in {}'s tweet of \"{}\"".format (extr['dancer_name'], extr['text']))
            text_to_parse = extr['text']
            ### 引用ツイートのURLを除外
            text_to_parse = ma.reduce_RT_url_from_text_to_parse (text_to_parse)
            ### RTのあれを除外
            text_to_parse = ma.reduce_TR_notice_from_text_to_parse (text_to_parse)

            #i_count += 1
            molphed_tweet = ma.parse_text_to_words (text_to_parse, exclude_dont_list = True)
            #print (extr['text'], molphed_tweet)
            word_dist_series = pd.Series (molphed_tweet, name = extr['id']).value_counts ()
            #word_dist_series_list.append (word_dist_series)

            tf_series = word_dist_series / len (molphed_tweet)
            tf_series.name = extr['id']
            tf_series_list.append (tf_series)
            #print (words_dist_series)
            print ("in {}'s \"{}\", length of molphed: {}, total counts: {}".format (extr['dancer_name'], text_to_parse, len (molphed_tweet), word_dist_series.sum ()))
            #if i_count > 3: break
        #word_dist_df = pd.concat (word_dist_series_list, axis = 1, join = 'outer')
        if len (tf_series_list) < 1:
            print ("この日は{}さんは呟いてなかったみたいです。プライベートで何かあったんでしょうか？".format (extr['dancer_name']))
            break
        tf_df        = pd.concat (tf_series_list, axis = 1, join = 'outer')
        #print (word_dist_df, word_dist_df.info ())
        print ("tf finished")

        tf_df_fillna = tf_df.fillna (0)
        #print (tf_df_fillna)
        #print (tf_df.count (axis = 1), tf_df.count (axis = 1) / len (tf_df.columns))
        print ("obtaining idf")
        Ndf_series = tf_df.count (axis = 1) / len (tf_df.columns) + 1
        idf_series = pd.Series ([math.log (Ndf, math.e) + 1.0 for Ndf in Ndf_series], index = Ndf_series.index)

        tf_idf_df = pd.DataFrame ()
        tf_idf_series_list = []
        print ("tf-idf in process")
        for _, tf_series_fillna in tf_df_fillna.iteritems ():
            tf_idf_series = tf_series_fillna / idf_series
            tf_idf_series.name = tf_series_fillna.name
            tf_idf_series_list.append (tf_idf_series)
        tf_idf_df = pd.concat (tf_idf_series_list, axis = 1, join = 'outer')
        print ("id idf dayo\n", tf_idf_df)



        #exit ()



