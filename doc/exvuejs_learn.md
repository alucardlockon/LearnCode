# Vue.js

http://cn.vuejs.org/guide/index.html  

Vue.js（读音 /vjuː/, 类似于 view）是一个构建数据驱动的 web 界面的库。Vue.js 的目标是通过尽可能简单的 API 实现响应的数据绑定和组合的视图组件。  
Vue.js 自身不是一个全能框架——它只聚焦于视图层。因此它非常容易学习，非常容易与其它库或已有项目整合。另一方面，在与相关工具和支持库一起使用时，Vue.js 也能完美地驱动复杂的单页应用。  

### 安装
```
# 最新稳定版本
$ npm install vue
# 最新稳定 CSP 兼容版本
$ npm install vue@csp

# 最新稳定版本
$ bower install vue
```

### 命令行工具
Vue.js 提供一个官方命令行工具，可用于快速搭建大型单页应用。该工具提供开箱即用的构建工具配置，带来现代化的前端开发流程。只需一分钟即可启动带热重载、保存时静态检查以及可用于生产环境的构建配置的项目：  
```
# 全局安装 vue-cli
$ npm install -g vue-cli
# 创建一个基于 "webpack" 模板的新项目
$ vue init webpack my-project
# 安装依赖，走你
$ cd my-project
$ npm install
$ npm run dev
```

### 上手示例
```html
<!-- 这是我们的 View -->
<div id="example-1">
  Hello {{ name }}!
</div>
```
```js
// 这是我们的 Model
var exampleData = {
  name: 'Vue.js'
}

// 创建一个 Vue 实例或 "ViewModel"
// 它连接 View 与 Model
var exampleVM = new Vue({
  el: '#example-1',
  data: exampleData
})
```


#### Hello world
```html
<div id="app">
  {{ message }}
</div>
```
```js
new Vue({
  el: '#app',
  data: {
    message: 'Hello Vue.js!'
  }
})
```

#### 双向绑定
```html
<div id="app">
  <p>{{ message }}</p>
  <input v-model="message">
</div>
```
```js
new Vue({
  el: '#app',
  data: {
    message: 'Hello Vue.js!'
  }
})
```

#### 渲染列表
```html
<div id="app">
  <ul>
    <li v-for="todo in todos">
      {{ todo.text }}
    </li>
  </ul>
</div>
```
```js
new Vue({
  el: '#app',
  data: {
    todos: [
      { text: 'Learn JavaScript' },
      { text: 'Learn Vue.js' },
      { text: 'Build Something Awesome' }
    ]
  }
})
```

#### 处理用户输入
```html
<div id="app">
  <p>{{ message }}</p>
  <button v-on:click="reverseMessage">Reverse Message</button>
</div>
```
```js
new Vue({
  el: '#app',
  data: {
    message: 'Hello Vue.js!'
  },
  methods: {
    reverseMessage: function () {
      this.message = this.message.split('').reverse().join('')
    }
  }
})
```

#### 综合
```html
<div id="app">
  <input v-model="newTodo" v-on:keyup.enter="addTodo">
  <ul>
    <li v-for="todo in todos">
      <span>{{ todo.text }}</span>
      <button v-on:click="removeTodo($index)">X</button>
    </li>
  </ul>
</div>
```
```js
new Vue({
  el: '#app',
  data: {
    newTodo: '',
    todos: [
      { text: 'Add some todos' }
    ]
  },
  methods: {
    addTodo: function () {
      var text = this.newTodo.trim()
      if (text) {
        this.todos.push({ text: text })
        this.newTodo = ''
      }
    },
    removeTodo: function (index) {
      this.todos.splice(index, 1)
    }
  }
})
```

### 指令
`v-if`(条件判断),`v-for`(显示数组元素),`v-bind`(绑定html特性)等。  
`.literal`修饰符告诉指令将它的值解析为一个字面字符串而不是一个表达式  

#### 缩写
```html
<!-- 完整语法 -->
<a v-bind:href="url"></a>
<!-- 缩写 -->
<a :href="url"></a>
<!-- 完整语法 -->
<button v-bind:disabled="someDynamicCondition">Button</button>
<!-- 缩写 -->
<button :disabled="someDynamicCondition">Button</button>


<!-- 完整语法 -->
<a v-on:click="doSomething"></a>
<!-- 缩写 -->
<a @click="doSomething"></a>
```

### 组件模板
```html
<div id="app">
  <app-nav></app-nav>
  <app-view>
    <app-sidebar></app-sidebar>
    <app-content></app-content>
  </app-view>
</div>
```




