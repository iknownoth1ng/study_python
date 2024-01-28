#!/usr/bin/env python
# -*- encoding: utf-8 -*-
"""
@File    :   example_closure.py
@Time    :   2024/01/28 23:54:22
@Author  :   owl
@Email   :   xxxxx@163.com
@Desp    :   闭包
"""
import dis


def f():
    data = []

    def inner(value):
        data.append(value)
        return data

    data = [0]  # * 证明不是复制局部变量data

    return inner


g = f()

# 打印函数f的字节码
print("Function 'f' bytecode:")
dis.dis(f)

# 获取并打印函数inner的实际引用
inner_func = g.__code__
print("\nFunction 'inner' bytecode:")
dis.dis(inner_func)

# 调用g函数以确保整个程序正常运行
print(g(1))
print(g(2))

print(g.__closure__)
print(hex(id(g(3))))
