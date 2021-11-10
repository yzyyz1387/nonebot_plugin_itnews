# python3
# -*- coding: utf-8 -*-
# @Time    : 2021/11/10 16:58
# @Author  : yzyyz
# @Email   :  youzyyz1384@qq.com
# @File    : __init__.py
# @Software: PyCharm
import nonebot
from nonebot import on_command
from nonebot.rule import to_me
from nonebot.adapters.cqhttp import Bot, Event,Message,MessageEvent,MessageSegment
from nonebot.typing import T_State
from . import itnews
from os.path import dirname
import os
import time
year = time.strftime("%Y", time.localtime())
mon = time.strftime("%m", time.localtime())
day = time.strftime("%d", time.localtime())

fname = dirname(__file__) +"/news/"+str(year) + str(mon) + str(day) + ".png"
itnew = on_command("itzixun", aliases={"it新闻", "It新闻","IT新闻","it咨讯", "It咨讯","IT咨讯","IT","it","It"})

@itnew.handle()
async def tianqi(bot: Bot, event: Event, state: dict):
    if event.get_user_id != event.self_id:
        path=fname
        if os.path.exists(path)==False:
            
            keys=nonebot.get_driver().config.custom_config_it
            itnews.draw_news(keys)
            await bot.send(
                event = event,
                message = MessageSegment.image(f"file:///{fname}"),
                at_sender = True
            )
        else:
            await bot.send(
                event=event,
                message=MessageSegment.image(f"file:///{fname}"),

            )

__usage__ = """
"it新闻", "It新闻","IT新闻","it咨讯", "It咨讯","IT咨讯","IT","it","It"
"""
__plugin_name__ = "it咨讯"

__permission__ = 2
__help__version__ = '0.1.5'