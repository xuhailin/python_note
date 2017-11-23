def f(x):
    return x * x;
    
r  = map(f,[1,2,3,4,5,6,7,8,9])
print(list(r))

#reduce  把一个函数作用在一个序列上 吧结果集合和序列的下一个元素做运算
#reduce(f,[x1,x2,x3,x4]) = f(f(f(x1,x2),x3),x4)

from functools import reduce
def add(x,y):
    return x+y

sum = reduce(add,[1,3,5,7,9])
print("sum = {}".format(sum))


#练习
def normalize(name):
    return name[0].upper()+name[1:].lower()

# 测试:
L1 = ['adam', 'LISA', 'barT']
L2 = list(map(normalize, L1))
print(L2)

def prod(L):
    return reduce(lambda x,y:x*y ,L)

print('3 * 5 * 7 * 9 =', prod([3, 5, 7, 9]))
if prod([3, 5, 7, 9]) == 945:
    print('测试成功!')
else:
    print('测试失败!')

def str2float(s):
    def chrInt(c):
       return int(c)
    i = s.find(".")
    s = s[:i]+s[i+1:]
    num = reduce(lambda x,y: x*10+y,map(chrInt,s))
    print(num)  
    p = 0
    if i != -1:
        p = len(s) - i
    return num * pow(10,-p)

print('str2float(\'123.4567\') =', str2float('123.4567'))
if abs(str2float('123.4567') - 123.4567) < 0.00001:
    print('测试成功!')
else:
    print('测试失败!')