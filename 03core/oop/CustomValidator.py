#!/usr/bin/env python
# -*- encoding: utf-8 -*-
"""
@File    :   面向对象编程VI.ipynb
@Time    :   2023/01/10 21:28:57
@Author  :   owl
@Email   :   xxxxx@163.com
@Desp    :   自定义验证器需要从 Validator 继承，并且必须提供 validate() 方法以根据需要测试各种约束。
"""

# here put the import lib
from AbstractValidator import Validator

"""
这是三个实用的数据验证工具：

1. OneOf 验证值是一组受约束的选项之一。

2. Number 验证值是否为 int 或 float。根据可选参数，它还可以验证值在给定的最小值或最大值之间。

3. String 验证值是否为 str。根据可选参数，它可以验证给定的最小或最大长度。它还可以验证用户定义的 predicate。
"""


class OneOf(Validator):
    def __init__(self, *options):
        self.options = set(options)

    def validate(self, value):
        if value not in self.options:
            raise ValueError(f"Expected {value!r} to be one of {self.options!r}")


class Number(Validator):
    def __init__(self, minvalue=None, maxvalue=None):
        self.minvalue = minvalue
        self.maxvalue = maxvalue

    def validate(self, value):
        if not isinstance(value, (int, float)):
            raise TypeError(f"Expected {value!r} to be an int or float")
        if self.minvalue is not None and value < self.minvalue:
            raise ValueError(f"Expected {value!r} to be at least {self.minvalue!r}")
        if self.maxvalue is not None and value > self.maxvalue:
            raise ValueError(f"Expected {value!r} to be no more than {self.maxvalue!r}")


class String(Validator):
    def __init__(self, minsize=None, maxsize=None, predicate=None):
        self.minsize = minsize
        self.maxsize = maxsize
        self.predicate = predicate

    def validate(self, value):
        if not isinstance(value, str):
            raise TypeError(f"Expected {value!r} to be an str")
        if self.minsize is not None and len(value) < self.minsize:
            raise ValueError(
                f"Expected {value!r} to be no smaller than {self.minsize!r}"
            )
        if self.maxsize is not None and len(value) > self.maxsize:
            raise ValueError(
                f"Expected {value!r} to be no bigger than {self.maxsize!r}"
            )
        if self.predicate is not None and not self.predicate(value):
            raise ValueError(f"Expected {self.predicate} to be true for {value!r}")
