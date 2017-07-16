#!/usr/bin/env python2.7.5
#-*-coding:utf-8 -*-
import urllib
import urllib2
import zlib
import re

def get_input():
    cityName=raw_input("please input a city name(Chinese)")
    while (cityName == ""):
        cityName = get_input()
    for ch in cityName.decode('utf-8'):
        if u'\u4e00'<=ch<=u'\u9fff':
            continue
        else:
            print("City name is not chinese")
            cityName=get_input()
            break
    return cityName

def get_name(cityName):
    url="http://wthrcdn.etouch.cn/weather_mini?city="
    url=url+urllib.quote(cityName)
    return url

def get_data(url):
    try:
        data=urllib2.urlopen(url).read()
        data=zlib.decompress(data,16+zlib.MAX_WBITS)
    except urllib2.URLError:
        print("Sorry,we can't connect to the server!")
        return ""
    return data

def data_beautify(data):
    data=data.replace("yesterday","昨天").replace("city","城市").replace("forecast","预报")
    data=data.replace("fengli","风力").replace("fengxiang","风向").replace("type","天气类型")
    data=data.replace("date","日期").replace("high","最高温").replace("low","最低温").replace("ganmao","感冒")
    data=data.replace("{","\n{")
    data=data.replace("}","}\n")
    return data

if __name__=='__main__':
    cityName=get_input()
    data=get_data(get_name(cityName))
    if(data==""):
        print("Data is null!")
    else:
        if(re.search("invilad",data)==None):
            print(data_beautify(data))
        else:
            print("Invalid city")

