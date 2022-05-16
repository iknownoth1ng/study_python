#!/usr/bin/env python
# -*- encoding: utf-8 -*-
'''
@File    :   01_init.py
@Time    :   2022/05/12 11:17:19
@Author  :   owl
@Email   :   xxxxx@163.com
@Desp    :   起步-【print函数、转义字符、二进制中的编码、标识符与保留字】
'''

# here put the import lib


'''
print函数
1.输出哪些内容
-输出数字、字符串、运算符的表达式
2.将内容输出的目的地
-显示器控制台、文件
3.输出形式
-换行、不换行

'''
# 1
# 输出数字


import keyword
from sys import prefix
from tracemalloc import start
print(520)
print(98.5)

# 输出字符串
print('hello world')
print("Hello Python interpreter!")

# 含有运算符的表达式
print(3+1)

# 2
# 显示器控制台
# 文件
# with open("./print.txt", "a+") as f:  # a+ 文件不存在就创建，存在就追加
#     print('hello world', file=f)

# 3
# 换行
# 不换行
print("hello", 'world', "!")

'''
转义字符:\
\\ 反斜杠
\' 单引号
\" 双引号

\n 换行
\t 制表
\r 回车
\b 退格
'''
# \n 换行
print("hello\nworld")
# \t 制表
print("hello\tworld")
e = "helloooo\tworld"
print(e)
print("helloooo\tworld".expandtabs(4))
# \r 回车
print("hello \rworld")
# \b 退格
print('hello\bworld')
# 原字符
print(r'hello \nworld')

'''
二进制中的编码

'''
print(chr(0b100111001011000))
print(ord('乘'))


'''
标识符与保留字
'''
# 关键字(保留字)
print(keyword.kwlist)
#['False', 'None', 'True', 'and', 'as', 'assert', 'break', 'class', 'continue', 'def', 'del', 'elif', 'else', 'except', 'finally', 'for', 'from', 'global', 'if', 'import', 'in', 'is', 'lambda', 'nonlocal', 'not', 'or', 'pass', 'raise', 'return', 'try', 'while', 'with', 'yield']

'''
·变量、函数、类、模块和其它对象的起的名字就叫标识符
·规则：
·字母、数字、下划线
·不能以数字开头
·不能是我的保留字
·我是严格区分大小写的
'''
