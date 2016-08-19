# Spring MVC
 
 
### 处理请求流程
客户端发送Http请求->匹配到路径后转交给DispatcherServlet-> DispatcherServlet根据请求的信息及配置找到处理请求的处理器(Handler)->通过Handler Adapter(适配器)对Handler进行封装，再对Handler的接口进行调用。->处理后返回ModelAndView和DispatcherServlet->对View(视图)进行渲染->最终客户端获得html页面或者XML或JSON 
 
### 了解Spring MVC框架工作原理的
1. DispatcherServlet如何截获特定HTTP请求,并交由SpringMVC处理 
2. Web层的Spring容器如何调用业务层的Sring容器，使Web层bean如何调用业务层的bean
3. 如何初始化Spring MVC的各个组件，并将它们装配到DispatcherServlet中 


### 注解
#### @Controller
使POJO成为一个能处理HTTP请求的控制器。  
#### @RequestMapping
在控制器的类定义及方法处使用。设置映射。
1. URL映射 value  
2. 请求方法GET/POST method 
3. 参数 params 
4. 报文头 headers 
 
##### 参数表达式
 param1/!param1/param1!=value1/param1=value  
分别为请求必须包含名为param1的请求参数，不能包含，必须包含且值不能为value1，必须包含切值必须为value1  


#### 参数绑定
##### @CookieValue
绑定请求中的Cookie值  
##### @RequestParam
绑定请求参数的值  
##### @RequestHeader  
绑定请求报文头的属性值  
##### 使用命令/表单对象  
直接使用POJO
##### ServletAPI
HttpServletRequest/HttpServletResponse  
还有SpringMVC定义的代理原生Servlet的接口，如WebRequest/NativeWebRequest  

#### @ModelAttribute
如果需要i将入参对象添加到模型中，则添加此注解。  
`@ModelAttribute("user")`  

### Spring标签
``` html
<%@ taglib prefix="form" uri="http://www.apringframework.org/tags/form"%>
<form:form ModelAttribute="user">

</form:form>
```

### FreeMarker
``` html
<!-- 列表迭代 -->
<#list userList as user>
  ${user.name}
<#list>
```
