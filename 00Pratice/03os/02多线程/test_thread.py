from threading import Thread,Semaphore,currentThread
import time,random

sm=Semaphore(3)

def task():
    with sm: #* 等效于sm.acquire()  sm.release()
        print(f"{currentThread().getName()} in")
        time.sleep(random.randint(1,3))
    
if __name__ == "__main__":
    for _ in range(10):
        t=Thread(target=task)
        t.start()
