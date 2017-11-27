# 错误处理  如果发生了错误，可以事先约定返回一个错误代码，这样就可以知道出错原因和出错位置

try:
    print('try...')
    r = 10 / 0
    print('result: ',r)
#可以用不同的except来获取不同类型的错误
except ZeroDivisionError as e:
    print('except:',e)
except ValueError as e:
    print('ValueError:',e)
finally:
    print('finally...')
print('end')

# try except 捕获异常时，会遵循继承关系，如果错误类型是子类的类型，也可以被捕获
# 还可以跨越多层调用

# 记录错误
import logging
def foo(s):
    return 10/int(s)

def bar(s):
    return foo(s) * 2

#多层调用
def main():
    try:
        bar('0')
    except Exception as e:
        print("except:",e)
        logging.exception(e)#打印错误信息后退出
    finally:
        print('finally...')

main()
print('END')

# 抛出错误 raise
# 定义一个错误类型
class FooError(ValueError):
    pass

def foo(s):
    n =int(s)
    if n == 0:
        raise FooError('invalid value: ', s)
    return 10 / n

#foo('0')


# 练习
#  运行下面的代码，根据异常信息，定位出错误源头，并修复
from functools import reduce

def str2num(s):
#    return int(s)
    try:
      return int(s)
    except ValueError as e:
        logging.exception(e)

def calc(exp):
    ss = exp.split('+')
    ns = map(str2num,ss)
    try:
        return reduce(lambda acc,x:acc + x , ns)
    except TypeError as e:
        print('TypeError',e)
def main2():
    r = calc('100 + 200 + 345')
    print('100 + 200 + 345 = ',r)
    # 7.6 出错
    r = calc('99 + 88 + 7.6')
    print('99 + 88 + 7.6 = ',r)

main2()
print('over')