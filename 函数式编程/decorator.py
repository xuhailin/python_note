# 装饰器：在代码运行期间动态增加功能

# def log(func):
    # def wrapper(*args,**kw):
        # print("call %s():" % func.__name__)
        # return func(*args,**kw)
    # return wrapper
    
    
# now = log(now)
# @log  
# def now():
    # print('2015-3-25')

# print(now())

# print(now.__name__)


# import functools

# def log2(text):
   # def decorator(func):
       # @functools.wraps(func)
       # def wrapper(*args,**kw):
           # print('%s %s():' % (text, func.__name__))
           # return func(*args, **kw)
       # return wrapper
   # return decorator

# @log2("excute")
# def now2():
   # print("2015-3-25 (2)")
   
# print(now2())
# print(now2.__name__)
def log(text):
    def decorator(func):
        def wrapper(*args, **kw):
            print('%s %s():' % (text, func.__name__))
            func(*args, **kw)
            
        return wrapper
    return decorator
@log('execute')
def now():
    print('2015-3-25')
now()


import time,functools

def metric(fn):
    @functools.wraps(fn)
    def wrapper(*args,**kw):
        print('%s executed in %s ms' % (fn.__name__, 10.24))
        return fn(*args,**kw)
    return wrapper

# 测试
@metric
def fast(x, y):
    time.sleep(0.0012)
    return x + y;

@metric
def slow(x, y, z):
    time.sleep(0.1234)
    return x * y * z;

f = fast(11, 22)
s = slow(11, 22, 33)
if f != 33:
    print('测试失败!')
elif s != 7986:
    print('测试失败!')
    
import types
def decorator(func):
    @functools.wraps(func)
    def wrapper(*args,**kw):
        print('begin call')
        fn = func(*args,**kw)
        print('end call')
        return fn
    return wrapper
           
def log3(arg):   
    if isinstance(arg,str):
        return decorator
    elif isinstance(arg,types.FunctionType):
        return decorator(arg)
    
    
 
@log3
def f1():
    print("f")
     
@log3('execute')
def s1():
    print("execute f")
 
f1()
s1()