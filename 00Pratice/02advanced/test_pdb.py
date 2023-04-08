#!/usr/bin/env python
# -*- encoding: utf-8 -*-
"""
@File    :   test_pdb.py
@Time    :   2023/04/08 01:20:40
@Author  :   owl
@Email   :   xxxxx@163.com
@Desp    :   测试pdb 官方文档https://docs.python.org/zh-cn/3/library/pdb.html
"""


def g(data):
    return data * data


def f(x):
    lst = []
    for i in range(x):
        val = g(i)
        lst.append(val)
    return lst


f(3)

r"""
1.执行pdb命令: python -m pdb .\test_pdb.py
2.打印变量: p i
3.运行下一行: n
4.进入函数内: s
5.运行大于某个行数(用于跳出循环):until 21
6.直接执行到返回值当前行: r
7.打印函数最后一次返回的返回值: retval
8.标记某个breakpoint: b 行数, 直接输入b是打印所有的断点,clear 1 删除第一个断点
9.打印所有的代码: ll, 当前行数附近源代码 l,  回到当前行数l .
10.查看调用栈: w, u往上调整当前帧 d往下调整当前帧
11.继续运行: c



"""
