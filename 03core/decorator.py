#!/usr/bin/env python
# -*- encoding: utf-8 -*-
'''
@File    :   decorator.py
@Time    :   2022/06/15 15:38:29
@Author  :   owl
@Email   :   xxxxx@163.com
@Desp    :   装饰器
'''

# here put the import lib
# 带自定义参数的装饰器

import functools


def repeat(nums):
    def my_decorator(func):
        @functools.wraps(func) # 使用内置的装饰器 @functools.wraps，它会帮助保留原函数的元信息（也就是将原函数的信息拷贝到对应的装饰器函数里）
        def wrapper(*args,**kws):
            for _ in range(nums):
                print('wrapper of decorator')
                func(*args,**kws)
        return wrapper
    return my_decorator

@repeat(5)
def greet(message):
    print(message)

greet('hello')

# 原函数还是原函数吗
print(greet.__name__)

'''
类装饰器
'''
class Count():
    def __init__(self,func):
        self.func=func
        self.num_calls=0
    
    def __call__(self, *args, **kws):
        self.num_calls+=1
        print('num of calls is:{}'.format(self.num_calls))
        return self.func(*args, **kws)

@Count
def example():
    print('hello world')

example()
example()


'''
多装饰器
'''

def decorator1(func):
    @functools.wraps(func)
    def wrapper(*args,**kws):
        print('excute decorator1')
        func(*args,**kws)
    return wrapper


def decorator2(func):
    @functools.wraps(func)
    def wrapper(*args, **kws):
        print('excute decorator2')
        func(*args, **kws)
    return wrapper


@decorator1
@decorator2
def greet(message):
    print(message)

greet('hello')
# excute decorator1
# excute decorator2
# hello
