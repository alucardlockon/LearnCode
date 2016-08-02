# Node.js
[教程1](http://www.runoob.com/nodejs/nodejs-tutorial.html)
[教程2-7天学会node.js](http://nqdeng.github.io/7-days-nodejs/#1.1)
[API](http://nodeapi.ucdok.com/#/api/)
[Express](http://www.expressjs.com.cn/)
### hello,world
#### 引入 required 模块并创建服务器
`var http = require("http");`
``` javascript
var http = require('http');
http.createServer(function (request, response) {
    // 发送 HTTP 头部
    // HTTP 状态值: 200 : OK
    // 内容类型: text/plain
    response.writeHead(200, {'Content-Type': 'text/plain'});
    // 发送响应数据 "Hello World"
    response.end('Hello World\n');
}).listen(8888);
// 终端打印如下信息
console.log('Server running at http://127.0.0.1:8888/');
```
运行server端:`node server.js`
 
### npm升级/安装模块
`npm install npm -g`
`npm install express` 安装express模块
`var express = require('express');` 引用模块
-g参数:全局安装，不带为本地安装
`$ npm ls -g`查看全局安装的模块
`npm uninstall/update/search express` 卸载/更新/搜索模块
 
### npm常用命令
使用npm help <command>可查看某条命令的详细帮助，例如npm help install。
在package.json所在目录下使用npm install . -g可先在本地安装当前命令行程序，可用于发布前的本地测试。
使用npm cache clear可以清空NPM本地缓存，用于对付使用相同版本号发布新版本代码的人。
###  package.json
package.json 位于模块的目录下，用于定义包的属性。
#### Package.json 属性说明
name - 包名。
version - 包的版本号。
description - 包的描述。
homepage - 包的官网 url 。
author - 包的作者姓名。
contributors - 包的其他贡献者姓名。
dependencies - 依赖包列表。如果依赖包没有安装，npm 会自动将依赖包安装在 node_module 目录下。
repository - 包代码存放的地方的类型，可以是 git 或 svn，git 可在 Github 上。
main - main 字段是一个模块ID，它是一个指向你程序的主要项目。就是说，如果你包的名字叫 express，然后用户安装它，然后require("express")。
keywords - 关键字
 
### 非阻塞代码
``` javascript
var fs = require("fs");
fs.readFile('input.txt', function (err, data) {
    if (err) return console.error(err);
    console.log(data.toString());
});
console.log("程序执行结束!");
```
### 事件驱动程序
``` javascript
// 引入 events 模块
var events = require('events');
// 创建 eventEmitter 对象
var eventEmitter = new events.EventEmitter();
 
// 创建事件处理程序
var connectHandler = function connected() {
   console.log('连接成功。');
   // 触发 data_received 事件
   eventEmitter.emit('data_received');
}
// 绑定 connection 事件处理程序
eventEmitter.on('connection', connectHandler);
// 使用匿名函数绑定 data_received 事件
eventEmitter.on('data_received', function(){
   console.log('数据接收成功。');
});
// 触发 connection 事件
eventEmitter.emit('connection');
 
console.log("程序执行完毕。");
```
#### 参数传递
``` javascript
//event.js 文件
var events = require('events');
var emitter = new events.EventEmitter();
emitter.on('someEvent', function(arg1, arg2) {
    console.log('listener1', arg1, arg2);
});
emitter.on('someEvent', function(arg1, arg2) {
    console.log('listener2', arg1, arg2);
});
emitter.emit('someEvent', 'arg1 参数', 'arg2 参数');
```
#### EventEmitter方法
addListener(event, listener) 为指定事件添加一个监听器到监听器数组的尾部。
on(event, listener) 为指定事件注册一个监听器，接受一个字符串 event 和一个回调函数。
once(event, listener) 为指定事件注册一个单次监听器，即 监听器最多只会触发一次，触发后立刻解除该监听器。
removeListener(event, listener) 移除指定事件的某个监听器，监听器 必须是该事件已经注册过的监听器。
removeAllListeners([event]) 移除所有事件的所有监听器， 如果指定事件，则移除指定事件的所有监听器。
setMaxListeners(n)  默认情况下， EventEmitters 如果你添加的监听器超过 10 个就会输出警告信息。 setMaxListeners 函数用于提高监听器的默认限制的数量。
listeners(event) 返回指定事件的监听器数组。
emit(event, [arg1], [arg2], [...])按参数的顺序执行每个监听器，如果事件有注册监听返回 true，否则返回 false。
> 类方法 listenerCount(emitter, event) 返回指定事件的监听器数量。
 
#### error事件
[链接](http://www.runoob.com/nodejs/nodejs-buffer.html)
EventEmitter 定义了一个特殊的事件 error，它包含了错误的语义，我们在遇到 异常的时候通常会触发 error 事件。
当 error 被触发时，EventEmitter 规定如果没有响 应的监听器，Node.js 会把它当作异常，退出程序并输出错误信息。
我们一般要为会触发 error 事件的对象设置监听器，避免遇到错误后整个程序崩溃。
 
### Buffer类(缓冲区)
`var buf = new Buffer(10);` 
`var buf = new Buffer([10, 20, 30, 40, 50]);` 
`var buf = new Buffer("www.runoob.com", "utf-8"); //utf-8是默认编码格式，可替换成"ascii", "utf8", "utf16le", "ucs2", "base64" 和 "hex"。` 
`buf.write(string[, offset[, length]][, encoding])`写入数据 
`buf.toString([encoding[, start[, end]]])`读取数据 
`buf.toJSON()`将Buffer转为json 
`Buffer.concat(list[, totalLength])` 缓冲区合并 
`buf.compare(otherBuffer);` 缓冲区比较 
`buf.copy(targetBuffer[, targetStart[, sourceStart[, sourceEnd]]])` 拷贝缓冲区 
`buf.slice([start[, end]])` 裁剪缓冲区 
`buf.length;` 缓冲区长度 
 
### Stream(流)
Stream 是一个抽象接口，Node 中有很多对象实现了这个接口。例如，对http 服务器发起请求的request 对象就是一个 Stream，还有stdout（标准输出）。
Node.js，Stream 有四种流类型：
- Readable - 可读操作。
- Writable - 可写操作。
- Duplex - 可读可写操作.
- Transform - 操作被写入数据，然后读出结果。
 
 
所有的 Stream 对象都是 EventEmitter 的实例。常用的事件有：
- data - 当有数据可读时触发。
- end - 没有更多的数据可读时触发。
- error - 在接收和写入过程中发生错误时触发。
- finish - 所有数据已被写入到底层系统时触发。
 
#### 读取流
``` javascript
var fs = require("fs");
var data = '';
// 创建可读流
var readerStream = fs.createReadStream('input.txt');
// 设置编码为 utf8。
readerStream.setEncoding('UTF8');
// 处理流事件 --> data, end, and error
readerStream.on('data', function(chunk) {
   data += chunk;
});
readerStream.on('end',function(){
   console.log(data);
});
readerStream.on('error', function(err){
   console.log(err.stack);
});
console.log("程序执行完毕");
```
#### 写入流
``` javascript
var fs = require("fs");
var data = '菜鸟教程官网地址：www.runoob.com';
// 创建一个可以写入的流，写入到文件 output.txt 中
var writerStream = fs.createWriteStream('output.txt');
// 使用 utf8 编码写入数据
writerStream.write(data,'UTF8');
// 标记文件末尾
writerStream.end();
// 处理流事件 --> data, end, and error
writerStream.on('finish', function() {
    console.log("写入完成。");
});
writerStream.on('error', function(err){
   console.log(err.stack);
});
console.log("程序执行完毕");
```
#### 管道流
``` javascript
var fs = require("fs");
// 创建一个可读流
var readerStream = fs.createReadStream('input.txt');
// 创建一个可写流
var writerStream = fs.createWriteStream('output.txt');
// 管道读写操作
// 读取 input.txt 文件内容，并将内容写入到 output.txt 文件中
readerStream.pipe(writerStream);
console.log("程序执行完毕");
```
#### 链式流
``` javascript
var fs = require("fs");
var zlib = require('zlib');
// 压缩 input.txt 文件为 input.txt.gz
fs.createReadStream('input.txt')
  .pipe(zlib.createGzip())
  .pipe(fs.createWriteStream('input.txt.gz'));
console.log("文件压缩完成。");
```
### 模块
为了让Node.js的文件可以相互调用，Node.js提供了一个简单的模块系统。
模块是Node.js 应用程序的基本组成部分，文件和模块是一一对应的。换言之，一个 Node.js 文件就是一个模块，这个文件可能是JavaScript 代码、JSON 或者编译过的C/C++ 扩展。
编写稍大一点的程序时一般都会将代码模块化。在NodeJS中，一般将代码合理拆分到不同的JS文件中，每一个文件就是一个模块，而文件路径就是模块名。
在编写每个模块时，都有`require`、`exports`、`module`三个预先定义好的变量可供使用。
#### require
require函数用于在当前模块中加载和使用别的模块，传入一个模块名，返回一个模块导出对象。模块名可使用相对路径（以./开头），或者是绝对路径（以/或C:之类的盘符开头）。另外，模块名中的.js扩展名可以省略。
#### exports
exports对象是当前模块的导出对象，用于导出模块公有方法和属性。别的模块通过require函数使用当前模块时得到的就是当前模块的exports对象。以下例子中导出了一个公有方法。
#### module
通过module对象可以访问到当前模块的一些相关信息，但最多的用途是替换当前模块的导出对象。例如模块导出对象默认是一个普通对象，如果想改成一个函数的话，可以使用以下方式。
 
### Linux 编译安装
编译安装
Linux系统下没有现成的安装程序可用，虽然一些发行版可以使用apt-get之类的方式安装，但不一定能安装到最新版。因此Linux系统下一般使用以下方式编译方式安装NodeJS。
1. 确保系统下g++版本在4.6以上，python版本在2.6以上。
2. 从nodejs.org下载tar.gz后缀的NodeJS最新版源代码包并解压到某个位置。
3. 进入解压到的目录，使用以下命令编译和安装。
```
$ ./configure
$ make
$ sudo make install
```
 
 
### 文件拷贝
小文件拷贝: 
 
``` javascript
var fs = require('fs');
function copy(src, dst) {
    fs.writeFileSync(dst, fs.readFileSync(src));
}
function main(argv) {
    copy(argv[0], argv[1]);
}
main(process.argv.slice(2));
```
process是一个全局变量，可通过process.argv获得命令行参数。由于argv[0]固定等于NodeJS执行程序的绝对路径，argv[1]固定等于主模块的绝对路径，因此第一个命令行参数从argv[2]这个位置开始。 
 
大文件拷贝:
 
``` javascript
var fs = require('fs');
function copy(src, dst) {
    fs.createReadStream(src).pipe(fs.createWriteStream(dst));
}
function main(argv) {
    copy(argv[0], argv[1]);
}
main(process.argv.slice(2));
```
### 工程目录
了解了以上知识后，现在我们可以来完整地规划一个工程目录了。以编写一个命令行程序为例，一般我们会同时提供命令行模式和API模式两种使用方式，并且我们会借助三方包来编写代码。除了代码外，一个完整的程序也应该有自己的文档和测试用例。因此，一个标准的工程目录都看起来像下边这样。 
```
- /home/user/workspace/node-echo/   # 工程目录
    - bin/                          # 存放命令行相关代码
        node-echo
    + doc/                          # 存放文档
    - lib/                          # 存放API相关代码
        echo.js
    - node_modules/                 # 存放三方包
        + argv/
    + tests/                        # 存放测试用例
    package.json                    # 元数据文件
    README.md                       # 说明文件
```
 
### HTTP Server
#### 创建Server
``` javascript
var http=require('http');
http.createServer(function(req,res){
    res.writeHead(200,{'Content-Type':'text/html'});
    res.write('<h1>Node.js</h1>');
    res.end('<p>Hello World</p>');
}).listen(3000);
```
#### 获取GET请求内容
``` javascript
var http=require('http');
var url=require('url');
var util=require('util');
 
http.createServer(function(){
  res.writeHead(200,{'Content-Type':'text/html'});
  res.end(util.inspect(url.parse(req.url,true))); //通过url.parse,原始的path被解析为一个对象，其中的query就是GET请求的内容,pathname则是路径
}).listen(3000);
```
#### 获取POST请求内容(仅测试，有效率和安全问题)
``` javascript
var http=require('http');
var querystring=require('querystring');
var util=require('util');
 
http.createServer(function(){
  var post='';
 
  req.on('data',function(chunk)){
    post+=chunk;
  });
 
  req.on('end',function(){
    post=querystring.parse(post);
    res.end(util.inspect(post));
  });
 
}).listen(3000);
```
### Node.js Web开发实战
#### MVC
* 模型是对象及其数据结构的实现，通常包含数据库操作
* 视图表示用户界面，在网站中通常就是HTML的组织结构
* 控制器用于处理用户请求和数据流,复杂模型，将输出传递给视图。
 
#### Express框架
示例  
``` javascript
var express =require('express');
 
var app=express.createServer();
app.use(express.bodyParser());
app.all('/',function(rq,res){
  res.send(req.body.title+req.body.text);
});
app.listen(3000);
```
通过应用生成器工具 express 可以快速创建一个应用的骨架。
`$ npm install express-generator -g` 
#### 路由规划
```
/ 首页 app.get('/',routes.index);
/u/[user] 用户主页 app.get('/u/:user',routes.user);
/post 发表信息 app.post('/post',routes.post);
/reg 用户注册 app.get('/reg',routes.reg); app.post('/reg',routes.doreg);
/login 用户登录
/logout 用户登出
```
repository:https://github.com/yuanzm/microblog