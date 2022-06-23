#!/usr/bin/env python
# -*- encoding: utf-8 -*-
'''
@File    :   gcI.py
@Time    :   2022/06/22 11:11:10
@Author  :   owl
@Email   :   xxxxx@163.com
@Desp    :   python的垃圾回收机制
'''

# here put the import lib
import gc
import os
import psutil
import sys

# 显示当前 python 程序占用的内存大小


def show_memory_info(hint):
    pid = os.getpid()
    p = psutil.Process(pid)

    info = p.memory_full_info()
    memory = info.uss / 1024./1024
    print('{} memory used :{} MB'.format(hint, memory))


def func():
    show_memory_info('initial')
    # global a
    a = {i for i in range(10000000)}
    show_memory_info('after a created')
    # return a


if __name__ == '__main__':
    func()
    show_memory_info('finished')
    # initial memory used :18.1640625 MB
    # after a created memory used :586.8515625 MB
    # finished memory used :18.796875 MB

    '''
    函数内部声明的列表a是局部变量，在函数返回后，
    局部变量的引用会注销掉；此时，列表a所指代对象的引用数为0,
    Python便 会执行垃圾回收，因此之前占用的大量内存就又回来了。
    
    新的这段代码中，global a表示将a声明为全局变量。
    那么，即使函数返回后，列表的弓I用依然存在，
    于是对象就不会被垃圾回收掉，依然占用 大量内存。
    同样，如果我们把生成的列表返回，然后在主程序中接收，
    那么引用依然存在，垃圾回收就不会被触发，大量内存仍然被占用着：'''

    # 引用计数
    a = []
    print(sys.getrefcount(a))

    def func(a):
        print(sys.getrefcount(a))

    func(a)

    print(sys.getrefcount(a))

    # 手动释放内存
    show_memory_info('initial')
    a = {i for i in range(10000000)}
    show_memory_info('after a created')
    del a
    gc.collect()
    show_memory_info('finished')
    # print(sys.getrefcount(a))

    # 循环引用
    def func2():
        show_memory_info('initial')
        a = [i for i in range(10000000)]
        b = [i for i in range(10000000)]
        show_memory_info('after a created')
        a.append(b)
        b.append(a)

    func2()
    gc.collect()  # 手动回收循环引用的对象
    show_memory_info('finished')

    # 可视化引用关系包 objgraph
    import objgraph

    a = [1, 2, 3]
    b = [4, 5, 6]

    a.append(b)
    b.append(a)
    objgraph.show_refs(a)
