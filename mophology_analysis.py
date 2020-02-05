import MeCab



tagger = MeCab.Tagger ("-d /usr/local/lib/mecab/dic/mecab-ipadic-neologd")

text = '今日はいい天気だなあ'

parsed_as_is = tagger.parse (text)



parsed_in_line_list = parsed_as_is.split ('\n')

parsed = {}
parsed_list = []
parsed['text'] = text
for i_str, parsed_in_line in enumerate (parsed_in_line_list):
    if parsed_in_line == 'EOS':   break
    parsed['i_str']  = i_str
    parsed['string'] = parsed_in_line.split ('\t')[0]
    parsed['POS']    = parsed_in_line.split ('\t')[1].split(',')[0]
    print (parsed)
    parsed_list.append (parsed)


print (parsed_list)




