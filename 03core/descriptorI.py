#!/usr/bin/env python
# -*- encoding: utf-8 -*-
"""
@File    :   descriptor.py
@Time    :   2022/06/16 16:35:14
@Author  :   owl
@Email   :   xxxxx@163.com
@Desp    :   描述符
"""

# here put the import lib
"""
这就是描述符所解决的问题
描述符是property的升级版，允许你为重复的property逻辑编写单独的类来处理
"""


class NonNegative(object):
    """一个可以屏蔽负数的描述符"""

    def __init__(self, default):
        self.default = default
        self.data = {}

    def __get__(self, instance, owner):
        # 当调用描述符时 即：x.d
        # instance 就是调用的那个实例对象 x，如果是类对象则为None
        # owner 就是 type(x)
        return self.data.get(instance, self.default)

    def __set__(self, instance, value):
        # 当调用描述符时 即：x.d = val
        # instance 就是调用的那个实例对象 x
        # owner 就是 type(x)
        if value < 0:
            raise ValueError(f"设置有误: {value}（请使用非负数）")
        self.data[instance] = value


class Movie(object):
    # 定义描述符
    rating = NonNegative(0)
    budget = NonNegative(0)
    gross = NonNegative(0)

    def __init__(self, title, rating, budget, gross):
        self.title = title
        self.rating = rating
        self.budget = budget
        self.gross = gross

    def profit(self):
        return self.gross - self.budget


m = Movie("三傻大闹宝莱坞", 97, 964000, 1300000)
print("电影评分：", m.rating)
try:
    m.rating = -100
except ValueError as ret:
    print(ret)

print("电影预算：", m.budget)
try:
    m.budget = -4567
except ValueError as ret:
    print(ret)
