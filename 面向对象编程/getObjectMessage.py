# 获取对象信息 

# 使用type 判断对象类型

type(123) == int
type('abc') == str

#对象是函数
import types
def fn():
    pass
    
type(fn) == types.FunctionType
type(abs) == types.BuiltinFunctionType
type(lambda x :x) == types.LambdaType
type((x for x in range(10))) == types.GeneratorType

#使用isinstance()判断已知类型
# 判断一个变量是否是某个类型中的一种

isinstance('a',str)
isinstance([1,2,3],(list,tuple)) 

# 使用dir
# 获得一个对象的所有属性和方法，可以使用dir()函数，返回一个包含字符串的list

dir('ABC')
len('ABC') #等同于 'ABC'.__len__()

#自己定义len(myObj)
class MyDog(object):
    def __len__(self):
        return 100
        
dog = MyDog()
len(dog) #100

#配合getattr() setattr() hasattr() 操作一个对象的状态

class MyObject(object):
    def __init__(self):
        self.x = 9
    def power(self):
        return self.x * self.x
obj = MyObject()

hasattr(obj,'x')
setattr(obj,'y')
getattr(obj,'x')

# 获取不到值得时候就会报错，可传入一个参数，如果不存在就会返回那个值
getattr(obj,'z',404)

