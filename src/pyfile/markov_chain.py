#!/usr/bin/python
# -*- coding: utf-8 -*-
import pandas as pd
import re
import MeCab
import random
from collections import deque

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


def wakati(text):
    t = MeCab.Tagger("-Owakati")
    parsed_text = ""
    for one_line_text in one_sentence_generator(text):
        parsed_text += " "
        parsed_text += t.parse(one_line_text)
    wordlist = parsed_text.rstrip("\n").split(" ")
    return wordlist

def one_sentence_generator(long_text):
    sentences = re.findall(".*?。", long_text)
    for sentence in sentences:
        yield sentence

def make_sentence(model, sentence_num=5, seed="[BOS]", max_words = 1000):    
    sentence_count = 0

    key_candidates = [key for key in model if key[0] == seed]
    if not key_candidates:
        print("Not find Keyword")
        return
    markov_key = random.choice(key_candidates)
    queue = deque(list(markov_key), order)

    sentence = "".join(markov_key)
    for _ in range(max_words):
        markov_key = tuple(queue)
        next_word = random.choice(model[markov_key])
        sentence += next_word
        queue.append(next_word)

        if next_word == "。":
            sentence_count += 1
            if sentence_count == sentence_num:
                break
    return sentence

def make_model(text):
    model = {}
    wordlist = wakati(text)
    queue = deque([], order)
    queue.append("[BOS]")
    for markov_value in wordlist:
        if len(queue) == order:
            if queue[-1] == "。":
                markov_key = tuple(queue)
                if markov_key not in model:
                    model[markov_key] = []
                model[markov_key].append("[BOS]")
                queue.append("[BOS]")

            markov_key = tuple(queue)      
            if markov_key not in model:
                model[markov_key] = []
            model[markov_key].append(markov_value)
        queue.append(markov_value)
    return model

if __name__ == "__main__":

    text = ""

    for i in (['19','20','21','22','23','24','25','26','27','28','29','30']):
        json_open = open('TwitterData11-2/2020-11-' +i+'.json', 'r')
        df_s = pd.read_json(json_open,orient='records')

        for index,row in (df_s.iterrows()):
            text = text + format_text(df_s.iloc[index,0]['text']) + "。"
        
    order = 2
    model = make_model(text)
    sentence = make_sentence(model)
    print(sentence)