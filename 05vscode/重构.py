#!/usr/bin/env python
# -*- encoding: utf-8 -*-
"""
@File    :   重构.py
@Time    :   2023/01/06 12:06:05
@Author  :   owl
@Email   :   xxxxx@163.com
@Desp    :   
"""

# here put the import lib

# * 提取变量 1.右键 2.点击灯泡 3.快捷键ctrl+shift+r
# x = 1 
# y = 2
# a = x + y
# b = x + y

x = 1
y = 2
new_var = x + y
a = new_var
b = x + y

# * 提取方法
def add(x, y):
    return x + y

def new_func(add):
    add(1,2)

new_func(add)

# * 排序import语句 右键sort import