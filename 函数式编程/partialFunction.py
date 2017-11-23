# 偏函数 functools.partial  创建一个偏函数

import functools
int2 = functools.partial(int,base=2)
print(int2('1000000'))

# 总结：functools.partial的作用就是把一个函数的某些参数给固定住，也就是设置默认值，返回一个新的函数，新的函数操作起来会更简单

max2 = functools.partial(max,10,20)
print(max2(5,6,7))

#相当于 args = (10,20,5,6,7) max(*args)

#创建偏函数时，可以接受函数对象，*agrgs,**kw这三个参数