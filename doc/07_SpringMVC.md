# Spring MVC

### 处理请求流程
客户端发送Http请求->匹配到路径后转交给DispatcherServlet->DispatcherServlet根据请求的信息及配置找到处理请求的处理器(Handler)->通过Handler Adapter(适配器)对Handler进行封装，再对Handler的接口进行调用。->处理后返回ModelAndView和DispatcherServlet->对View(视图)进行渲染->最终客户端获得html页面或者XML或JSON  

