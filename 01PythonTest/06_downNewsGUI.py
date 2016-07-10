#-*-coding:utf-8-*- 

from re import search 

import urllib2 

import MySQLdb 

from BeautifulSoup import BeautifulSoup 

import threading 

from datetime import datetime 

from optparse import OptionParser 

import sys 

import logging 

import socket 

from urlparse import urlparse 

import httplib 

  

URLS={} 

lock=threading.Lock() 

  

class newThread(threading.Thread): 

    def __init__(self,level,url,db): 

        threading.Thread.__init__(self) 

        self.level=level 

        self.url=url 

        self.db=db 

    def run(self): 

        global lock 

        global log 

        for i in self.url: 

            log.debug('%s:%s'%(datetime.now(),i)) 

            print i 

            temp,html,data=getURL(i) 

            #由于无法打开此url，超时，返回的状态码不是200， 

            #弃掉此url，重新开始循环 

            if not temp: 

                continue 

            #获取锁，让此线程安全的更新数据 

            if lock.acquire() : 

                self.db.save(i,html,data) 

                #所有线程将收集到的url存入URLS列表， 

                #然后在主线程中将URL中重复的url删除。 

                URLS[self.level].extend(temp) 

                lock.release() 

  

class saveData(): 

    def __init__(self): 

        self.db=MySQLdb.connect(user='root',db='sp',unix_socket='/tmp/mysql.sock') 

        self.cur=self.db.cursor() 

        self.cur.execute('delete from webdata') 

        self.commit() 

        log.info('%s:Connect database success'%datetime.now()) 

    def save(self,url,html,pureData): 

        global log 

        SQL='''insert into webdata values('%s','%s','%s')'''%(url,html,pureData) 

        try: 

            self.cur.execute(SQL) 

        except(MySQLdb.ProgrammingError,MySQLdb.OperationalError),e: 

            log.error('%s:%s'%(datetime.now(),e)) 

            return 

        self.commit() 

    def commit(self): 

        self.db.commit() 

    def close(self): 

        self.db.close() 

  

def getURL(url): 

    URLS=[] 

    global log 

    global source 

    global domainName 

    try: 

        page=urllib2.urlopen(url) 

    except(urllib2.URLError,httplib.BadStatusLine): 

        log.error('%s:URL CAN NOT OPEN----%s'%(datetime.now(),url)) 

        return('','','') 

    else: 

        if page.code==200: 

            try: 

                html=page.read().decode('gbk','ignore').encode('utf-8') 

            except: 

                log.error('%s:TIME OUT----%s'%(datetime.now(),url)) 

                print'TIME OUT' 

                return('','','') 

        else: 

            log.error('%s:RESPONSE CODE IS NOT 200----%s'%(datetime.now(),url)) 

            return('','','') 

    html=html.replace("'",'"') 

    #获取去掉HTML元素后的数据 

    try: 

        pureData=''.join(BeautifulSoup(html).findAll(text=True)).encode('utf-8') 

    except UnicodeEncodeError: 

        pureData=html 

    #下面的代码用于在网页中寻找符合条件的url地址 

    rawHtml=html.split('\n') 

    for i in rawHtml: 

        times=i.count('') 

        if times: 

            for y in range(times): 

                pos=i.find('') 

                if pos!=-1: 

                    #在网页中寻找a标记，提取其中的链接， 

                    #链接有两种形式的，一种双引号，一种单引号 

                    newURL=search('<a href=".+"',i[:pos]) 

                    if newURL is not None: 

                        newURL=newURL.group().split(' ')[1][6:-1] 

                        if'">' in newURL: 

                            newURL=search('.+">',newURL) 

                            if newURL is None: 

                                continue 

                            newURL=newURL.group()[:-2] 

                        #若地址为空，则进入下一个循环 

                        if not newURL: 

                            continue 

                        #如果是相对地址，需要转为绝对地址    

                        if not newURL.startswith('http'): 

                            if newURL[0]=='/': 

                                newURL=source+newURL 

                            else: 

                                newURL=source+'/'+newURL 

                        if domainName not in newURLornewURLinURLSornewURL==urlornewURL==url+'/': 

                            continue 

                        URLS.append(newURL) 

                    i=i[pos+4:] 

    return(URLS,html,pureData) 

  

