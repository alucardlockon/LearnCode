#need to install pywin32
import win32clipboard as w
import win32con

def getText():
     w.OpenClipboard()
     d = w.GetClipboardData(win32con.CF_TEXT)
     w.CloseClipboard()
     return d

def setText(aString):
     w.OpenClipboard()
     w.EmptyClipboard()
     w.SetClipboardData(win32con.CF_TEXT, aString)
     w.CloseClipboard()

setText('123')
