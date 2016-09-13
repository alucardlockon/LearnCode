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
 
### demo04 定义组件
`React.createClass()`定义一个组件。定义后可以像使用html标签一样使用它。 
组件名称需要首字母大写，并且一个组件只应该由一个顶级节点。 
```javascript
var HelloMessage = React.createClass({
  render: function() {
    return <h1>Hello {this.props.name}</h1>;
  }
});
 
ReactDOM.render(
  <HelloMessage name="John" />,
  document.getElementById('example')
);
```
 
### demo05  this.props.children
React使用`this.props.children`来访问组件的子节点。 
```javascript
var NotesList = React.createClass({
  render: function() {
    return (
      <ol>
      {
        React.Children.map(this.props.children, function (child) {
          return <li>{child}</li>;
        })
      }
      </ol>
    );
  }
});
 
ReactDOM.render(
  <NotesList>
    <span>hello</span>
    <span>world</span>
  </NotesList>,
  document.getElementById('example')
);
```
 
### demo06 PropTypes
 
```javascript
var data = 123;
 
var MyTitle = React.createClass({
  propTypes: {
    title: React.PropTypes.string.isRequired,
  },
 
  render: function() {
    return <h1> {this.props.title} </h1>;
  }
});
 
ReactDOM.render(
  <MyTitle title={data} />,
  document.getElementById('example')
);
```
给默认值赋值:`getDefaultProps()`    
```javascript
var MyTitle = React.createClass({
  getDefaultProps : function () {
    return {
      title : 'Hello World'
    };
  },

  render: function() {
     return <h1> {this.props.title} </h1>;
   }
});

ReactDOM.render(
  <MyTitle />,
  document.getElementById('example')
);
```

### demo07 查找dom节点
使用`ref`属性来找到dom节点  
```javascript
var MyComponent = React.createClass({
  handleClick: function() {
    this.refs.myTextInput.focus();
  },
  render: function() {
    return (
      <div>
        <input type="text" ref="myTextInput" />
        <input type="button" value="Focus the text input" onClick={this.handleClick} />
      </div>
    );
  }
});

ReactDOM.render(
  <MyComponent />,
  document.getElementById('example')
);
```

### demo08 this.state
react把组件作为一个状态机,`getInitialState()`用来初始化`this.state`,`this.setState()`来更新`this.state()`状态来重新渲染这个组件。  
```javascript
var LikeButton = React.createClass({
  getInitialState: function() {
    return {liked: false};
  },
  handleClick: function(event) {
    this.setState({liked: !this.state.liked});
  },
  render: function() {
    var text = this.state.liked ? 'like' : 'haven\'t liked';
    return (
      <p onClick={this.handleClick}>
        You {text} this. Click to toggle.
      </p>
    );
  }
});

ReactDOM.render(
  <LikeButton />,
  document.getElementById('example')
);
```

### demo09 Form
`event.target`来访问event的目标  
```javascript
var Input = React.createClass({
  getInitialState: function() {
    return {value: 'Hello!'};
  },
  handleChange: function(event) {
    this.setState({value: event.target.value});
  },
  render: function () {
    var value = this.state.value;
    return (
      <div>
        <input type="text" value={value} onChange={this.handleChange} />
        <p>{value}</p>
      </div>
    );
  }
});

ReactDOM.render(<Input/>, document.getElementById('example'));
```

### demo10 组件生命周期  
组件的生命周期:Mounting(插入Dom中),Updating(被重新渲染),Unmounting(从Dom中被移除)  
react提供生命周期的hook，`will`方法在事件发生前调用,`did`方法在事件发生后调用。 
```javascript
var Hello = React.createClass({
  getInitialState: function () {
    return {
      opacity: 1.0
    };
  },

  componentDidMount: function () {
    this.timer = setInterval(function () {
      var opacity = this.state.opacity;
      opacity -= .05;
      if (opacity < 0.1) {
        opacity = 1.0;
      }
      this.setState({
        opacity: opacity
      });
    }.bind(this), 100);
  },

  render: function () {
    return (
      <div style={{opacity: this.state.opacity}}>
        Hello {this.props.name}
      </div>
    );
  }
});

ReactDOM.render(
  <Hello name="world"/>,
  document.getElementById('example')
);
```

### demo11 ajax
```jsx
var UserGist = React.createClass({
  getInitialState: function() {
    return {
      username: '',
      lastGistUrl: ''
    };
  },

  componentDidMount: function() {
    $.get(this.props.source, function(result) {
      var lastGist = result[0];
      if (this.isMounted()) {
        this.setState({
          username: lastGist.owner.login,
          lastGistUrl: lastGist.html_url
        });
      }
    }.bind(this));
  },

  render: function() {
    return (
      <div>
        {this.state.username}'s last gist is
        <a href={this.state.lastGistUrl}>here</a>.
      </div>
    );
  }
});

ReactDOM.render(
  <UserGist source="https://api.github.com/users/octocat/gists" />,
  document.getElementById('example')
);
```

### demo12 显示Promise object的值
```javascript
ReactDOM.render(
  <RepoList
    promise={$.getJSON('https://api.github.com/search/repositories?q=javascript&sort=stars')}
  />,
  document.getElementById('example')
);
```

### demo13 服务端渲染
运行方式:  
```
# install the dependencies in demo13 directory
$ npm install

# translate all jsx file in src subdirectory to js file
$ npm run build

# launch http server
$ node server.js
```

### JSX预编译成js
先安装babel  
```
$ npm install -g babel
```
然后重新编译jsx为js  
```
$ babel src --out-dir build
```
将编译好的js文件放入html  
```html
<!DOCTYPE html>
<html>
  <head>
    <title>Hello React!</title>
    <script src="build/react.js"></script>
    <script src="build/react-dom.js"></script>
    <!-- No need for Browser.js! -->
  </head>
  <body>
    <div id="example"></div>
    <script src="build/helloworld.js"></script>
  </body>
</html>
```


