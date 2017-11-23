# 生成器 ()

# g = (x*x for x in range(10))

# 通过next()获得generator的下一个返回值
# next(g) #0
# next(g) #1

#可以迭代
# for n in g:
    # print(n)
    
# Fibonacci
# def fib(max):
    # n,a,b = 0,0,1
    # while n<max:
        # print(b) # yield b
        # a,b = b,a+b
        # n = n+1
    # return 'done'

#杨辉三角

def triangles():
    G = L = [1]
    while True:
        yield G
        G = []
        g = (v for v in L)
        pre = last = next(g)
        G.append(pre)
        while True:
            try:
                current = next(g)
                G.append(pre + current)
                pre = current
            except StopIteration as e:
                break
        G.append(last)
        L = G

def triangles():
    ret = [1]
	while True:
	    yield ret
		for i in range(1,len(ret)):
		    ret[i] = pre[i]+pre[i-1]
		ret.append(1)
		pre = ret[:]
n = 0
results = []
for t in triangles():
    print(t)
    results.append(t)
    n = n + 1
    if n == 10:
        break
if results == [
    [1],
    [1, 1],
    [1, 2, 1],
    [1, 3, 3, 1],
    [1, 4, 6, 4, 1],
    [1, 5, 10, 10, 5, 1],
    [1, 6, 15, 20, 15, 6, 1],
    [1, 7, 21, 35, 35, 21, 7, 1],
    [1, 8, 28, 56, 70, 56, 28, 8, 1],
    [1, 9, 36, 84, 126, 126, 84, 36, 9, 1]
]:
    print('测试通过!')
else:
    print('测试失败!')