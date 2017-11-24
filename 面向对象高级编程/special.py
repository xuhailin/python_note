# 定制类
# 特殊变量 类似__slots__ __xxx__的变量或者函数名，都是有特殊用途的

# __str__  __repr__

class Student(object):
    def __init__(self,name):
        self.name = name
    # 用于打印实例对象，而不是展示一个地址
    def __str__(self):
        return 'Student object (name : %s)' % self.name

    #解决变量直接调用
    __repr__ = __str__
print(Student('Michael'))

s = Student("Bob")
s
#变量直接调用会显示的不是__str__() 而是__repr__() 
# __str__()是返回用户看到的字符串，__repr__()返回程序开发者看到的字符串

# __iter__

class Fib(object):
    def __init__(self):
        self.a,self.b = 0,1
      
    #用于for...in 循环时， __next__() 返回循环的下一个值
    def __iter__(self):
        return self
        
    def __next__(self):
        self.a,self.b = self.b,self.a + self.b
        if self.a>100000:
            raise StopIteration()
        return self.a

    # 可以获得任意一项了
    # 但是list有一个切片方法 list(range(100))[5:10] 对于__getitem__()传入的可能是一个int 也可能是一个切片对象slice
    def __getitem__(self,n):
        if isinstance(n,int):    
            a ,b = 1,1
            for x in range(n):
                a,b = b,a+b
            return a
        if(isinstance(n,slice)):
            start = n.start
            stop = n.stop
            if  start is None:
                start = 0
            a,b = 1,1
            L = []
            for x in range(stop):
                if x >= start:
                    L.append(a)
                a,b = b,a+b
            return L
    
for n in Fib():
    print(n)
    
    
    
# __getitem__
# __iter__取不到具体某个值
f = Fib()
print(f[0])
print(f[0:5])
print(f[:10]) #但是不能对有step的参数做处理，也没有对负数做处理


# 与之对应的有 __setitem__()方法 把对象视作list和dict来赋值
# __delitem__() 方法 用于删除某个元素


# __getattr__
# 当访问类的一个属性时，会动态返回一个属性 也可以返回表达式
# 注意，只有在没有找到属性的情况下，才会调用__getattr__
class Student2(object):
    def __getattr__(self,attr):
        if attr == 'age':
            return lambda:25
        return '123'
s = Student2()
print(s.name)
print(s.age())

# 比如写SDK 给每个url对应的API都写一个方法 获得对应的path

import types
class Chain(object):

    def __init__(self, path=''):
        self._path = path

    def __getattr__(self, path):
        return Chain('%s/%s' % (self._path, path))
            
    def __call__(self, *name): 
        path = name    
        if isinstance(name,tuple):
            path = ''
            for n in name:
               path = path + '/:%s' % n
        return Chain('%s%s' % (self._path, path))  
        
    def __str__(self):
        return self._path

    __repr__ = __str__

print(Chain())
print(Chain().status.user)
print(Chain().user().status)
print(Chain().user("Michael").status)
print(Chain().user("Michael","aaa").status)


#__call__  调用实例方法时

class Student3(object):
    def __init__(self,name):
        self.name = name
        
    def __call__(self):
        print('My name is %s.' % self.name)

s3 = Student3('Michael')
s3()

# 通过callable()函数 判断一个对象是否为可调用对象
print(callable(Student3('name')))
print(callable(max))
print(callable([1,2,3]))
print(callable(None))
print(callable('str'))











