#定义类  class 类名
#创建实例 类名+()


#__init__方法 创建实例时必须参数相匹配，self不需要在传

class Student(object):
    def __init__(self, name, score):
        self.name = name
        self.score = score

    def get_grade(self):
        if self.score >= 90:
            return 'A'
        elif self.score >= 60:
            return 'B'
        else:
            return 'C'

            
lisa = Student('Lisa', 99)
bart = Student('Bart', 59)
print(lisa.name, lisa.get_grade())
print(bart.name, bart.get_grade())

#总结：
# 类是创建实例的模板，而实例则是一个一个对象，各个实例拥有的数据都互相独立，互不影响
# 方法就是与实例绑定的函数，和普通函数不同，方法可以直接访问实例的数据
# 通过在实例上调用方法，我们就直接操作了对象内部的数据，但无需知道方法内部的实现细节。
