# Python

### 定义变量
``` python
a=1 #整形 长整形
a=1.2,b=2E-10 #浮点
b='String',b=u"str" #字符串 ,unicode字符
c=[1,2] #列表
d=(‘a’,'c') #元组
e={"a":1,"b":2} #字典
```
### 定义方法
``` python
def a():
  #方法体
```
### if/while/for
``` python
#if
if a==1:
  print 1
elif a==2:
  print 2
else:
  print 3

#while
while 1:
  pass

#for 打印0-5
for i in range(0,6):
  print i
else
  pass
```
### 模块导入
``` python
import
from 模块 import 变量
```
### 列表
``` python
l=[1,2]
l.append(3) #添加元素
l.insert(1,3) #在位置1添加3
l.count(1) #count个数
l.index(2) #返回2出现的第一个的位置
l.pop(1) #删除(返回删除的值)
l.remove(1) #删除
l.extend([3,4]) #在列表l中添加列表[3,4]
l.reverse() #反转列表
```

### 元组和list转换
``` python
tuple(lis)
list(tem)
```

### 文件
``` python
f=open("","w") #w写,r读取,a追加
f.write("py大法好") #写文件
f.close()
```

### 异常
``` python
try:
  pass
except SomeException,e:
  print "wrong!"
except:
  print "wrong else!"
```
### Python运算符
**  幂 3**3
/   除
//  整除
%   取模
& |   按位与/或
^ ~   按位异或 5^3=6/翻转x的按位翻转-(x+1)
### Python库
#### sys 包含系统相关功能
sys.platform 平台类型  
sys.modules 载入的模块

### 其他语句
#### exec 'print "abc"'
exec语句用来执行储存在字符串或文件中的Python语句；eval语句用来计算存储在字符串中的有效Python表达式。  
#### assert a==true
assert语句用来断言某个条件是真的，并且在它非真的时候引发一个错误--AssertionError。
#### eval
eval语句用来计算存储在字符串中的有效Python表达式。  
#### lambda a:2+a*2
lambda语句被用来创建新的函数对象，并在运行时返回它们。lambda需要一个参数，后面仅跟单个表达式作为函数体，而表达式的值被这个新建的函数返回。 注意，即便是print语句也不能用在lambda形式中，只能使用表达式。
``` python
lam1=lambda a,b:a+b*b
print lam1(1,2)
```
