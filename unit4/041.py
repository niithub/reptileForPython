#coding:utf-8
#根据url下载文件
#以照片为例

from urllib.request import urlopen
from urllib.request import urlretrieve
from bs4 import BeautifulSoup

html = urlopen('httP://www.pythonscraping.com')
bsObj = BeautifulSoup(html)
imageLocation = bsObj.find('a',{'id':'logo'}).find('img')['src']
urlretrieve(imageLocation,'logo.jpg')