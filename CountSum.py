#!/usr/bin/python
# -*- coding: utf-8 -*-

"""
辞書型をがしゃこんで足していく
"""

import json
import pandas as pd
from tqdm import tqdm

base = pd.DataFrame(columns=['word','count'])
result = pd.DataFrame(columns=['word','count'])

#print(base)


for i in ['12','10-2','10','11-1','11-2']:#,'10','11','12','13','14','15','16','17','18','19','20','21','22','23','24','25','26','27','28','29','30','31']:
    json_open = open('sum_' +i+'.json', 'r')
    df_s = pd.read_json(json_open)
    base = pd.concat([df_s,base], join='outer')

print(base[base['word']=='コミュ'])

for index,row in tqdm(base.iterrows(),total = len(result)):
    count = base[base['word'] == row['word']]['count'].sum()
    result = result.append({'word':row['word'],'count':count},ignore_index=True)

result = result.drop_duplicates(subset='word')
result = result.sort_values('count', ascending=False)
print(result)

#base = base.to_dict()
json_data = result.to_dict()
with open('sum_10to12.json','w',encoding='utf-8') as f:
    json.dump(json_data,f,ensure_ascii=False,indent=4)

