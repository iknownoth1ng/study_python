#!/usr/bin/env python
# -*- encoding: utf-8 -*-
"""
@File    :   06序列增量赋值.py
@Time    :   2023/04/10 09:58:00
@Author  :   owl
@Email   :   xxxxx@163.com
@Desp    :   序列增量赋值
"""
# * 列表的增量赋值
a = list(range(5))
b = list(range(5, 10))

temp = a
# a = a + b  # ? 加号会生成一个新的列表，运算符重载看到+号，会调用__add__()方法
# print(a, temp is a)
print(a.__add__)

a += b  # ? 在a的后面追加。会调用__iadd__()方法
print(a, temp is a)
print(a.__iadd__)

# * 元组的增量赋值
a = (1, 2, 3)
b = (4, 5, 6)
temp = a
# a = a + b
# print(a, temp is a)
print(a.__add__)

a += b  # ? 元组仍然会生成一个新的元组，元组没有__iadd__()方法，还是会调用__add__()方法。
print(a, temp is a)
