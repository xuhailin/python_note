from collections import Iterable
# 可迭代对象
print(isinstance([],Iterable))

print(isinstance({},Iterable))
print(isinstance((x for x in range(10)), Iterable))
print(isinstance("ADS",Iterable))
print(isinstance(100,Iterable))


# 能够被next()函数调用并不断返回下一值的对象称为迭代器 生成器
#生成器都是Iterator对象 但list dict str不是
# 使用iter()函数可以将可迭代对象变成Iterator
from collections import Iterator
print(isinstance(iter([]),Iterator))

#Iterator 是惰性求值的，不断通过next()函数返回下一个数据。
# Iterator 可以表示一个无限大的数据流，比如全体自然数，而list是无法表示的