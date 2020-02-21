import MeCab


class MorphAnalysis:
    def __init__ (self):
        self.tagger = MeCab.Tagger ("-d /usr/local/lib/mecab/dic/mecab-ipadic-neologd")
        print ("load dictionary for MeCab")

        #text = '今日はいい天気だなあ'
    def parse_text (self, text):
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
            parsed_text = ma.parse_text (extr['text'])

            str_list = []
            ### MeCabでツイートをバラす。
            for i_str in range (int (parsed_text['length'])):
                fragmented_str = dont_list.evaluate_simple (parsed_text[i_str]['string'])
                if fragmented_str == None:  continue
                ### dont listになくて、助詞でないやつを抽出。
                #if parsed_text[i_str]['POS'] == '名詞' or parsed_text[i_str]['POS'] == '形容詞' or parsed_text[i_str]['POS'] == '動詞' or parsed_text[i_str]['POS'] == '形容動詞':
                if parsed_text[i_str]['POS'] == '名詞' or parsed_text[i_str]['POS'] == '形容詞' or parsed_text[i_str]['POS'] == '形容動詞':
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


if __name__ == '__main__':
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
        out_path = extr_path + 'out.dat'        

        aggr_dict_list = ma.aggrigate_molphed_tweets (extr_dict, dl)

        with open (out_path, 'w', encoding = 'utf_8') as fp_out:
            #json.dump (aggr_dict, fp_out, indent = 4, ensure_ascii = False)
            json.dump (aggr_dict_list, fp_out, indent = 4, ensure_ascii = False)


