#coding:utf-8
#第一个例子

from urllib.request import urlopen
from bs4 import  BeautifulSoup
html = urlopen('http://www.sparke.cn/exercise/settopic/lx_a/rand/2475.html')
f = open('/home/engineman/Desktop/02.txt','w')
#this code is used to save byte to txt
f.buffer.write(html.read())
f.close()
