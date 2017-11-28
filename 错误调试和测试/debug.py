# 调试

#1. 用print将可能有问题的变量打印出来看（麻烦，会包含很多垃圾信息）
#2. 断言 替代print()  python -0 参数来关闭assert
def foo(s):
    n = int(s)
    assert n != 0,'n is zero'
    return 10 / n
    
def main():
    foo('0')
    
#3. logging  不会抛出错误，而且可以输出到文件
import logging
#配置指定记录信息的级别，有debug,info,warning,error等几个级别，当我们指定levle = INFO时，logging的debug就不起作用了
logging.basicConfig(level = logging.INFO)

s = '0'
n = int(s)
logging.info('n =%d' % n)
print(10 / n)

#pdb 启动Python的调试器 让程序可以单步执行，可以随时查看运行状态 python -m pdb **.python
#输入命令n可以单步执行代码 输入p 变量名查看变量 输入q结束调试
# import pdb  pdb.set_trace()可以添加设置一个断点 命令c可以继续运行 p可以查看变量