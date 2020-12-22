#!/usr/bin/python
# -*- coding: utf-8 -*-

"""
jsonを読み込んで単語を集計し、集計結果をjsonに吐き出す。
protected = true で鍵垢なので、それは避ける
"""

import json
import pandas as pd
import MeCab
import datetime
import re
from tqdm import tqdm


def format_text(text):
    '''
    MeCabに入れる前のツイートの整形方法例
    '''
    text = re.sub(r' ', '', text)
    text = re.sub(r'https?://[\w/:%#\$&\?\(\)~\.=\+\-…]+', "", text)
    text = re.sub('RT', "", text)
    text = re.sub('お気に入り', "", text)
    text = re.sub('まとめ', "", text)
    #ハッシュタグの検出のため、¥n#にしてから抜いていく
    text = re.sub(r'#', '\n#', text)
    text = re.sub(r'(\A|\n|[ -/:-@\[-~]|\s)#.+(\n|[ -/:-@\[-~]|\Z|\s)', "", text) #ハッシュタグは別で入れるのでここでは消していたい
    #同じようにして@ユーザー名も消したい
    text = re.sub(r'(\A|\n|[ -/:-@\[-~]|\s)@.+(\n|[ -/:-@\[-~]|\Z|\s)', "", text)
    text = re.sub(r'[ -/:-@\[-~]', "", text)  # 半角記号
    text = re.sub(r'[︰-＠]', "", text)  # 全角記号
    text = re.sub('\n', " ", text)  # 改行文字

    return text

#Mecab
t = MeCab.Tagger()
#t.parse('')

result = pd.DataFrame(columns=["word","count"])
df_word = pd.DataFrame(columns=["word"])

for i in (['19','20','21','22','23','24','25','26','27','28','29','30']):
    json_open = open('TwitterData11-2/2020-11-' +i+'.json', 'r')
    print('TwitterData11-2/2020-11-' +i+'.json')
    df_s = pd.read_json(json_open,orient='records')

    for index,row in tqdm(df_s.iterrows(), total=len(df_s)):
        text = df_s.iloc[index,0]['text']
        text = format_text(df_s.iloc[index,0]['text'])
        m = t.parseToNode(text)
        while m:
            if m.feature.split(',')[0] == '名詞' and m.feature.split(',')[1] == '一般':
                word = pd.Series(m.surface,index =['word'])
                df_word = df_word.append(word,ignore_index=True)
            m = m.next

for index,row in tqdm(df_word.iterrows(), total=len(df_word)):
    if len(row['word']) == 1:
        continue
    word_count = (df_word['word'].str.match(row['word']).sum())
    result = result.append({'word':row['word'],'count':word_count}, ignore_index=True)

result = result.drop_duplicates(subset='word')
result = result.sort_values('count', ascending=False)
print(result)

json_data = result.to_dict()
with open('sum_11-2.json','w',encoding='utf-8') as f:
    json.dump(json_data,f,ensure_ascii=False,indent=4)