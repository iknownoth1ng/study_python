#!/usr/bin/env python
# -*- encoding: utf-8 -*-
"""
@File    :   12hash函数.py
@Time    :   2023/04/10 11:29:32
@Author  :   owl
@Email   :   xxxxx@163.com
@Desp    :   哈希函数
"""
"""
Important Points:
1. __hash__ must never change
2. dict,list,set are all inherently mutable and therefore unhashable.
str,bytes,frozenset,and tuple are immutable and therefore hashable.
3. dict's key has to be hashable
4. __hash__ is only called once when an object is inserted into a dict or a set

Contract:
If a==b then hash(a)==hash(b). __eq__() is equal then hash() is equal
If hash(a) == hash(b), then a might equal b. hash() is equal then __eq__() might equal
If hash(a) != hash(b) ,then a != b. hash() is not equal then __eq__() is not equal
"""
from typing import Any

a = "abcd"
print(hash(a))
print(hash("abcd"))
print(str.__hash__("abcd"))
#! print(hash([1,2,3])) TypeError: unhashable type: 'list'


class MyCls:
    def __init__(self, value) -> None:
        # self._value = value
        object.__setattr__(self, "_value", value)

    def __setattr__(self, __name: str, __value: Any) -> None:
        raise TypeError("MyCls is immutable")  # * 可以使用attrs库或者immutables库

    def __eq__(self, __o: object) -> bool:
        print("自定义__eq__被调用......")
        return __o._value == self._value if isinstance(__o, MyCls) else False

    def __hash__(self) -> int:
        return hash(self._value)


h1 = MyCls("a")
h2 = MyCls("a")
print(h1 is h2)
print(h1 == h2)

print(
    hash(h1)
)  #! 调用只实现了__eq__()的h1的哈希函数会报错 TypeError: unhashable type: 'MyCls'，两个方法都必须要实现。

h1._value = "b"  #! TypeError: MyCls is immutable
