#!/usr/bin/env python
# -*- encoding: utf-8 -*-
"""
@File    :   10双端队列.py
@Time    :   2023/04/10 11:08:17
@Author  :   owl
@Email   :   xxxxx@163.com
@Desp    :   双端队列 https://docs.python.org/zh-cn/3/library/collections.html
"""
# deque(double-ended queue) is thread-safe
# 对从队列的头尾元素的操作数据进行了性能优化
# 结合append + pop 可以当作FILO 栈使用
from collections import deque

# from queue import Queue,LifoQueue,PriorityQueue

dq = deque(range(10), maxlen=10)
print(dq)
dq.rotate(3)  # *右移
print(dq)
dq.rotate(-2)  # * 左移
print(dq)
dq.append(-1)
print(dq)
dq.appendleft(-2)
print(dq)
dq.extend([11, 22, 33])
print(dq)
dq.extendleft([10, 20, 30, 40])
print(dq)

# *作为一个栈
dq = deque(range(0))
dq.append(1)
print(dq)
dq.append(2)
print(dq)
dq.pop()
print(dq)
dq.pop()
print(dq)
