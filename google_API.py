# coding: utf-8
# Author：南岛鹋 
# Blog: www.ndmiao.cn
# Date ：2020/8/14 19:07
# Tool ：PyCharm


# coding=utf-8
# -*- coding: UTF-8 -*-
import sys
import requests
import re
from bs4 import BeautifulSoup
import time
import random



def tidySentence(inputs):
    inputs = re.sub(u'&quot;', '"', inputs)
    inputs = re.sub(u'&lt;', '<', inputs)
    inputs = re.sub(u'&gt;', '>', inputs)
    inputs = re.sub(u'&.*?( |;)', ' ', inputs)
    return inputs


def getHTMLText(url):
    header = {
        'authority': 'translate.google.cn',
        'method': 'GET',
        'path': '',
        'scheme': 'https',
        'accept': '*/*',
        'accept-encoding': 'gzip, deflate, br',
        'accept-language': 'zh-CN,zh;q=0.9',
        'cookie': '',
        'user-agent': 'Mozilla/5.0 (Windows NT 10.0; WOW64)  AppleWebKit/537.36 (KHTML, like Gecko) Chrome/63.0.3239.108 Safari/537.36',
        'x-client-data': 'CIa2yQEIpbbJAQjBtskBCPqcygEIqZ3KAQioo8oBGJGjygE='
    }
    try:
        r = requests.get(url,header, timeout=30)
        r.raise_for_status()
        return r.text
    except:
        print("Get HTML Text Failed!")
        return 0


def google_translate(to_translate, from_language="en", to_language="ch-CN"):
    # 根据参数生产提交的网址
    base_url = u"https://translate.google.cn/m?hl={}&sl={}&ie=UTF-8&q={}"
    url = base_url.format(to_language, from_language, tidySentence(to_translate))

    # 获取网页
    html = getHTMLText(url)
    if html:
        soup = BeautifulSoup(html, "html.parser")

    # 解析网页得到翻译结果
    try:
        result = soup.find_all("div", {"class": "t0"})[0].text
    except:
        try:
            print(len(to_translate), str(to_translate))
        except:
            print(len(to_translate), 'Not_a_str')
        print("Translation Failed!")
        result = to_translate

    return result



def google_start():

    language_set = []
    with open("google_set.txt", "r") as f:
        language_type = f.readlines()
        for f_type in language_type:
            language_set.append(f_type.rstrip("\n"))
    with open("article.txt", "r",encoding='utf-8') as f:
        data = f.readlines()
    k = 0
    for sentence in data:
        i=0
        while(i+1 < len(language_set)):
            sentence = google_translate(sentence,from_language=language_set[i], to_language=language_set[i+1])
            i=i+1
            time.sleep(random.random()*3)
            print(sentence)
        k=k+1
        print('第%s句话翻译结束'%(k))
        with open('result.txt', 'a') as f:  # 设置文件对象
            f.write(sentence+'\n')

if __name__ == '__main__':
    google_start()


