# Node.js
[教程1](http://www.runoob.com/nodejs/nodejs-tutorial.html)
[API](http://nodeapi.ucdok.com/#/api/)
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
