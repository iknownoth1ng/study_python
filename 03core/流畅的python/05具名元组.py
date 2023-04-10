#!/usr/bin/env python
# -*- encoding: utf-8 -*-
"""
@File    :   05具名元组.py
@Time    :   2023/04/10 00:56:37
@Author  :   owl
@Email   :   xxxxx@163.com
@Desp    :   具名元组 https://docs.python.org/zh-cn/3/library/collections.html
"""
from collections import namedtuple

a = {"name": "shanghai", "population": 100}
# * name,population 元组的话一般只能用注释来记录
a = ("shanghai", 100)

# * 使用具名元组
City = namedtuple("City", "name population")
a = City("Shanghai", 100)
b = a.name
c = a._replace(name="Beijing")
d = a._asdict()
print(a, type(a), id(a))
print(c, id(c))
print(b)
print(d)

d = {"name": "Guangzhou", "population": 200}
e = City(**d)
print(e)
