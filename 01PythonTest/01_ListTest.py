#test List
print "Please insert your List,type 'exit' to exit";
ls=[];
value="";
exitStr="exit"
while value!=exitStr:
    value=raw_input();
    if(value!=exitStr):
        ls.append(value);
ls.sort();
print "your sorted List is:"+str(ls);
raw_input();
