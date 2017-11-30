# -*- coding: utf-8 -*-
# 序列化
# 变量从内存中变成可存储或传输的过程
# 序列化之后，可以把序列化后的内容写入到磁盘，反过来，就是反序列化，把变量内容从序列化的对象重新读到内存里

import pickle
import sys
d = dict(name='Bob2',age = 20,score = 88)
pickle.dumps(d)
# 把任意对象序列化成一个bytes 然后可以将这个bytes写入文件
# pickle.dump()直接把对象序列化后写入一个file－like Object

f = open('dump.txt','wb')
pickle.dump(d,f)
f.close()

f= open('dump.txt','rb')
d = pickle.load(f)
f.close()
print(d)


# JSON
# 在不同编程语言之间传递对象，就必须将对象序列化成标准格式 比如xml json
import json
d = dict(name="Bob2",age = 20,score = 90)
j = json.dumps(d)
print(j)
# dumps()方法可以直接返回一个str 内容就是标准的file－like object
# 反序列化
json_str = '{"age":20,"isChild":false}'
l = json.loads(json_str)
print(l)

# JSON进阶
# dict对象可以直接序列化为JSON的{} 用class表示一个对象
class Student(object):
	def __init__(self,name,age,score):
		self.name = name
		self.age = age
		self.score = score

#由于Student不是一个可序列化的对象，但是dumps可以传一个参数default，可以将任意一个对象变成可以序列为json的对象，就是转换函数
def student2dict(std):
	return {
		'name':std.name,
		'age':std.age,
		'score':std.score
	}
s = Student('Bob',20,100)
print(json.dumps(s,default=student2dict))
print(json.dumps(s,default=lambda obj:obj.__dict__)) # 也可以直接变成dict实例

# 反序列
def dict2student(d):
	return Student(d['name'],d['age'],d['score'])
json_str = '{"age": 20, "score": 88, "name": "Bob"}'
print(json.loads(json_str,object_hook=dict2student))

# 练习
# 对中文进行JSON序列化时，json.dumps()提供了一个ensure_ascii参数，观察该参数对结果的影响：

# ensure_ascii会进行转码 默认为true
obj = dict(name='小明',age = 20)
s = json.dumps(obj,ensure_ascii=False)
print(s)