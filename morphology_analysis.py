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

        print (text)
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




