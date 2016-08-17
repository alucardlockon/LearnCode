# Spring MVC


### 处理请求流程
客户端发送Http请求->匹配到路径后转交给DispatcherServlet-> DispatcherServlet根据请求的信息及配置找到处理请求的处理器(Handler)->通过Handler Adapter(适配器)对Handler进行封装，再对Handler的接口进行调用。->处理后返回ModelAndView和DispatcherServlet->对View(视图)进行渲染->最终客户端获得html页面或者XML或JSON  

### 了解Spring MVC框架工作原理的
1. DispatcherServlet如何截获特定HTTP请求,并交由SpringMVC处理  
2. Web层的Spring容器如何调用业务层的Sring容器，使Web层bean如何调用业务层的bean
3. 如何初始化Spring MVC的各个组件，并将它们装配到DispatcherServlet中  


