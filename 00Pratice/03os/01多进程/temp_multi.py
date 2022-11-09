# 查看子进程的父进程id
from multiprocessing import Process
import time
import os

def task():
    print("{} is running, parent id is {}".format(os.getpid(),os.getppid()))
    time.sleep(3)
    print("{} is done, parent id is {}".format(os.getpid(),os.getppid()))

if __name__ == "__main__":
    __spec__ = "ModuleSpec(name='builtins', loader=<class '_frozen_importlib.BuiltinImporter'>)"

    p=Process(target=task)
    p.start() # 仅仅只是给操作系统发送了一个信号
    p.terminate() # 发送中断信号
    # print(p.is_alive()) # True

    p.join() # 或者time.sleep(3) 等待操作系统中断该进程
    print(p.is_alive()) # false
    
    p.join() # 等待子进程执行完毕
    print('主进程')

    print(p.name) # 未起名会默认Process-1

