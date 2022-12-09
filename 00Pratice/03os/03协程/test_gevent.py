from gevent import spawn,joinall,monkey;monkey.patch_all()
import timeit

import time
def task(pid):
    """
    Some non-deterministic task 非确定
    """
    time.sleep(0.5)
    print(f'Task {pid} done')


def synchronous():
    for i in range(10):
        task(i)

def asynchronous():
    g_l=[spawn(task,i) for i in range(10)]
    joinall(g_l)

if __name__ == '__main__':
    print('Synchronous:')
    print(timeit.timeit(synchronous,number=1))
    print('Asynchronous:')
    print(timeit.timeit(asynchronous,number=1))
