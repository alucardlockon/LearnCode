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
    command=['attack','void','def','fireball']
    def __init__(self,name,lv):
        self.name=name
        self.lv=lv
        self.initRoleByLv(lv)
    def initRoleByLv(self,lv):
        self.exp=lv*(1000+lv*200)
        self.nextLv=(lv+1)*(1000+(lv+1)*100)-self.exp
        stra=lv*1.1*random.random()
    def showInfo(self):
        return self.name+"[lv:"+str(self.lv)+",exp:"+str(self.exp)+\
               ",nextLv:"+str(self.nextLv)+\
               ",stra:"+str(self.stra)+",inte:"+str(self.inte)+\
               ",spd:"+str(self.spd)+",defe:"+str(self.defe)+\
               ",rest:"+str(self.rest)+\
               ",void:"+str(self.void)+",command:["+",".join(self.command)+"]]"
        

my=role('my',2)
print my.showInfo()
