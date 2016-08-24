# MongoDB
[文档]( http://www.runoob.com/mongodb/mongodb-intro.html)  
MongoDB 是一个基于分布式文件存储的数据库。由 C++ 语言编写。旨在为 WEB 应用提供可扩展的高性能数据存储解决方案。
MongoDB 是一个介于关系数据库和非关系数据库之间的产品，是非关系数据库当中功能最丰富，最像关系数据库的。 
 
 
### 基本概念
#### 和传统数据库之间的对应概念
|SQL术语|MongoDB术语|解释/说明|
|---|---|---|
|database|database|数据库|
|table|collection|数据库表/集合|
|row|document|数据记录行/文档|
|column|field| 数据字段/域|
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
Double  浮点
 
Min/Max keys  将一个值与 BSON（二进制的 JSON）元素的最低值和最高值相对比。 
Arrays  用于将数组或列表或多个值存储为一个键。
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
`username:password@hostname/dbname` 用此格式连接 
 
连接到指定数据库: 
```
mongodb://admin:123456@localhost/
 
```
### 创建删除数据库
`USE database` 如果数据库不存在，则创建数据库，否则切换到指定数据库。 
` db.dropDatabase() `:删除数据库 
` db.collection.drop() `:删除集合 
 
 
### 文档操作
` db.COLLECTION_NAME.insert(document) `插入文档 
` db.col.find() `查看已插入文档 
插入文档你也可以使用 db.col.save(document) 命令。如果不指定 \_id 字段 save() 方法类似于 insert() 方法。如果指定 \_id 字段，则会更新该 \_id 的数据。 
 
update(): 
```
db.collection.update(
   <query>,
   <update>,
   {
     upsert: <boolean>,
     multi: <boolean>,
     writeConcern: <document>
   }
)
 
 
db.col.update({'title':'MongoDB 教程'},{$set:{'title':'MongoDB'}})
 
```
remove():
```
db.collection.remove(
   <query>,
   <justOne>
)
//2.6以后
db.collection.remove(
   <query>,
   {
     justOne: <boolean>,
     writeConcern: <document>
   }
)
```
如果你想删除所有数据，可以使用以下方式（类似常规 SQL 的 truncate 命令）：`db.col.remove({})` 
 
#### 查询文档
`db.COLLECTION_NAME.find()` 
 
`db.col.find().pretty()`易读化方式查询 
除了 find() 方法之外，还有一个 findOne() 方法，它只返回一个文档。 
 
MongoDB 的 find() 方法可以传入多个键(key)，每个键(key)以逗号隔开，及常规 SQL 的 AND 条件。`db.col.find({key1:value1, key2:value2}).pretty()` 
 
MongoDB OR 条件语句使用了关键字 $or,语法格式如下：
 
```
>db.col.find(
   {
      $or: [
         {key1: value1}, {key2:value2}
      ]
   }
).pretty()
```
AND和OR联合使用: 
```
>db.col.find({"likes": {$gt:50}, $or: [{"by": "菜鸟教程"},{"title": "MongoDB 教程"}]}).pretty()
{
        "_id" : ObjectId("56063f17ade2f21f36b03133"),
        "title" : "MongoDB 教程",
        "description" : "MongoDB 是一个 Nosql 数据库",
        "by" : "菜鸟教程",
        "url" : "http://www.runoob.com",
        "tags" : [
                "mongodb",
                "database",
                "NoSQL"
        ],
        "likes" : 100
}
```
### 操作条件符
MongoDB中条件操作符有：
* (>) 大于 - $gt
*   (<) 小于 - $lt
*   (>=) 大于等于 - $gte
*   (<= ) 小于等于 - $lte 
 
 
$type操作符是基于BSON类型来检索集合中匹配的数据类型，并返回结果。 
 
类型  数字  备注   
Double 1     
String 2     
Object 3     
Array 4     
Binary data 5     
Undefined 6 已废弃。   
Object id 7     
Boolean 8     
Date 9     
Null 10     
Regular Expression 11     
JavaScript 13     
Symbol 14     
JavaScript (with scope) 15     
32-bit integer 16     
Timestamp 17     
64-bit integer 18     
Min key 255 Query with -1. 
Max key 127      
示例: 
```
db.col.find({"title" : {$type : 2}})
 
```
### LIMIT
```
>db.COLLECTION_NAME.find().limit(NUMBER)
 
```
我们除了可以使用limit()方法来读取指定数量的数据外，还可以使用skip()方法来跳过指定数量的数据，skip方法同样接受一个数字参数作为跳过的记录条数。 
 
### 排序
```
db.COLLECTION_NAME.find().sort({KEY:1})
 
```
### 索引
MongoDB使用 ensureIndex() 方法来创建索引。
 
```
>db.COLLECTION_NAME.ensureIndex({KEY:1})
 
```
语法中 Key 值为你要创建的索引字段，1为指定按升序创建索引，如果你想按降序来创建索引指定为-1即可。 
 
### 聚合
MongoDB中聚合的方法使用aggregate()。 
 
```
db.COLLECTION_NAME.aggregate(AGGREGATE_OPERATION)
 
```
### 复制
MongoDB复制是将数据同步在多个服务器的过程。 
复制提供了数据的冗余备份，并在多个服务器上存储数据副本，提高了数据的可用性， 并可以保证数据的安全性。 
复制还允许您从硬件故障和服务中断中恢复数据。
### 分片
在Mongodb里面存在另一种集群，就是分片技术,可以满足MongoDB数据量大量增长的需求。 
当MongoDB存储海量的数据时，一台机器可能不足以存储数据，也可能不足以提供可接受的读写吞吐量。这时，我们就可以通过在多台机器上分割数据，使得数据库系统能存储和处理更多的数据。  
### 备份
在Mongodb中我们使用mongodump命令来备份MongoDB数据。该命令可以导出所有数据到指定目录中。 
mongodump命令可以通过参数指定导出的数据量级转存的服务器。 
```
mongodump -h dbhost -d dbname -o dbdirectory
 
```
-h： 
MongDB所在服务器地址，例如：127.0.0.1，当然也可以指定端口号：127.0.0.1:27017 
-d： 
需要备份的数据库实例，例如：test 
-o： 
备份的数据存放位置，例如：c:\data\dump，当然该目录需要提前建立，在备份完成后，系统自动在dump目录下建立一个test目录，这个目录里面存放该数据库实例的备份数据。 
### mongostat 命令
mongostat是mongodb自带的状态检测工具，在命令行下使用。它会间隔固定时间获取mongodb的当前运行状态，并输出。如果你发现数据库突然变慢或者有其他问题的话，你第一手的操作就考虑采用mongostat来查看mongo的状态。 
启动你的Mongod服务，进入到你安装的MongoDB目录下的bin目录， 然后输入mongostat命令，如下所示：  
```
D:\set up\mongodb\bin>mongostat
 
```
### JAVA
环境配置 
在 Java 程序中如果要使用 MongoDB，你需要确保已经安装了 Java 环境及 MongoDB JDBC 驱动。 
本章节实例时候 Mongo 3.x 以上版本。 
你可以参考本站的Java教程来安装Java程序。现在让我们来检测你是否安装了 MongoDB JDBC 驱动。 
首先你必须下载mongo jar包，下载地址：http://mongodb.github.io/mongo-java-driver/, 请确保下载最新版本。 
``` java
import com.mongodb.MongoClient;
import com.mongodb.client.MongoDatabase;
 
public class MongoDBJDBC{
   public static void main( String args[] ){
      try{ 
       // 连接到 mongodb 服务
         MongoClient mongoClient = new MongoClient( "localhost" , 27017 );
 
         // 连接到数据库
         MongoDatabase mongoDatabase = mongoClient.getDatabase("mycol");
       System.out.println("Connect to database successfully");
 
      }catch(Exception e){
        System.err.println( e.getClass().getName() + ": " + e.getMessage() );
     }
   }
}
```
``` java
mongoDatabase.createCollection("test");//创建集合
 
MongoCollection<Document> collection = mongoDatabase.getCollection("test");//获取集合
 
 
 
//插入文档
Document document = new Document("title", "MongoDB").
append("description", "database").
append("likes", 100).
append("by", "Fly");
List<Document> documents = new ArrayList<Document>();
documents.add(document);
collection.insertMany(documents);
 
 
//检索所有文档
/**
* 1. 获取迭代器FindIterable<Document>
* 2. 获取游标MongoCursor<Document>
* 3. 通过游标遍历检索出的文档集合
* */
FindIterable<Document> findIterable = collection.find();
MongoCursor<Document> mongoCursor = findIterable.iterator();
while(mongoCursor.hasNext()){
  System.out.println(mongoCursor.next());
} 
 
//更新文档   将文档中likes=100的文档修改为likes=200  
collection.updateMany(Filters.eq("likes", 100), new Document("$set",new Document("likes",200))); 
 
//删除符合条件的第一个文档 
collection.deleteOne(Filters.eq("likes", 200)); 
//删除所有符合条件的文档 
collection.deleteMany (Filters.eq("likes", 200)); 
 
```
 
 
 
 
 