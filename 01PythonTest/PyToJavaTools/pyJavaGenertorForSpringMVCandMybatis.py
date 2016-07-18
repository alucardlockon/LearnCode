import re
#making comment
def getcomment(text):
    result=""
    for table in re.findall(r"CREATE TABLE .*?\);",text,re.I|re.S):
        table=table.decode('gbk')
        table_name=re.findall(r"CREATE TABLE .*?\(",table,re.I)[0][12:-1].strip()
        table_output="comment on table "+table_name+" is '"+table_name+"';"
        for line in table.split('\n'):
            field =re.findall(r"(^\s+[\S]+\s+)",line)
            if len(field)>0 :
                table_output+="comment on column "+table_name+"."+field[0].strip()
            remarks=re.findall(r"--.*$",line)
            if len(remarks)>0:
                table_output+=" is '"+remarks[0][2:].strip()+"';"
            table_output+="\n"
        result+=table_output+"\n"
    return result

#making domin
def getdomin(text):
    result=""
    for table in re.findall(r"CREATE TABLE .*?\);",text,re.I|re.S):
        table=table.decode('gbk')
        table_name=""
        table_output=""
        for line in table.split('\n'):
            field =re.findall(r"(^\s+[\S]+\s+)",line)
            if len(field)>0 :
                table_output+="String "+underline_to_camel(field[0].strip())+";"
            remarks=re.findall(r"--.*$",line)
            if len(remarks)>0:
                table_output+="//"+remarks[0][2:].strip()
            table_output+="\n"
        result+=table_output+"\n"
    return result
#making mapper
def getmapper(text):
    result=""
    for table in re.findall(r"CREATE TABLE .*?\);",text,re.I|re.S):
        table=table.decode('gbk')
        table_name=underline_to_camel_first_upper(re.findall(r"\..*?\(",table,re.I)[0][1:-1].strip())
        table_output="List<"+table_name+"> find"+table_name+"List("+table_name+" "+(table_name[0].lower()+table_name[1:])+");"+ \
                      "\n"+\
                      "Integer insert"+table_name+"("+table_name+" "+(table_name[0].lower()+table_name[1:])+");"+\
                      "\n"+\
                      "Integer update"+table_name+"("+table_name+" "+(table_name[0].lower()+table_name[1:])+");"+\
                      "\n"+\
                      "Integer delete"+table_name+"("+table_name+" "+(table_name[0].lower()+table_name[1:])+");"
        #select
        select_sql='<select id="find'+table_name+'List" parameterType="'+table_name+'" resultType="'+table_name+'">'
        select_sql+="\n\tSELECT"
        for line in table.split('\n'):
            field =re.findall(r"(^\s+[\S]+\s+)",line)
            if len(field)>0 :
                select_sql+="\n\t"+field[0].strip()+","
        select_sql+="\n\tFROM "+re.findall(r"CREATE TABLE .*?\(",table,re.I)[0][12:-1].strip()
        select_sql+="\n\tWHERE 1=1 "
        for line in table.split('\n'):
            field =re.findall(r"(^\s+[\S]+\s+)",line)
            if len(field)>0 :
                field_local=field[0].strip()
                select_sql+='\n\t<if test="'+field_local+' != null and '+field_local+'!=\'\'">'
                select_sql+="\n\t\t and  "+field_local+"=#{"+underline_to_camel(field_local)+"}"
                select_sql+="\n\t</if>"
        select_sql+="\n\t</select>"
        
        #insert
        insert_sql='<insert id="insert'+table_name+'" parameterType="'+table_name+'" >'
        insert_sql+="\n\tINSERT INTO "+re.findall(r"CREATE TABLE .*?\(",table,re.I)[0][12:-1].strip()+"("
        for line in table.split('\n'):
            field =re.findall(r"(^\s+[\S]+\s+)",line)
            if len(field)>0 :
                insert_sql+=" "+field[0].strip()+","
        insert_sql=insert_sql[:-1]+")\n\tVALUES ("
        for line in table.split('\n'):
            field =re.findall(r"(^\s+[\S]+\s+)",line)
            if len(field)>0 :
                field_local=field[0].strip()
                insert_sql+=" #{"+underline_to_camel(field_local)+"},"
        insert_sql=insert_sql[:-1]+")\n\t</insert>"

        #update
        update_sql='<update id="update'+table_name+'" parameterType="'+table_name+'" >'
        update_sql+="\n\tUPDATE "+re.findall(r"CREATE TABLE .*?\(",table,re.I)[0][12:-1].strip()+"\n\tSET "
        for line in table.split('\n'):
            field =re.findall(r"(^\s+[\S]+\s+)",line)
            if len(field)>0 :
                update_sql+=field[0].strip()+"=#{"+underline_to_camel(field[0].strip())+"},"
        update_sql=update_sql[:-1]+")\n\tWHERE 1=1 "
        for line in table.split('\n'):
            field =re.findall(r"(^\s+[\S]+\s+)",line)
            if len(field)>0 :
                field_local=field[0].strip()
                update_sql+=" and  "+field_local+"=#{"+underline_to_camel(field_local)+"}"
        update_sql+="\n\t</update>"
        
        #delete
        delete_sql='<delete id="delete'+table_name+'" parameterType="'+table_name+'" >'
        delete_sql+="\n\tDELETE FROM "+re.findall(r"CREATE TABLE .*?\(",table,re.I)[0][12:-1].strip()+"\n\tWHERE 1=1 "
        for line in table.split('\n'):
            field =re.findall(r"(^\s+[\S]+\s+)",line)
            if len(field)>0 :
                field_local=field[0].strip()
                delete_sql+='\n\t<if test="'+field_local+' != null and '+field_local+'!=\'\'">'
                delete_sql+="\n\t\t and  "+field_local+"=#{"+underline_to_camel(field_local)+"}"
                delete_sql+="\n\t</if>"
        delete_sql+="\n\t</delete>"

        table_output+=select_sql
        table_output+=insert_sql
        table_output+=update_sql
        table_output+=delete_sql
        result+=table_output+"\n"
    return result
#making html(only input)
def gethtml(text):
    result=""
    for table in re.findall(r"CREATE TABLE .*?\);",text,re.I|re.S):
        table=table.decode('gbk')
        table_name=""
        table_output=""
        for line in table.split('\n'):
            field =re.findall(r"(^\s+[\S]+\s+)",line)
            if len(field)>0 :
                table_output+='\n<input type="text" class="form-control" name="'+underline_to_camel(field[0].strip())+'"/>'
        result+=table_output+"\n"
    return result

#utils
def underline_to_camel(underline_format):  
    camel_format = ''    
    for _s_ in underline_format.split('_'):  
        camel_format += _s_.capitalize()
    camel_format=camel_format[0].lower()+camel_format[1:]
    return camel_format  
def underline_to_camel_first_upper(underline_format):  
    camel_format = ''    
    for _s_ in underline_format.split('_'):  
        camel_format += _s_.capitalize()
    return camel_format

#main:
create=open("create.txt","r")
createlines=create.readlines();
create.close()
text=""
for line in createlines:
    text+=line

#result=getcomment(text)
#result=getdomin(text)
#result=getmapper(text)
#result=gethtml(text)
#print result
#output
output=open("create_out.txt","w")
output.write("\n\tcomment:\n\n")
output.write(getcomment(text).encode('gbk'))
output.write("\n\tcomment:\n\n")
output.write(getdomin(text).encode('gbk'))
output.write("\n\tcomment:\n\n")
output.write(getmapper(text).encode('gbk'))
output.write("\n\tcomment:\n\n")
output.write(gethtml(text).encode('gbk'))
output.close()