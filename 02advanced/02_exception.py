#!/usr/bin/env python
# -*- encoding: utf-8 -*-
'''
@File    :   02_exception.py
@Time    :   2022/05/31 10:51:52
@Author  :   owl
@Email   :   xxxxx@163.com
@Desp    :   错误与异常
'''

# here put the import lib
'''
# 1.语法错误
# 2.异常
# 3.异常处理
# 4.抛出异常
# 5.用户自定义异常
# 6.定义清理行为
# 7.预定义清理行为'''

# 1.语法错误
# while True print('Hello world')
# File
# "D:/cs/language/python/geekbangpython-master/my_pratice/errors_exceptions.py", line 50
# while True print('Hello world')
# ^
# SyntaxError: invalid syntax
# 2.异常
# 10 * (1 / 0)
# 4 + spm * 3
# '2' + 2
# 3.异常处理
# while True:
# try:
# x = int(input('Please enter a number'))
# break
# except ValueError:
# print("Oops! That was no valid number. Try again...")

# try:
# raise Exception('spam', 'eggs')
# except Exception as inst:
# print(type(inst))
# print(inst.args)
# print(inst)
#
# x, y = inst.args
# print(x)
# print(y)

# 4.抛出异常
# raise NameError('HiThere')
#
# try:
# raise NameError('HiThere')
# except NameError:
# print('An exception flew by!')
# raise

# 5.用户自定义异常
class MyError(Exception):
    def __init__(self, value):
        self.value = value

    def __str__(self):
        return repr(self.value)

try:
    raise MyError(2 * 2)
except MyError as e:
    print(e.value)

# 6.定义清理行为
# try:
# raise KeyboardInterrupt
# finally:
# print('Goodbye, world!')


def divide(x,y):
    try:
        result=x/y
    except ZeroDivisionError:
        print('division by zero!')
    else:
        print('result is', result)
    finally:
        print('executing finally clause')


# divide(2, 1)
# result is 2.0
# executing finally clause

# divide(2, 0)
# division by zero!
# executing finally clause

# divide('2', '1')
# executing finally clause
# TypeError: unsupported operand type(s) for /: 'str' and 'str'

# 7.预定义清理行为
#没有关闭
for line in open("name.txt"):
    print(line)

#语句执行后，文件f总会被关闭，即使是在处理文件中的数据时出错也一样。其它对象是否提供了预定义的清理行为要查看它们的文档。
with open("name.txt") as f:
    for line in f:
        print(line)