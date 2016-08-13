# jquery

[jquery手册](http://www.w3school.com.cn/jquery/index.asp)

### CDN
Google:  
``` html
<head>
<script type="text/javascript" src="http://ajax.googleapis.com/ajax/libs
/jquery/1.4.0/jquery.min.js"></script>
</head>
```
MS:
``` html
<head>
<script type="text/javascript" src="http://ajax.microsoft.com/ajax/jquery
/jquery-1.4.min.js"></script>
</head>
```
### jQuery 语法实例
$(this).hide()  
演示 jQuery hide() 函数，隐藏当前的 HTML 元素。  
$("#test").hide()  
演示 jQuery hide() 函数，隐藏 id="test" 的元素。  
$("p").hide()  
演示 jQuery hide() 函数，隐藏所有 <p> 元素。  
$(".test").hide()  
演示 jQuery hide() 函数，隐藏所有 class="test" 的元素。  

### 效果
#### 显示隐藏
``` javascript
$("p").hide();
$("p").show();
$(selector).hide(speed,callback);
$(selector).show(speed,callback);
$("p").toggle();
$(selector).toggle(speed,callback);
```
可以使用 toggle() 方法来切换 hide() 和 show() 方法。
#### 淡入淡出
```
jQuery fadeIn()
<!-- 演示 jQuery fadeIn() 方法。用于淡入已隐藏的元素。 -->
jQuery fadeOut()
<!-- 演示 jQuery fadeOut() 方法。 用于淡出可见元素。 -->
jQuery fadeToggle()
<!-- 演示 jQuery fadeToggle() 方法。可以在 fadeIn() 与 fadeOut() 方法之间进行切换 -->
jQuery fadeTo()
<!-- 演示 jQuery fadeTo() 方法。允许渐变为给定的不透明度（值介于 0 与 1 之间）。 -->
```
#### 滑动
jQuery slideDown() 方法用于向下滑动元素。
jQuery slideUp() 方法用于向上滑动元素。
jQuery slideToggle() 方法可以在 slideDown() 与 slideUp() 方法之间进行切换
#### 动画
``` javascript
示例  
$("button").click(function(){
  $("div").animate({
    left:'250px',
    opacity:'0.5',
    height:'150px',
    width:'150px'
  });
}); 
```
使用相对值  
``` javascript
$("button").click(function(){
  $("div").animate({
    left:'250px',
    height:'+=150px',
    width:'+=150px'
  });
});
```
使用队列功能  
``` javascript
$("button").click(function(){
  var div=$("div");
  div.animate({height:'300px',opacity:'0.4'},"slow");
  div.animate({width:'300px',opacity:'0.8'},"slow");
  div.animate({height:'100px',opacity:'0.4'},"slow");
  div.animate({width:'100px',opacity:'0.8'},"slow");
});
```
#### STOP
jQuery stop() 方法用于停止动画或效果，在它们完成之前  
#### Chaining
Chaining 允许我们在一条语句中允许多个 jQuery 方法（在相同的元素上）。
``` javascript
$("#p1").css("color","red").slideUp(2000).slideDown(2000);
```

### jquery HTML
#### 获得内容
``` javascript
$("#btn1").click(function(){
  alert("Text: " + $("#test").text());
});
$("#btn2").click(function(){
  alert("HTML: " + $("#test").html());
});
```
#### 设置内容
``` javascript
$("#btn1").click(function(){
  $("#test1").text("Hello world!");
});
$("#btn2").click(function(){
  $("#test2").html("<b>Hello world!</b>");
});
$("#btn3").click(function(){
  $("#test3").val("Dolly Duck");
});
```
#### 添加元素
append() - 在被选元素的结尾插入内容  
prepend() - 在被选元素的开头插入内容  
after() - 在被选元素之后插入内容  
before() - 在被选元素之前插入内容  
#### 删除元素
通过 jQuery，可以很容易地删除已有的 HTML 元素。  
remove() - 删除被选元素（及其子元素）  
empty() - 从被选元素中删除子元素  
#### 获取并设置 CSS 类
addClass() - 向被选元素添加一个或多个类  
removeClass() - 从被选元素删除一个或多个类  
toggleClass() - 对被选元素进行添加/删除类的切换操作  
css() - 设置或返回样式属性  
#### 尺寸
width() 方法设置或返回元素的宽度（不包括内边距、边框或外边距）。  
height() 方法设置或返回元素的高度（不包括内边距、边框或外边距）。  
innerWidth() 方法返回元素的宽度（包括内边距）。  
innerHeight() 方法返回元素的高度（包括内边距）。  
outerWidth() 方法返回元素的宽度（包括内边距和边框）。  
outerHeight() 方法返回元素的高度（包括内边距和边框）。  
### 遍历
#### 祖先
parent()  
parents()  
parentsUntil()  
#### 后代
children()  
find()  
#### 同胞
siblings()
next()
nextAll()
nextUntil()
prev()
prevAll()
prevUntil()
#### 过滤
first() 方法返回被选元素的首个元素。
last() 方法返回被选元素的最后一个元素。
eq(index) 方法返回被选元素中带有指定索引号的元素。
filter(".intro") 方法允许您规定一个标准。不匹配这个标准的元素会被从集合中删除，匹配的元素会被返回。
not(".intro")  方法返回不匹配标准的所有元素。
### Ajax
AJAX = 异步 JavaScript 和 XML（Asynchronous JavaScript and XML）。  
#### load方法
``` javascript
$(selector).load(URL,data,callback);
//示例
$("#div1").load("demo_test.txt");
$("#div1").load("demo_test.txt #p1");
```
可选的 callback 参数规定当 load() 方法完成后所要允许的回调函数。回调函数可以设置不同的参数：
* responseTxt - 包含调用成功时的结果内容
* statusTXT - 包含调用的状态
* xhr - 包含 XMLHttpRequest 对象
``` javascript
$("button").click(function(){
  $("#div1").load("demo_test.txt",function(responseTxt,statusTxt,xhr){
    if(statusTxt=="success")
      alert("外部内容加载成功！");
    if(statusTxt=="error")
      alert("Error: "+xhr.status+": "+xhr.statusText);
  });
});
```
#### get() 和 post() 方法
两种在客户端和服务器端进行请求-响应的常用方法是：GET 和 POST。
GET - 从指定的资源请求数据
POST - 向指定的资源提交要处理的数据
##### get()
``` javascript
$.get(URL,callback);
//示例
$("button").click(function(){
  $.get("demo_test.asp",function(data,status){
    alert("Data: " + data + "\nStatus: " + status);
  });
});
```
##### post()
``` javascript
$.post(URL,data,callback);
//示例
$("button").click(function(){
  $.post("demo_test_post.asp",
  {
    name:"Donald Duck",
    city:"Duckburg"
  },
  function(data,status){
    alert("Data: " + data + "\nStatus: " + status);
  });
});
```
### 如何在页面上同时使用 jQuery 和其他框架？
noConflict() 方法会释放会 $ 标识符的控制，这样其他脚本就可以使用它了。  
``` javascript
$.noConflict();
jQuery(document).ready(function(){
  jQuery("button").click(function(){
    jQuery("p").text("jQuery 仍在运行！");
  });
});
```
### 选择器
<html>
<table class="dataintable">
<tbody><tr>
<th>选择器</th>
<th>实例</th>
<th>选取</th>
</tr>

<tr>
<td><a title="jQuery * 选择器" href="/jquery/selector_all.asp">*</a></td>
<td>$("*")</td>
<td>所有元素</td>
</tr>

<tr>
<td><a title="jQuery # 选择器" href="/jquery/selector_id.asp">#<i>id</i></a></td>
<td>$("#lastname")</td>
<td>id="lastname" 的元素</td>
</tr>

<tr>
<td><a title="jQuery . 选择器" href="/jquery/selector_class.asp">.<i>class</i></a></td>
<td>$(".intro")</td>
<td>所有 class="intro" 的元素</td>
</tr>

<tr>
<td><a title="jQuery element 选择器" href="/jquery/selector_element.asp"><i>element</i></a></td>
<td>$("p")</td>
<td>所有 &lt;p&gt; 元素</td>
</tr>

<tr>
<td>.<i>class</i>.<i>class</i></td>
<td>$(".intro.demo")</td>
<td>所有 class="intro" 且 class="demo" 的元素</td>
</tr>

<tr>
<td style="background-color:#fff;">&nbsp;</td>
<td style="background-color:#fff;">&nbsp;</td>
<td style="background-color:#fff;">&nbsp;</td>
</tr>

<tr>
<td><a title="jQuery :first 选择器" href="/jquery/selector_first.asp">:first</a></td>
<td>$("p:first")</td>
<td>第一个 &lt;p&gt; 元素</td>
</tr>

<tr>
<td><a title="jQuery :last 选择器" href="/jquery/selector_last.asp">:last</a></td>
<td>$("p:last")</td>
<td>最后一个 &lt;p&gt; 元素</td>
</tr>

<tr>
<td><a title="jQuery :even 选择器" href="/jquery/selector_even.asp">:even</a></td>
<td>$("tr:even")</td>
<td>所有偶数 &lt;tr&gt; 元素</td>
</tr>

<tr>
<td><a title="jQuery :odd 选择器" href="/jquery/selector_odd.asp">:odd</a></td>
<td>$("tr:odd")</td>
<td>所有奇数 &lt;tr&gt; 元素</td>
</tr>

<tr>
<td style="background-color:#fff;">&nbsp;</td>
<td style="background-color:#fff;">&nbsp;</td>
<td style="background-color:#fff;">&nbsp;</td>
</tr>

<tr>
<td><a title="jQuery :eq() 选择器" href="/jquery/selector_eq.asp">:eq(<i>index</i>)</a></td>
<td>$("ul li:eq(3)")</td>
<td>列表中的第四个元素（index 从 0 开始）</td>
</tr>

<tr>
<td><a title="jQuery :gt 选择器" href="/jquery/selector_gt.asp">:gt(<i>no</i>)</a></td>
<td>$("ul li:gt(3)")</td>
<td>列出 index 大于 3 的元素</td>
</tr>

<tr>
<td><a title="jQuery :lt 选择器" href="/jquery/selector_lt.asp">:lt(<i>no</i>)</a></td>
<td>$("ul li:lt(3)")</td>
<td>列出 index 小于 3 的元素</td>
</tr>

<tr>
<td>:not(<i>selector</i>)</td>
<td>$("input:not(:empty)")</td>
<td>所有不为空的 input 元素</td>
</tr>

<tr>
<td style="background-color:#fff;">&nbsp;</td>
<td style="background-color:#fff;">&nbsp;</td>
<td style="background-color:#fff;">&nbsp;</td>
</tr>

<tr>
<td><a title="jQuery :header 选择器" href="/jquery/selector_header.asp">:header</a></td>
<td>$(":header")</td>
<td>所有标题元素 &lt;h1&gt; - &lt;h6&gt;</td>
</tr>

<tr>
<td><a title="jQuery :animated 选择器" href="/jquery/selector_animated.asp">:animated</a></td>
<td>&nbsp;</td>
<td>所有动画元素</td>
</tr>

<tr>
<td style="background-color:#fff;">&nbsp;</td>
<td style="background-color:#fff;">&nbsp;</td>
<td style="background-color:#fff;">&nbsp;</td>
</tr>

<tr>
<td><a title="jQuery :contains 选择器" href="/jquery/selector_contains.asp">:contains(<i>text</i>)</a></td>
<td>$(":contains('W3School')")</td>
<td>包含指定字符串的所有元素</td>
</tr>

<tr>
<td><a title="jQuery :empty 选择器" href="/jquery/selector_empty.asp">:empty</a></td>
<td>$(":empty")</td>
<td>无子（元素）节点的所有元素</td>
</tr>

<tr>
<td>:hidden</td>
<td>$("p:hidden")</td>
<td>所有隐藏的 &lt;p&gt; 元素</td>
</tr>

<tr>
<td><a title="jQuery :visible 选择器" href="/jquery/selector_visible.asp">:visible</a></td>
<td>$("table:visible")</td>
<td>所有可见的表格</td>
</tr>

<tr>
<td style="background-color:#fff;">&nbsp;</td>
<td style="background-color:#fff;">&nbsp;</td>
<td style="background-color:#fff;">&nbsp;</td>
</tr>

<tr>
<td>s1,s2,s3</td>
<td>$("th,td,.intro")</td>
<td>所有带有匹配选择的元素</td>
</tr>

<tr>
<td style="background-color:#fff;">&nbsp;</td>
<td style="background-color:#fff;">&nbsp;</td>
<td style="background-color:#fff;">&nbsp;</td>
</tr>

<tr>
<td><a title="jQuery [attribute] 选择器" href="/jquery/selector_attribute.asp">[<i>attribute</i>]</a></td>
<td>$("[href]")</td>
<td>所有带有 href 属性的元素</td>
</tr>

<tr>
<td><a title="jQuery [attribute=value] 选择器" href="/jquery/selector_attribute_equal_value.asp">[<i>attribute</i>=<i>value</i>]</a></td>
<td>$("[href='#']")</td>
<td>所有 href 属性的值等于 "#" 的元素</td>
</tr>

<tr>
<td><a title="jQuery [attribute!=value] 选择器" href="/jquery/selector_attribute_notequal_value.asp">[<i>attribute</i>!=<i>value</i>]</a></td>
<td>$("[href!='#']")</td>
<td>所有 href 属性的值不等于 "#" 的元素</td>
</tr>

<tr>
<td><a title="jQuery [attribute$=value] 选择器" href="/jquery/selector_attribute_end_value.asp">[<i>attribute</i>$=<i>value</i>]</a></td>
<td>$("[href$='.jpg']")</td>
<td>所有 href 属性的值包含以 ".jpg" 结尾的元素</td>
</tr>

<tr>
<td style="background-color:#fff;">&nbsp;</td>
<td style="background-color:#fff;">&nbsp;</td>
<td style="background-color:#fff;">&nbsp;</td>
</tr>

<tr>
<td><a title="jQuery :input 选择器" href="/jquery/selector_input.asp">:input</a></td>
<td>$(":input")</td>
<td>所有 &lt;input&gt; 元素</td>
</tr>

<tr>
<td><a title="jQuery :text 选择器" href="/jquery/selector_input_text.asp">:text</a></td>
<td>$(":text")</td>
<td>所有 type="text" 的 &lt;input&gt; 元素</td>
</tr>

<tr>
<td><a title="jQuery :password 选择器" href="/jquery/selector_input_password.asp">:password</a></td>
<td>$(":password")</td>
<td>所有 type="password" 的 &lt;input&gt; 元素</td>
</tr>

<tr>
<td><a title="jQuery :radio 选择器" href="/jquery/selector_input_radio.asp">:radio</a></td>
<td>$(":radio")</td>
<td>所有 type="radio" 的 &lt;input&gt; 元素</td>
</tr>

<tr>
<td><a title="jQuery :checkbox 选择器" href="/jquery/selector_input_checkbox.asp">:checkbox</a></td>
<td>$(":checkbox")</td>
<td>所有 type="checkbox" 的 &lt;input&gt; 元素</td>
</tr>

<tr>
<td><a title="jQuery :submit 选择器" href="/jquery/selector_input_submit.asp">:submit</a></td>
<td>$(":submit")</td>
<td>所有 type="submit" 的 &lt;input&gt; 元素</td>
</tr>

<tr>
<td><a title="jQuery :reset 选择器" href="/jquery/selector_input_reset.asp">:reset</a></td>
<td>$(":reset")</td>
<td>所有 type="reset" 的 &lt;input&gt; 元素</td>
</tr>

<tr>
<td><a title="jQuery :button 选择器" href="/jquery/selector_input_button.asp">:button</a></td>
<td>$(":button")</td>
<td>所有 type="button" 的 &lt;input&gt; 元素</td>
</tr>

<tr>
<td><a title="jQuery :image 选择器" href="/jquery/selector_input_image.asp">:image</a></td>
<td>$(":image")</td>
<td>所有 type="image" 的 &lt;input&gt; 元素</td>
</tr>

<tr>
<td><a title="jQuery :file 选择器" href="/jquery/selector_input_file.asp">:file</a></td>
<td>$(":file")</td>
<td>所有 type="file" 的 &lt;input&gt; 元素</td>
</tr>

<tr>
<td style="background-color:#fff;">&nbsp;</td>
<td style="background-color:#fff;">&nbsp;</td>
<td style="background-color:#fff;">&nbsp;</td>
</tr>

<tr>
<td><a title="jQuery :enabled 选择器" href="/jquery/selector_input_enabled.asp">:enabled</a></td>
<td>$(":enabled")</td>
<td>所有激活的 input 元素</td>
</tr>

<tr>
<td><a title="jQuery :disabled 选择器" href="/jquery/selector_input_disabled.asp">:disabled</a></td>
<td>$(":disabled")</td>
<td>所有禁用的 input 元素</td>
</tr>

<tr>
<td><a title="jQuery :selected 选择器" href="/jquery/selector_input_selected.asp">:selected</a></td>
<td>$(":selected")</td>
<td>所有被选取的 input 元素</td>
</tr>

<tr>
<td><a title="jQuery :checked 选择器" href="/jquery/selector_input_checked.asp">:checked</a></td>
<td>$(":checked")</td>
<td>所有被选中的 input 元素</td>
</tr>
</tbody></table>
</html>

### 事件
<html>
<table class="dataintable">
<tbody><tr>
<th style="width:35%;">方法</th>
<th>描述</th>
</tr>

<tr>
<td><a title="jQuery 事件 - bind() 方法" href="/jquery/event_bind.asp">bind()</a></td>
<td>向匹配元素附加一个或更多事件处理器</td>
</tr>

<tr>
<td><a title="jQuery 事件 - blur() 方法" href="/jquery/event_blur.asp">blur()</a></td>
<td>触发、或将函数绑定到指定元素的 blur 事件</td>
</tr>


<tr>
<td><a title="jQuery 事件 - change() 方法" href="/jquery/event_change.asp">change()</a></td>
<td>触发、或将函数绑定到指定元素的 change 事件</td>
</tr>

<tr>
<td><a title="jQuery 事件 - click() 方法" href="/jquery/event_click.asp">click()</a></td>
<td>触发、或将函数绑定到指定元素的 click 事件</td>
</tr>

<tr>
<td><a title="jQuery 事件 - dblclick() 方法" href="/jquery/event_dblclick.asp">dblclick()</a></td>
<td>触发、或将函数绑定到指定元素的 double click 事件</td>
</tr>

<tr>
<td><a title="jQuery 事件 - delegate() 方法" href="/jquery/event_delegate.asp">delegate()</a></td>
<td>向匹配元素的当前或未来的子元素附加一个或多个事件处理器</td>
</tr>

<tr>
<td><a title="jQuery 事件 - die() 方法" href="/jquery/event_die.asp">die()</a></td>
<td>移除所有通过 live() 函数添加的事件处理程序。</td>
</tr>

<tr>
<td><a title="jQuery 事件 - error() 方法" href="/jquery/event_error.asp">error()</a></td>
<td>触发、或将函数绑定到指定元素的 error 事件</td>
</tr>

<tr>
<td><a title="jQuery 事件 - isDefaultPrevented() 方法" href="/jquery/event_isdefaultprevented.asp">event.isDefaultPrevented()</a></td>
<td>返回 event 对象上是否调用了 event.preventDefault()。</td>
</tr>

<tr>
<td><a title="jQuery 事件 - pageX 属性" href="/jquery/event_pagex.asp">event.pageX</a></td>
<td>相对于文档左边缘的鼠标位置。</td>
</tr>

<tr>
<td><a title="jQuery 事件 - pageY 属性" href="/jquery/event_pagey.asp">event.pageY</a></td>
<td>相对于文档上边缘的鼠标位置。</td>
</tr>

<tr>
<td><a title="jQuery 事件 - preventDefault() 方法" href="/jquery/event_preventdefault.asp">event.preventDefault()</a></td>
<td>阻止事件的默认动作。</td>
</tr>

<tr>
<td><a title="jQuery 事件 - result 属性" href="/jquery/event_result.asp">event.result</a></td>
<td>包含由被指定事件触发的事件处理器返回的最后一个值。</td>
</tr>

<tr>
<td><a title="jQuery 事件 - target 属性" href="/jquery/event_target.asp">event.target</a></td>
<td>触发该事件的 DOM 元素。</td>
</tr>

<tr>
<td><a title="jQuery 事件 - timeStamp 属性" href="/jquery/event_timeStamp.asp">event.timeStamp</a></td>
<td>该属性返回从 1970 年 1 月 1 日到事件发生时的毫秒数。</td>
</tr>

<tr>
<td><a title="jQuery 事件 - type 属性" href="/jquery/event_type.asp">event.type</a></td>
<td>描述事件的类型。</td>
</tr>

<tr>
<td><a title="jQuery 事件 - which 属性" href="/jquery/event_which.asp">event.which</a></td>
<td>指示按了哪个键或按钮。</td>
</tr>

<tr>
<td><a title="jQuery 事件 - focus() 方法" href="/jquery/event_focus.asp">focus()</a></td>
<td>触发、或将函数绑定到指定元素的 focus 事件</td>
</tr>

<tr>
<td><a title="jQuery 事件 - keydown() 方法" href="/jquery/event_keydown.asp">keydown()</a></td>
<td>触发、或将函数绑定到指定元素的 key down 事件</td>
</tr>

<tr>
<td><a title="jQuery 事件 - keypress() 方法" href="/jquery/event_keypress.asp">keypress()</a></td>
<td>触发、或将函数绑定到指定元素的 key press 事件</td>
</tr>

<tr>
<td><a title="jQuery 事件 - keyup() 方法" href="/jquery/event_keyup.asp">keyup()</a></td>
<td>触发、或将函数绑定到指定元素的 key up 事件</td>
</tr>

<tr>
<td><a title="jQuery 事件 - live() 方法" href="/jquery/event_live.asp">live()</a></td>
<td>为当前或未来的匹配元素添加一个或多个事件处理器</td>
</tr>

<tr>
<td><a title="jQuery 事件 - load() 方法" href="/jquery/event_load.asp">load()</a></td>
<td>触发、或将函数绑定到指定元素的 load 事件</td>
</tr>

<tr>
<td><a title="jQuery 事件 - mousedown() 方法" href="/jquery/event_mousedown.asp">mousedown()</a></td>
<td>触发、或将函数绑定到指定元素的 mouse down 事件</td>
</tr>

<tr>
<td><a title="jQuery 事件 - mouseenter() 方法" href="/jquery/event_mouseenter.asp">mouseenter()</a></td>
<td>触发、或将函数绑定到指定元素的 mouse enter 事件</td>
</tr>

<tr>
<td><a title="jQuery 事件 - mouseleave() 方法" href="/jquery/event_mouseleave.asp">mouseleave()</a></td>
<td>触发、或将函数绑定到指定元素的 mouse leave 事件</td>
</tr>

<tr>
<td><a title="jQuery 事件 - mousemove() 方法" href="/jquery/event_mousemove.asp">mousemove()</a></td>
<td>触发、或将函数绑定到指定元素的 mouse move 事件</td>
</tr>

<tr>
<td><a title="jQuery 事件 - mouseout() 方法" href="/jquery/event_mouseout.asp">mouseout()</a></td>
<td>触发、或将函数绑定到指定元素的 mouse out 事件</td>
</tr>

<tr>
<td><a title="jQuery 事件 - mouseover() 方法" href="/jquery/event_mouseover.asp">mouseover()</a></td>
<td>触发、或将函数绑定到指定元素的 mouse over 事件</td>
</tr>

<tr>
<td><a title="jQuery 事件 - mouseup() 方法" href="/jquery/event_mouseup.asp">mouseup()</a></td>
<td>触发、或将函数绑定到指定元素的 mouse up 事件</td>
</tr>

<tr>
<td><a title="jQuery 事件 - one() 方法" href="/jquery/event_one.asp">one()</a></td>
<td>向匹配元素添加事件处理器。每个元素只能触发一次该处理器。</td>
</tr>

<tr>
<td><a title="jQuery 事件 - ready() 方法" href="/jquery/event_ready.asp">ready()</a></td>
<td>文档就绪事件（当 HTML 文档就绪可用时）</td>
</tr>

<tr>
<td><a title="jQuery 事件 - resize() 方法" href="/jquery/event_resize.asp">resize()</a></td>
<td>触发、或将函数绑定到指定元素的 resize 事件</td>
</tr>

<tr>
<td><a title="jQuery 事件 - scroll() 方法" href="/jquery/event_scroll.asp">scroll()</a></td>
<td>触发、或将函数绑定到指定元素的 scroll 事件</td>
</tr>

<tr>
<td><a title="jQuery 事件 - select() 方法" href="/jquery/event_select.asp">select()</a></td>
<td>触发、或将函数绑定到指定元素的 select 事件</td>
</tr>

<tr>
<td><a title="jQuery 事件 - submit() 方法" href="/jquery/event_submit.asp">submit()</a></td>
<td>触发、或将函数绑定到指定元素的 submit 事件</td>
</tr>

<tr>
<td><a title="jQuery 事件 - toggle() 方法" href="/jquery/event_toggle.asp">toggle()</a></td>
<td>绑定两个或多个事件处理器函数，当发生轮流的 click 事件时执行。</td>
</tr>

<tr>
<td><a title="jQuery 事件 - trigger() 方法" href="/jquery/event_trigger.asp">trigger()</a></td>
<td>所有匹配元素的指定事件</td>
</tr>

<tr>
<td><a title="jQuery 事件 - triggerHandler() 方法" href="/jquery/event_triggerhandler.asp">triggerHandler()</a></td>
<td>第一个被匹配元素的指定事件</td>
</tr>

<tr>
<td><a title="jQuery 事件 - unbind() 方法" href="/jquery/event_unbind.asp">unbind()</a></td>
<td>从匹配元素移除一个被添加的事件处理器</td>
</tr>

<tr>
<td><a title="jQuery 事件 - undelegate() 方法" href="/jquery/event_undelegate.asp">undelegate()</a></td>
<td>从匹配元素移除一个被添加的事件处理器，现在或将来</td>
</tr>

<tr>
<td><a title="jQuery 事件 - unload() 方法" href="/jquery/event_unload.asp">unload()</a></td>
<td>触发、或将函数绑定到指定元素的 unload 事件</td>
</tr>
</tbody></table>
</html>
### 效果
<html>
<table class="dataintable">
<tbody><tr>
<th>方法</th>
<th>描述</th>
</tr>

<tr>
<td><a title="jQuery 效果 - animate() 方法" href="/jquery/effect_animate.asp">animate()</a></td>
<td>对被选元素应用“自定义”的动画</td>
</tr>

<tr>
<td><a title="jQuery 效果 - clearQueue() 方法" href="/jquery/effect_clearqueue.asp">clearQueue()</a></td>
<td>对被选元素移除所有排队的函数（仍未运行的）</td>
</tr>

<tr>
<td>delay()</td>
<td>对被选元素的所有排队函数（仍未运行）设置延迟</td>
</tr>

<tr>
<td>dequeue()</td>
<td>运行被选元素的下一个排队函数</td>
</tr>

<tr>
<td><a title="jQuery 效果 - fadeIn() 方法" href="/jquery/effect_fadein.asp">fadeIn()</a></td>
<td>逐渐改变被选元素的不透明度，从隐藏到可见</td>
</tr>

<tr>
<td><a title="jQuery 效果 - fadeOut() 方法" href="/jquery/effect_fadeout.asp">fadeOut()</a></td>
<td>逐渐改变被选元素的不透明度，从可见到隐藏</td>
</tr>

<tr>
<td><a title="jQuery 效果 - fadeTo() 方法" href="/jquery/effect_fadeto.asp">fadeTo()</a></td>
<td>把被选元素逐渐改变至给定的不透明度</td>
</tr>

<tr>
<td><a title="jQuery 效果 - hide() 方法" href="/jquery/effect_hide.asp">hide()</a></td>
<td>隐藏被选的元素</td>
</tr>

<tr>
<td>queue()</td>
<td>显示被选元素的排队函数</td>
</tr>

<tr>
<td><a title="jQuery 效果 - show() 方法" href="/jquery/effect_show.asp">show()</a></td>
<td>显示被选的元素</td>
</tr>

<tr>
<td><a title="jQuery 效果 - slideDown() 方法" href="/jquery/effect_slidedown.asp">slideDown()</a></td>
<td>通过调整高度来滑动显示被选元素</td>
</tr>

<tr>
<td><a title="jQuery 效果 - slideToggle() 方法" href="/jquery/effect_slidetoggle.asp">slideToggle()</a></td>
<td>对被选元素进行滑动隐藏和滑动显示的切换</td>
</tr>

<tr>
<td><a title="jQuery 效果 - slideUp() 方法" href="/jquery/effect_slideup.asp">slideUp()</a></td>
<td>通过调整高度来滑动隐藏被选元素</td>
</tr>

<tr>
<td><a title="jQuery 效果 - stop() 方法" href="/jquery/effect_stop.asp">stop()</a></td>
<td>停止在被选元素上运行动画</td>
</tr>

<tr>
<td><a title="jQuery 效果 - toggle() 方法" href="/jquery/effect_toggle.asp">toggle()</a></td>
<td>对被选元素进行隐藏和显示的切换</td>
</tr>
</tbody></table>
</html>

### 文档操作方法
<html>
<table class="dataintable">
<tbody><tr>
<th style="width:30%;">方法</th>
<th>描述</th>
</tr>

<tr>
<td><a title="jQuery HTML - addClass() 方法" href="/jquery/attributes_addclass.asp">addClass()</a></td>
<td>向匹配的元素添加指定的类名。</td>
</tr>

<tr>
<td><a title="jQuery HTML - after() 方法" href="/jquery/manipulation_after.asp">after()</a></td>
<td>在匹配的元素之后插入内容。</td>
</tr>

<tr>
<td><a title="jQuery HTML - append() 方法" href="/jquery/manipulation_append.asp">append()</a></td>
<td>向匹配元素集合中的每个元素结尾插入由参数指定的内容。</td>
</tr>

<tr>
<td><a title="jQuery HTML - appendTo() 方法" href="/jquery/manipulation_appendto.asp">appendTo()</a></td>
<td>向目标结尾插入匹配元素集合中的每个元素。</td>
</tr>

<tr>
<td><a title="jQuery HTML - attr() 方法" href="/jquery/attributes_attr.asp">attr()</a></td>
<td>设置或返回匹配元素的属性和值。</td>
</tr>

<tr>
<td><a title="jQuery HTML - before() 方法" href="/jquery/manipulation_before.asp">before()</a></td>
<td>在每个匹配的元素之前插入内容。</td>
</tr>

<tr>
<td><a title="jQuery HTML - clone() 方法" href="/jquery/manipulation_clone.asp">clone()</a></td>
<td>创建匹配元素集合的副本。</td>
</tr>

<tr>
<td><a title="jQuery HTML - detach() 方法" href="/jquery/manipulation_detach.asp">detach()</a></td>
<td>从 DOM 中移除匹配元素集合。</td>
</tr>

<tr>
<td><a title="jQuery HTML - empty() 方法" href="/jquery/manipulation_empty.asp">empty()</a></td>
<td>删除匹配的元素集合中所有的子节点。</td>
</tr>

<tr>
<td><a title="jQuery HTML - hasClass() 方法" href="/jquery/attributes_hasclass.asp">hasClass()</a></td>
<td>检查匹配的元素是否拥有指定的类。</td>
</tr>

<tr>
<td><a title="jQuery HTML - html() 方法" href="/jquery/manipulation_html.asp">html()</a></td>
<td>设置或返回匹配的元素集合中的 HTML 内容。</td>
</tr>

<tr>
<td><a title="jQuery HTML - insertAfter() 方法" href="/jquery/manipulation_insertafter.asp">insertAfter()</a></td>
<td>把匹配的元素插入到另一个指定的元素集合的后面。</td>
</tr>

<tr>
<td><a title="jQuery HTML - insertBefore() 方法" href="/jquery/manipulation_insertbefore.asp">insertBefore()</a></td>
<td>把匹配的元素插入到另一个指定的元素集合的前面。</td>
</tr>

<tr>
<td><a title="jQuery HTML - prepend() 方法" href="/jquery/manipulation_prepend.asp">prepend()</a></td>
<td>向匹配元素集合中的每个元素开头插入由参数指定的内容。</td>
</tr>

<tr>
<td><a title="jQuery HTML - prependTo() 方法" href="/jquery/manipulation_perpendto.asp">prependTo()</a></td>
<td>向目标开头插入匹配元素集合中的每个元素。</td>
</tr>

<tr>
<td><a title="jQuery HTML - remove() 方法" href="/jquery/manipulation_remove.asp">remove()</a></td>
<td>移除所有匹配的元素。</td>
</tr>

<tr>
<td><a title="jQuery HTML - removeAttr() 方法" href="/jquery/attributes_removeattr.asp">removeAttr()</a></td>
<td>从所有匹配的元素中移除指定的属性。</td>
</tr>

<tr>
<td><a title="jQuery HTML - removeClass() 方法" href="/jquery/attributes_removeclass.asp">removeClass()</a></td>
<td>从所有匹配的元素中删除全部或者指定的类。</td>
</tr>

<tr>
<td><a title="jQuery HTML - replaceAll() 方法" href="/jquery/manipulation_replaceall.asp">replaceAll()</a></td>
<td>用匹配的元素替换所有匹配到的元素。</td>
</tr>

<tr>
<td><a title="jQuery HTML - replaceWith() 方法" href="/jquery/manipulation_replacewith.asp">replaceWith()</a></td>
<td>用新内容替换匹配的元素。</td>
</tr>

<tr>
<td><a title="jQuery HTML - text() 方法" href="/jquery/manipulation_text.asp">text()</a></td>
<td>设置或返回匹配元素的内容。</td>
</tr>

<tr>
<td><a title="jQuery HTML - toggleClass() 方法" href="/jquery/attributes_toggleclass.asp">toggleClass()</a></td>
<td>从匹配的元素中添加或删除一个类。</td>
</tr>

<tr>
<td><a title="jQuery HTML - unwrap() 方法" href="/jquery/manipulation_unwrap.asp">unwrap()</a></td>
<td>移除并替换指定元素的父元素。</td>
</tr>

<tr>
<td><a title="jQuery HTML - val() 方法" href="/jquery/attributes_val.asp">val()</a></td>
<td>设置或返回匹配元素的值。</td>
</tr>

<tr>
<td><a title="jQuery HTML - wrap() 方法" href="/jquery/manipulation_wrap.asp">wrap()</a></td>
<td>把匹配的元素用指定的内容或元素包裹起来。</td>
</tr>

<tr>
<td><a title="jQuery HTML - wrapAll() 方法" href="/jquery/manipulation_wrapall.asp">wrapAll()</a></td>
<td>把所有匹配的元素用指定的内容或元素包裹起来。</td>
</tr>

<tr>
<td><a title="jQuery HTML - wrapinner() 方法" href="/jquery/manipulation_wrapinner.asp">wrapinner()</a></td>
<td>将每一个匹配的元素的子内容用指定的内容或元素包裹起来。</td>
</tr>
</tbody></table>
</html>

### 属性操作
<html>
<table class="dataintable">
<tbody><tr>
<th>方法</th>
<th>描述</th>
</tr>

<tr>
<td><a title="jQuery HTML - addClass() 方法" href="/jquery/attributes_addclass.asp">addClass()</a></td>
<td>向匹配的元素添加指定的类名。</td>
</tr>

<tr>
<td><a title="jQuery HTML - attr() 方法" href="/jquery/attributes_attr.asp">attr()</a></td>
<td>设置或返回匹配元素的属性和值。</td>
</tr>

<tr>
<td><a title="jQuery HTML - hasClass() 方法" href="/jquery/attributes_hasclass.asp">hasClass()</a></td>
<td>检查匹配的元素是否拥有指定的类。</td>
</tr>

<tr>
<td><a title="jQuery HTML - html() 方法" href="/jquery/manipulation_html.asp">html()</a></td>
<td>设置或返回匹配的元素集合中的 HTML 内容。</td>
</tr>

<tr>
<td><a title="jQuery HTML - removeAttr() 方法" href="/jquery/attributes_removeattr.asp">removeAttr()</a></td>
<td>从所有匹配的元素中移除指定的属性。</td>
</tr>

<tr>
<td><a title="jQuery HTML - removeClass() 方法" href="/jquery/attributes_removeclass.asp">removeClass()</a></td>
<td>从所有匹配的元素中删除全部或者指定的类。</td>
</tr>

<tr>
<td><a title="jQuery HTML - toggleClass() 方法" href="/jquery/attributes_toggleclass.asp">toggleClass()</a></td>
<td>从匹配的元素中添加或删除一个类。</td>
</tr>

<tr>
<td><a title="jQuery HTML - val() 方法" href="/jquery/attributes_val.asp">val()</a></td>
<td>设置或返回匹配元素的值。</td>
</tr>

</tbody></table>
</html>

### CSS操作
<html>
<table class="dataintable">
<tbody><tr>
<th>CSS 属性</th>
<th>描述</th>
</tr>

<tr>
<td><a title="jQuery CSS 操作 - css() 方法" href="/jquery/css_css.asp">css()</a></td>
<td>设置或返回匹配元素的样式属性。</td>
</tr>

<tr>
<td><a title="jQuery CSS 操作 - height() 方法" href="/jquery/css_height.asp">height()</a></td>
<td>设置或返回匹配元素的高度。</td>
</tr>

<tr>
<td><a title="jQuery CSS 操作 - offset() 方法" href="/jquery/css_offset.asp">offset()</a></td>
<td>返回第一个匹配元素相对于文档的位置。</td>
</tr>

<tr>
<td><a title="jQuery CSS 操作 - offsetParent() 方法" href="/jquery/css_offsetparent.asp">offsetParent()</a></td>
<td>返回最近的定位祖先元素。</td>
</tr>

<tr>
<td><a title="jQuery CSS 操作 - position() 方法" href="/jquery/css_position.asp">position()</a></td>
<td>返回第一个匹配元素相对于父元素的位置。</td>
</tr>

<tr>
<td><a title="jQuery CSS 操作 - scrollLeft() 方法" href="/jquery/css_scrollleft.asp">scrollLeft()</a></td>
<td>设置或返回匹配元素相对滚动条左侧的偏移。</td>
</tr>

<tr>
<td><a title="jQuery CSS 操作 - scrollTop() 方法" href="/jquery/css_scrolltop.asp">scrollTop()</a></td>
<td>设置或返回匹配元素相对滚动条顶部的偏移。</td>
</tr>

<tr>
<td><a title="jQuery CSS 操作 - width() 方法" href="/jquery/css_width.asp">width()</a></td>
<td>设置或返回匹配元素的宽度。</td>
</tr>

</tbody></table>
</html>

### Ajax
<html>
<table class="dataintable">
<tbody><tr>
<th>函数</th>
<th>描述</th>
</tr>

<tr>
<td><a title="jQuery ajax - ajax() 方法" href="/jquery/ajax_ajax.asp">jQuery.ajax()</a></td>
<td>执行异步 HTTP (Ajax) 请求。</td>
</tr>

<tr>
<td><a title="jQuery ajax - ajaxComplete() 方法" href="/jquery/ajax_ajaxcomplete.asp">.ajaxComplete()</a></td>
<td>当 Ajax 请求完成时注册要调用的处理程序。这是一个 Ajax 事件。</td>
</tr>

<tr>
<td><a title="jQuery ajax - ajaxError() 方法" href="/jquery/ajax_ajaxerror.asp">.ajaxError()</a></td>
<td>当 Ajax 请求完成且出现错误时注册要调用的处理程序。这是一个 Ajax 事件。</td>
</tr>

<tr>
<td><a title="jQuery ajax - ajaxSend() 方法" href="/jquery/ajax_ajaxsend.asp">.ajaxSend()</a></td>
<td>在 Ajax 请求发送之前显示一条消息。</td>
</tr>

<tr>
<td><a title="jQuery ajax - ajaxSetup() 方法" href="/jquery/ajax_ajaxsetup.asp">jQuery.ajaxSetup()</a></td>
<td>设置将来的 Ajax 请求的默认值。</td>
</tr>

<tr>
<td><a title="jQuery ajax - ajaxStart() 方法" href="/jquery/ajax_ajaxstart.asp">.ajaxStart()</a></td>
<td>当首个 Ajax 请求完成开始时注册要调用的处理程序。这是一个 Ajax 事件。</td>
</tr>

<tr>
<td><a title="jQuery ajax - ajaxStop() 方法" href="/jquery/ajax_ajaxstop.asp">.ajaxStop()</a></td>
<td>当所有 Ajax 请求完成时注册要调用的处理程序。这是一个 Ajax 事件。</td>
</tr>

<tr>
<td><a title="jQuery ajax - ajaxSuccess() 方法" href="/jquery/ajax_ajaxsuccess.asp">.ajaxSuccess()</a></td>
<td>当 Ajax 请求成功完成时显示一条消息。</td>
</tr>

<tr>
<td><a title="jQuery ajax - get() 方法" href="/jquery/ajax_get.asp">jQuery.get()</a></td>
<td>使用 HTTP GET 请求从服务器加载数据。</td>
</tr>

<tr>
<td><a title="jQuery ajax - getJSON() 方法" href="/jquery/ajax_getjson.asp">jQuery.getJSON()</a></td>
<td>使用 HTTP GET 请求从服务器加载 JSON 编码数据。</td>
</tr>

<tr>
<td><a title="jQuery ajax - getScript() 方法" href="/jquery/ajax_getscript.asp">jQuery.getScript()</a></td>
<td>使用 HTTP GET 请求从服务器加载 JavaScript 文件，然后执行该文件。</td>
</tr>

<tr>
<td><a title="jQuery ajax - load() 方法" href="/jquery/ajax_load.asp">.load()</a></td>
<td>从服务器加载数据，然后把返回到 HTML 放入匹配元素。</td>
</tr>

<tr>
<td><a title="jQuery ajax - param() 方法" href="/jquery/ajax_param.asp">jQuery.param()</a></td>
<td>创建数组或对象的序列化表示，适合在 URL 查询字符串或 Ajax 请求中使用。</td>
</tr>

<tr>
<td><a title="jQuery ajax - post() 方法" href="/jquery/ajax_post.asp">jQuery.post()</a></td>
<td>使用 HTTP POST 请求从服务器加载数据。</td>
</tr>

<tr>
<td><a title="jQuery ajax - serialize() 方法" href="/jquery/ajax_serialize.asp">.serialize()</a></td>
<td>将表单内容序列化为字符串。</td>
</tr>

<tr>
<td><a title="jQuery ajax - serializeArray() 方法" href="/jquery/ajax_serializearray.asp">.serializeArray()</a></td>
<td>序列化表单元素，返回 JSON 数据结构数据。</td>
</tr>
</tbody></table>
</html>

### 遍历
<html>
<table class="dataintable">
<tbody><tr>
<th style="width:22%">函数</th>
<th>描述</th>
</tr>

<tr>
<td><a title="jQuery 遍历 - add() 方法" href="/jquery/traversing_add.asp">.add()</a></td>
<td>将元素添加到匹配元素的集合中。</td>
</tr>

<tr>
<td><a title="jQuery 遍历 - andSelf() 方法" href="/jquery/traversing_andSelf.asp">.andSelf()</a></td>
<td>把堆栈中之前的元素集添加到当前集合中。</td>
</tr>

<tr>
<td><a title="jQuery 遍历 - children() 方法" href="/jquery/traversing_children.asp">.children()</a></td>
<td>获得匹配元素集合中每个元素的所有子元素。</td>
</tr>

<tr>
<td><a title="jQuery 遍历 - closest() 方法" href="/jquery/traversing_closest.asp">.closest()</a></td>
<td>从元素本身开始，逐级向上级元素匹配，并返回最先匹配的祖先元素。</td>
</tr>

<tr>
<td><a title="jQuery 遍历 - contents() 方法" href="/jquery/traversing_contents.asp">.contents()</a></td>
<td>获得匹配元素集合中每个元素的子元素，包括文本和注释节点。</td>
</tr>

<tr>
<td><a title="jQuery 遍历 - each() 方法" href="/jquery/traversing_each.asp">.each()</a></td>
<td>对 jQuery 对象进行迭代，为每个匹配元素执行函数。</td>
</tr>

<tr>
<td><a title="jQuery 遍历 - end() 方法" href="/jquery/traversing_end.asp">.end()</a></td>
<td>结束当前链中最近的一次筛选操作，并将匹配元素集合返回到前一次的状态。</td>
</tr>

<tr>
<td><a title="jQuery 遍历 - eq() 方法" href="/jquery/traversing_eq.asp">.eq()</a></td>
<td>将匹配元素集合缩减为位于指定索引的新元素。</td>
</tr>

<tr>
<td><a title="jQuery 遍历 - filter() 方法" href="/jquery/traversing_filter.asp">.filter()</a></td>
<td>将匹配元素集合缩减为匹配选择器或匹配函数返回值的新元素。</td>
</tr>

<tr>
<td><a title="jQuery 遍历 - find() 方法" href="/jquery/traversing_find.asp">.find()</a></td>
<td>获得当前匹配元素集合中每个元素的后代，由选择器进行筛选。</td>
</tr>

<tr>
<td><a title="jQuery 遍历 - first() 方法" href="/jquery/traversing_first.asp">.first()</a></td>
<td>将匹配元素集合缩减为集合中的第一个元素。</td>
</tr>

<tr>
<td><a title="jQuery 遍历 - has() 方法" href="/jquery/traversing_has.asp">.has()</a></td>
<td>将匹配元素集合缩减为包含特定元素的后代的集合。</td>
</tr>

<tr>
<td><a title="jQuery 遍历 - is() 方法" href="/jquery/traversing_is.asp">.is()</a></td>
<td>根据选择器检查当前匹配元素集合，如果存在至少一个匹配元素，则返回 true。</td>
</tr>

<tr>
<td><a title="jQuery 遍历 - last() 方法" href="/jquery/traversing_last.asp">.last()</a></td>
<td>将匹配元素集合缩减为集合中的最后一个元素。</td>
</tr>

<tr>
<td><a title="jQuery 遍历 - map() 方法" href="/jquery/traversing_map.asp">.map()</a></td>
<td>把当前匹配集合中的每个元素传递给函数，产生包含返回值的新 jQuery 对象。</td>
</tr>

<tr>
<td><a title="jQuery 遍历 - next() 方法" href="/jquery/traversing_next.asp">.next()</a></td>
<td>获得匹配元素集合中每个元素紧邻的同辈元素。</td>
</tr>

<tr>
<td><a title="jQuery 遍历 - nextAll() 方法" href="/jquery/traversing_nextall.asp">.nextAll()</a></td>
<td>获得匹配元素集合中每个元素之后的所有同辈元素，由选择器进行筛选（可选）。</td>
</tr>

<tr>
<td><a title="jQuery 遍历 - nextUntil() 方法" href="/jquery/traversing_nextuntil.asp">.nextUntil()</a></td>
<td>获得每个元素之后所有的同辈元素，直到遇到匹配选择器的元素为止。</td>
</tr>

<tr>
<td><a title="jQuery 遍历 - not() 方法" href="/jquery/traversing_not.asp">.not()</a></td>
<td>从匹配元素集合中删除元素。</td>
</tr>

<tr>
<td><a title="jQuery 遍历 - offsetParent() 方法" href="/jquery/traversing_offsetparent.asp">.offsetParent()</a></td>
<td>获得用于定位的第一个父元素。</td>
</tr>

<tr>
<td><a title="jQuery 遍历 - parent() 方法" href="/jquery/traversing_parent.asp">.parent()</a></td>
<td>获得当前匹配元素集合中每个元素的父元素，由选择器筛选（可选）。</td>
</tr>

<tr>
<td><a title="jQuery 遍历 - parents() 方法" href="/jquery/traversing_parents.asp">.parents()</a></td>
<td>获得当前匹配元素集合中每个元素的祖先元素，由选择器筛选（可选）。</td>
</tr>

<tr>
<td><a title="jQuery 遍历 - parentsUntil() 方法" href="/jquery/traversing_parentsuntil.asp">.parentsUntil()</a></td>
<td>获得当前匹配元素集合中每个元素的祖先元素，直到遇到匹配选择器的元素为止。</td>
</tr>

<tr>
<td><a title="jQuery 遍历 - prev() 方法" href="/jquery/traversing_prev.asp">.prev()</a></td>
<td>获得匹配元素集合中每个元素紧邻的前一个同辈元素，由选择器筛选（可选）。</td>
</tr>

<tr>
<td><a title="jQuery 遍历 - prevAll() 方法" href="/jquery/traversing_prevall.asp">.prevAll()</a></td>
<td>获得匹配元素集合中每个元素之前的所有同辈元素，由选择器进行筛选（可选）。</td>
</tr>

<tr>
<td><a title="jQuery 遍历 - prevUntil() 方法" href="/jquery/traversing_prevuntil.asp">.prevUntil()</a></td>
<td>获得每个元素之前所有的同辈元素，直到遇到匹配选择器的元素为止。</td>
</tr>

<tr>
<td><a title="jQuery 遍历 - siblings() 方法" href="/jquery/traversing_siblings.asp">.siblings()</a></td>
<td>获得匹配元素集合中所有元素的同辈元素，由选择器筛选（可选）。</td>
</tr>

<tr>
<td><a title="jQuery 遍历 - slice() 方法" href="/jquery/traversing_slice.asp">.slice()</a></td>
<td>将匹配元素集合缩减为指定范围的子集。</td>
</tr>
</tbody></table>
</html>

### 数据操作
<html>
<table class="dataintable">
<tbody><tr>
<th>函数</th>
<th>描述</th>
</tr>

<tr>
<td><a title="jQuery 数据 - clearQueue() 方法" href="/jquery/data_clearqueue.asp">.clearQueue()</a></td>
<td>从队列中删除所有未运行的项目。</td>
</tr>

<tr>
<td><a title="jQuery 数据 - data() 方法" href="/jquery/data_data.asp">.data()</a></td>
<td>存储与匹配元素相关的任意数据。</td>
</tr>

<tr>
<td><a title="jQuery 数据 - jQuery.data() 方法" href="/jquery/data_jquery_data.asp">jQuery.data()</a></td>
<td>存储与指定元素相关的任意数据。</td>
</tr>

<tr>
<td><a title="jQuery 数据 - dequeue() 方法" href="/jquery/data_dequeue.asp">.dequeue()</a></td>
<td>从队列最前端移除一个队列函数，并执行它。</td>
</tr>

<tr>
<td><a title="jQuery 数据 - jQuery.dequeue() 方法" href="/jquery/data_jquery_dequeue.asp">jQuery.dequeue()</a></td>
<td>从队列最前端移除一个队列函数，并执行它。</td>
</tr>

<tr>
<td><a title="jQuery 数据 - jQuery.hasData() 方法" href="/jquery/data_hasdata.asp">jQuery.hasData()</a></td>
<td>存储与匹配元素相关的任意数据。</td>
</tr>

<tr>
<td><a title="jQuery 数据 - queue() 方法" href="/jquery/data_queue.asp">.queue()</a></td>
<td>显示或操作匹配元素所执行函数的队列。</td>
</tr>

<tr>
<td><a title="jQuery 数据 - jQuery.queue() 方法" href="/jquery/data_jquery_queue.asp">jQuery.queue()</a></td>
<td>显示或操作匹配元素所执行函数的队列。</td>
</tr>

<tr>
<td><a title="jQuery 数据 - removeData() 方法" href="/jquery/data_removedata.asp">.removeData()</a></td>
<td>移除之前存放的数据。</td>
</tr>

<tr>
<td><a title="jQuery 数据 - jQuery.removeData() 方法" href="/jquery/data_jquery_removedata.asp">jQuery.removeData()</a></td>
<td>移除之前存放的数据。</td>
</tr>

</tbody></table>
</html>

### DOM元素
<html>
<table class="dataintable">
<tbody><tr>
<th>函数</th>
<th>描述</th>
</tr>

<tr>
<td><a title="jQuery DOM 元素方法 - get() 方法" href="/jquery/dom_element_methods_get.asp">.get()</a></td>
<td>获得由选择器指定的 DOM 元素。</td>
</tr>

<tr>
<td><a title="jQuery DOM 元素方法 - index() 方法" href="/jquery/dom_element_methods_index.asp">.index()</a></td>
<td>返回指定元素相对于其他指定元素的 index 位置。</td>
</tr>

<tr>
<td><a title="jQuery DOM 元素方法 - size() 方法" href="/jquery/dom_element_methods_size.asp">.size()</a></td>
<td>返回被 jQuery 选择器匹配的元素的数量。</td>
</tr>

<tr>
<td><a title="jQuery DOM 元素方法 - toArray() 方法" href="/jquery/dom_element_methods_toarray.asp">.toArray()</a></td>
<td>以数组的形式返回 jQuery 选择器匹配的元素。</td>
</tr>

</tbody></table>
</html>

### 核心
<html>
<table class="dataintable">
<tbody><tr>
<th>函数</th>
<th>描述</th>
</tr>

<tr>
<td><a title="jQuery jQuery() 方法" href="core_jquery.asp">jQuery()</a></td>
<td>接受一个字符串，其中包含了用于匹配元素集合的 CSS 选择器。</td>
</tr>

<tr>
<td><a title="jQuery noConflict() 方法" href="core_noconflict.asp">jQuery.noConflict()</a></td>
<td>运行这个函数将变量 $ 的控制权让渡给第一个实现它的那个库。</td>
</tr>
</tbody></table>
</html>

### 属性
<html>
<table class="dataintable">
<tbody><tr>
<th>属性</th>
<th>描述</th>
</tr>

<tr>
<td><a title="jQuery CSS 操作 - css() 方法" href="/jquery/prop_context.asp">context</a></td>
<td>在版本 1.10 中被弃用。包含传递给 jQuery() 的原始上下文。</td>
</tr>

<tr>
<td><a title="jQuery CSS 操作 - height() 方法" href="/jquery/prop_jquery.asp">jquery</a></td>
<td>包含 jQuery 版本号。</td>
</tr>

<tr>
<td><a title="jQuery CSS 操作 - offset() 方法" href="/jquery/prop_jquery_fx_interval.asp">jQuery.fx.interval</a></td>
<td>改变以毫秒计的动画速率。</td>
</tr>

<tr>
<td><a title="jQuery CSS 操作 - offsetParent() 方法" href="/jquery/prop_jquery_fx_off.asp">jQuery.fx.off</a></td>
<td>全局禁用/启用所有动画。</td>
</tr>

<tr>
<td><a title="jQuery CSS 操作 - position() 方法" href="/jquery/prop_jquery_support.asp">jQuery.support</a></td>
<td>表示不同浏览器特性或漏洞的属性集合（用于 jQuery 内部使用）。</td>
</tr>

<tr>
<td><a title="jQuery CSS 操作 - scrollLeft() 方法" href="/jquery/prop_length.asp">length</a></td>
<td>包含 jQuery 对象中的元素数目。</td>
</tr>

</tbody></table>
</html>


