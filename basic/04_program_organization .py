#!/usr/bin/env python
# -*- encoding: utf-8 -*-
'''
@File    :   04_program_organization .py
@Time    :   2022/05/17 10:22:13
@Author  :   owl
@Email   :   xxxxx@163.com
@Desp    :   程序的组织结构
'''

# here put the import lib
'''
程序的组织结构
-1996年,计算机科学家证明了这样的事实:任何简单或复杂的算法
都可以由顺序结构、选择结构和循环结构这三种基本结构组合而成
计算机的流程控制:
顺序结构
选择结构:
◆if语句
循环结构:
whilei语句
for-in语句
'''
# 顺序结构：按照从上到下执行

# 选择结构：
# 测试对象的布尔值
'''
Python一切皆对象，所有对象都有一个布尔值，使用bool()获得。
以下对象布尔值均为False
·False
·数值0
·None
空字符串
空列表
空元组
空字典
空集合
'''
'''
from multiprocessing.connection import answer_challenge
print(bool(0))
print(bool([]))
print(bool(0.0))
print(bool(None))
print(bool(1))
# 单分支机构
x = 'abc'
if x == 'abc':
    print('x和abc相等')
# 双分支结构
if x == 'abc':
    print('x和abc相等')
else:
    print('x和abc不相等')
# 多分支结构
score = int(input("请输入你的成绩"))
if 90 <= score <= 100:
    print("A")
elif 80 <= score < 90:
    print("B")
elif 70 <= score < 80:
    print("C")
elif 60 <= score < 70:
    print("D")
elif 0 <= score < 60:
    print("E")
else:
    print("成绩输入有误")
# 嵌套if
answer = input("您是会员吗？y/n")
money = float(input("请输入您的购物金额"))
# 外层判断是否是会员
if answer == 'y':
    if money >= 200:
        print("打八折：付款金额为", money*0.8)
    else:
        print("不打折")
else:
    print("非会员")

# 条件表达式，为if……else的简写
n1 = int(input("请输入n1"))
n2 = int(input("请输入n2"))
print(('n1>=n2')if n1 >= n2 else ('n2>n1'))
# pass语句
if x == 'abc':
    pass
else:
    pass
'''

# 循环结构
# range()函数
r = range(10)
print(r, type(r))
print(list(r))

r = range(1, 10)
print(list(r))

r = range(1, 10, 3)
print(list(r))

# while循环
# 1到100的偶数和
sum, n = 0, 0
while n <= 100:
    sum = sum+n
    n = n+2
print(sum)
# 1到100的奇数和
sum, n = 0, 1
while n <= 100:
    if n % 2:
        sum += n
    n += 1
print(sum)

# for……in 循环
for i in range(10):
    print(i)
for _ in range(5):
    print('python')
# 1到100的偶数和
sum = 0
for i in range(1, 101):
    if not i % 2:
        sum += i
print(sum)


# 计算100-999之间的水仙花数
for i in range (100, 1000):
    ge=i%10
    shi=(i//10)%10
    bai=i//100
    if i==bai**3+shi**3+ge**3:
        print(i)
