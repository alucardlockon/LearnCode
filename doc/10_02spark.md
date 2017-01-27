# Spark

[Spark入门(py)](http://blog.jobbole.com/86232/)

### 设置Spark
解压并放到指定目录  
```
$ tar -xzf spark-1.2.0-bin-hadoop2.4.tgz
$ mv spark-1.2.0-bin-hadoop2.4 /srv/spark-1.2.0
```
环境变量  
```
export SPARK_HOME=/srv/spark
export PATH=$SPARK_HOME/bin:$PATH
```
执行`source`命令让变量立即生效,然后`pyspark`运行Python的spark  



