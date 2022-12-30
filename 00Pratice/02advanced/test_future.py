import time
from concurrent.futures import Future,ThreadPoolExecutor,ProcessPoolExecutor

def func(value):
    time.sleep(1)
    print(value)

# 创建线程池
pool=ThreadPoolExecutor(max_workers=5)

# 创建进程池
# pool=ProcessPoolExecutor(max_workers=5)

for i in range(10):
    fut=pool.submit(func,i)
    print(fut)