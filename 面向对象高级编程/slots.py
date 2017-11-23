# 使用__slots__
# 定义的属性仅对当前类实例起作用，对继承的子类不起作用 在子类中也定义__slots__ 这样就是自身的加父类的__slots__

class Student(object):
    __slots__ = ('name','age','score','set_age','set_score') #允许绑定的属性名称
    
s = Student()
s.name = "Michael" #动态给实例绑定一个属性
print(s.name)

def set_age(self,age):
    self.age = age

from types import MethodType

s.set_age = MethodType(set_age,s)
s.set_age(25)
print(s.age)

#但是给一个实例绑定的方法，对另一个实例是不起作用的
s2 = Student()
# s2.set_age(25) 报错没有这个方法

#所以为了给所有实例都绑定方法，可以给class绑定方法
def set_score(self,score):
    self.score = score
    
Student.set_score = set_score


s.set_score(100)
print(s.score)

s2.set_score(90)
print(s2.score)

class GraduateStudent(Student):
    __slots__ = ('age','name')

# 子类加父类的__slots
g = GraduateStudent()
g.score = 99999
print(g.score)

