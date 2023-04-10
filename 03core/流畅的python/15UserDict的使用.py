#!/usr/bin/env python
# -*- encoding: utf-8 -*-
"""
@File    :   15UserDict的使用.py
@Time    :   2023/04/10 12:58:25
@Author  :   owl
@Email   :   xxxxx@163.com
@Desp    :   https://docs.python.org/zh-cn/3/library/collections.html
"""
"""dict is written in c,UserDict in python"""
from collections import UserDict


# * 如果自定义类继承dict，c语言实现的get方法不会调用__missing__
class MyDict(dict):
    def __init__(self, factory):
        self._factory = factory

    def __missing__(self, key):
        print("__missing__", key)
        v = self._factory()
        self[key] = v
        return v


d = MyDict(list)
d["hello"].append(1)
print(d)
d.get("world")  # ? 并没有进入魔术方法
print(d)


class NewDict(UserDict):
    def __init__(self, factory):
        super().__init__()
        self._factory = factory

    def __missing__(self, key):
        print("__missing__", key)
        v = self._factory()
        self.data[key] = v
        return v


d = NewDict(list)
d.get("world")
print(d)
