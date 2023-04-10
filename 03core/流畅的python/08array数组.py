#!/usr/bin/env python
# -*- encoding: utf-8 -*-
"""
@File    :   08array数组.py
@Time    :   2023/04/10 10:18:45
@Author  :   owl
@Email   :   xxxxx@163.com
@Desp    :   数组
"""
# ? 已经有list了，为什么还有array？https://docs.python.org/zh-cn/3/library/array.html
"""
1.Python中的数组模块需要所有数组元素都具有相同类型
2.数组需要声明，列表不用(因为是python内置的)。
3.数组可以高效的存储数据(特别是面向大量数据时)。
4.数组非常适合数组运算，而列表不行(报错)。

那我们如何选择数组或列表呢？
场景一: 需要存储相对较短的元素序列且不进行数值运算，使用列表。
场景二: 元素序列很长，使用数组。因为数组结构提供了更有效的数据结构
场景三: 对元素组合进行数值计算，使用数组
"""
from array import array
from random import random

data = [random() for _ in range(10000)]
a = array("d", data)
print(data.__sizeof__() - a.__sizeof__())

with open("./array.bin", "wb") as f:
    a.tofile(f)

with open("./array.txt", "w") as f:
    f.write(repr(data))


b = array("d")
with open("./array.bin", "rb") as f:
    b.fromfile(f, 10)

print(b)
print(b[0])
