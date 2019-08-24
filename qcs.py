# -*- coding: utf-8 -*-
# @Time    : 2019/8/21 12:06
# @Author  : WJ
import requests
import time
from lxml import etree
from ScrapySpider.ScrapySpider.spiders.go_shopping_settings import *

def sasa_spider():
    response = requests.get(sasa["url"], headers=sasa["headers"])
    etree_obj = etree.HTML(response.text)
    title = etree_obj.xpath('//title/text()')[0]
    print(title)

def wastons_spider():
    response = requests.get(wastons["url"], headers=wastons["headers"])
    etree_obj = etree.HTML(response.text)
    title = etree_obj.xpath('//title/text()')[0]
    print(title)

def dfs_spider():
    response = requests.get(dfs["url"], headers=dfs["headers"])
    etree_obj = etree.HTML(response.text)
    title = etree_obj.xpath('//title/text()')[0]
    print(title)

# while 1:
#     sasa_spider()
#     wastons_spider()
#     dfs_spider()
#     time.sleep(5)
sasa_spider()
wastons_spider()
dfs_spider()