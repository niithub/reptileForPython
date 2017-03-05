#coding:utf-8
#测试爬取维基百科中凯文.贝肯的信息
#本篇测试代码尽量不要多次运行，这会加大wiki的服务器负载，不要过多的占用wiki这个教育资源

from urllib.request import urlopen
from bs4 import BeautifulSoup
import re
import datetime
import random

#用系统当前时间生成一个随机数
#保证每次程序运行的时候，维基百科词条的选择都是一个全新的随机路径
random.seed(datetime.datetime.now())

#定义一个getLinks函数
def getLinks(articleUrl):
    html = urlopen('http://en.wikipedia.org'+articleUrl)
    bsObj = BeautifulSoup(html)
    return bsObj.find('div',{'id':'bodyContent'}).find_all('a',href = re.compile('^(/wiki/)((?!:).)*$'))

links = getLinks('/wiki/Kevin_Bacon')
f = open('/home/engineman/Desktop/wiki.txt','w')
while len(links) > 0 :
    newArticle = links[random.randint(0,len(links)-1)].attrs['href']
    f.write(newArticle)
    f.write('\n')
    links = getLinks(newArticle)
f.close()