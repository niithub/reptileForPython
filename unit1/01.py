#coding:utf-8
#第一个例子

from urllib.request import urlopen
from bs4 import  BeautifulSoup
from urllib.error import HTTPError,URLError
def getTitle(url):
    try:
        html = urlopen(url)
    except (HTTPError,URLError) as e:
        return None
    try:
        bsObj = BeautifulSoup(html.read())
        title = bsObj.body.div
    except AttributeError as e:
        return None
    return title
title = getTitle('http://www.sparke.cn/exercise/settopic/lx_a/rand/2475.html')
if title == None:
    print('Title is not found')
else:
    print(title)