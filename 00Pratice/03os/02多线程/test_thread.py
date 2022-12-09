from threading import Thread
import time

def task(name):
    print(f"{name} is running")
    time.sleep(1)
    print(f"{name} is done")

if __name__ == "__main__":
    t1=Thread(target=task,args=("子线程1",))
    t1.start()

    print("主线程") #* 资源角度看是主进程，执行角度看是主线程
    
