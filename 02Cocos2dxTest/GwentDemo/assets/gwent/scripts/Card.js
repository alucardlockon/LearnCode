cc.Class({
    extends: cc.Component,

    properties: {
        dragpos:null,
        dragFlag:false
    },

    // use this for initialization
    onLoad: function () {
        var self = this;
        var pos = self.node.getPosition();
        var listener = {
            event: cc.EventListener.MOUSE,
            onMouseDown: function (event) {
                cc.log('Mouse Down: ' + event);
                self.dragFlag=true;
            },
            onMouseUp: function (event) {
                cc.log('Mouse Up: ' + event);
                if(self.dragFlag){
                    var seq = cc.sequence(cc.moveTo(0.5, event.getLocation().x,event.getLocation().y));
                    self.node.runAction(seq);
                }
                self.dragFlag=false;
            },
            onMouseMove: function (event) {
               cc.log('Mouse Move: ' + event);
            },
            onMouseScroll: function (event) {
               cc.log('Mouse Scroll: ' + event);
            }
        }
        
        cc.eventManager.addListener(listener, self.node);
        
    },

    // called every frame, uncomment this function to activate update callback
    update: function (dt) {
        
    }
});
