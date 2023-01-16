import threading
import time

lock = threading.Lock()
n = 0


def foo():
    global n
    with lock:
        temp = n
        time.sleep(0.1)
        n = temp + 1  #! 不安全


threads = []
for _ in range(100):
    t = threading.Thread(target=foo)
    threads.append(t)
    t.start()

for t in threads:
    t.join()

print(n)
