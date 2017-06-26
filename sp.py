# -*- coding:utf-8 -*-

"""
Please note, this code is only for python 3+. If you are using python 2+, please modify the code accordingly.
created by: Shine
Date: 2017/6/26
"""

from Tkinter import *
from ScrolledText import ScrolledText # 文本滚动条
import urllib, requests
import re
import threading
import sys
reload(sys)
sys.setdefaultencoding('utf-8') # 输出的内容


url_name = []
a = 1 # 页数
def get():
    global a
    hd = {'User-Agent':'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/59.0.3071.109 Safari/537.36'}
    url = 'http://www.budejie.com/video/' + str(a)
    var1.set('已经获取搭配第%s页视频'%(a))
    html = requests.get(url, headers=hd).text # 获取源码
    # print html
    url_content = re.compile(r'(<div class="j-r-list-c">.*?</div>.*?</div>)', re.S) # 提高效率  .*? 懒惰匹配
    url_contents = re.findall(url_content, html)
    # print url_contents # list 中文在可迭代对象里面是unicode编码问题

    # 匹配视频
    for i in url_contents:
        url_reg = r'data-mp4="(.*?)">' #.*?任意匹配（）取出来的
        url_items = re.findall(url_reg, i)
        # print url_items # 匹配到视频
        if url_items: # 判断视频列表是否存在
            name_reg = re.compile('<a href="/detail-.{8}?.html">(.*?)</a>') #.{8}?表示8位数字
            name_items = re.findall(name_reg, i)
            # print name_items #视频的名称
            for i, k in zip(name_items, url_items):
                url_name.append([i, k])
                # print i,k
    return url_name

# 视频下载并且展示在GUI
id = 1 #视频的个数
def write():
    global id
    while id<10:
        url_name = get() # 调用上面的函数
        for i in url_name: #i[0] name i[1] url
            urllib.urlretrieve(i[1],'video\\%s.mp4'%(i[0].decode('utf-8').encode('gbk')))
            text.insert(END, str(id)+'.'+i[1]+'\n'+i[0]+'\n')
            url_name.pop(0) # 删除已经有的东西
            id+=1
        var1.set('视频名字和视频链接已经抓取完毕')


# 多线程
def start():
    th = threading.Thread(target=write)
    th.start()




root = Tk() # 实例化一个变量
root.title('python shine')
root.geometry('+600+100') # 改变窗口的位置+ 改变窗口的大小x

text = ScrolledText(root, font=('微软雅黑', 10))
text.grid()

button = Button(root,text="开始爬取", font=('微软雅黑', 10), command=start)
button.grid()

var1 = StringVar()
label = Label(root, font=('微软雅黑', 10), fg='red', textvariable=var1) # textvariable 可改变
label.grid()
var1.set('已准备...')



root.mainloop() # 发送指令