if __name__=='__main__': 

    USAGE=''' 

    spider -u [url] -d [num] -t [num] -o [secs] -l [filename] -v [level] 

        -u:    url of a websit 

        -d:    the deeps of the spider will get into.default is 2 

        -t:    how many threads work at the same time.default is 10 

        -o:    url request timeout.default is 20 secs 

        -l:    assign the logfile name and location.default name is 'logSpider.log' 

        -v:    values are 'quiet' 'normal' 'all'.default is 'normal' 

            'simple'----    only log the error message 

            'normal'----    error message and some addtion message 

                'all'    ----    not only message ,but also urls will be logged. 

    Examples: 

        spider -u http://www.chinaunix.net -t 16 -v normal 

    ''' 

    LEVELS={'simple':logging.WARNING, 

            'normal':logging.INFO, 

            'all':logging.DEBUG} 

    opt=OptionParser(USAGE) 

    opt.add_option('-u',type='string',dest='url') 

    opt.add_option('-d',type='int',dest='level',default=2) 

    opt.add_option('-t',type='int',dest='nums',default=10) 

    opt.add_option('-o',type='int',dest='out',default=20) 

    opt.add_option('-l',type='string',dest='name',default='logSpider.log') 

    opt.add_option('-v',type='string',dest='logType',default='normal') 

    options,args=opt.parse_args(sys.argv) 

    source=options.url 

    level=options.level 

    threadNums=options.nums 

    timeout=options.out 

    logfile=options.name 

    logType=options.logType 

    if not sourceorlevel<0 or threadNums<1 or timeout<1 or logType not in LEVELS.keys(): 

        print opt.print_help() 

        sys.exit(1) 

    if not source.startswith('http://'): 

        source='http://'+source 

    if source.endswith('/'): 

        source=source[:-1] 

    domainName=urlparse(source)[1].split('.')[-2] 

    if domainName in['com','edu','net','org','gov','info','cn']: 

        domainName=urlparse(source)[1].split('.')[-3] 

    socket.setdefaulttimeout(timeout) 

    log=logging.getLogger() 

    handler=logging.FileHandler(logfile) 

    log.addHandler(handler) 

    log.setLevel(LEVELS[logType]) 

  

    startTime=datetime.now() 

    log.info('Started at %s'%startTime) 

    subURLS={} 

    threads=[] 

    for i in range(level+1): 

        URLS[i]=[] 

    #初始化-链接数据库 

    db=saveData() 

    #得到首页内的url 

    URLS[0],html,pureData=getURL(source) 

    if not URLS[0]: 

        log.error('cannot open %s'%source) 

        print 'cannot open '+source 

        sys.exit(1) 

    db.save(source,html,pureData) 

    for le in range(level): 

        #根据线程数将当前的URLS大列表切割成小的列表 

        nowL='-------------level %d------------'%(le+1) 

        print nowL 

        log.info(nowL) 

        preNums=len(URLS[le])/threadNums 

        for i in range(threadNums): 

            temp=URLS[le][:preNums] 

            if i==threadNums-1: 

                subURLS[i]=URLS[le] 

            else: 

                subURLS[i]=temp 

            URLS[le]=URLS[le][preNums:] 

        #将线程加入线程池，并启动。首先清空线程池 

        threads=threads[0:0] 

        for i in range(threadNums): 

            t=newThread(le+1,subURLS[i],db) 

            t.setDaemon(True) 

            threads.append(t) 

        for i in threads: 

            i.start() 

        #等待所有线程结束 

        for i in threads: 

            i.join() 

        nowLevel=le+1 

        #将列表中相同的url去除 

        URLS[nowLevel]=list(set(URLS[nowLevel])) 

        for i in range(nowLevel): 

            for url in URLS[i]: 

                if url in URLS[nowLevel]: 

                    URLS[nowLevel].remove(url) 

        #写入数据库 

    #    db.commit() 

    db.close() 

    endTime=datetime.now() 

    log.info('Ended at %s'%endTime) 

    log.info('Takes %s'%(endTime-startTime)) 
