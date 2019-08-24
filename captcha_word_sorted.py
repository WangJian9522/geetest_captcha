# -*- coding: utf-8 -*-
# @Time    : 2019/8/23 21:39
# @Author  : WJ

import requests
from lxml import etree
from collections import Counter

class captcha_identify():
    """有词义的点字验证码, 使用百度或google搜索结果识别顺序, 一般只要不出现乱七八糟的词语就不会出错"""
    def __init__(self):
        self.url = 'https://www.baidu.com/s?'
        self.ua = {
            "User-Agent": "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/76.0.3809.100 Safari/537.36"}
        self.params = {'wd': '哈哈娃'}
    def req_baidu(self):
        """返回搜索结果的标题列表"""
        response = requests.get(self.url, headers=self.ua, params=self.params)
        etree_obj = etree.HTML(response.text)
        # title = etree_obj.xpath('//title/text()')[0]
        # print(title)
        title_ls = etree_obj.xpath('//h3[@class="t"]/a')
        result = []
        for i in title_ls:
            t = ''
            title_item = i.xpath('.//text()')
            # print(title_item)
            for j in title_item:
                t += j
            result.append(t)
        # print(result)
        return self.matching_result(result)
    def matching_result(self, result):
        """进行结果匹配"""
        key = self.params.get('wd')
        count = []
        for result_item in result:
            # 对条目字符串进行遍历
        # result_item = result[1]
        # print(result_item)
            for i in result_item:
                # 如果条目元素符合搜索关键字
                if i in key:
                    # 获取坐标并根据搜索关键字长度切片
                    num = result_item.index(i)
                    maybe_item = result_item[num: num+len(key)]
                    # 判断双方元素个数是否相等
                    if Counter(key) == Counter(maybe_item):
                        count.append(maybe_item)
        # end & end 返回搜索结果最多的排序 ~
        most_result = Counter(count).most_common()
        print(most_result[0][0])
if __name__ == '__main__':
    c = captcha_identify()
    c.req_baidu()
# for i in result:
#     if i in key:
#         num = result.index(i)
#         a = result[num: len(key)]
#         if set(key) == set(a):
#             print(a)


