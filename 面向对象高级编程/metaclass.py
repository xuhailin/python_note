#使用元类


#type()  动态语言和静态语言最大的不同就是函数和类的定义 不是编译的时候定义的 而是运行时动态创建的

class Hello(object):
    def hello(self,name='world'):
        print('hello, %s.' % name)

#当解释器载入Hello模块时 就会依次执行该模块的所有语句，动态创建出一个Hello的class对象
# type() 函数可以查看一个类型或者变量的类型，Hello是一个class 它的类型是type 而h是一个class Hello
print(type(Hello))


# metaclass  元类
# 除了type()动态创建类以外，要控制类的创建行为，还可以使用metaclass
# 先定义metaclass就可以创建类，最后创建实例。


class ListMetaClass(type):
    def __new__(cls,name,bases,attrs):
        attrs['add'] = lambda self,value:self.append(value)
        return type.__new__(cls,name,bases,attrs)

#__new__()方法接受到的参数是
# 1.当前创建的类的对象
# 2.类的名字
# 3.类继承的父类集合
# 4.类的方法集合

class MyList(list,metaclass=ListMetaClass):
    pass

L = MyList()
L.add(1)
print(L)

a = 123
print(str(123))
# 它负责保存数据库表的字段名和字段类型
class Field(object):
    def __init__(self,name,column_type):
        self.name = name
        self.column_type = column_type

    def __str__(self):
        return '<%s:%s>' % (self.__class__.__name__,self.name)

class StringField(Field):
    def __init__(self,name):
        super(StringField, self).__init__(name,'varchar(100)')

class IntegerField(Field):
    def __init__(self,name):
        super(IntegerField, self).__init__(name,'bigint')

class ModelMetaclass(type):
    def __new__(cls, name,bases,attrs):
        if name == 'Model':
            return type.__new__(cls,name,bases,attrs)
        print('Found Model: %s' % name)
        mappings = dict()
        for k,v in attrs.items():
            if isinstance(v,Field):
                print('Found mapping: %s ==> %s' % (k,v))
                mappings[k] = v
        for k in mappings.keys():
            attrs.pop(k)

        attrs['__mappings__'] = mappings # 保存属性和列的映射关系
        attrs['__table__'] = name # 假设表名和类名一致
        return type.__new__(cls,name,bases,attrs)


class Model(dict,metaclass=ModelMetaclass):
    def __init__(self,**kw):
        super(Model,self).__init__(**kw)

    def __getattr__(self, key):
        try:
            return self[key]
        except KeyError:
            raise AttributeError(r"'Model' object has no attribute '%s'" % key)

    def __setattr__(self, key, value):
        self[key] = value

    def save(self):
        fields = []
        params = []
        args = []
        for k,v in self.__mappings__.items():
            fields.append(v.name)
            params.append('?')
            args.append(getattr(self,k,None))
        sql = 'insert into %s (%s) values (%s)' % (self.__table__,','.join(fields),','.join(params))
        print('SQL: %s' % sql)
        print('ARGS: %s' % str(args))
#metaclass 修改类定义的例子 orm框架

class User(Model):
    # 定义类的属性到列的映射：
    id = IntegerField('id')
    name = StringField('username')
    email = StringField('email')
    password = StringField('password')


# 创建一个实例
u = User(id=12345,name='Michal',email='test@orm.org',password = 'my-pwd')

# 保存到数据库
u.save()

