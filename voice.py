# coding: utf-8
# Author：南岛鹋
# Blog: www.ndmiao.cn
# Date ：2020/8/14 19:07
# Tool ：PyCharm

import requests
import time
import random

def change_voice():
    k = 0
    languages = []
    with open("result.txt", "r") as f:
        language_type = f.readlines()
        for f_type in language_type:
            languages.append(f_type.rstrip("\n"))
    for language in languages:
        base_url = 'http://tts.baidu.com/text2audio?cuid=baiduid&lan=zh&ctp=1&pdt=311&tex={}'
        url = base_url.format(language)
        res = requests.get(url)
        music = res.content
        k = k+1
        print('第%s句话转化语音成功' %(k))
        path = 'voice/'+str(k)+'.mp3'
        with open(path, 'ab') as file: #保存到本地的文件名
            file.write(music)
            file.flush()
        time.sleep(random.random()*3)

if __name__ == '__main__':
    change_voice()