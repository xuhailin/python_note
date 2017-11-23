# 去除特定字符
# filter(lambda x:x!=".","123.456") 

#filter 函数用于过滤序列
#根据返回值是True还是false决定保留还是丢弃该元素

def is_odd(n):
    return n%2 == 1

L = list(filter(is_odd,[1,2,3,4,5,6,7]))
print("奇数集合为:\n",L)



def not_empty(s):
    return s and s.strip()

print(list(filter(not_empty,['A','','B',None,'C',''])))


print("用filter求素数:")
def _odd_iter():
    n=1
    while(True):
        n=n+2
        yield n

def _not_divisible(n):
    return lambda x : x % n > 0
    
def primes():
    yield 2
    it = _odd_iter()
    while True:
        n = next(it)
        yield n
        it = filter(_not_divisible(n),it)
# 打印1000以内的素数:
for n in primes():
    if n < 10:
        print(n)
    else:
        break
        
        
        
print("用filter求回数:")
def is_palindrome(n):
    s = str(n)
    length = len(s)
    for i in range(int(length/2)):
        if  s[i] != s[length-1-i]:
            return False
    return True    
    
    
# 测试:
output = filter(is_palindrome, range(1, 1000))
print('1~1000:', list(output))
if list(filter(is_palindrome, range(1, 200))) == [1, 2, 3, 4, 5, 6, 7, 8, 9, 11, 22, 33, 44, 55, 66, 77, 88, 99, 101, 111, 121, 131, 141, 151, 161, 171, 181, 191]:
    print('测试成功!')
else:
    print('测试失败!')