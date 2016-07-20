cc.Class({
    extends: cc.Component,

    properties: {
        player:null,
        opp:null
    },

    // use this for initialization
    onLoad: function () {
        this.setUpBoard();
    },

    setUpBoard:function(){
        this.setDeck();
    },

    setDeck:function(){
        // 加载 Prefab
        cc.loader.loadRes("gwent/resources/prefebs/pre_card", function (err, prefab) {
          var newNode = cc.instantiate(prefab);
          cc.director.getScene().addChild(newNode);
        });

    }

    // called every frame, uncomment this function to activate update callback
    // update: function (dt) {

    // },
});
