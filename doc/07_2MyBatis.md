# MyBatis

#### 获取SqlSessionFactory
``` java
String resource="org/mybatis/Configuration.xml";  
Reader reader=Resources.getResourceAsReader(resource);
sqlMapper=new SqlSessionFactoryBuilder().build(reader);
```
#### 从SqlSessionFactory中获取SqlSession
``` java
SqlSession session=sqlMapper.openSession();
try{
  Blog blog=(Blog)session.selectOne("org.mybatis.example.BlogMapper.selectBlog",101);
}finally{
  seesion.close();
}
//新方法
SqlSession session=sqlSessionFactory.openSession();
try{
  BlogMapper mapper=session.getMapper(BlogMapper.class);
  Blog blog=mapper.selectBlog(101);
}finally{
  session.close();
}
```
### XML配置文件
configuration 配置   
properties 属性  
settings 设置   
typeAliases 类型命名  
typeHandlers 类型处理器  
objectFactory 对象工厂  
plugins 插件  
environments 环境  
-- environment 环境变量  
----- transactionManager 事务管理器   
----- dataSource 数据源  
映射器  
### SELECT
``` XML
<select id="selectPerson" parameterType="int" resultType="hashmap">
  SELECT * FROM PERSON WHERE ID=#{id}
</select>
```


