#!/usr/bin/env python
# -*- encoding: utf-8 -*-
"""
@File    :   面向对象编程VI.ipynb
@Time    :   2023/01/10 21:33:05
@Author  :   owl
@Email   :   xxxxx@163.com
@Desp    :   这是在真实类中使用数据验证器的方法：https://www.cnblogs.com/weiweivip666/p/17299024.html
"""

# here put the import lib
from CustomValidator import *


class Component:
    name = String(minsize=3, maxsize=10, predicate=str.isupper)
    kind = OneOf("wood", "metal", "plastic")
    quantity = Number(minvalue=0)

    def __init__(self, name, kind, quantity):
        self.name = name
        self.kind = kind
        self.quantity = quantity


Component("Widget", "metal", 5)
Component("WIDGET", "metle", 5)
Component("WIDGET", "metal", -5)
Component("WIDGET", "metal", "V")
c = Component("WIDGET", "metal", 5)
