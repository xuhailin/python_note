# 文档测试 
# python   自动执行写在注释中的代码
# python内置的文档测试doctest模块可以直接提取注释中的代码并执行测试
# doctest严格按照Python交互式命令行的输入和输出来判断结果是否正确，只有测试异常的时候，可以用...表示中间一大段烦人的输出
def abs(n):
    '''
    Function to get absolute value of number.

    Example:

    >>> abs(1)
    1
    >>> abs(-1)
    1
    >>> abs(0)
    0
    '''
    return n if n>=0 else (-n)
    
class Dict(dict):
    '''
    Simple dict but also support access as x.y style.

    >>> d1 = Dict()
    >>> d1['x'] = 100
    >>> d1.x
    100
    >>> d1.y = 200
    >>> d1['y']
    200
    >>> d2 = Dict(a=1, b=2, c='3')
    >>> d2.c
    '3'
    >>> d2['empty']
    Traceback (most recent call last):
        ...
    KeyError: 'empty'
    >>> d2.empty
    Traceback (most recent call last):
        ...
    AttributeError: 'Dict' object has no attribute 'empty'
    '''
    #当异常信息太多时,可以用...代替异常的中间内容
    def __init__(self, **kw):
        super(Dict, self).__init__(**kw)

    def __getattr__(self, key):
        try:
            return self[key]
        except KeyError:
            raise AttributeError(r"'Dict' object has no attribute '%s'" % key)

    def __setattr__(self, key, value):
        self[key] = value

#练习 
# 对函数fact(n) 编写doctest并执行

def fact(n):
    '''
    Calculate 1*2*...*n
    
    Example:
    
    >>> fact(1)
    1
    >>> fact(10)
    3628800
    >>> fact(-1)
    Traceback (most recent call last):
        ...
    ValueError
    '''
    if n<1:
        raise ValueError()
    if n == 1:
        return 1
    return n * fact(n-1)
      
if __name__=='__main__':
    import doctest
    doctest.testmod()
   
# 当注释里面的测试信息输入和输出有问题时，就会报错

#小结
# doctest非常有用,不但可以用来测试，还可以直接作为示例代码。通过某些文档生成工具，可以自动把包含doctest的注释提取出来