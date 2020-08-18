# coding: utf-8
# Author：南岛鹋 
# Blog: www.ndmiao.cn
# Date ：2020/8/16 21:31
# Tool ：PyCharm

# /usr/bin/env python
# coding=utf8

import json
import http.client  # 修改引用的模块
import hashlib  # 修改引用的模块
from urllib import parse
import random
import time

def get_secretkey():
    app_secret = []
    with open("appid.txt", "r") as f:
        language_type = f.readlines()
        for f_type in language_type:
            app_secret.append(f_type.rstrip("\n"))
    return app_secret


def baidu_translate(to_translate, from_language="en", to_language="zh"):
    app_secret = get_secretkey()
    appid = app_secret[0]  # 你的appid
    secretKey = app_secret[1]  # 你的密钥

    httpClient = None
    myurl = '/api/trans/vip/translate'
    q = to_translate
    fromLang = from_language
    toLang = to_language
    salt = random.randint(32768, 65536)
    sign = appid + q + str(salt) + secretKey
    m1 = hashlib.md5()
    m1.update(sign.encode("utf-8"))
    sign = m1.hexdigest()
    myurl = myurl + '?appid=' + appid + '&q=' + parse.quote(q) + '&from=' + fromLang + '&to=' + toLang + '&salt=' + str(
        salt) + '&sign=' + sign

    try:
        httpClient = http.client.HTTPConnection('api.fanyi.baidu.com')
        httpClient.request('GET', myurl)
        response = httpClient.getresponse()

        # 转码
        html = response.read().decode('utf-8')
        html = json.loads(html)
        dst = html["trans_result"][0]["dst"]
        return dst
    except Exception as e:
        print(e)
    finally:
        if httpClient:
            httpClient.close()

def baidu_start():
    language_set = []
    with open("baidu_set.txt", "r") as f:
        language_type = f.readlines()
        for f_type in language_type:
            language_set.append(f_type.rstrip("\n"))
    with open("article.txt", "r",encoding='utf-8') as f:
        data = f.readlines()
    k = 0
    for sentence in data:
        i=0
        while(i+1 < len(language_set)):
            sentence = baidu_translate(sentence,from_language=language_set[i], to_language=language_set[i+1])
            i=i+1
            time.sleep(1)
            print(sentence)
        k=k+1
        print('第%s句话翻译结束'%(k))
        with open('result.txt', 'a') as f:  # 设置文件对象
            f.write(sentence+'\n')

if __name__ == '__main__':
    baidu_start()