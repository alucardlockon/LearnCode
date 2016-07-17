cc.Class({
    extends: cc.Component,
    
    properties: {
        label: {
            default: null,
            type: cc.Label
        },
        text: 'Hello, World!'
    },

    // use this for initialization
    onLoad: function () {
        this.label.string = this.text;
        this.label.string = "every day young life junes!";
        // 添加键盘事件监听器
        var listener = {
            event: cc.EventListener.KEYBOARD,
            onKeyPressed: function (keyCode, event) {
                cc.log('keyDown: ' + keyCode);
            },
            onKeyReleased: function (keyCode, event) {
                cc.log('keyUp: ' + keyCode);
            }
        }
        // 绑定键盘事件
        cc.eventManager.addListener(listener, this.node);
    },
    
    // called every frame
    update: function (dt) {
        
        

        
    },
});
