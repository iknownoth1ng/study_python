from concurrent.futures import ThreadPoolExecutor
from threading import currentThread
import os,time,random

def task(n):
    print(f"{currentThread().getName()} is running, pid is {os.getpid()}")
    time.sleep(random.randint(1,3))
    return n*n

if __name__ == "__main__":
    pool=ThreadPoolExecutor(max_workers=5)
    
    pool.map(task,range(1,12))

    print('主')
