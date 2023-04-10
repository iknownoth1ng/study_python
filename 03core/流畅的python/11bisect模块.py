#!/usr/bin/env python
# -*- encoding: utf-8 -*-
"""
@File    :   11bisect模块.py
@Time    :   2023/04/10 11:22:49
@Author  :   owl
@Email   :   xxxxx@163.com
@Desp    :   bisect https://docs.python.org/zh-cn/3/library/bisect.html
"""
# * bisection algorithm
import bisect

a = [3, 5, 6, 10]
# a.sort() # 保证有序
print(bisect.bisect(a, 6))  # 3
print(bisect.bisect_right(a, 6))  # 3
print(bisect.bisect_left(a, 6))  # 2

bisect.insort(a, 6)
bisect.insort_right(a, 6)
bisect.insort_left(a, 6)
print(a)
