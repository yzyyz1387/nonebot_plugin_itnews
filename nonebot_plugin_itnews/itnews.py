# python3
# -*- coding: utf-8 -*-
# @Time    : 2021/11/10 16:59
# @Author  : yzyyz
# @Email   :  youzyyz1384@qq.com
# @File    : itnews.py
# @Software: PyCharm

import requests
from PIL import Image, ImageDraw, ImageFont
import time
from os.path import dirname
year = time.strftime("%Y", time.localtime())
mon = time.strftime("%m", time.localtime())
day = time.strftime("%d", time.localtime())
fname = dirname(__file__) +"/news/"+str(year) + str(mon) + str(day) + ".png"
datetitle = str(year) + "." + str(mon) + "." + str(day)

headers={
    "User-Agent": "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWe bKit/537.36 (KHTML, like Gecko) Chrome/93.0.4544.0 Safari/537.36 Edg/93.0.933.1",
}

def get_news(keys):
    url = "http://api.tianapi.com/it/index?key="+keys+"&num=15"
    html = requests.get(url,headers=headers).json()

    data = []
    for title in html["newslist"]:
        print(title["title"])
        data.append(title["title"])
    return data


def draw_news(keys):
    news_list=get_news(keys)
    text = "IT 咨讯"
    ttfpath = dirname(__file__) +"/source/font.ttc"
    bgpath = dirname(__file__) +"/source/background.png"
    chars_x = 50
    img = Image.open(bgpath)
    ttf = ImageFont.truetype(ttfpath, 35)
    tf = ImageFont.truetype(ttfpath, 160)
    img_draw = ImageDraw.Draw(img)
    img_draw.text((250, 140), text, font=tf, fill=(255, 255, 255))
    img_draw.text((400, 400), datetitle, font=ttf, fill=(255, 255, 255))
    chars_y = 500
    for i in range(15):
        img_draw.text((chars_x, chars_y), str(i + 1) + ". " + news_list[i], font=ttf, fill=(100, 100, 100))
        chars_y += 65
    byttf = ImageFont.truetype(ttfpath, 15)
    img_draw.text((850, 1550), "BY Rubot @yzyyz", font=byttf, fill=(0, 0, 0))
    img.save(fname)

