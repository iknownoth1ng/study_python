#!/usr/bin/env python
# -*- encoding: utf-8 -*-
"""
@File    :  02jupyter.py
@Time    :  2024/11/29 15:14:10
@Author  :  owl
@Email   :  xxxxx@163.com
@Desp    :  https://developer.aliyun.com/article/1529841
"""


# %%
class HauntedBus:
    """A bus model haunted by ghost passengers"""

    def __init__(self, passengers=[]):
        self.passengers = passengers

    def pick(self, name):
        self.passengers.append(name)

    def drop(self, name):
        self.passengers.remove(name)


bus1 = HauntedBus()
bus1.pick("小明")
bus1.pick("小红")
print(bus1.passengers)  # 输出: ['小明', '小红']

bus2 = HauntedBus()
print(bus2.passengers)  # 输出: ['小明', '小红']
# * 原因解析
# 在Python中，默认参数是在函数定义的时候只初始化一次的，而不是每次调用函数时重新初始化。如果默认参数是一个可变类型/对象，那么后续对这个函数的调用将共享同一个默认参数对象。
