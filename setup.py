# python3
# -*- coding: utf-8 -*-
# @Time    : 2021/11/10 21:13
# @Author  : yzyyz
# @Email   :  youzyyz1384@qq.com
# @File    : setup.py.py
# @Software: PyCharm
from setuptools import setup, find_packages

setup(
    name="nonebot_plugin_itnews",
    version="0.1.3",
    keywords=("pip", "nonebot2", "nonebot", "itnews", "nonebot_plugin"),
    description="a nonebot plugin",
    long_description="a nonebot plugin, generate pictures from news",
    license="MIT Licence",

    url="https://github.com/yzyyz1387/nonebot_plugin_itnews",
    author="yzyyz1387",
    author_email="youzyyz1384@qq.com",

    packages=find_packages(),
    include_package_data=True,
    platforms="any",
    install_requires=["Pillow","requests"]
)