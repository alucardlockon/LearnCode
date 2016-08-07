#coding=utf-8
import wx
import os
import wx.html2
import urllib
import re
from bs4 import BeautifulSoup

def getHtml(url):
    page=urllib.urlopen(url)
    html=page.read()
    return html

def getDiv(html):
    #reg2=r'<div class="js-repo-filter position-relative">.*<div id="pinned-repos-modal-wrapper"></div>'
    #imgre=re.compile(reg2)
    #imglist=re.findall(imgre,html)
    soup = BeautifulSoup(html, 'html.parser')
    lst=soup.find_all('div', id="contributions-calendar")
    #two = i.find_all('li')
    if len(lst) > 0:
        #print lst[0]
        return lst[0]
    else :
        return "no html found"

def getHead(html):
    soup = BeautifulSoup(html, 'html.parser')
    return soup.head
    

class MyBrowser(wx.Dialog):
  def __init__(self, *args, **kwds):
    wx.Dialog.__init__(self, *args, **kwds)
    sizer = wx.BoxSizer(wx.VERTICAL)
    self.browser = wx.html2.WebView.New(self)
    sizer.Add(self.browser, 1, wx.EXPAND, 10)
    self.SetSizer(sizer)
    self.SetSize((1200, 200))

html=getHtml("https://github.com/alucardlockon")
localhtml=getHtml("file:\\\\\\"+os.getcwd()+"\\08.html")  
app = wx.App()
dialog = MyBrowser(None, -1)
#dialog.browser.LoadURL("https://github.com/alucardlockon")
#dialog.browser.LoadURL(os.getcwd()+"/08.html")
#dialog.browser.SetPage("<body>08.html</body>",os.getcwd()+"/08.html")
head=getHead(localhtml)
div=getDiv(html)
dialog.browser.SetPage(str(head).decode('UTF-8')+'<body>'+str(div).decode('UTF-8')+'</body>'\
    ,os.getcwd()+"/08.html")
dialog.SetTitle('GithubComboPage')
dialog.Show()
app.MainLoop()

'''MainWindow类完成最简单的编辑功能，添加一个主菜单，两个子菜单（about和exit）
import wx

class MainWindow(wx.Frame):
  def __init__(self, parent, title):
    wx.Frame.__init__(self, parent, title=title, size=(300, 300))
    self.control = wx.TextCtrl(self, style=wx.TE_MULTILINE)
  
    self.setupMenuBar()
    self.Show(True)
  
  def setupMenuBar(self):
    self.CreateStatusBar()
  
    menubar = wx.MenuBar()
    menufile = wx.Menu()
  
    mnuabout = menufile.Append(wx.ID_ABOUT, '&About', 'about this shit')
    mnuexit = menufile.Append(wx.ID_EXIT, 'E&xit', 'end program')
  
    menubar.Append(menufile, '&File')
  
    #事件绑定
    self.Bind(wx.EVT_MENU, self.onAbout, mnuabout)
    self.Bind(wx.EVT_MENU, self.onExit, mnuexit)
      
    self.SetMenuBar(menubar)
  
  def onAbout(self, evt):
      dlg = wx.MessageDialog(self, 'This app is a simple text editor', 'About my app', wx.OK)
      dlg.ShowModal()
      dlg.Destroy()
  
  def onExit(self, evt):
      self.Close(True)
app = wx.App(False)
frame = MainWindow(None, 'Small Editor')
frame.SetTitle('GithubComboPage')
wx.wxWebView.Create(frame,'www.github.com',)
app.MainLoop() #循环监听事件
'''

'''
# tk test
from Tkinter import *

class Application(Frame):
    def say_hi(self):
        print "hi there, everyone!"

    def createWidgets(self):
        self.QUIT = Button(self)
        self.QUIT["text"] = "QUIT"
        self.QUIT["fg"]   = "red"
        self.QUIT["command"] =  self.quit

        self.QUIT.pack({"side": "left"})

        self.hi_there = Button(self)
        self.hi_there["text"] = "Hello",
        self.hi_there["command"] = self.say_hi

        self.hi_there.pack({"side": "left"})

    def __init__(self, master=None):
        Frame.__init__(self, master)
        self.pack()
        self.createWidgets()

root = Tk()
app = Application(master=root)

app.mainloop()
root.destroy()
'''


