# 在测试环境下，每个线程都有自己的数据。使用局部变量最好，如果是全局变量必须加锁

import threading

#创建全局的ThreadLocal对象
local_school = threading.local()

def process_student():
	 # 获取当前线程关联的student
	std = local_school.student
	print('Hello,%s (in %s)' % (std,threading.current_thread().name))

def process_thread(name):
	#绑定ThreadLocal的student
	local_school.student = name
	process_student()

t1 = threading.Thread(target=process_thread,args=('Alice',),name="Thread-A")
t2 = threading.Thread(target=process_thread,args=('Bob',),name='Thread-B')
t1.start()
t2.start()
t1.join()
t2.join()

# 一个ThreadLocal变量虽然是全局变量，但是每个线程都只能读写自己线程的独立副本，互不干扰。