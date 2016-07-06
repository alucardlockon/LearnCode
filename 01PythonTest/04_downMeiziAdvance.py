#coding=utf-8
import urllib
import re
import os

def getHtml(url):
    page=urllib.urlopen(url)
    html=page.read()
    return html

def getImgContent(html):
    reg=r'href="(.+?\.html)"'
    imgre=re.compile(reg)
    contentlist=re.findall(imgre,html)
    x=0
    for url in contentlist:
        html=getHtml(url)
        getImgAdvance(html,x)
        x+=1
    return imglist

def getImgAdvance(html,i):
    reg=r'src="(.+?\.jpg)"'
    imgre=re.compile(reg)
    imglist=re.findall(imgre,html)
    x=0
    for imgurl in imglist:
        if not os.path.isdir('img'+str(i)):
            os.makedirs('img'+str(i))
        urllib.urlretrieve(imgurl,'img'+str(i)+'\\'+str(x)+'.jpg')
        x+=1
    return imglist

html=getHtml("http://www.meizitu.com/")

print getImgContent(html)
