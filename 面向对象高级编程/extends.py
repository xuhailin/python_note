# d多重继承
# MixIn ： 让类可以继承多个类 并非单一继承下来
# 类似相当于java的接口，可以实现多接口

#MixIn 目的就是给一个类增加多个功能，通过多重继承而不是设计多层次的复杂继承关系
class Mamal(object):
    pass

class RunnableMinIn(object):
    pass

#通过在括号后面增加参加，来增加继承的对象
class Dog(Mamal,RunnableMinIn):
    pass