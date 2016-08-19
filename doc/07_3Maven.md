# Maven
 
### 使用
create:
```
mvn -B archetype:generate \
  -DarchetypeGroupId=org.apache.maven.archetypes \
  -DgroupId=com.mycompany.app \
  -DartifactId=my-app
```
pom.xml:(Project Object Model)
``` xml
<!-- pom.xml -->
<project xmlns="http://maven.apache.org/POM/4.0.0"
  xmlns:xsi="http://www.w3.org/2001/XMLSchema-instance"
  xsi:schemaLocation="http://maven.apache.org/POM/4.0.0
                      http://maven.apache.org/xsd/maven-4.0.0.xsd">
  <modelVersion>4.0.0</modelVersion>
  <groupId>com.mycompany.app</groupId>
  <artifactId>my-app</artifactId>
  <packaging>jar</packaging>
  <version>1.0-SNAPSHOT</version>
  <name>Maven Quick Start Archetype</name>
  <url>http://maven.apache.org</url>
  <dependencies>
    <dependency>
      <groupId>junit</groupId>
      <artifactId>junit</artifactId>
      <version>4.11</version>
      <scope>test</scope>
    </dependency>
  </dependencies>
</project>
```
编译项目:  
`mvn compile`  
测试:  
编译测试`mvn test-compile` 编译并运行测试 `mvn test`
创建jar:  
`mvn package` 添加到本地仓库 `mvn install`  
清空坂本:
`mvn clean`   
生成项目相关信息网站  
`mvn site`  
生成idea/eclipse项目  
`mvn idea:idea`,`mvn eclipse:eclipse`  

#### 快照坂本
版本号后有-SNAPSHOT,表示最新开发版  



 
 