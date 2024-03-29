# 思考下列代码的执行结果有哪些情况，为什么？
from multiprocessing  import Process
import time

def foo():
    print("123")
    time.sleep(1)
    print("end123")

def bar():
    print("456")
    time.sleep(1)
    print("end456")

if __name__ == "__main__":
    p1 = Process(target=foo)
    p2 = Process(target=bar)
    p1.daemon = True
    p1.start()
    p2.start()

    print("主进程结束")
