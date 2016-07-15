#coding utf-8
#f1=open('out.txt','w')
#f1.write("""听说Python会乱码
#你怎么说?
#是不是这样呢?？是吗!?
#""")
#f1.close()

f2=open('out.txt','r')
a=f2.readlines()
f2.close()
for b in a.split('\n'):
	b+=b
    print a
raw_input()