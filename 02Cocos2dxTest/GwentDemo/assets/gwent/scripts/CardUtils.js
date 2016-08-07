/**
这是一个Card的工具类
**/

cc.Class({
    extends: cc.Component,

    properties: {
        
    },
    
    //添加卡牌到场地
    addCardToField:function(playerNode,backOrFront){
        var self=this;
        // 加载 Prefab
        cc.loader.loadRes("gwent/resources/prefebs/pre_card", function (err, prefab) {
          var newNode = cc.instantiate(prefab);
          var card=newNode.getComponent('Card');
          
          card=self.initCardRd(card);
          card.backOrFront=backOrFront;
          if(card.backOrFront){
            cc.loader.loadRes(card.cardPicUrl, cc.SpriteFrame, function (err, spriteFrame) {
                newNode.getComponent(cc.Sprite).spriteFrame=spriteFrame;
                card.cardSF=spriteFrame;
            });
          }else{
            cc.loader.loadRes(card.cardBackPicUrl, cc.SpriteFrame, function (err, spriteFrame) {
                newNode.getComponent(cc.Sprite).spriteFrame=spriteFrame;
                card.cardBackSF=spriteFrame;
            });
          }
          var handnode=playerNode.getChildByName('Hand');
          newNode.setPosition(handnode.getChildren().length*50,0);
          //cc.director.getScene().addChild(newNode);
          handnode.addChild(newNode);
        });
    },
    //添加复数卡牌到场地
    addCardsToField:function(cardnumbers,playerNode,backOrFront){
        var self=this;
        for (var i=0;i<cardnumbers;i++){
          self.addCardToField(playerNode,backOrFront);
        }
    },
    
    initCard:function(card,id){
        card.cardtype='CloseCombat';
        card.cardname='monster';
        card.strength=0;
        card.cardintro='this is test1 message';
        card.cardeffect=[];
        card.cardPicUrl='gwent/resources/cards/'+id+'';
        //card.backOrFront=false;
        card.dragpos=null;
        card.dragFlag=false;
        
        return card;
    },
    
    initCardRd:function(card){
        var id=parseInt(3+cc.random0To1()*141.0);
        card.cardtype='CloseCombat';
        card.cardname='monster';
        card.strength=0;
        card.cardintro='this is test1 message';
        card.cardeffect=[];
        card.cardPicUrl='gwent/resources/cards/'+id+'';
        card.backOrFront=false;
        card.dragpos=null;
        card.dragFlag=false;
        return card;
    },
    
    
    
});

