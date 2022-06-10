#!/usr/bin/env python
# -*- encoding: utf-8 -*-
'''
@File    :   09_generator.py
@Time    :   2022/06/09 16:11:01
@Author  :   owl
@Email   :   xxxxx@163.com
@Desp    :   生成器
'''

# here put the import lib
def func(n):
    x=0
    i=0
    a=2
    b=1
    while True:
        if i>n:
            break
        y=a*x+b
        temp=yield (x,y)
        if temp:
            a,b=temp
        i+=1
        x=y

f=func(5)
print(next(f))
print(next(f))
print(next(f))
print(next(f))
print(f.send((3,2)))


# 获取一个素数序列
def _odd_iter():  # 先构造一个从3开始的奇数序列
    n = 1
    while True:
        n = n + 2
        yield n

def _not_divisible(n):  # 定义一个筛选函数
    return lambda x: x % n > 0

def primes():
    yield 2
    it = _odd_iter()  # 初始序列
    while True:
        n = next(it)  # 返回序列的第一个数
        yield n
        it = filter(lambda x, y = n: x % y > 0, it)
        #it = filter(_not_divisible(n), it)  # 构造新序列
		
# 打印1000以内的素数:
for n in primes():
    if n < 10:
        #print(n, end=' ')
        print(n)
    else:
        break


# g=(x for x in range(5))
# print(g)
# print(next(g))
# print('------')
# for i in g:
#     print(i)
# print('------')
# for j in g:
#     print('*')
#     print(j)
