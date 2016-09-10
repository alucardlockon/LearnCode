https://github.com/ruanyf/react-demos  
### 引入
```html
<script src="../build/react.js"></script>
<script src="../build/react-dom.js"></script>
<script src="../build/browser.min.js"></script>
```

### demo01 渲染JSX
输出hello,world,注意type为:text/babel  
ReactDOM.render()方法将JSX转换为HTML  
```html
<script type="text/babel">
  ReactDOM.render(
    <h1>Hello, world!</h1>,
    document.getElementById('example')
  );
</script>  
```

### demo02 在JSX中使用javascript
```html
<script type="text/babel">
  var names = ['Alice', 'Emily', 'Kate'];

  ReactDOM.render(
    <div>
    {
      names.map(function (name) {
        return <div>Hello, {name}!</div>
      })
    }
    </div>,
    document.getElementById('example')
  );
</script>
```

### demo03 在JSX中使用数组
```html
<script type="text/babel">
  var arr = [
    <h1>Hello world!</h1>,
    <h2>React is awesome</h2>,
  ];
  ReactDOM.render(
    <div>{arr}</div>,
    document.getElementById('example')
  );
</script>
```


