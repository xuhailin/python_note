# import os

# print('Process (%s) start...' % os.getpid())

#不能在window下运行
# pid = os.fork()
# fork()系统调用，非常特殊。普通的函数调用，调用一次，返回一次，但是fork()调用一次，返回两次
# 子进程永远返回0 而父程序返回子进程的ID.
# if pid == 0:
    # 返回子进程
    # print('I am child process (%s) and my parent is %s' % (os.getpid(),os.getpid()))
# else:
    # print('I (%s) just create a child process (%s).' % (os.getpid(),pid))
    
# multiprocessing 跨平台版本的多进程模块

from multiprocessing import Process

import os

#子进程要执行的代码
def run_proc(name):
    print('Run child process %s (%s)...' % (name,os.getpid()))
    
if __name__== '__main__':
    print('Parent process %s.' % os.getpid())
    #创建子进程时只需要传入一个执行函数和函数的参数，创建一个Process实例，用start()方法启动
    p = Process(target = run_proc,args = ('test',))
    print('Child process will start.')
    p.start()
    p.join()
    # join()方法可以等待子进程结束后再继续往下运行，通常用于同步
    print('Child process end.')
    
    
    
# Pool
# 如果要启动大量的子进程，可以用进程池的方式批量创建子进程

from multiprocessing import Pool
import os,time,random

def long_time_task(name):
    print('Run task %s (%s)...' % (name,os.getpid()))
    start = time.time()
    time.sleep(random.random()*3)
    end = time.time()
    print('Task %s runs %0.2f seconds.' % (name,(end-start)))
    
if __name__ == '__main__':
    print('Parent process %s.' % os.getpid())
    p = Pool(4) # 意味这同时可以跑几个进程
    for i in range(5):
        p.apply_async(long_time_task,args = (i,))
    print('waiting for all subprocesses done...')
    p.close()
    p.join()
    print('All subprocesses done.')


# 子进程  subprocess
# 控制子进程的输入和输出
import subprocess
print('$ nslookup www.python.org')
r = subprocess.call(['nslookup','www.python.org'])
print('Exit code:',r)

# 如果子进程还需要输入，则可以通过communicate()方法输入
print('$ nslookup')
p = subprocess.Popen(['nslookup'],stdin=subprocess.PIPE,stdout=subprocess.PIPE,stderr=subprocess.PIPE)
output,err = p.communicate(b'set q=mx\npython.org\nexit\n')
print(output.decode('utf-8'))
print('Exit code:',p.returncode)

#进程之间的相互通信  Queue Pipes
from multiprocessing import  Process,Queue
import os,time,random

# 写数据进程执行的代码
def write(q):
    print('Process to write: %s ' % os.getpid())
    for value in ['A','B','C']:
        print('Put %s to queue...' % value)
        q.put(value)
        time.sleep(random.random())

# 读数据进程执行的代码
def read(q):
    print('Process to read: %s' % os.getpid())
    while True:
        value = q.get(True)
        print('Get %s from queue.' % value)


if __name__ == '__main__':
# 父进程创建Queue,并传给各个子进程：
    q = Queue()
    pw = Process(target=write,args=(q,))
    pr = Process(target=read,args=(q,))
# 启动子进程pw 写入
    pw.start()
# 启动子进程pr 读取：
    pr.start()
# 等待pw结束：
    pw.join()
# pr进程里是死循环，无法等待其结束，只能强行终止：
    pr.terminate()

# 在unix/Liunx下，可以使用fork()调用实现多进程
# 要实现跨平台的多进程，可以使用multiprocessing模块
# 进程间通信是通过Queue Pipes等实现的