#!/usr/bin/env python
# -*- encoding: utf-8 -*-
"""
@File    :   17bytes和bytearray的使用.py
@Time    :   2023/04/10 13:43:08
@Author  :   owl
@Email   :   xxxxx@163.com
@Desp    :   https://docs.python.org/zh-cn/3/library/stdtypes.html#binary-sequence-types-bytes-bytearray-memoryview
"""
# * bytes不可变
b = bytes("abc哈", "utf_8")  # \xe5\x93\x88
print(b)
print(type(b))

b = bytes(
    [
        1,
        97,  # a
        3,
    ]
)
# b[0] = 98 #!TypeError: 'bytes' object does not support item assignment
print(b)

# * bytearray可变
ba = bytearray("abc", "utf8")
print(ba)
ba[0] = 98
print(ba)
