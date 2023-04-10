#!/usr/bin/env python
# -*- encoding: utf-8 -*-
"""
@File    :   07排序.py
@Time    :   2023/04/10 10:12:47
@Author  :   owl
@Email   :   xxxxx@163.com
@Desp    :   sorted和list.sort
"""

a = [2, 1, 3]
b = sorted(a)  # ? 会生成一个新的列表
print(a)
print(b)
print(a is b)

a.sort()  # ? 直接在a中操作
print(a)

a = ["a", "B", "C"]
b = sorted(a)
print(b)  # ['B', 'C', 'a']
b = sorted(a, key=str.lower)
print(b)  # ['a', 'B', 'C']
