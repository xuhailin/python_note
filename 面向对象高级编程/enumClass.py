# 枚举
from enum import Enum,unique

# 定义为一个class类型，每个常量都是class的唯一实例
Month = Enum('Month',('Jan', 'Feb', 'Mar', 'Apr', 'May', 'Jun', 'Jul', 'Aug', 'Sep', 'Oct', 'Nov', 'Dec'))

for name,member in Month.__members__.items():
    print(name,'=>',member,',',member.value)
    
    
# member.value  属性是自动赋值给成员的int常量，默认从1开始计数
# 如果要更精确的控制枚举类型，可以从Enum派生出自定义类

#@unique装饰器可以帮助我们检查保证没有重复值
@unique
class Weekday(Enum):
    Sun = 0
    Mon = 1
    Tue = 2
    Wed = 3
    Thu = 4
    Fri = 5
    Sat = 6
    
# 既可以用成员名称引用枚举常量，又可以直接根据value的值获得枚举常量
day1 = Weekday.Mon
print(day1)
print(Weekday.Tue)
print(Weekday['Tue'])
print(Weekday['Tue'].value)
print(Weekday(1))
for name,member in Weekday.__members__.items():
    print(name,'=>',member,',',member.value)
    
    
#练习
# 把Student的gender属性改造为枚举类型，可以避免使用字符串：

@unique
class Gender(Enum):
    Male = 0
    Female = 1
    
class Student(object):
    def __init__(self,name,gender):
        self.name = name
        self.gender = gender
        if isinstance(gender,Enum):
            print("gender type is Enum")
        
# Enum 可以把一组相关常量定义在一个class中，且class不可变 而且成员变量可以直接比较       
bart = Student('Bart', Gender.Male)
if bart.gender == Gender.Male:
    print('测试通过!')
else:
    print('测试失败!')

