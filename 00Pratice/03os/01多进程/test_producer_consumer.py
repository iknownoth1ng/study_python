from multiprocessing import JoinableQueue,Process
import time

def producer(q,name,product):
    """生产者

    Parameters
    ----------
    q : _type_ queue
        _description_ 队列容器
    name : _type_
        _description_ 生产者名字
    product : _type_
        _description_ 生产的产品名字
    """
    for i in range(1,6):
        res=f"{product}{i}"
        time.sleep(0.5)
        print(f"{name} 生产了 {res}")
        q.put(res)
    q.join() #* 一直等待队列被取空，取空就会结束。
        
def consumer(q,name):
    """生产者

    Parameters
    ----------
    q : _type_
        _description_ 队列容器
    name : _type_
        _description_ 消费者名字
    """
    while True:
        time.sleep(1.5)
        res=q.get() #* 如果不是守护进程，会一直在这里等着取数据
        if res is None: break
        print(f"{name} 消费了 {res}")
        q.task_done() #* 像队列发送取完一个数据的信号
    
if __name__=="__main__":
    #* 容器
    q=JoinableQueue()
    p1=Process(target=producer,args=(q,"生产者1","包子"))
    p2=Process(target=producer,args=(q,"生产者2","饺子"))
    p3=Process(target=producer,args=(q,"生产者3","粽子"))
    c1=Process(target=consumer,args=(q,"雅木茶"))
    c2=Process(target=consumer,args=(q,"悟空"))
    c1.daemon = True #* 主进程结束，生产者结束
    c2.daemon = True
    
    #开始
    p_l=[p1,p2,p3,c1,c2]
    for p in p_l:
        p.start()
    
    #* 等到生产者结束，生产者结束，q一定结束。
    p_2=[p1,p2,p3]
    for p in p_2:
        p.join()
        
    print("主线程")

# 主进程等--->p1,p2,p3等---->c1,c2
# p1,p2,p3结束了,证明c1,c2肯定全都收完了p1,p2,p3发到队列的数据
# 因而c1,c2也没有存在的价值了,应该随着主进程的结束而结束,所以设置成守护进程
