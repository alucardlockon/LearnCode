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
                self.dragFlag=true;
            },
            onMouseUp: function (event) {
                self.dragFlag=false;
            },
            onMouseMove: function (event) {
                if(self.dragFlag==true){
                    self.node.setPosition(event.getLocation());
                }
            }
        }
        
        cc.eventManager.addListener(listener, self.node);
        
    },

    // called every frame, uncomment this function to activate update callback
    update: function (dt) {
        
    }
});
