# 实例属性和类属性

# 给实例绑定属性的方法是通过实例变量 或者self
class StudentTest(object):
    def __init__(self,name):
        self.name = name
 
s = StudentTest('Bob')
s.score = 90

# 类本身属性，在实例中不能直接访问到。但可以访问
# class Student(object):
    # name = "Student"
    
# s = Student()
# Student.name

# s.name
# Student.name

#练习
class Student(object):
    count = 0
    
    def __init__(self,name):
        self.name = name
        Student.count = Student.count + 1
        
        
# 测试:
if Student.count != 0:
    print('测试失败!')
else:
    bart = Student('Bart')
    if Student.count != 1:
        print('测试失败!')
    else:
        lisa = Student('Bart')
        if Student.count != 2:
            print('测试失败!')
        else:
            print('Students:', Student.count)
            print('测试通过!')