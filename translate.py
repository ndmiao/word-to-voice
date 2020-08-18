# coding: utf-8
# Author：南岛鹋 
# Blog: www.ndmiao.cn
# Date ：2020/8/17 20:18
# Tool ：PyCharm

import google_API
import baidu_API
import voice
import os
while(1):
    num = int(input('请输入你想要的功能（谷歌翻译输1，百度翻译输2，转语音输3,退出其他任意数字）：'))
    if num == 1:
        google_API.google_start()
    elif num == 2:
        baidu_API.baidu_start()
    elif num == 3:
        voice.change_voice()
    else:
        os._exit(0)


