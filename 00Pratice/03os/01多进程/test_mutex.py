from multiprocessing import Process,Lock
import time
import json

def search(name):
    # 模拟网络延迟
    time.sleep(1)
    dic=json.load(open(r"00Pratice\03os\01多进程\db.txt", "r"))
    print(f'{name} 查看剩余票数：{dic["count"]}')
    
def get(name,mutex):
    time.sleep(1)
    mutex.acquire() #* 加锁
    dic=json.load(open(r"00Pratice\03os\01多进程\db.txt", "r"))
    if dic["count"] > 0:
        dic["count"]=dic["count"]-1
        print(f"{name} 购票成功")
        time.sleep(3)
        json.dump(dic, open(r"00Pratice\03os\01多进程\db.txt", "w"))
    else:
        print(f"{name} 购票失败")
    mutex.release() #* 解锁

def task(name,mutex):
    #! 查票操作不要加锁，影响效率。
    search(name)
    get(name,mutex)

if __name__ =="__main__":
    #* 加锁
    mutex=Lock()
    for i in range(10):
        p=Process(target=task,args=(f"路人{i}",mutex))
        p.start()
    
