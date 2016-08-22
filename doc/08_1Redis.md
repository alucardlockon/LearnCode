# Redis

[快速入门](http://www.yiibai.com/redis/redis_quick_guide.html)  
[中文手册](https://wizardforcel.gitbooks.io/redis-doc/content/doc/1.html)  
Redis是一个开源的，先进的 key-value 存储可用于构建高性能，可扩展的 Web 应用程序的解决方案。Redis官方网网站是：http://www.redis.io/  
Redis 有三个主要使其有别于其它很多竞争对手的特点：  
* Redis是完全在内存中保存数据的数据库，使用磁盘只是为了持久性目的； 
* Redis相比许多键值数据存储系统有相对丰富的数据类型； 
* Redis可以将数据复制到任意数量的从服务器中；  

Redis是非常快的，每秒可以执行大约110000设置操作，81000个/每秒的读取操作。  
```
sudo apt-get install redis-server
```
### 数据类型:
#### 字符串
Redis 字符串是一个字节序列。在 Redis 中字符串是二进制安全的，这意味着它们没有任何特殊终端字符来确定长度，所以可以存储任何长度为 512 兆的字符串。   
```
redis 127.0.0.1:6379> SET name "yiibai"
OK
redis 127.0.0.1:6379> GET name
"yiibai"
```
在上面的例子中，SET 和 GET 是 Redis 命令，name 和 "yiibai" 是存储在 Redis 的键和字符串值。 
#### 哈希
Redis哈希是键值对的集合。 Redis哈希是字符串字段和字符串值之间的映射，所以它们用来表示对象。   
```
redis 127.0.0.1:6379> HMSET user:1 username yiibai password yiibai points 200
OK
redis 127.0.0.1:6379> HGETALL user:1
 
1) "username"
2) "yiibai"
3) "password"
4) "yiibai"
5) "points"
6) "200"
```
在上面的例子中，哈希数据类型用于存储包含用户基本信息的用户对象。这里 HSET，HEXTALL 是 Redis 命令同时 user:1 也是一个键。   
#### 列表
Redis 列表是简单的字符串列表，通过插入顺序排序。可以添加一个元素到 Redis 列表的头部或尾部。  
```
redis 127.0.0.1:6379> lpush tutoriallist redis
(integer) 1
redis 127.0.0.1:6379> lpush tutoriallist mongodb
(integer) 2
redis 127.0.0.1:6379> lpush tutoriallist rabitmq
(integer) 3
redis 127.0.0.1:6379> lrange tutoriallist 0 10
 
1) "rabitmq"
2) "mongodb"
3) "redis"
```
列表的最大长度为  232 - 1 个元素（4294967295，每个列表的元素超过四十亿）。   
#### 集合
Redis 集合是字符串的无序集合。在 Redis 可以添加，删除和测试成员存在的时间复杂度为 O（1）。  
```
redis 127.0.0.1:6379> sadd tutoriallist redis
(integer) 1
redis 127.0.0.1:6379> sadd tutoriallist mongodb
(integer) 1
redis 127.0.0.1:6379> sadd tutoriallist rabitmq
(integer) 1
redis 127.0.0.1:6379> sadd tutoriallist rabitmq
(integer) 0
redis 127.0.0.1:6379> smembers tutoriallist
 
1) "rabitmq"
2) "mongodb"
3) "redis"
```
注：在上面的例子中 rabitmq 被添加两次，但由于它是只集合具有唯一特性。集合中的成员最大数量为 232 - 1（4294967295，每个集合有超过四十亿条记录）。   
#### 集合排序(有序集合)
不同的是，一个有序集合的每个成员都可以排序，就是为了按有序集合排序获取它们，按权重分值从最小到最大排序。虽然成员都是独一无二的，按权重分数值可能会重复。   
```
redis 127.0.0.1:6379> zadd tutoriallist 0 redis
(integer) 1
redis 127.0.0.1:6379> zadd tutoriallist 0 mongodb
(integer) 1
redis 127.0.0.1:6379> zadd tutoriallist 0 rabitmq
(integer) 1
redis 127.0.0.1:6379> zadd tutoriallist 0 rabitmq
(integer) 0
redis 127.0.0.1:6379> ZRANGEBYSCORE tutoriallist 0 1000
 
1) "redis"
2) "mongodb"
3) "rabitmq"
```
### Redis HyperLogLog
Redis HyperLogLog 是用来做基数统计的算法，HyperLogLog 的优点是，在输入元素的数量或者体积非常非常大时，计算基数所需的空间总是固定 的、并且是很小的。  
在 Redis 里面，每个 HyperLogLog 键只需要花费 12 KB 内存，就可以计算接近 2^64 个不同元素的基 数。  
```
redis 127.0.0.1:6379> PFADD tutorials "redis"
 
1) (integer) 1
 
redis 127.0.0.1:6379> PFADD tutorials "mongodb"
 
1) (integer) 1
 
redis 127.0.0.1:6379> PFADD tutorials "mysql"
 
1) (integer) 1
 
redis 127.0.0.1:6379> PFCOUNT tutorials
 
(integer) 3
```
### 发布/订阅
`SUBSCRIBE redisChat`   
`PUBLISH redisChat "Redis is a great caching technique"`   
### 事务
Redis事务允许一组命令在单一步骤中执行。事务有两个属性，说明如下：   
* 在一个事务中的所有命令作为单个独立的操作顺序执行。在Redis事务中的执行过程中而另一客户机发出的请求，这是不可以的；
* Redis事务是原子的。原子意味着要么所有的命令都执行，要么都不执行；   

Redis 事务由指令 MULTI 发起的，之后传递需要在事务中和整个事务中，最后由 EXEC 命令执行所有命令的列表。   
```
redis 127.0.0.1:6379> MULTI
OK
List of commands here
redis 127.0.0.1:6379> EXEC
```
### 脚本
语法:  
```
EVAL script numkeys key [key ...] arg [arg ...]
```
示例:  
```
redis 127.0.0.1:6379> EVAL "return {KEYS[1],KEYS[2],ARGV[1],ARGV[2]}" 2 key1 key2 first second
 
1) "key1"
2) "key2"
3) "first"
4) "second"
```
### 备份/恢复
使用SAVE命令创建当前数据库备份   
在执行此命令之后，将在 redis 目录中创建一个 dump.rdb 文件。  
BGSAVE会启动备份进程  
要恢复 redis 数据只需要要将 Redis 的备份文件（dump.rdb）放到 Redis 的目录中，并启动服务器。要了解知道 Redis 目录在什么位置，可使用 CONFIG 命令`config get dir`  
### 安全
`CONFIG get requirepass`  获取是否设置密码  
`AUTH password` 验证身份  
### 性能
```
redis-benchmark [option] [option value]
```
### Java连接
使用jedis  
