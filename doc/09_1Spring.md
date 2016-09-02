# Spring

### 项目结构及MVC层次
#### 类包规划
分为dao,domain,service和web:domain属于业务层,但同时能被持久层和展现层共享，所以单独划分包。  

#### 持久层
持久层负责数据的访问和操作，DAO类被上层的业务类调用。  
```java
@Repository //通过Spring注解定义一个DAO
public class UserDao{
  @Autowired //自动注入jdbcTemplate的bean
  private JdbcTemplate jdbcTemplate;
}
```
#### 领域对象(domain)
领域对象一般要实现Seriallzable接口以便可以序列化。  

#### 业务层
```java
@service //将UserService标注为一个服务层的Bean
public class UserService{
  @Autowired ///注入UserDao类
  private UserDao userDao;
  
  ...
}
```
配置事务管理器，配置AOP提供事务管理增强。  
#### 测试类
```java
@ContextConfiguration(locations={"/applicationCOntext.xml"}) //启动Spring容器
public class UserServiceTest extends AbstractTestNGSpringContextTests{ //基于TestNG的Spring测试框架
  @Autowired
  private UserService userService;
  @Test//标注虎测试方法
  public void hasMatchUser(){
    ...
    assertTrue(userService.hasMatchUser("admin","123456"));
    assertEquals(a,"1");
    ...
  }
}
```
#### 展现层
配置Spring MVC框架,从类路径下加载Spring配置文件,配置一个Servlet截获url请求。  
Spring MVC配置文件:需要在WEB-INF目录下提供一个<servlet名>-servlet.xml的配置文件。  
##### POJO控制器类
LoginController.java:(需要在xxx-servlet.xml声明此控制器)
```java
@Controller //标注味一个Spring MVC的Controller
@RequestMapping(value="/admin")
public class LoginController{
  ...
  @RequestMapping(value="/login.html") //负责处理/login.html的请求
  public String loginPage(){
    return "login";
  }
  
  @RequestMapping(value="/loginCheck.html") //负责处理loginCHeck.html请求
  public ModelAndView loginCheck(HttpServletRequest request,LoginCommand loginCommand){
    ....
    return new ModelAndView("main");
  }
  ...
}
```
##### 配置ModelAndView解析
在xxx-servlet.xml中提供一个定义解析规则的Bean。  
```xml
<bean class="org.springframework.web.xxxx"
  p:viewClass="xxx" p:prefix="/WEB-INF/jsp" p:suffix=".jsp" />
```
##### 编写jsp页面
JSTL标签引入error变量`<c:out value="${error}" />`，对应ModelAndView("login","error","密码错误")对象所声明的error参数。  

### Spring IoC
*Ioc(控制反转)* 就是通过容器来控制业务对象之间的依赖关系，而非传统实现中，由代码直接操控。也就是控制权由应用代码中转到了外部容器，控制权的转移，就是反转。  
#### BeanFactory和applicationContext
BeanFactory是Spring框架最核心的接口，它提供了高级IoC的配置机制,使管理不同类型的java对象还曾为可能。applicationContext建立在BeanFactory基础之上，提供了更多面向应用的功能，提供了国际化支持和框架事件体系，更易于创建实际应用。一般称BeanFactory为IoC容器，称applicationContext为应用上下文。但有时applicationContext也被称为Spring容器。  
##### 获取applicationContext
通过类路径:`ApplicationContext ctx=new ClassPathXmlApplicationContext("com/ywh/context/bean.xml")`  
文件系统:`ApplicationContext ctx=new FileSystemXmlApplicationContext("com/ywh/context/beans.xml")`  
可以传入多个路径:`new FileSystemXmlApplicationContext(new String[]{"com/ywh/context/beans1.xml","com/ywh/context/beans2.xml"})`  
#### 基于类注解的配置
Spring 3.0以上开始支持，相比XML配置更加灵活!并提供了ApplicationContext的实现类AnnotationConfigApplicationContext类。
```java
@Configuration //表示是一个配置信息提供类
public class Beans{
  @Bean(name="car") //定义一个bean
  public Car buildCar(){
    Car car=new Car();
    car.setBrand("Tesla");
    return car;
  }
}
```
#### 配置log4j
将log4j配置文件放在WEB-INF/calsses下即可顺利启动。如果放在其他路径下需要到web.xml中指定Log4j的配置文件位置。  

### 依赖注入
#### 属性注入
即通过setXXX()方法注入Bean的属性值或依赖对象。  
属性注入要求Bean提供一个默认的构造函数，并为需要注入的属性提供对应的Setter方法。  
> 一般情况下变量以小写字母开头，但允许大写字母，但必须满足"变量的前两个字母要么全部大写，要么全部小写"的要求。  

```xml
<bean id="car" class="xxx.Car">
  <property name="maxSpeed"><value>120</value></property>
</bean>
```

#### 构造函数注入
构造函数注入保证一些必要的属性在Bean实例化就得到设置。  
使用属性注入的前提是Bean必须提供带参数的构造函数。  
```xml
<bean id="car" class="xxx.Car">
  <constructor-arg type="java.lang.String">
    <value>特斯拉model s</value>
  </constructor-arg>
  <constructor-arg type="double">
    <value>2000</value>
  </constructor-arg>
</bean>
```

