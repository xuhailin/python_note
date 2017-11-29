#编写一个程序，能在当前目录以及当前目录的所有子目录下查找文件名包含指定字符串的文件，并打印出相对路径

import os

searchkey = '.py'
up = '.'

def printPath(path):
     for x in os.listdir(path):
         abx_x = os.path.join(path,x)  # 获得当前x的正确相对路径
         if os.path.isdir(abx_x):
             printPath(os.path.join(path,x))
         if os.path.isfile(abx_x) and os.path.split(abx_x)[1].find(searchkey) != -1:
             print(abx_x)
     
printPath(up)

print("\n\nby os.walk\n")
def printPath2(path):
    
    for x in os.walk(path): # x 有三个值 0是路径 1是文件夹 2是文件
        for i in x[2]:
           if i.find(searchkey) != -1:
               print(os.path.abspath(os.path.join(x[0],i)))
        

printPath2(up)