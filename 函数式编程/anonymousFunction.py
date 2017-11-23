# 匿名函数 lambda表示匿名函数 lambda x: x*x 
# 冒号前面的x代表函数参数
# 限制： 只能有一个表达式，就是该表达式的结果，不用return

#用匿名函数改造
def is_odd(n):
    return n%2 == 1
L = list(filter(is_odd,range(1,20)))
print(L)


L2 = list(filter(lambda n: n%2 == 1,range(1,20)))    
print(L2)