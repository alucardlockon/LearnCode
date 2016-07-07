#trun based rpg
import random
class role:
    name=""
    lv=1
    exp=0
    nextLv=1000
    stra=5
    inte=5
    spd=5
    defe=5
    rest=5
    void=5
    dropItems=[None]
    dropPrecent=[100]
    command=['attack','void','def','fireball']
    def __init__(self,name,lv):
        self.name=name
        self.lv=lv
        self.initRoleByLv(lv)
    def initRoleByLv(self,lv):
        self.exp=lv*(1000+lv*200)
        self.nextLv=(lv+1)*(1000+(lv+1)*200)
        self.stra=int(self.stra+lv*2*random.random())
        self.inte=int(self.inte+lv*2*random.random())
        self.spd=int(self.spd+lv*2*random.random())
        self.defe=int(self.defe+lv*2*random.random())
        self.rest=int(self.rest+lv*2*random.random())
        self.void=int(self.void+lv*2*random.random())
    def getInfo(self):
        return self.name+"[lv:"+str(self.lv)+",exp:"+str(self.exp)+\
               ",nextLv:"+str(self.nextLv)+\
               ",stra:"+str(self.stra)+",inte:"+str(self.inte)+\
               ",spd:"+str(self.spd)+",defe:"+str(self.defe)+\
               ",rest:"+str(self.rest)+\
               ",void:"+str(self.void)+",command:["+",".join(self.command)+"]]"
    def addExp(self,exp):
        self.exp+=exp
        if self.exp>=self.nextLv:
            self.lvUp();
    def lvUp(self):
        self.lv+=1
        self.nextLv=(self.lv+1)*(1000+(self.lv+1)*200)
        self.stra=int(self.stra+2*random.random())
        self.inte=int(self.inte+2*random.random())
        self.spd=int(self.spd+2*random.random())
        self.defe=int(self.defe+2*random.random())
        self.rest=int(self.rest+2*random.random())
        self.void=int(self.void+2*random.random())
        if self.exp>=self.nextLv:
            self.lvUp();

class stage:
    stagename="stage"
    stageLv=1
    compelete=False
    startPos=0
    endPos=100
    emenyLIst=[role("man",1)]
    emenyPrecent=[100]
    boss=role("boss",3)
    def __init__(self,stagename,stagelv):
        self.stagename=stagename
        self.stagelv=stagelv
        self.startPos=0
    def getInfo(self):
        s=''
        for num in self.emenyPrecent :s+str(num)+','
        return self.stagename+"[stageLv:"+str(self.stageLv)+",compelete:"+str(self.compelete)+\
               ",startPos:"+str(self.startPos)+\
               ",endPos:"+str(self.endPos)+",emenyLIst:["+","+\
               "],emenyPrecent:["+s+"]]"
#my=role('my',7)
#print my.getInfo()
#my.addExp(18000)
#print my.getInfo()
stage=stage("forest",1)
stage.getInfo()


