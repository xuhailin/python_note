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
    print('Task %s runs %0.2f seconds.' % (name,(end-start))
    
if __name == '__main__'