#!/usr/bin/python
# -*- coding: utf-8 -*-

"""
辞書型をがしゃこんで足していく
"""

import json
import pandas as pd
from tqdm import tqdm

base = pd.DataFrame(columns=["word","count"])
result = pd.DataFrame(columns=["word","count"])

#print(base)
json_open = open("sum_6to7_10to12.json", 'r')
base = pd.read_json(json_open)


for i in ["01","02","03","04","05","06"]:
    json_open = open("新しいフォルダー/202007" +i+".json", 'r')
    jj = json.load(json_open)
    print("新しいフォルダー/202007" +i+".json")
    print(type(jj))
    df_s = pd.DataFrame(jj)
    base = pd.concat([df_s,base], join='outer',sort=False)


for index,row in tqdm(base.iterrows(),total = len(base)):
    count = base[base["word"] == row["word"]]["count"].sum()
    result = result.append({"word":row["word"],"count":count},ignore_index=True)

result = result.drop_duplicates(subset="word")
result = result.sort_values("count", ascending=False)
print(result)

#base = base.to_dict()
result.to_json("sum_6to12.json",force_ascii=False,orient="records")
#with open("sum_6to12.json",'w',encoding='utf-8') as f:
#    json.dump(json_data,f,ensure_ascii=False,indent=4)
