# HBase
 
 
[简单教程]( http://www.yiibai.com/hbase/)
 
HBase是建立在Hadoop文件系统之上的分布式面向列的数据库。它是一个开源项目，是横向扩展的。
HBase是一个数据模型，类似于谷歌的大表设计，可以提供快速随机访问海量结构化数据。它利用了Hadoop的文件系统（HDFS）提供的容错能力。
它是Hadoop的生态系统，提供对数据的随机实时读/写访问，是Hadoop文件系统的一部分。
人们可以直接或通过HBase的存储HDFS数据。使用HBase在HDFS读取消费/随机访问数据。 HBase在Hadoop的文件系统之上，并提供了读写访问。
 
|HDFS|HBase|
|----|-----|
|HDFS是适于存储大容量文件的分布式文件系统。| HBase是建立在HDFS之上的数据库。 |
|HDFS不支持快速单独记录查找。| HBase提供在较大的表快速查找 |
|它提供了高延迟批量处理;没有批处理概念。 |它提供了数十亿条记录低延迟访问单个行记录（随机存取）。|
|它提供的数据只能顺序访问。 |HBase内部使用哈希表和提供随机接入，并且其存储索引，可将在HDFS文件中的数据进行快速查找。 |
 
* 表是行的集合。
* 行是列族的集合。
* 列族是列的集合。
* 列是键值对的集合。
 
### 命令
命令返回包括在系统上运行的服务器的细节和系统的状态。
```
hbase(main):009:0> status
```
`version`返回系统使用的版本
`table_help`此命令将引导如何使用表引用的命令。下面给出的是使用这个命令的语法。
`whoami`该命令返回HBase用户详细信息。如果执行这个命令，返回当前HBase用户
 
### 建表
```
create ‘<table name>’,’<column family>’
```
使用list命令可以看到表是否创建了。 
使用java api建表: 
```java
import java.io.IOException;
 
 
import org.apache.hadoop.hbase.HBaseConfiguration;
import org.apache.hadoop.hbase.HColumnDescriptor;
import org.apache.hadoop.hbase.HTableDescriptor;
import org.apache.hadoop.hbase.client.HBaseAdmin;
import org.apache.hadoop.hbase.TableName;
 
import org.apache.hadoop.conf.Configuration;
 
public class CreateTable {
 
   public static void main(String[] args) throws IOException {
 
   // Instantiating configuration class
   Configuration con = HBaseConfiguration.create();
 
   // Instantiating HbaseAdmin class
   HBaseAdmin admin = new HBaseAdmin(con);
 
   // Instantiating table descriptor class
   HTableDescriptor tableDescriptor = new
   TableDescriptor(TableName.valueOf("emp"));
 
   // Adding column families to table descriptor
   tableDescriptor.addFamily(new HColumnDescriptor("personal"));
   tableDescriptor.addFamily(new HColumnDescriptor("professional"));
 
 
   // Execute the table through admin
   admin.createTable(tableDescriptor);
   System.out.println(" Table created ");
   }
  }
```
 
### 列出表
使用`list`命令，会给出所有表。 
使用java api: 
```java
import java.io.IOException;
 
import org.apache.hadoop.conf.Configuration;
 
import org.apache.hadoop.hbase.HBaseConfiguration;
import org.apache.hadoop.hbase.HTableDescriptor;
import org.apache.hadoop.hbase.MasterNotRunningException;
import org.apache.hadoop.hbase.client.HBaseAdmin;
 
 
public class ListTables {
 
   public static void main(String args[])throws MasterNotRunningException, IOException{
 
   // Instantiating a configuration class
   Configuration conf = HBaseConfiguration.create();
 
   // Instantiating HBaseAdmin class
   HBaseAdmin admin = new HBaseAdmin(conf);
 
   // Getting all the list of tables using HBaseAdmin object
   HTableDescriptor[] tableDescriptor =admin.listTables();
 
   // printing all the table names.
   for (int i=0; i<tableDescriptor.length;i++ ){
      System.out.println(tableDescriptor[i].getNameAsString());
   }
 
   }
}
```
 
### 禁用表
使用`disable ‘emp’`命令禁用表。 
`is_disabled`查看表是否被禁用。 
`disable_all 'r.*'`命令用于禁用所有匹配给定正则表达式的表。 
使用java api: 
```java
import java.io.IOException;
 
import org.apache.hadoop.conf.Configuration;
 
import org.apache.hadoop.hbase.HBaseConfiguration;
import org.apache.hadoop.hbase.MasterNotRunningException;
import org.apache.hadoop.hbase.client.HBaseAdmin;
 
public class DisableTable{
 
   public static void main(String args[]) throws MasterNotRunningException, IOException{
 
   // Instantiating configuration class
   Configuration conf = HBaseConfiguration.create();
 
   // Instantiating HBaseAdmin class
   HBaseAdmin admin = new HBaseAdmin(conf);
 
   // Verifying weather the table is disabled
   Boolean bool = admin.isTableDisabled("emp");
   System.out.println(bool);
 
   // Disabling the table using HBaseAdmin object
   if(!bool){
      admin.disableTable("emp");
      System.out.println("Table disabled");
   }
 
   }
}
```
 
### 启用表
`enable ‘emp’`来启用表。 
`scan 'emp'`启用表后，进行扫描，能看到的模式，则说明启用成功。 
`is_enabled 'table name'`查看表是否本启用。 
使用java api: 
```java
import java.io.IOException;
 
import org.apache.hadoop.conf.Configuration;
 
import org.apache.hadoop.hbase.HBaseConfiguration;
import org.apache.hadoop.hbase.MasterNotRunningException;
import org.apache.hadoop.hbase.client.HBaseAdmin;
 
public class EnableTable{
 
   public static void main(String args[]) throws MasterNotRunningException, IOException{
 
   // Instantiating configuration class
   Configuration conf = HBaseConfiguration.create();
 
   // Instantiating HBaseAdmin class
   HBaseAdmin admin = new HBaseAdmin(conf);
 
   // Verifying weather the table is disabled
   Boolean bool = admin.isTableEnabled("emp");
   System.out.println(bool);
 
   // Disabling the table using HBaseAdmin object
   if(!bool){
      admin.enableTable("emp");
      System.out.println("Table Enabled");
   }
 
   }
}
```
 
### 表描述和修改
`describe 'table name'`返回表的说明。 
`alter 't1', NAME => 'f1', VERSIONS => 5`来改变列家族单元的最大数目 
`alter 't1', READONLY(option)`设置表为只读 
`alter 't1', METHOD => 'table_att_unset', NAME => 'MAX_FILESIZE'`删除表范围运算 
`alter ‘ table name ’, ‘delete’ => ‘ column family ’`删除列族
添加列族: 
```java
// Instantiating configuration class.
Configuration conf = HBaseConfiguration.create();
 
// Instantiating HBaseAdmin class.
HBaseAdmin admin = new HBaseAdmin(conf);
 
// Instantiating columnDescriptor class
HColumnDescriptor columnDescriptor = new HColumnDescriptor("contactDetails");
 
// Adding column family
admin.addColumn("employee", columnDescriptor);
System.out.println("coloumn added");
```
删除列族: 
```java
// Instantiating configuration class.
Configuration conf = HBaseConfiguration.create();
 
// Instantiating HBaseAdmin class.
HBaseAdmin admin = new HBaseAdmin(conf);
 
// Deleting a column family
admin.deleteColumn("employee","contactDetails");
System.out.println("coloumn deleted");
```
 
### Exists
可以使用`exists`命令验证表的存在。
```java
// Instantiating configuration class
Configuration conf = HBaseConfiguration.create();
 
// Instantiating HBaseAdmin class
HBaseAdmin admin = new HBaseAdmin(conf);
 
// Verifying the existance of the table
boolean bool = admin.tableExists("emp");
System.out.println( bool);
```
 
### 删除表
用`drop`命令可以删除表。在删除一个表之前必须先将其禁用。 
`drop_all ‘t.*’ `来删除匹配正则表达式的表。 
```java
// Instantiating configuration class
Configuration conf = HBaseConfiguration.create();
 
// Instantiating HBaseAdmin class
HBaseAdmin admin = new HBaseAdmin(conf);
 
// disabling table named emp
admin.disableTable("emp12");
 
// Deleting emp
admin.deleteTable("emp12");
System.out.println("Table deleted");
```
 
### HBASE关闭 
可以通过键入`exit`命令退出shell。 
要停止HBase，浏览进入到HBase主文件夹，然后键入以下命令。 
```
./bin/stop-hbase.sh
```
使用java api停止hbase: 
```java
// Instantiating configuration class
Configuration conf = HBaseConfiguration.create();
 
// Instantiating HBaseAdmin class
HBaseAdmin admin = new HBaseAdmin(conf);
 
// Shutting down HBase
System.out.println("Shutting down hbase");
admin.shutdown();
```
 
### 客户端api
#### HBaseConfiguration类
添加 HBase 的配置到配置文件。这个类属于org.apache.hadoop.hbase包。 
`static org.apache.hadoop.conf.Configuration create()`此方法创建使用HBase的资源配置 
#### HTable类
HTable表示HBase表中HBase的内部类。它用于实现单个HBase表进行通信。这个类属于org.apache.hadoop.hbase.client类。
构造函数: 
HTable() 
HTable(TableName tableName, ClusterConnection connection, ExecutorService pool)使用此构造方法，可以创建一个对象来访问HBase表。 
方法及说明: 
`void close()` 释放HTable的所有资源 
`void delete(Delete delete)` 删除指定的单元格/行
`boolean exists(Get get)` 使用这个方法，可以测试列的存在，在表中，由Get指定获取。 
`Result get(Get get)` 检索来自一个给定的行某些单元格。 
`org.apache.hadoop.conf.Configuration getConfiguration()` 返回此实例的配置对象。
`TableName getName()` 返回此表的表名称实例。 
`HTableDescriptor getTableDescriptor()`  返回此表的表描述符。 
`byte[] getTableName()`  返回此表的名称。 
`void put(Put put)` 使用此方法，可以将数据插入到表中。 
#### Put类
此类用于为单个行执行PUT操作。它属于org.apache.hadoop.hbase.client包。 
构造函数: 
`Put(byte[] row)` 使用此构造方法，可以创建一个将操作指定行。 
`Put(byte[] rowArray, int rowOffset, int rowLength)` 使用此构造方法，可以使传入的行键的副本，以保持到本地。 
`Put(byte[] rowArray, int rowOffset, int rowLength, long ts)` 使用此构造方法，可以使传入的行键的副本，以保持到本地。 
`Put(byte[] row, long ts)`  使用此构造方法，我们可以创建一个Put操作指定行，用一个给定的时间戳。 
方法: 
`Put add(byte[] family, byte[] qualifier, byte[] value)`  添加指定的列和值到 Put 操作。 
`Put add(byte[] family, byte[] qualifier, long ts, byte[] value)` 添加指定的列和值，使用指定的时间戳作为其版本到Put操作。 
`Put add(byte[] family, ByteBuffer qualifier, long ts, ByteBuffer value)` 添加指定的列和值，使用指定的时间戳作为其版本到Put操作。 
`Put add(byte[] family, ByteBuffer qualifier, long ts, ByteBuffer value)` 添加指定的列和值，使用指定的时间戳作为其版本到Put操作。 
#### Get类
此类用于对单行执行get操作。这个类属于org.apache.hadoop.hbase.client包。 
构造函数: 
`Get(byte[] row)` 使用此构造方法，可以为指定行创建一个Get操作。 
`Get(Get get)` 
方法: 
`Get addColumn(byte[] family, byte[] qualifier)` 检索来自特定列家族使用指定限定符 
`Get addFamily(byte[] family)` 检索从指定系列中的所有列。 
#### Delete类
这个类用于对单行执行删除操作。要删除整行，实例化一个Delete对象用于删除行。这个类属于org.apache.hadoop.hbase.client包。 
构造函数: 
`Delete(byte[] row)` 创建一个指定行的Delete操作。 
`Delete(byte[] rowArray, int rowOffset, int rowLength)` 创建一个指定行和时间戳的Delete操作。 
`Delete(byte[] rowArray, int rowOffset, int rowLength, long ts)` 创建一个指定行和时间戳的Delete操作。 
`Delete(byte[] row, long timestamp)` 创建一个指定行和时间戳的Delete操作。 
方法: 
`Delete addColumn(byte[] family, byte[] qualifier)` 删除指定列的最新版本。 
`Delete addColumns(byte[] family, byte[] qualifier, long timestamp)` 删除所有版本具有时间戳小于或等于指定的时间戳的指定列。 
`Delete addFamily(byte[] family)` 删除指定的所有列族的所有版本。 
`Delete addFamily(byte[] family, long timestamp)` 删除指定列具有时间戳小于或等于指定的时间戳的列族。 
#### Result类
这个类是用来获取Get或扫描查询的单行结果。 
构造函数: 
`Result()` 使用此构造方法，可以创建无Key Value的有效负载空的结果;如果调用Cells()返回null。 
方法: 
`byte[] getValue(byte[] family, byte[] qualifier)` 此方法用于获取指定列的最新版本 
`byte[] getRow()` 此方法用于检索对应于从结果中创建行的行键。 
 
### 创建数据
使用`put`命令或者:
`add()` - Put类的方法
`put()` - HTable 类的方法.
```
put ’<table name>’,’row1’,’<colfamily:colname>’,’<value>’
put 'emp','1','personal data:name','raju'
```
```java
public static void main(String[] args) throws IOException {
 
      // Instantiating Configuration class
      Configuration config = HBaseConfiguration.create();
 
      // Instantiating HTable class
      HTable hTable = new HTable(config, "emp");
 
      // Instantiating Put class
      // accepts a row name.
      Put p = new Put(Bytes.toBytes("row1"));
 
      // adding values using add() method
      // accepts column family name, qualifier/row name ,value
      p.add(Bytes.toBytes("personal"),
      Bytes.toBytes("name"),Bytes.toBytes("raju"));
 
      p.add(Bytes.toBytes("personal"),
      Bytes.toBytes("city"),Bytes.toBytes("hyderabad"));
 
      p.add(Bytes.toBytes("professional"),Bytes.toBytes("designation"),
      Bytes.toBytes("manager"));
 
      p.add(Bytes.toBytes("professional"),Bytes.toBytes("salary"),
      Bytes.toBytes("50000"));
 
      // Saving the put Instance to the HTable.
      hTable.put(p);
      System.out.println("data inserted");
 
      // closing HTable
      hTable.close();
   }
 
```
### 更新数据
```
put ‘table name’,’row ’,'Column family:column name',’new value’
```
```java
public static void main(String[] args) throws IOException {
 
      // Instantiating Configuration class
      Configuration config = HBaseConfiguration.create();
 
      // Instantiating HTable class
      HTable hTable = new HTable(config, "emp");
 
      // Instantiating Put class
      //accepts a row name
      Put p = new Put(Bytes.toBytes("row1"));
 
      // Updating a cell value
      p.add(Bytes.toBytes("personal"),
      Bytes.toBytes("city"),Bytes.toBytes("Delih"));
 
      // Saving the put Instance to the HTable.
      hTable.put(p);
      System.out.println("data Updated");
 
      // closing HTable
      hTable.close();
   }
```
### 读取数据
```
get ’<table name>’,’row1’
```
```java
public static void main(String[] args) throws IOException, Exception{
 
      // Instantiating Configuration class
      Configuration config = HBaseConfiguration.create();
 
      // Instantiating HTable class
      HTable table = new HTable(config, "emp");
 
      // Instantiating Get class
      Get g = new Get(Bytes.toBytes("row1"));
 
      // Reading the data
      Result result = table.get(g);
 
      // Reading values from Result class object
      byte [] value = result.getValue(Bytes.toBytes("personal"),Bytes.toBytes("name"));
 
      byte [] value1 = result.getValue(Bytes.toBytes("personal"),Bytes.toBytes("city"));
 
      // Printing the values
      String name = Bytes.toString(value);
      String city = Bytes.toString(value1);
 
      System.out.println("name: " + name + " city: " + city);
   }
 
```
 
### 删除数据
```
delete ‘<table name>’, ‘<row>’, ‘<column name >’, ‘<time stamp>’
```
```java
public static void main(String[] args) throws IOException {
 
      // Instantiating Configuration class
      Configuration conf = HBaseConfiguration.create();
 
      // Instantiating HTable class
      HTable table = new HTable(conf, "employee");
 
      // Instantiating Delete class
      Delete delete = new Delete(Bytes.toBytes("row1"));
      delete.deleteColumn(Bytes.toBytes("personal"), Bytes.toBytes("name"));
      delete.deleteFamily(Bytes.toBytes("professional"));
 
      // deleting the data
      table.delete(delete);
 
      // closing the HTable object
      table.close();
      System.out.println("data deleted.....");
   }
 
```
 
### 扫描
```
scan ‘<table name>’
```
```java
public static void main(String args[]) throws IOException{
 
  // Instantiating Configuration class
  Configuration config = HBaseConfiguration.create();
 
  // Instantiating HTable class
  HTable table = new HTable(config, "emp");
 
  // Instantiating the Scan class
  Scan scan = new Scan();
 
  // Scanning the required columns
  scan.addColumn(Bytes.toBytes("personal"), Bytes.toBytes("name"));
  scan.addColumn(Bytes.toBytes("personal"), Bytes.toBytes("city"));
 
  // Getting the scan result
  ResultScanner scanner = table.getScanner(scan);
 
  // Reading values from scan result
  for (Result result = scanner.next(); result != null; result = Scanner.next())
 
  System.out.println("Found row : " + result);
  //closing the scanner
  scanner.close();
}
```
 
### 计数和截断
可以使用count命令计算表的行数量: 
```
count ‘<table name>’
```
`truncate`命令将禁止删除并重新创建一个表 
```
truncate 'table name'
```
 
### 安全
#### grant
grant命令授予特定的权限，如读，写，执行和管理表给定一个特定的用户。 
```
grant <user> <permissions> [<table> [<column family> [<column; qualifier>]]
```
我们可以从RWXCA组，其中给予零个或多个特权给用户
* R - 代表读取权限
* W - 代表写权限
* X - 代表执行权限
* C - 代表创建权限
* A - 代表管理权限
#### revok
revoke命令用于撤销用户访问表的权限
```
revoke <user>
```
#### user_permission
此命令用于列出特定表的所有权限。
```
hbase>user_permission ‘tablename’
```