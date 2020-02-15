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
            parsed[i_str]['string'] = parsed_in_line.split ('\t')[0]
            parsed[i_str]['POS']    = parsed_in_line.split ('\t')[1].split(',')[0]
        parsed['length'] = i_str
        parsed_list.append (parsed)
            #print (parsed)
            #print (parsed_list)


        return parsed



if __name__ == '__main__':
    import pandas as pd
    import json
    
    ### 1日ikkaiMeCabで形態素解析をして、その度数分布を作る。
    ### 日々のゴミ共のツイートの保存されているJSONのファイルリストを作る。
    extr_path_list = glob.glob ('./*dat', recursive =True)
    print (extr_path_list)

    sigma_chan_df = pd.DataFrame (data = None, index = None, columns = None, dtype = None)

    aggr_dict = {}
    ### それぞれのJSONファイルから情報を抽出する。
    for extr_path in extr_path_list:
        ### JSONを開く。
        with open (extr_path, 'r')as fp_in:
            extr_dict = json.load (fp_in)

        ### JSONの中の項目を読み込んでく。
        str_tuple_list = []
        for extr in extr_dict.values ():
            parsed_text = ma.parse_text (extr['text'])
            str_list = []
            ### MeCabでツイートをバラす。
            for i_str in range (int (parsed_text['length'])):
                fragmented_str = dl.evaluate_simple (parsed_text[i_str]['string'])
                ### dont listになくて、助詞でないやつを抽出。
                if parsed_text[i_str]['POS'] != '助詞' and fragmented_str != None:
                    ### sigma_chan_dfのインデックスにないやつは追加
                    if sigma_chan_df[fragmented_str] == None:
                        sigma_chan_fragment = pd.Series ([1], index = [fragmented_str], dtype = int, name = fragment)
                        sigma_chan_df.append (sigma_chan_fragment)
                    ### sigma_chan_dfにあるやつはカウントを追加
                    else:
                        sigma_chan_df[framgented_str] += 1
            print (sigma_chan_df)
            #str_list.append (dl.evaluate_simple (parsed_text[i_str]['string']))
            exit ()



                        

            
            ### 文字列の重複をカウントする。
            str_dist = collections.Counter (str_list)
            str_dist = str_dist.most_common ()
            str_tuple_list.extend (str_dist)
            print (str_dist[:10])
            break


        
        str_dict = {}
        print ("integrate")
        str_dist_list = []
        for str_tuple in str_tuple_list:
            if len (str_dist_list) > 0:
                for str_dist in str_dist_list:
                    key    = list (str_dist.keys ()) [0]
                    amount = list (str_dist.values ()) [0]
                    if key == str_tuple[0]:

                        print (key, amount, str_tuple[1], str_dist[key])
                        str_dist[key] = int (str_dist[key]) + int (str_tuple[1])

                    else:
                        print (key, str_tuple)
                        str
            else:
                str_dict[str_tuple[0]] = str_tuple[1]
                str_dist_list.append (str_dict)
                print (str_dict)




        exit ()
        for str_tuple in str_tuple_list:
            print ("tuple as is:", str_tuple, str_tuple[0], str_tuple[1])
            if str_tuple[0] not in str_dict.keys():
                str_dict[str_tuple[0]] = str_tuple[1]
                print ("first:  ", str_dict)
            else:
                print ("before: ", str_dict[str_tuple[0]], str_tuple[1])
                str_dict[str_tuple[0]] = int (str_tuple[1]) + int (str_dict[str_tuple[0]])
                print ("after:  ", str_dict[str_tuple[0]], str_tuple[1])

        str_dict = sort 
        with open ('summary_series_{}.json'.format (extr), 'w') as fp_out:
            json.dump (str_dict, fp_out, indent = 4, ensure_ascii = False)
                

            


