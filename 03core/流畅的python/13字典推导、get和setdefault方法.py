#!/usr/bin/env python
# -*- encoding: utf-8 -*-
"""
@File    :   13字典推导、get和setdefault方法.py
@Time    :   2023/04/10 12:07:58
@Author  :   owl
@Email   :   xxxxx@163.com
@Desp    :   字典推导
"""

D = [("China", 86), ("Australia", 61)]

# * 方法0
d = dict(D)
print(d)

# * 方法1
d1 = {}
for country, code in D:
    d1[country] = code

print(d1)
# * 方法2
d2 = {country: code for country, code in D}
print(d2)

# * 方法3
keys = ["China", "Australia"]
codes = [86, 61]

d3 = {country: code for country, code in zip(keys, codes)}
print(d3)


# * get方法
d = {"hello": 1}

# d["world"]  #! KeyError: 'world'

if "world" in d:
    print(d["world"])

a = d.get("world")
print(a)
a = d.get("world", -1)
print(a)

# *setdefault方法
l = ["hello", "world", "hello", "python"]
d = {}
for idx, word in enumerate(l):
    # if word in d.keys():
    #     d[word].append(idx)
    # else:
    #     d[word] = []
    #     d[word].append(idx)
    d.setdefault(word, []).append(idx)

print(d)

# * defaultdict
from collections import defaultdict

l = ["hello", "world", "hello", "python"]
d = defaultdict(list)
for idx, word in enumerate(l):
    d[word].append(idx)

print(d)
