#!usr/bin/env python2
# -*- coding: utf-8 -*-

# reference:http://0x007.blog.51cto.com/6330498/1641743
#           http://i.links.cn/subdomain/
import requests,re  # re是Python 2.7.13内置库，无需安装。


def subdomain_query(raw_url):  # PEP8，至少两个空行。
    payload = {'domain': raw_url, 'b2': '1', 'b3': '1', 'b4': '1'}
    r = requests.get("http://i.links.cn/subdomain/", params=payload)  # 带参数的HTTP的GET请求
    file = r.text.encode('ISO-8859-1')  # r是一个响应对象，可以从r中获取信息。
    # 正则
    regex = re.compile('value="(.+?)"><input')
    # 匹配
    result = regex.findall(file)
    # list转换str
    list = '\n'.join(result)
    # 把匹配到的结果写入txt  txt名字取用户输入
    f = open(raw_url+'.txt','w')
    f.write(list)
    f.close()
    return
