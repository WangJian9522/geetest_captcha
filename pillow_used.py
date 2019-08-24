# -*- coding: utf-8 -*-
# @Time    : 2019/8/24 14:17
# @Author  : WJ

import requests
from PIL import Image

# response = requests.get('http://static.geetest.com/nerualpic/phrase_l1_zh_2019.08.06/harley1/05c3e08d531a5e43c6eab78a8c6d08ac.jpg?challenge=7e037d86ebe9b83c810207a229271678')
# #
# img = response.content
img = r'D:\Documents\NewProject\ScrapySpider\ScrapySpider\spiders\geetest.png'
picture = Image.open(img)
r_picture = picture.crop((0,0,380,380))
r_picture.save('geetest.png')
# r_picture.show()