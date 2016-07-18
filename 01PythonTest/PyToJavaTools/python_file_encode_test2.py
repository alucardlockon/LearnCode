#import codecs

a="""
--业务招待费审批表
drop table MIS.APPROVE_YWZDF_DATA;
create table MIS.APPROVE_YWZDF_DATA(
    --通用字段:
    SPD_CODE VARCHAR(30), --审批单代码
    SPD_TYPE VARCHAR(20), --审批单类型
    STEP INTEGER, --步骤
    STEP_FLOW_ID VARCHAR(20), --步骤流程
    ATTACH_NAME VARCHAR(200), --附件文件名称
    ATTACH_FORMAT_NAME VARCHAR(200), --附件编码后名称
    USER_ID VARCHAR(12), --操作用户 
    OPRT_TIME TIMESTAMP, --操作时间
    --审批单字段:
    ORG_NO VARCHAR(8),  --机构号
    SQRQ DATE, --申请日期
    ZDSY VARCHAR(4000), --招待事由
    YJCJRS INTEGER,--预计参加人数
    QZWHPTRY INTEGER,--其中:我行陪同人员
    ZDSJ DATE,--招待时间
    ZDDD VARCHAR(200),--招待地点
    KHRY VARCHAR(100),--客户人员
    YJ_CYF DECIMAL(16,2),--预计招待金额:餐饮费
    YJ_JNP DECIMAL(16,2),--预计招待金额:纪念品
    YJ_JTF DECIMAL(16,2),--预计招待金额:交通费
    YJ_ZSF DECIMAL(16,2),--预计招待金额:住宿费
    YJ_QT DECIMAL(16,2),--预计招待金额:其他
    YJ_HJ DECIMAL(16,2),--预计招待金额:金额合计
    SJ_CYF DECIMAL(16,2),--实际交待金额:餐饮费
    SJ_JNP DECIMAL(16,2),--实际交待金额:纪念品
    SJ_JTF DECIMAL(16,2),--实际交待金额:交通费
    SJ_ZSF DECIMAL(16,2),--实际交待金额:住宿费
    SJ_QT DECIMAL(16,2),--实际交待金额:其他
    SJ_HJ DECIMAL(16,2) --实际交待金额:金额合计
);
"""
#print a
f1=open('out.txt','w')
f1.write(a)
f1.close()
#正常
print a.decode('gbk').encode('gbk')
f2=open('out.txt','r')
b=f2.readlines()
result=""
for c in b:
	result+=c
print result	
print result.split('\n')
