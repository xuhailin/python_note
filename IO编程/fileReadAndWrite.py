# 文件读写

# 读写文件的功能一般都是由操作系统提供。
# 读写文件就是请求操作系统打开一个文件对象（通常指文件描述符）
#，然后，通过操作系统提供的接口从这个文件对象中读取数据（读文件）
# 或者把数据写入这个文件对象，写文件

# 'r'代表读文件，如果文件不存在 会抛出一个IOError

# try:
    # f = open('test.txt','r') 
    # print(f.read())
# finally:
    # if f:
        # f.close()    

#代码更加简洁，不必调用f.close()方法
with open('test.txt','r') as f:
    print(f.read())
    
#read()会一次性读取全部内容，可以通过反复调用read(size)来每次读取size的字节的内容
# readline()每次可以读取一行内容，调用readlines()可以读取所有内容并按行返回list
# for line in f.readlines():
    # print(line.strip())# 把末尾的'\n'删掉
    
#file-like Object
# 像open函数返回的这种有个read()方法的对象，在python中统称为file-like Object.除了file外，还可以是内存的字节流
# 网络流，自定义流等。
# StringIO就是在内存中创建的file-like Object 常作临时缓冲

#二进制文件 'rb'
# f = open('test.jpg','rb')
# f.read()

#字符编码 读取非UTF-8编码的文本文件 encoding参数 errors参数可以遇到非法编码的字符
# f = open('gbk.txt','r',encoding='gdk',errors = 'ignore')
# f.read()

# 写文件
# 'w' 'wb'
f = open('test.txt','w+')
f.write('newHelloworld')
print(f.read()) #异步
f.close()



#练习 请将本地一个文本文件读为一个str并打印出来：
fpath = r'C:\Windows\system.ini'

with open(fpath, 'r') as f:
    s = f.read()
    print(s)







 