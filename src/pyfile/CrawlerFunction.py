#!/usr/bin/python
# -*- coding: utf-8 -*-

import json
from requests_oauthlib import OAuth1Session
import pandas as pd
from time import sleep
import datetime
from tqdm import tqdm
import os

import config

def InitilizeConfig():
    # Twitter API
    CK = config.CONSUMER_KEY
    CS = config.CONSUMER_SECRET
    AT = config.ACCESS_TOKEN
    ATS = config.ACCESS_TOKEN_SECRET
    twitter = OAuth1Session(CK, CS, AT, ATS)  # 認証処理
 
    return twitter

def GetTweet(url,twitter):
    while(True):
        res = twitter.get(url,params={"count":100})
        if res.status_code != 200:
            WaitTime(15)
            
        else:
            timelines = json.loads(res.text)
            return timelines

def SaveData(timeline,LastId):

    for line in timeline:
        #すでに読み込んでいるツイートか判定
        if int(line['id']) <= int(LastId):
            break
        
        #ファイルに追記（日付でファイル名が変わる）
        text = ('../../TwitterData/'+Todays(line).strftime('%Y-%m-%d')+ '.json')
        print(text)
        #df['TweetData'].append(line)
        df={}
        if not os.path.exists(text):
            df={'TweetData':[]}
        else:
            with open(text,'r',encoding='utf-8') as f:
                df = json.load(f)
        with open(text, 'w',encoding='utf-8') as datafile:
            df['TweetData'].append(line)
            json.dump(df,datafile,ensure_ascii=False,indent=4)




def WaitTime(minute):
    for _ in tqdm(range(minute*60)):
        sleep(1)      

def Todays(data):
    CreatedAt = data['created_at'].replace('+0000',"")
    date_dt = datetime.datetime.strptime(CreatedAt, '%a %b %d %H:%M:%S  %Y')
    date = datetime.datetime(year=int(date_dt.strftime('%Y')),
                            month=int(date_dt.strftime('%m')),
                            day = int(date_dt.strftime('%d')),
                            tzinfo=datetime.timezone.utc
                            )
    return date

def UpdateId(data):
    for line in data:
        Id = int(line['id'])
        break
    return Id

"""
def SkipID(timeline,LastId):
    data = pd.DataFrame()
    for line in timeline:
        if int(line['id']) <= int(LastId):
            WaitTime(5)
            return data
        tmp_se = line
        data = data.append(tmp_se, ignore_index=True)
    return data

def SkipDay(df_data):
    date = datetime.datetime.now(datetime.timezone.utc)
    delta = abs(Todays(df_data) - date)
    if delta.days > 0:
        days_frag = 1
        return days_frag, date

    return date

def AppendTweet(data,tweet):
    data = tweet.append(data,ignore_index=True,sort=True)
    return data


def SaveData(data,path):
    dt_now = datetime.datetime.now(datetime.timezone.utc)
    text = (path + dt_now.strftime('%Y-%m-%d')+ '.json')
    data.to_json(text)


def UpdateId(data):
    Id = int(data.iloc[0,8])
    return Id

def ChangeDays(data,frag,dfcolumns):
    if frag == 1:
        data = pd.DataFrame(columns = dfcolumns)
    return data, 0
"""
