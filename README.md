# 百度指数(咨询指数)半自动化爬取

脚本仅爬取咨询指数
百度指数-> https://github.com/longxiaofei/spider-BaiduIndex/tree/master/new_spider_without_selenium

环境  chrome 76 selenium

mouse.py 
获取当前鼠标位置 

spiderselenium.py
使用方法：
1.修改源码中url链接为百度指数xxx的展示页面，行18.
  修改行31，具体看注释
2.运行spiderselenium.py
3.登录百度账号，将你要抓取的折线图完整的显示出来，可能需要拉伸浏览器
4.依照脚本提示，运行mouse.py ，需要模拟鼠标移动。在spiderselenium.py输入X 初始Y 末Y ，分别对应鼠标移动初始点的（X，初始Y），末尾点的（x，末Y）
5.继续执行




 
