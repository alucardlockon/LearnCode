#trun based rpg
import random
import time
class role:
    name=""
    lv=1
    exp=0
    nextLv=1000
    hp=100
    mp=30
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
        self.hp=int(self.hp+lv*30*random.random())
        self.mp=int(self.mp+lv*10*random.random())
        self.stra=int(self.stra+lv*2*random.random())
        self.inte=int(self.inte+lv*2*random.random())
        self.spd=int(self.spd+lv*2*random.random())
        self.defe=int(self.defe+lv*2*random.random())
        self.rest=int(self.rest+lv*2*random.random())
        self.void=int(self.void+lv*2*random.random())
    def getInfo(self):
        return self.name+"[lv:"+str(self.lv)+",exp:"+str(self.exp)+\
               ",nextLv:"+str(self.nextLv)+\
               ",hp:"+str(self.hp)+",mp:"+str(self.mp)+\
               ",stra:"+str(self.stra)+",inte:"+str(self.inte)+\
               ",spd:"+str(self.spd)+",defe:"+str(self.defe)+\
               ",rest:"+str(self.rest)+\
               ",void:"+str(self.void)+",command:["+",".join(self.command)+"]]"
    def addExp(self,exp):
        self.exp+=exp
        if self.exp>=self.nextLv:
            self.lvUp();
        print self.name+' get '+str(exp)+' exp!'
    def lvUp(self):
        self.lv+=1
        self.nextLv=(self.lv+1)*(1000+(self.lv+1)*200)
        self.hp=int(self.hp+30*random.random())
        self.mp=int(self.mp+10*random.random())
        self.stra=int(self.stra+2*random.random())
        self.inte=int(self.inte+2*random.random())
        self.spd=int(self.spd+2*random.random())
        self.defe=int(self.defe+2*random.random())
        self.rest=int(self.rest+2*random.random())
        self.void=int(self.void+2*random.random())
        if self.exp>=self.nextLv:
            self.lvUp();
        print self.name+' LEVELUP!'+self.getInfo()

class stage:
    stagename="stage"
    stageLv=1
    compelete=False
    startPos=0
    endPos=100
    emenyLIst=[role("man",1),role("slime",3),role("swordman",4),\
               role("dragon baby",5),role("dragon",7),role("vampire",8)]
    emenyPrecent=[30,30,20,10,5,5]
    boss=role("boss",10)
    def __init__(self,stagename,stagelv):
        self.stagename=stagename
        self.stagelv=stagelv
        self.startPos=0
    def getInfo(self):
        s=''
        for num in self.emenyPrecent :s+=str(num)+','
        s2=''
        for num2 in self.emenyLIst :s2+=num2.name+','
        return self.stagename+"[stageLv:"+str(self.stageLv)+",compelete:"+str(self.compelete)+\
               ",startPos:"+str(self.startPos)+\
               ",endPos:"+str(self.endPos)+\
               ",emenyLIst:["+s2+\
               "],emenyPrecent:["+s+"]]"
#my=role('my',7)
#print my.getInfo()
#my.addExp(18000)
#print my.getInfo()
#stage=stage("forest",1)
#print stage.getInfo()

#commads:
def attack(roleself,roleattacked):
    damage=0
    if roleself.stra-roleattacked.defe>0:
        damage=int((roleself.stra-roleattacked.defe)*random.random()*20)
    else:
        damage=int(random.random()*20)
    roleattacked.hp-=damage
    print roleself.name+'\'s attack:deal '+str(damage)+' damage to '+roleattacked.name

#methods:
def expolore(stage):
    while True:
        r=int(random.random()*100);
        precentnew=0;
        for (precent,emeny) in zip(stage.emenyPrecent,stage.emenyLIst):
            stage.startPos+=int(4*random.random())+1;
            if(stage.startPos>=stage.endPos):
                print "stage clear!"
                return "stage clear!"
            precentold=precentnew
            precentnew+=precent
            if r>=precentold and r<precentnew :
                while True:
                    
                    print time.strftime("%Y-%m-%d-%H-%M-%S",\
                                        time.localtime(time.time())),\
                                        precentold,\
                                        precentnew,emeny.name,emeny.hp,emeny.mp,player.name,player.hp,player.mp
                    #print emeny.getInfo()
                    #print player.getInfo()
                    cmd=raw_input()
                    if cmd=="exit" :
                        break
                    if cmd=="show":
                        print stage.startPos,stage.endPos,player.getInfo(),emeny.getInfo()
                        break
                    if emeny.spd>player.spd:
                        attack(emeny,player)
                    if cmd=="a" or cmd=="attack":
                        attack(player,emeny)
                    if emeny.spd<=player.spd:
                        attack(emeny,player)
                    if emeny.hp<=0:
                        player.addExp(int((emeny.lv+emeny.inte+emeny.stra)*500*random.random()))
                        break
                    elif player.hp<=0:
                        print "game over"
                        return 'game over'
                    
        


#main methods:
global player
player=role("player",8)
while True:
    print 'Please type enter to start,type"exit" to exit'
    cmd=raw_input()
    if cmd=="exit" :
        break
    else:
        expolore(stage("forest",1))
    
