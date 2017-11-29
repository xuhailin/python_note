# 操作文件和目录 
# 通过内置的os模块
import os
name = os.name
#操作系统类型 posix 是Linux Unix或者Max OS X 如果是nt 就是Windows系统
print(name)
# print(os.uname()) #uname()获取详细的系统信息 不在windows系统上提供uname()方法

#环境变量 在操作系统中定义的环境变量都存在os.environ变量里
print(os.environ)
# 获取某个环境变量的值
print(os.environ.get('PATH'))
print(os.environ.get('x','default'))# 当key不存在时，输出default

# 操作文件和目录的函数一部分放在os模块中，一部分放在os.path中
# 查看当前目录的绝对路径
print(os.path.abspath('.'))

#在某个目录下创建一个新目录 首先把新目录的完整路径标识出来
#  os.path.join('/user/michael','testdir') 获得路径
#  os.mkdir('/user/michael/testdir') 创建目录
#  os.rmdir('/user/michael/testdir')  删除目录

# 拼接路径用join
# 拆分路径用split os.path.split() 拆除最后一个路径和前面的路径
# 获得文件扩展名 splitext() 
print(os.path.join("aa","bb","cc"))

print(os.path.split("aa/bb/cc"))

print(os.path.splitext("aa/bb/cc.txt"))


# 文件操作
# os.rename('test.txt','test.py')
# os.remove('test.py')

#文件复制 shutill模块的copyfile()函数

# 列出当前目录下的所有文件夹
[x for x in os.listdir('.') if os.path.isdir(x)]

# 列出当所有的.py文件
[x for x in os.listdir('.') if os.path.isfile(x) and os.path.splitext(x)[1] == '.py']
