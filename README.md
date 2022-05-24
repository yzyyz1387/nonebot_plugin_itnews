<p align="center">
  <a href="https://v2.nonebot.dev/"><img src="https://v2.nonebot.dev/logo.png" width="200" height="200" alt="nonebot"></a>
</p>


<div align="center">

   
**你的star是我的动力**  
**↓**  
<img src="https://img.shields.io/github/stars/yzyyz1387/nonebot_plugin_itnews.svg?style=social">  
# nonebot IT咨讯📰

_✨ NoneBot2 IT咨讯插件 ✨_

</div>


## 安装💿
`pip install nonebot-plugin-itnews -i https://pypi.python.org/simple`


## 导入📲
在**bot.py** 导入，语句：
`nonebot.load_plugin("nonebot_plugin_itnews")`


## 目录结构📂

初次使用时会创建`news`和`source`并下载资源文件至`source`下
```
├─news
├   └─20211110.png
├─source
├   └─background.png.
├   └─font.ttf
├─__init__.py
├─itnews.py
```

## 配置📝
请前往天行数据申请api:
https://www.tianapi.com/apiview/20
(api每日免费100次调用,插件每日只请求一次，当`news`目录中存在当天的新闻时，直接从本地文件发送，不调用api)

## 在`.env.dev`中添加✏
CUSTOM_CONFIG_IT=[你申请api的key]

## 指令💻
`it新闻`
`It新闻`
`IT新闻`
`it咨讯`
`It咨讯`
`IT咨讯`
`IT`
`it`
`It`

每日只请求一次，当`news`目录中存在当天的新闻时，直接从本地文件发送，不请求api

**给个star吧~**

## 其他插件 
[简易群管](https://github.com/yzyyz1387/nonebot_plugin_admin)  
[在线运行代码](https://github.com/yzyyz1387/nonebot_plugin_code)  
[it咨讯（垃圾插件）](https://github.com/yzyyz1387/nonebot_plugin_itnews "it资讯")  
[工作性价比（还没更新beta不能用）](https://github.com/yzyyz1387/nonebot_plugin_workscore)  
[黑丝插件（jsdelivr问题国内服务器不能用）](https://github.com/yzyyz1387/nonebot_plugin_heisi)

## 截图🖼

![](https://cdn.jsdelivr.net/gh/yzyyz1387/blogimages/img/nonebot_p_it.png)

![](https://cdn.jsdelivr.net/gh/yzyyz1387/blogimages/img/none_p_it2.png)



