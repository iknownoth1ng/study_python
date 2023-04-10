#!/usr/bin/env python
# -*- encoding: utf-8 -*-
"""
@File    :   01魔术方法.py
@Time    :   2023/01/31 16:06:55
@Author  :   owl
@Email   :   xxxxx@163.com
@Desp    :   常用的魔术方法 https://www.bilibili.com/video/BV1tG4y1K7xG/?spm_id_from=pageDriver&vd_source=002a329d5a6f5498931adabaffce19bc
"""

# here put the import lib


class Dice:
    def __init__(self) -> None:
        self._values = list(range(1, 7))

    def __len__(self):  #!  TypeError: object of type 'Dice' has no len()
        return len(self._values)

    def __getitem__(self, idx):  #! TypeError: 'Dice' object is not subscriptable
        print("__getitem__ is called", idx)
        return self._values[idx]

    def __contains__(self, value):
        print("__contains__ is called", value)
        return value in self._values


dice = Dice()
print(len(dice))

print(dice[1])

for i in dice:
    print(i)

print(3 in dice)

print(dice[1:3])
