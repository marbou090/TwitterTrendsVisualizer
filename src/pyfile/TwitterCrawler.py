#!/usr/bin/python
# -*- coding: utf-8 -*-

import CrawlerFunction as cf

import pandas as pd

def main():
    url = "https://api.twitter.com/1.1/statuses/home_timeline.json"  # タイムライン取得エンドポイント
    twitter = cf.InitilizeConfig()

    LastId = 0
    while(True):
        timeline = cf.GetTweet(url,twitter)
        cf.SaveData(timeline,LastId)
        cf.WaitTime(5)
        #print(timeline)

        LastId = cf.UpdateId(timeline)



if __name__ == '__main__':
    main()