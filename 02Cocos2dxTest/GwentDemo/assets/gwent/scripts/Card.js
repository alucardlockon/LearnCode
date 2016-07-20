cc.Class({
    extends: cc.Component,

    properties: {
        //basic
        str:0,
        cardtype:'closeCombat',
        cardname:'monster',
        cardintro:"this is test1 message",
        cardeffect:[],
        cardTexture:null,
        //props
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
            },
            onMouseUp: function (event) {
                self.dragFlag=false;
            },
            onMouseMove: function (event) {
                if(self.dragFlag==true){
                    //self.node.setPosition(event.getLocation());
                    self.node.setPosition(self.node.parent.convertToNodeSpaceAR(event.getLocation()));;
                }
            }
        }

        cc.eventManager.addListener(listener, self.node);

        this.node.on('mousedown', function (event) {
          cc.log(self.cardintro);
          self.dragFlag=true;
          var cardinfo=cc.find("Canvas/UI/CardInfo");
          cardinfo.getComponent(cc.Label).string=self.cardintro+'A';
        }, this);
    },

    // called every frame, uncomment this function to activate update callback
    update: function (dt) {

    }
});
