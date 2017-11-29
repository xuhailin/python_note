# StringIO  数据读写不一定是文件 也可以在内存中读写

# StringIO 和BytesIO是在内存中操作str和bytes的方法，使得和读写文件具有一致的接口
from io import StringIO
# 把str写入StringIO
f = StringIO()
f.write('hello')
f.write(' ')
f.write("world")
print(f.getvalue())
#getvalue()方法用于获得写入后的str

#读取StringIO 可以用str先初始化StringIO
f2 = StringIO('Hello\nHi!\nGoodBye!')
while True:
    s = f2.readline()
    if s == '':
        break
    print(s.strip())
    
    
# BytesIO实现了在内存中读写bytes
from io import BytesIO
f  = BytesIO()
f.write('中文'.encode('utf-8')) #转为utf-8编码的bytes
f.write(b'\xe4\xb8\xad\xe6\x96\x87')
print(f.getvalue())

#读取
f2 = BytesIO(b'\xe4\xb8\xad\xe6\x96\x87')
print(f2.read())

