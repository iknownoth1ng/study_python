from multiprocessing import Process

n=100

def work():
    global n
    n=0
    print("子进程n：{}".format(n))

if __name__ == "__main__":
    __spec__ = "ModuleSpec(name='builtins', loader=<class '_frozen_importlib.BuiltinImporter'>)"

    p=Process(target=work,)
    p.start()
    p.join()

    print("主进程n：{}".format(n))
