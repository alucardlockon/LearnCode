# WebServer
### Jetty
[jetty安装及配置](http://blog.csdn.net/zhuying_linux/article/details/6597510) 
基本步骤:   
创建server   
配置connector   
配置handler   
配置servlet   
启动server   
 
### Tomcat
[tomcat部署](http://www.cnblogs.com/xing901022/p/4463896.html) 
部署时，涉及到一个变量appBase。这个变量标识了一个目录，该目录存放着部署的web应用。
一般默认情况下，appBase为CATALINA_HOME/webapps，配置信息位于server.xml中。
  
### JBoss
[JBoss](http://blog.csdn.net/liuzheng2684/article/details/7191709)  
部署目录:jboss/server 其中有三个目录：all，default，minimal，代表了jboss提供的三种部署方式，all表示jboss提供的服务全部打开，default表示默认的 jboss服务，minimal表示只打开最基本的。这里面可以增加自己的部署，我们只使用default。  

进入default目录后，有以下几个目录：  
conf：一些配置文件  
data：保存的数据，比如有状态会话bean  
deploy：部署目录，所有的应用都部署在这里面，相当于apache的htdocs  
lib：部署的应用程序需要使用到的其它库(jar)  
log：jboss的日志  
tmp：部署应用是产生的临时文件  
work:工作目录，所部署的应用（一些jar压缩文件）会被解压在这里  

### WebSphere
[WebSphere 的应用部署](http://blog.csdn.net/hotdust/article/details/8193734)  
./startServer.sh server1 可以开启服务   
./stopServer.sh server1 可以停止服务   
备份以前的stat.war:  
`cd opt/IBM/WebSphere/AppServer/profiles/default/installedApps/was…/`
将以前的东西备份一下。tar -zcvf myfiles.tar.gz ./stat_war.ear (将./stat_war.ear打包到当前目录下)
相应的解包操作：tar  zxvf ./myfiles.tar.gz  /home(将./stat_war.ear打包到home目录下)  
部署:进入控制台页面配置。  
 
### Apache
[Apache部署](http://www.linuxidc.com/Linux/2013-11/92304.htm)  
启动服务:`apachectl start`  
查看是否开启:`netstat -lnt|grep 80 `  
 
### Nginx
[Nginx](http://www.open-open.com/lib/view/open1419826381531.html)  



 