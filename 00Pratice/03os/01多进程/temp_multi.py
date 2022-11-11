# 查看子进程的父进程id
import random
import time
from multiprocessing import Process


def task(n):
    time.sleep(random.randint(1, 3))
    print("--------->{}".format(n))
    

if __name__ == "__main__":
    __spec__ = "ModuleSpec(name='builtins', loader=<class '_frozen_importlib.BuiltinImporter'>)"

    start_time = time.time()
    p1=Process(target=task,args=(1,))
    p2=Process(target=task,args=(2,))
    p3=Process(target=task,args=(3,))
    p_l=[p1,p2,p3]
    
    for p in p_l:
        p.start() # 仅仅只是给操作系统发送了一个信号
        p.join()


    print('--------->4')
