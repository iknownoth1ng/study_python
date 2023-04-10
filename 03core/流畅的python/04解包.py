#!/usr/bin/env python
# -*- encoding: utf-8 -*-
"""
@File    :   04解包.py
@Time    :   2023/04/10 00:30:53
@Author  :   owl
@Email   :   xxxxx@163.com
@Desp    :   解包
"""
print(divmod(20, 8))

# * 解包1
a = (20, 8)
a1, a2 = a
print(divmod(a1, a2))

# * 解包2
print(divmod(*a))

# * 解包3
a1, *rest, a2 = range(5)
print(a1)
print(a2)
print(rest)

# * 解包4
city = [
    ("Hangzhou", "Zhejiang", ("0571", "310000")),
    ("Guangdong", "Guangzhou", ("0755", "210000")),
]
for city, prov, (code, postcode) in city:
    print(postcode)
