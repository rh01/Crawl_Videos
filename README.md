本教程主要对 [百思不得姐](https://budejie.com)视频网站进行爬取视频，并且利用GUI编程创建可视化的窗口界面。用于显示抓取的状态信息和内容。

## Priciple Of Spider

打开网站 -- 获取源码 -- 想要的内容（正则表达式）-- 匹配



## Introduction

爬视频,最终的图像界面如下所示。

![](https://ooo.0o0.ooo/2017/06/26/59511e46583a1.png )

click **抓取视频** --

![](https://ooo.0o0.ooo/2017/06/26/59511ef8e4d59.png)

![](https://ooo.0o0.ooo/2017/06/26/5951201345108.png)
## requirement

* PyCharm
* Python=3.5.2
    - Tkinter(default)
    - threading
    - requests
    - urllib
    - sys
    - re

## Steps

1. 创建窗口
2. 爬视频 --多线程
    * 获取整个页面的源码
    * 解析源码（正则表达式）
    * 匹配到最大的div盒子（视频+名字）
    * 匹配视频
    * 匹配名字
    * 分别匹配
    * 下载并且展示

## Tips

1. findall(正则表达式,html源码)
2. zip()函数
3. Tkinter package
4. re module
5. 正则表达式

## License

![](https://img.shields.io/packagist/l/doctrine/orm.svg)

    
    
    