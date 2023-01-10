#!/usr/bin/env python
# -*- encoding: utf-8 -*-
"""
@File    :   面向对象编程VI.ipynb
@Time    :   2023/01/10 21:27:37
@Author  :   owl
@Email   :   xxxxx@163.com
@Desp    :   验证器是一个用于托管属性访问的描述器。在存储任何数据之前，它会验证新值是否满足各种类型和范围限制。如果不满足这些限制，它将引发异常，从源头上防止数据损坏。
这个 Validator 类既是一个 abstract base class 也是一个托管属性描述器。
"""

# here put the import lib
from abc import ABC, abstractmethod


class Validator(ABC):
    def __set_name__(self, owner, name):
        self.private_name = f"_{name}"

    def __get__(self, obj, objtype=None):
        return getattr(obj, self.private_name)

    def __set__(self, obj, value):
        self.validate(value)
        setattr(obj, self.private_name, value)

    @abstractmethod
    def validate(self, value):
        pass
