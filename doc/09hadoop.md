# Hadoop

###课堂笔记
#### HDFS(the Hadoop Distributed File System)
具有高性能，容错机制，主从架构，可扩展等特点。  
组成:NameNode和SecondaryNameNode
##### NameNode
云数据信息存储，包含:文件存放路径所有者，block名称和路径。  
##### SecondaryNameNode
定期从NameNode获取信息每小时或100w次提交则执行checkpoint
##### HA高可用性
SecondaryNameNode可在NameNode宕机时接管它  
##### 联邦(Federaion)模式
多个独立NameNode,每个NameNode管理namespace的一部分  

##### 其他
常用端口:50070
命令:hadoop fs -cat/-mkdir/ls/put/rm  

#### MapRedurce
流程检查
#### YARN
作为集群管理平台
ResourceManager 作业初始化  
NodeManager 作业控制  
JobHistoryManeger 历史信息   
YARN组成:Container/ApplicationMaster  
#### Hbase  
具有高可用性，支持海量数据等特点  
基于列簇，单行事物，rowkey是唯一索引,支持PB+数据,高吞吐量  
#### Hive
使用Sql查询，可ETL转码文字  
#### Impala
效率高于Hive
#### Spark
大规模数据处理引擎  

#### solr
搜索服务器
