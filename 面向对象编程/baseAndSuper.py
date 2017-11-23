#继承 和 多态
#总结
# 继承可以把父类的所有功能都直接拿过来，子类只需要新增自己特有的方法，或者重写父类的方法
# 动态语言的鸭子类型决定了继承不像静态语言那样是必须的

# java 向上转型 静态语言 
 # class A{}
 # class B extend A{}
 # A a = new B()


# 基类 父类 超类
class Animal(object):
    def run(self):
        print("Animal is running")

# 子类直接从父类继承  获得
class Dog(Animal):
    def run (self):
        print('Dog is running...')   

class Cat(Animal):
    def run(self):
        print('Cat is running...')
   
# 子类会继承父类的方法，当子类和父类存在相同的方法时，
# 子类会覆盖父类的方法，多态 
dog = Dog()
cat = Cat()
dog.run()
cat.run()

def run_twice(animal):
    animal.run()
    animal.run()
    
run_twice(Animal())
run_twice(Dog())

#新增一个Animal的子类，不必对run_twice做任何修改
class Tortoise(Animal):
    def run(self):
        print("Tortoise is run slowly...")
        
run_twice(Tortoise())

# 具体方法作用在对象上，由对象的确切类型所决定，调用方只管调用，不管细节
# 对扩展开放：允许新增子类
# 对修改封闭:  不需要修改Animal类型的run_twice()等函数

