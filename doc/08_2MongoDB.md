# MongoDB
[文档](http://www.runoob.com/mongodb/mongodb-intro.html)  
MongoDB 是一个基于分布式文件存储的数据库。由 C++ 语言编写。旨在为 WEB 应用提供可扩展的高性能数据存储解决方案。
MongoDB 是一个介于关系数据库和非关系数据库之间的产品，是非关系数据库当中功能最丰富，最像关系数据库的。  

### 基本概念
#### 和传统数据库之间的对应概念
|SQL术语|MongoDB术语|解释/说明|
|---|---|---|
|database|database|数据库|
|table|collection|数据库表/集合|
|row|document|数据记录行/文档|
|column|field|数据字段/域|
|index|index|索引|
|table joins||表连接,MongoDB不支持|
|primary key|primary key|主键,MongoDB自动将_id字段设置为主键|  

#### 数据库
默认数据库为db。  
`show dbs`显示所有数据库  
`use test`切换到test数据库  
`db`:显示当前的数据库  

#### 文档
就是一个BSON,键值对
```
{"site":"www.runoob.com", "name":"菜鸟教程"}
```
### 数据类型
String 字符串  
Integer 整数  
Boolean 布尔  
Double 浮点
Min/Max keys 将一个值与 BSON（二进制的 JSON）元素的最低值和最高值相对比。  
Arrays 用于将数组或列表或多个值存储为一个键。 
Timestamp 时间戳
Object 内嵌文档  
Null 空值  
Symbol 符号。该数据类型基本上等同于字符串类型，但不同的是，它一般用于采用特殊符号类型的语言。  
Date 日期  
Object ID 对象 ID。用于创建文档的 ID。   
Binary Data 二进制数据  
Code 代码类型。用于在文档中存储 JavaScript 代码。  
Regular expression 正则表达式类型。用于存储正则表达式。  

### 连接
`username:password@hostname/dbname' 用此格式连接  
连接到指定数据库:  
```
mongodb://admin:123456@localhost/
```
### 创建删除数据库
`USE database`如果数据库不存在，则创建数据库，否则切换到指定数据库。  
`db.dropDatabase()`:删除数据库  
`db.collection.drop()`:删除集合  

### 文档操作
`db.COLLECTION_NAME.insert(document)`插入文档  
`db.col.find()`查看已插入文档  
插入文档你也可以使用 db.col.save(document) 命令。如果不指定 _id 字段 save() 方法类似于 insert() 方法。如果指定 _id 字段，则会更新该 _id 的数据。  


