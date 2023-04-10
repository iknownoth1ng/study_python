#!/usr/bin/env python
# -*- encoding: utf-8 -*-
"""
@File    :   16MappingProxy的使用.py
@Time    :   2023/04/10 13:29:18
@Author  :   owl
@Email   :   xxxxx@163.com
@Desp    :   https://docs.python.org/zh-cn/3/library/types.html
"""
from types import MappingProxyType

d = {"happy": "new year"}
d_proxy = MappingProxyType(d)
print(d_proxy)
print(type(d_proxy))
# d_proxy[
#     "happy"
# ] = "birthday"  #! TypeError: 'mappingproxy' object does not support item assignment

d["happy"] = "birthday"
print(d_proxy)

