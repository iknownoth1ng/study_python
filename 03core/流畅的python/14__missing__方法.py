#!/usr/bin/env python
# -*- encoding: utf-8 -*-
"""
@File    :   14__missing__方法.py
@Time    :   2023/04/10 12:43:33
@Author  :   owl
@Email   :   xxxxx@163.com
@Desp    :   __missing__
"""
# defaultdict的使用
# __missing__,__getitem__

# * C语言实现的简单逻辑
# class MimicDict:
#     def __init__(self) -> None:
#         self.data = {}

#     def __getitem__(self, key):
#         if key in self.data.keys():
#             return self.data[key]
#         if hasattr(self.__class__, "__missing__"):
#             return self.__class__.__missing__(self, key)
#         raise KeyError(key)


# * 自定义dict，实现defaultdict简单功能
class MyDict(dict):
    def __init__(self, factory):
        self._factory = factory

    def __missing__(self, key):
        v = self._factory()
        self[key] = v
        return v


d = MyDict(list)
d["hello"].append(1)
print(d)  # {'hello': [1]}
