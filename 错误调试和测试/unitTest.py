# 单元测试
#  对于一个模块 一个函数或者一个类来进行正确性检验的测试工作

class Dict(dict):
	def __init__(self,**kw):
		super().__init__(**kw)

	def __getattr__(self, item):
		try:
			return self[item]
		except KeyError:
			raise AttributeError(r"'Dict' object has no attribute %s" % item)

	def __setattr__(self, key, value):
		self[key] = value

# 一般测试
d = Dict(a=1,b=2)
d['a']
d.a

# 单元测试 unittest模块
# 以test开头的方法就是测试方法，不以test开头的方法不被认为是测试方法，测试的时候不需要执行

import unittest
class TestDict(unittest.TestCase):

	def test_init(self):
		d = Dict(a = 1,b = 'test')
		self.assertEqual(d.a,1)
		self.assertEqual(d.b,'test')
		self.assertTrue(isinstance(d,dict))

	def test_key(self):
		d = Dict()
		d['key'] = 'value'
		self.assertEqual(d.key,'value')

	def test_attr(self):
		d = Dict()
		d.key = 'value'
		self.assertTrue('key' in d)
		self.assertEqual(d['key'],'value')

# 通过d['empty']访问不存在的key时，断言会抛出KeyError
	def test_keyerror(self):
		d = Dict()
		with self.assertRaises(KeyError):
			value = d['empty']

# 通过d.empty 访问不存在的key时，抛出AttributeError
	def test_attrerror(self):
		d = Dict()
		with self.assertRaises(AttributeError):
			value = d.empty

	# setUp和tearDown方法会在调用每一个测试方法的前后被执行 比如可以用在数据库方面 连接数据库和关闭数据库
	def setUp(self):
		print('setUp...')

	def tearDown(self):
		print('tearDown...')

# 可以直接在文件中运行  也可以通过python test.py 也可以在命令行通过-m unittest test 直接运行单元测试
if __name__ == '__main__':
	unittest.main()