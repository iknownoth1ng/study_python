#!/usr/bin/env python
# -*- encoding: utf-8 -*-
'''
@File    :   01_function.py
@Time    :   2022/05/27 09:51:50
@Author  :   owl
@Email   :   xxxxx@163.com
@Desp    :   函数
'''

# here put the import lib
'''
·1、函数的创建和调用
·2、函数的参数传递
·3、函数的返回值
·4、函数的参数定义
·5、变量的作用域
·6、递归函数'''


# 函数的创建和调用
def calc(a, b, c=0):  # 创建
    print('a:', a)
    print('b:', b)
    print('c:', c)
    return a+b+c


result = calc(2, 3)  # 调用
print(result)

# 函数名其实就是指向一个函数对象的引用，完全可以把函数名赋给一个变量，相当于给这个函数起了一个“别名”：
a = abs  # 变量a指向abs函数
a(-1)  # 所以也可以通过a调用abs函数


# 函数的参数传递与定义
# 1位置传参
result = calc(2, 3)

# 2关键字传参
result = calc(b=2, a=3)

# 3个数可变的位置参数


def calc(*numbers):  # 参数numbers接收到的是一个tuple
    sum = 0
    for n in numbers:
        sum = sum + n * n
    return sum


# Python允许你在list或tuple前面加一个*号，把list或tuple的元素变成可变参数传进去：
nums = [1, 2, 3]
calc(*nums)

# 4个数可变的关键字参数
# 允许你传入0个或任意个含参数名的参数，这些关键字参数在函数内部自动组装为一个dict。请看示例：


def person(name, age, **kw):
    print('name:', name, 'age:', age, 'other:', kw)


person('Bob', 35, city='Beijing')
extra = {'city': 'Beijing', 'job': 'Engineer'}
person('Jack', 24, **extra)
# **extra表示把extra这个dict的所有key-value用关键字参数传入到函数的**kw参数，kw将获得一个dict，注意kw获得的dict是extra的一份拷贝，对kw的改动不会影响到函数外的extra。

# 5默认参数,见calc()的第三个参数c
# 定义默认参数要牢记一点：默认参数必须指向不变对象！

# 6命名关键字参数
# 和关键字参数**kw不同，命名关键字参数需要一个特殊分隔符*，*后面的参数被视为命名关键字参数。


def person(name, age, *, city, job):
    print(name, age, city, job)


person('Jack', 24, city='Beijing', job='Engineer')

# 函数调用的参数传递内存分析


def fun(arg1, arg2):
    print('arg1:', arg1)
    print('arg2:', arg2)
    arg1 = 100
    arg2.append(10)
    print('arg1:', arg1)
    print('arg2:', arg2)


n1 = 11
n2 = [22, 33, 44]
print('函数调用前')
print('n1:', n1)
print('n2:', n2)
print('函数开始调用')
fun(n1, n2)
print('函数调用后')
print('n1:', n1)
print('n2:', n2)
'''
在函数调用的过程中，进行参数的传递：
如果是不可变对象，在函数体的修改不会影响实参的值，arg1的修改为100，不会影响n1的值。
如果是可变对象，在函数体的修改会影响实参的值，arg2的修改，会影响n2的值。
'''

# 函数的返回值
# 函数执行完毕也没有return语句时，自动return None。
# 函数可以同时返回多个值，但其实就是一个tuple。


def fun(num):
    odd = []  # 存奇数
    even = []  # 存偶数
    for i in num:
        if i % 2:
            odd.append(i)
        else:
            even.append(i)
    return odd, even


print(fun([10, 29, 34, 33, 44, 53, 55]))


# 变量的定义域
def fun1():
    age = 18
    print(age)

# print(age) 局部变量不能访问


def fun2():
    global name  # global 定义为全局变量
    name = '张三'
    print(name)


fun2()
print(name)


# 递归函数
# 使用递归计算阶乘
def fac(n):
    if n == 1:
        return 1
    else:
        return n*fac(n-1)


print(fac(6))

# 斐波那契数列


def fib(n):
    if n == 1 or n == 2:
        return 1
    else:
        return fib(n-1)+fib(n-2)


print(fib(6))

# 汉诺塔的移动可以用递归函数非常简单地实现。
# 请编写move(n, a, b, c)函数，它接收参数n，表示3个柱子A、B、C中第1个柱子A的盘子数量，然后打印出把所有盘子从A借助B移动到C的方法，例如：


def move(n, a, b, c):
    # 如果n=1,直接a到c
    if n == 1:
        print(a, '-->', c)
    # n＞1,视为1个最大的圆盘和剩余n-1个圆盘当一个整体移动,
    # 那n-1个移到b,最大那个移到c,即可实现递归
    else:
        move(n-1, a, c, b)  # n-1个以整体移到b
        print(a, '-->', c)  # 剩下那个最大的移到c
        move(n-1, b, a, c)  # n-1个变成新的问题:如何将n-1个从b移到c.(递归即可)


move(2, 'A', 'B', 'C')


# lambda表达式，用于创建小巧的匿名函数
