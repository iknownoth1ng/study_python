#!/usr/bin/env python
# -*- encoding: utf-8 -*-
'''
@File    :   05_modules.py
@Time    :   2022/06/02 15:46:00
@Author  :   owl
@Email   :   xxxxx@163.com
@Desp    :   模块
'''

import builtins
import math  # 使用import只能导入模块、包
import sys
import time
from math import pow  # 使用from可以导入包、模块、函数、变量

import mypackage.mymodule as md
# here put the import lib
import schedule
from mypackage.mymodule import a

print(id(math))  # 2267991424360
print(type(math))  # <class 'module'>
print(math)  # <module 'math' (built-in)>

print(dir(math))
print(math.pi)
print(math.pow(2, 3))
print(math.ceil(9.01))
print(math.floor(9.99))

print(pow(2, 3))
print(builtins.pow(2, 3))

'''
·以主程序形式运行
·在每个模块的定义中都包括一个记录模块名称的变量name,程序可
以检查该变量，以确定他们在哪个模块中执行。如果一个模块不是被导
入到其它程序中执行，那么它可能在解释器的顶级模块中执行。顶级模
块的name变量的值为main
if name='_main_':
pass'''

print(a)
md.add(1, 2)

# 常用内置模块

print(sys.getsizeof(24))  # 占用多少字节

print(time.time())
print(time.localtime(time.time()))


def job():
    print("哈哈 ------")


schedule.every(3).seconds.do(job)
# while True:
#     schedule.run_pending()
#     time.sleep(1)
