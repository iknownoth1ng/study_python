#!/usr/bin/env python
# -*- encoding: utf-8 -*-
'''
@File    :   01_init.py
@Time    :   2022/05/12 11:17:19
@Author  :   owl
@Email   :   xxxxx@163.com
@Desp    :   起步，【print函数、转义字符】
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
print("hello",'world',"!")

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
e="helloooo\tworld"
print(e)
print("helloooo\tworld".expandtabs(4))
if __name__ == '__main__':
	print()
