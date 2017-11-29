#练习
# 1.
#!/usr/bin/env python3
# -*- coding: utf-8 -*-
import os
import time
import re


def listFile(path):
    print('权限\t文件数\t用户名\t群组名\t大小\t月份\t日期\t时间\t文件名')
    for x in os.listdir(path):
        dir=os.path.join(path,x)
        st=os.stat(dir) # 获得文件的系统状态信息
        print(oct(st.st_mode)[-3:],end='\t')# 获得文件的相关权限 装换成8进制 取最后三位
        print(numOfFiles(dir),end='\t') # 文件数
        print(st.st_uid,end='\t')  # 用户id
        print(st.st_gid,end='\t')         
        print(st.st_size,end='\t') #大小
        lc_time=time.localtime(st.st_mtime) #获得最后一次修改的时间
        print(time.strftime('%b',lc_time),end='\t') #月份
        print(lc_time.tm_mday,end='\t') # 天
        print(time.strftime('%H:%M',lc_time),end='\t') #时间
        print(x) #文件名

#计算文件夹数，最小为1
def numOfFiles(path,num=1):
    try:
        for x in os.listdir(path):
            dir=os.path.join(path,x)
            if os.path.isdir(dir):
                num+=1
                num=numOfFiles(dir,num)
    except BaseException as e:
        pass
    finally:
        return num
        
dirpath=r'D:\python'
listFile(dirpath)