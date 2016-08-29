#!/usr/bin/python
# -*- coding: utf-8 -*-
import requests
import tweepy

weather_url='http://weather.livedoor.com/forecast/webservice/json/v1?city=270000'

tw_apikey = ''
tw_apisec = ''
tw_acctoken = ''
tw_accsec = ''

def handler_hotjava(event, context):
    r = requests.get(weather_url)
    if(r.status_code==200):
        # 気温情報取得
        weather_json=r.json()
        link_url=weather_json['link']
        forecast=weather_json['forecasts'][0]
        today_max=int(forecast['temperature']['max']['celsius'])
        date_label=forecast['dateLabel']
        date_num=forecast['date']
        
        # 気温がホットジャバかどうか判断
        java_tbl=[(28, u'の気温がHotJava'),
                  (35, u'の気温はモットジャバ'),
                  (37, u'も気温がモットジャバ')]
        java_tbl.reverse();
        for tpl in java_tbl:
            if tpl[0]<=today_max:
                tweet_java(date_label+tpl[1]+" "+link_url+" "+date_num)
                return

def tweet_java(msg):
    auth=tweepy.OAuthHandler(tw_apikey, tw_apisec)
    auth.set_access_token(tw_acctoken, tw_accsec)
    api=tweepy.API(auth)
    api.update_status(msg)

if __name__ == '__main__':
    handler_hotjava([],[])
