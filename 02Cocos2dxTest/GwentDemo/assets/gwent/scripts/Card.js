cc.Class({
    extends: cc.Component,

    properties: {
        //basic
        str:0,
        cardtype:'CloseCombat',
        cardname:'monster',
        strength:0,
        cardintro:'this is test1 message',
        cardeffect:[],
        cardPicUrl:'gwent/resources/cards/110',
        cardBackPicUrl:'gwent/resources/cards/bg1',
        cardSF:cc.SpriteFrame,
        cardBackSF:cc.SpriteFrame,
        //props
        backOrFront:false,
        dragpos:null,
        dragFlag:false
    },

    // use this for initialization
    onLoad: function () {
        var self = this;
        cc.loader.loadRes(this.cardPicUrl, cc.SpriteFrame, function (err, spriteFrame) {
            //self.node.getComponent(cc.Sprite).spriteFrame  = spriteFrame;
            self.cardSF=spriteFrame;
            if(this.backOrFront){
              self.node.getComponent(cc.Sprite).spriteFrame  = spriteFrame;
            }
        });
        cc.loader.loadRes(this.cardBackPicUrl, cc.SpriteFrame, function (err, spriteFrame) {
            //self.node.getComponent(cc.Sprite).spriteFrame  = spriteFrame;
            self.cardBackSF=spriteFrame;
            if(!this.backOrFront){
              self.node.getComponent(cc.Sprite).spriteFrame  = spriteFrame;
            }
        });
        
        
        
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
          self.dragFlag=true;
        }, this);
        this.node.on('mouseenter', function (event) {
          self.setCardInfoLabel(true);
        }, this);
        this.node.on('mouseleave', function (event) {
          self.setCardInfoLabel(false);
        }, this);
    },

    // called every frame, uncomment this function to activate update callback
    update: function (dt) {

    },

    setCardInfoLabel:function(show){
        var cardinfo=cc.find("Canvas/UI/CardInfo");
        var cardpic=cc.find("Canvas/UI/CardPic");
        if(show){
          cardinfo.getComponent(cc.Label).string=this.cardname+
          "\n\n类型: "+this.cardtype+
          "\n\n力量: "+this.strength+
          "\n\n介绍: "+this.cardintro;
          if(this.backOrFront){
            cardpic.getComponent(cc.Sprite).spriteFrame=this.cardSF;
          }else{
            cardpic.getComponent(cc.Sprite).spriteFrame=this.cardBackSF;
          }
        }else{
          cardpic.getComponent(cc.Sprite).spriteFrame=null;
          cardinfo.getComponent(cc.Label).string="";
        }
    }
});
