#!/usr/bin/env python
# -*- encoding: utf-8 -*-
'''
@File    :   withI.py
@Time    :   2022/06/15 14:26:15
@Author  :   owl
@Email   :   xxxxx@163.com
@Desp    :   上下文管理器with
'''

# here put the import lib
from contextlib import contextmanager

'''
Python 还提供了一个 contextmanager 的装饰器，更进一步简化了上下文管理器的实现方式。
通过 yield 将函数分割成两部分，
yield 之前的语句在__enter__方法中执行，
yield 之后的语句在 __exit__ 方法中执行。
紧跟在 yield 后面的值是函数的返回值。'''

@contextmanager
def my_open(path, mode):
    f = open(path, mode)
    yield f
    f.close()

with my_open('out.txt', 'w') as f:
    f.write("hello , the simplest context manager")