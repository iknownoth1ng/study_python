from multiprocessing import Process
import os

def task():
    print(f"子进程ID：{os.getpid()},父进程ID：{os.getppid()}")

if __name__ == "__main__":
    p1=Process(target=task)
    p1.start()

    print("主进程ID",os.getpid()) 
    
