#!/usr/bin/env python
# -*- encoding: utf-8 -*-
"""
@File    :   09内存视图.py
@Time    :   2023/04/10 10:50:45
@Author  :   owl
@Email   :   xxxxx@163.com
@Desp    :   内存视图
"""
# python底层的数据结构是用C语言写的，每次操作的时候都需要先拷贝一次，非常低效，于是引入一种协议buffer protocol，实现了这种协议的数据结构，会把自己的数据用c语言的api的形式暴露出来。外部直接通过调用c的api进行操作，不需要拷贝。https://docs.python.org/zh-cn/3/library/stdtypes.html#memoryview
# * 使用memoryview对象来调用c的api : (处理大型的二进制数据)

from array import array
from time import perf_counter as pc

numbers = array("h", [-1, 0, 1, 2, 3, 4])
mv = memoryview(numbers)
mv[1] = 5
print(numbers)

t0 = pc()
numbers[:4]
tnumber = pc() - t0
print(tnumber)

t0 = pc()
mv[:4]
tmv = pc() - t0
print(tmv)

print(tnumber / tmv)
