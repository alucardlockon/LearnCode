#coding=utf-8
import urllib
import re

def getHtml(url):
    page=urllib.urlopen(url)
    html=page.read()
    return html

def getImg(html):
    reg2=r'<div class="boxed-group flush">.*</div>'
    reg=r'<div class="boxed-group flush">/.*/</div><div class="activity-listing contribution-activity" id="js-contribution-activity">'
    imgre=re.compile(reg2)
    imglist=re.findall(imgre,html)
    return imglist

html=getHtml("https://github.com/alucardlockon")

print getImg(html)
