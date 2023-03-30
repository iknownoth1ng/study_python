#!/usr/bin/env python
# -*- encoding: utf-8 -*-
"""
@File    :   copyII.py
@Time    :   2023/03/30 19:32:40
@Author  :   owl
@Email   :   xxxxx@163.com
@Desp    :   深拷贝和浅拷贝
"""
import copy

# * 一个列表中包含列表元素，当列表元素发生改变时，如果只是浅拷贝，拷贝后的对象也会变化，而深拷贝的对象是不会改变的。

a = [1, 2, 3, [4, 5, 6]]
c = copy.copy(a)  # 浅拷贝
d = copy.deepcopy(a)  # 深拷贝
print("a,c,d没有区别")
print(a)
print(c)
print(d)
a[2] = "tt"
print("c,d没有区别")
print(a)
print(c)
print(d)
a[3][0] = "haha"
print("c,d有区别")
print(a)
print(c)
print(d)


a = [1, 2, 3, [4, 5, 6]]
b = a
b[2] = "tt"
print(a)
print(b)
