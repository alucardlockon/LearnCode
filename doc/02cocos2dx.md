# Cocos2dx
 
[CocosCreator使用手册](http://cocos.com/docs/creator/index.html) 
### 加载模块
``` javascript
var Monster = require("Monster");
var monsterComp = monster.getComponent(Monster);
```
直接调用 
``` javascript
var cardUtils = cc.find('Canvas/Scripts').getComponent('CardUtils');
cardUtils.addCardToField();
```