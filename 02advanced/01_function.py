#!/usr/bin/env python
# -*- encoding: utf-8 -*-
'''
@File    :   01_function.py
@Time    :   2022/05/27 09:51:50
@Author  :   owl
@Email   :   xxxxx@163.com
@Desp    :   函数
'''

import functools
import time

# here put the import lib
from functools import reduce

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


move(3, 'A', 'B', 'C')


# lambda表达式，用于创建小巧的匿名函数
def add(x, y):
    return x+y


print(add(1, 2))
print(lambda x, y: x+y)  # <function <lambda> at 0x0000027D695BB158>


def make_incrementor(n):
    return lambda x: x+n


f = make_incrementor(42)
print(f(0))
print(f(1))


pairs = [(1, 'one'), (2, 'two'), (3, 'three')]
pairs.sort(key=lambda x: x[1])
print(pairs)

# python 内建函数 reduce(),map()
# map()函数接收两个参数，一个是函数，一个是Iterable，map将传入的函数依次作用到序列的每个元素，并把结果作为新的Iterator返回。


def f(x):
    return x*x


lst = [1, 2, 3, 4, 5, 6]
r = map(f, lst)
print(r)
# map()传入的第一个参数是f，即函数对象本身。由于结果r是一个Iterator，Iterator是惰性序列，因此通过list()函数让它把整个序列都计算出来并返回一个list。
print(list(r))

# 把这个list所有数字转为字符串
print(list(map(str, [1, 2, 3, 4, 5, 6, 7, 8, 9])))

# reduce()
# reduce把一个函数作用在一个序列[x1, x2, x3, ...]上，这个函数必须接收两个参数，reduce把结果继续和序列的下一个元素做累积计算
r = reduce(add, [1, 2, 3, 4, 5, 6])
print(r)

# 把字符串转化为整数的函数
DIGITS = {'0': 0, '1': 1, '2': 2, '3': 3, '4': 4,
          '5': 5, '6': 6, '7': 7, '8': 8, '9': 9}


def char2num(s):
    return DIGITS[s]


def str2int(s):
    return reduce(lambda x, y: x * 10 + y, map(char2num, s))


r = str2int('13579')
print(r, type(r))

# filter()
# filter()把传入的函数依次作用于每个元素，然后根据返回值是True还是False决定保留还是丢弃该元素。


def is_odd(n):
    return n % 2 == 1


list(filter(is_odd, [1, 2, 4, 5, 6, 9, 10, 15]))

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
        it = filter(_not_divisible(n), it)  # 构造新序列


# 打印1000以内的素数:
for n in primes():
    if n < 6:
        print(n, end=' ')
    else:
        break

# sorted()函数
l = sorted([36, 5, -12, 9, -21])
print(l)
# sorted()函数也是一个高阶函数，它还可以接收一个key函数来实现自定义的排序，例如按绝对值大小排序：
l = sorted([36, 5, -12, 9, -21], key=abs)
print(l)

# 返回函数（闭包）


def lazy_sum(*args):
    def sum():
        ax = 0
        for n in args:
            ax = ax + n
        return ax
    return sum


f = lazy_sum(1, 3, 5, 7, 9)
f()
# 使用闭包时，对外层变量赋值前，需要先使用nonlocal声明该变量不是当前函数的局部变量。


def inc():
    x = 0

    def fn():
        nonlocal x
        x = x + 1
        return x
    return fn


f = inc()
print(f())  # 1
print(f())  # 2

# 返回闭包时牢记一点：返回函数不要引用任何循环变量，或者后续会发生变化的变量


def count():
    fs = []
    for i in range(1, 4):
        def f():
            return i*i
        fs.append(f)
    return fs


f1, f2, f3 = count()
# 全部都是9！原因就在于返回的函数引用了变量i，但它并非立刻执行。等到3个函数都返回时，它们所引用的变量i已经变成了3，因此最终结果为9。
print(f1())
print(f2())
print(f3())

# 装饰器
# 由于函数也是一个对象，而且函数对象可以被赋值给变量，所以，通过变量也能调用该函数。
def now():
    print('2022-5-30')
    print(time.localtime())

f = now
f()
print(f.__name__,now.__name__)

# 装饰器增强函数功能
def log(func):
    def wrapper(*args, **kw):
        print('call %s():' % func.__name__)
        return func(*args, **kw)
    return wrapper

@log #把@log放到now()函数的定义处，相当于执行了语句：now = log(now)
def now():
    print('2015-3-25')

now()
print(now.__name__)  # wrapper

#如果decorator本身需要传入参数，那就需要编写一个返回decorator的高阶函数
def log(text):
    def decorator(func):
        def wrapper(*args, **kw):
            print('%s %s():' % (text, func.__name__))
            return func(*args, **kw)
        return wrapper
    return decorator

@log('execute') #now = log('execute')(now)
def now():
    print('2015-3-25')

now()
print(now.__name__)  # wrapper


# 需要把原始函数的__name__等属性复制到wrapper()函数中
def log(func):
    @functools.wraps(func)
    def wrapper(*args, **kw):
        print('call %s():' % func.__name__)
        return func(*args, **kw)
    return wrapper
@log
def now():
    print('2015-3-25')

now()
print(now.__name__)  # now

# 偏函数
# 简单总结functools.partial的作用就是，把一个函数的某些参数给固定住（也就是设置默认值），返回一个新的函数，调用这个新函数会更简单
int2=functools.partial(int, base=2)
print(int2('1000000'))
# 创建偏函数时，实际上可以接收函数对象、*args和**kw这3个参数
int2 = functools.partial(int, base=2)
# 相当于
kw = {'base': 2}
int('10010', **kw)

max2 = functools.partial(max, 10)
# 实际上会把10作为*args的一部分自动加到左边，也就是
max2(5, 6, 7) # 10
# 相当于
args = (10, 5, 6, 7)
max(*args)