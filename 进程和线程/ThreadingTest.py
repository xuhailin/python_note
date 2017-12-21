# _thread(低级模块)和threading(高级模块)
# 启动一个线程就是把一个函数传入并创建Thread实例，然后调用start()开始执行：
import time,threading

# 新线程执行的代码：
def loop():
	print('thread %s is running...' % threading.current_thread().name)
	n = 0
	while n < 5:
		n = n + 1
		print('thread %s >>> %s' % (threading.current_thread().name,n))
		time.sleep(1)

	print('thread %s ended.' % threading.current_thread().name)

print('thread %s is running...' % threading.current_thread().name)
t = threading.Thread(target=loop,name='LoopThread')
t.start()
t.join()
print('thread %s ended.' % threading.current_thread().name)



# Lock   多进程和多进程最大的不同在于，多进程中，同一个变量，各自有一份拷贝存在于每个进程。多线程中，所有变量都有所有线程共享。

import time, threading

# 假定这是你的银行存款
balance = 0
lock = threading.Lock()

def change_it(n):
	# 先存后取，结果应该为0:
	global balance
	balance = balance + n
	balance = balance - n

def run_thread(n):
	for i in range(100000):
		# 先获取锁
		lock.acquire()
		try:
			# 作修改操作
			change_it(n)
		finally:
			# 改完之后释放锁
			lock.release()

t1 = threading.Thread(target=run_thread,args=(5,))
t2 = threading.Thread(target=run_thread,args=(8,))
t1.start()
t2.start()
t1.join()
t2.join()
print(balance)



# 小结
# 多线程编程，模型复杂，容易发生冲突，必须用锁加以隔离，同时，要小心死锁的发生。
# 由于python解释器设计有GIL的全局锁，导致了多线程无法利用多核。
