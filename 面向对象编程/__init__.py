#面向对象编程  OOP  
# 把对象作为程序的基本单元，一个对象包含了数据和操作数据的函数

#面向过程
# std1 = {'name':'Michael','score':98}
# std2 = {'name':'Bob','score':81}

# 处理
# def print_score(std):
    # print('%s: %s' % (std['name'],std['score']))
    
    
#面向对象
class Student(object):

    def __init__(self, name, score):
        self.name = name
        self.score = score

    def print_score(self):
        print('%s: %s' % (self.name, self.score))
        


if __name__ == '__main__':
    bart = Student('Bart Simpson', 59)
    lisa = Student('Lisa Simpson', 87)
    bart.print_score()
    lisa.print_score()