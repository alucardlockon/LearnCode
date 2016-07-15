import re
#making domin
create=open("create.sql","r")
createlines=create.readlines();
create.close()
text=""
for line in createlines:
    text+=line
for table in re.findall(r"CREATE TABLE .*?\);",text,re.I|re.S):
    table=table.decode('gbk')
    table_name=""
    table_output=""
    for line in table.split('\n'):
        field =re.findall(r"(\s?[^\s]+\s*)?",line)
        if len(field)>0:
            print field[0]
        remarks=re.findall(r"--.*$",line)
        if len(remarks)>0:
            table_output+=remarks[0][2:].strip()


#making mapper
#making html
#making action
#making service

