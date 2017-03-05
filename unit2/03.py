#coding:utf-8
#测试导航树

from urllib.request import urlopen
from bs4 import BeautifulSoup
import re

html = urlopen('http://www.pythonscraping.com/pages/page3.html')
bsObj = BeautifulSoup(html)

#找出table标签下的所有字标签
# for child in bsObj.find('table',{'id':'giftList'}).children:
#     print(child)

#处理兄弟标签
# for sibling in bsObj.find('table',{'id':'giftList'}).tr.next_siblings:
#     print(sibling)
#
# #父标签处理
# print(bsObj.find('img',{'src':'../img/gifts/img6.jpg'}).parent.previous_sibling.get_text())

#找到所有的img标签
# imgList = bsObj.find_all('img')
# for a in imgList:
#     print(a)

#找到特定格式的img标签
images = bsObj.find_all('img',{'src':re.compile('\.\.\/img\/gifts\/img.*\.jpg')})
for image in images:
    print(image)