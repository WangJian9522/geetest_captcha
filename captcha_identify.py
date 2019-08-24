# -*- coding: utf-8 -*-
# @Time    : 2019/8/24 13:10
# @Author  : WJ

from aip import AipOcr
# from PIL.CurImagePlugin import

class WebImgIdentify(object):
    def __init__(self):
        self.config = {
            'appId': '17076064',
            'apiKey': 'Vy2pbGG2meG24AwsZKbP8XVq',
            'secretKey': 'hg3n0I9HugWtG4Gs9K45pwa8DFasz2zA',
        }
        self.client = AipOcr(**self.config)

    """ 读取图片 """

    def get_file_content(self, filePath=r'D:\Documents\NewProject\ScrapySpider\ScrapySpider\spiders\geetest.png'):
        with open(filePath, 'rb') as fp:
            return fp.read()

    def web_img_identify(self, img):

        # 如果有可选参数
        options = {}
        options["detect_direction"] = "true"
        options["detect_language"] = "true"

        # 带参数调用网络图片文字识别, 图片参数为本地图片
        result = self.client.webImage(img, options)
        print(result)

if __name__ == '__main__':
    m = WebImgIdentify()
    m.web_img_identify(m.get_file_content())