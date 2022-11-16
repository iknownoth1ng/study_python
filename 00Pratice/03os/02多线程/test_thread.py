from threading import Thread,Lock
import time

n=100

def task(mutex):
    global n 
    mutex.acquire()
    temp=n
    time.sleep(0.1)
    n=temp-1
    mutex.release()

if __name__ == "__main__":
    mutex=Lock()
    t_L=[]
    for _ in range(100):
        t=Thread(target=task,args=(mutex,))
        t_L.append(t)
        t.start()
        
    for t in t_L:
        t.join()
    
    print('主线程',n) #! 0
