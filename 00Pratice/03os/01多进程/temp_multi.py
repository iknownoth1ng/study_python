# 查看子进程的父进程id
import os
import time
from multiprocessing import Process


def task(name):
    print("{} is running".format(name))
    time.sleep(3)

if __name__ == "__main__":
    __spec__ = "ModuleSpec(name='builtins', loader=<class '_frozen_importlib.BuiltinImporter'>)"

    p1=Process(target=task,args=('子进程1',))
    p2=Process(target=task,args=('子进程2',))
    p3=Process(target=task,args=('子进程3',))

    p1.start() # 仅仅只是给操作系统发送了一个信号
    p2.start() 
    p3.start() 

    # p1.join() # 等待子进程执行完毕
    # p2.join() 
    # p3.join() 
    print('主进程{}，父id{}'.format(os.getpid(),os.getppid()))


