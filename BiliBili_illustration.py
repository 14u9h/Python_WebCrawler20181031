#!/usr/bin/python
# coding:utf-8
# requests模块 动态网页抓取(异步更新), bilibili画友，最热插画批量下载；
# 请勿恶意使用，以免给目标站及自己造成不必要的麻烦；

import requests
import re
import time
#伪装浏览器报头
headers = {'User-Agent' : 'Mozilla/5.0 (Windows; U; Windows NT 6.1; en-US; rv:1.9.1.6) Gecko/20091201 Firefox/3.5.6','Pragma' : 'no-cache','Referer' : 'https://h.bilibili.com/eden/draw_area','Cache-Control' : 'no-cache','Connection' : 'keep-alive'}
#拼接url抓取页面源码
kk = 0
for i in range(25):
    link_parm = {'category':'illustration', 'type':'hot', 'page_num': i * 1}
    link_url = 'https://api.vc.bilibili.com/link_draw/v2/Doc/list'
    r = requests.get(link_url,params=link_parm,headers=headers)
    print(r.url)
#正则匹配页面源码中的插画url   
    html = r.text
    prpr_url = re.findall('{"img_src":"(.*?)"',html)
#下载保存匹配到的图片（需在脚本目录下手动新建“photo”文件夹以存放图片）
    for save_url in prpr_url:
        save_img = requests.get(save_url,headers=headers)
        with open('photo\\'+'img'+str(kk)+'.jpg','ab')as file:
            file.write(save_img.content)
            kk+=1
            time.sleep(10)  # 秒为单位，自行修改为合适的速度。
