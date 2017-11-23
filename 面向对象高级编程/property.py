# 在绑定属性时，如果我们直接把属性暴露出去，会没有办法检查参数,导致参数值被更改

#我们可以将其变成私有属性，在开放出get和set方法控制输入，但是这样过于繁琐

#property装饰器  把一个方法当做属性调用
class Student(object):
    
    #get方法只要加@property 就能变成属性，同时会创建一个.setter方法
    @property
    def score(self):
        return self.score
        
    @score.setter
    def score(self, value):
        if not isinstance(value, int):
            raise ValueError('score must be an integer!')
        if value < 0 or value > 100:
            raise ValueError('score must between 0 ~ 100!')
        self._score = value

s = Student()
s.score = 60

# s.score = 999 出错

class Student2(object):

    @property
    def birth(self):
        return 5
        
#不定义setter方法就是一个只读属性
s2 = Student2()
#s2.birth = 5

# 练习 
# 请利用@property给一个Screen对象加上width和height属性，以及一个只读属性resolution：


class Screen(object):
    
    @property
    def width(self):
        return self._width
 
    @width.setter
    def width(self,width):
        self._width = width

    @property
    def height(self):
        return self._height
 
    @height.setter
    def height(self,height):
        self._height = height 
   
    @property
    def resolution(self):
        return self.width * self.height
        
        
# 测试:
s = Screen()
s.width = 1024
s.height = 768
print('resolution =', s.resolution)
if s.resolution == 786432:
    print('测试通过!')
else:
    print('测试失败!')





















