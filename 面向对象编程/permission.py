# 访问限制
class StudentTest(object):
    
    def __init__(self,name,score):
        self.__name = name
        self.__score = score
     
    def print_score(self):
        print('%s: %s' % (self.__name, self.__score))
        
    def get_name(self):
        return self.__name
     
    def set_name(self,name):
        self.__name = name
    
    def get_score(self):
        return self.__score
      
    def set_score(self,score):
        self.__score = score    
# 实例中的变量名如果以__开头，就变成了一个私有变量 只有内部可以访问，外部不能访问

#bart = Student('Bart Simpson',59)
#bart.__name #报错 会访问不到__name这个属性

#外部要获得和修改值的时候  使用get  set方法

# 注意  __XXX__这样的变量，是特殊变量，外部也是可以访问的，所以使用__xxx代表私有变量

# bart._Student__name 
#获取私有变量  还是有方法可以获取

# 练习
class Student(object):
    def __init__(self,name,gender):
        self.__name = name
        self.__gender = gender
    def set_gender(self,gender):
        if isinstance(gender,str) and gender in ['male','female']:
            self.__gender = gender
    def get_gender(self):
        return self.__gender
        
        
# 测试:
bart = Student('Bart', 'male')
if bart.get_gender() != 'male':
    print('测试失败!')
else:
    bart.set_gender('female')
    if bart.get_gender() != 'female':
        print('测试失败!')
    else:
        print('测试成功!')
        
bob = Student('Bob','male')
if bob.get_gender() != 'male':
    print('测试失败!')
else:
    bob.set_gender('males')
    if bob.get_gender() != 'male':
        print('测试失败!')
    else:
        print('测试成功!')