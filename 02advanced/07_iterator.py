#!/usr/bin/env python
# -*- encoding: utf-8 -*-
'''
@File    :   07_iterator.py
@Time    :   2022/06/08 17:07:51
@Author  :   owl
@Email   :   xxxxx@163.com
@Desp    :   迭代器
'''

# here put the import lib
# 1.为什么会有迭代器
'''
在实际开发工作中，经常需要快速的将对象转化问其他的不同的数据类型，此时如果能快速的遍历出自定义的对象，这样大大减少代码的几余，而且可读性会更优美
问题是，怎样实现呢？
今天我们要学习的知识只有1个，那就是"选代器'''

# 2.什么是迭代
'''迭代是访问集合元素的一种方式
'''
from collections.abc import Iterable
from collections.abc import Iterator
nums = [11, 22, 33]
for _ in nums:
    print(_)

# 3.什么是可迭代对象
'''
可以用for……in 遍历的都是
可以迭代的：列表·元组·字典·字符串
不能迭代的：·整型·浮点型'''

# 判断是否可以迭代
print(isinstance([], Iterable))
print(isinstance((), Iterable))
print(isinstance({}, Iterable))
print(isinstance('abc', Iterable))

print(isinstance(1, Iterable))
print(isinstance(1.0, Iterable))

# 4.迭代器
# iter()获取迭代器
print(type(nums))  # <class 'list'>
nums_iter = iter(nums)
print(type(nums_iter))  # <class 'list_iterator'>
# next()获取迭代器的数据
num1 = next(nums_iter)
print(num1)
num2 = next(nums_iter)
print(num2)
num3 = next(nums_iter)
print(num3)
'''
小总结：
for循环的过程可以通过上面的iter(和next()函数来实现
也就是说：
1,先调用iter,将nums当做实参,得到nums这个可迭代对象的迭代器
2,调用next(),将上一步得到的迭代器进行取值
3,将上一步取出来的值赋值给num这个变量
4,执行for循环体中的代码,print(num)
5,接下来重复执行2/3/4步,当nums所有数据被获取后,再获取下一个数据时
会报错StopIteration,但是for循环会自动处理异常,遇到异常StopIteration会自动结束循环
'''
for num in nums:
    print(num)
# next()获取时的异常StopIteration
# num4=next(nums_iter) StopIteration
# print(num4)

# 练习
# 一.自己实现一个WhileTrue遍历列表
# 1.定义一个列表
lst = [1, 2, 3, 4, 5, 6]
# 2.获取它的迭代器
lst_iter = iter(lst)
# 3.循环的方式获取迭代器里的值
while True:
    try:
        num = next(lst_iter)
        print(num)
    except StopIteration as e:
        break

# 二.自定义迭代器
# 有__iter__()方法的对象，就是一个可迭代对象


class MyList(object):
    def __init__(self) -> None:
        self.container = []

    def __iter__(self):
        return MyIterator()

    def add(self, item):
        self.container.append(item)


myList = MyList()
myList.add(11)
myList.add(22)
myList.add(33)

# 看对象里是否有__iter__()方法
print('myList是否是可迭代对象：', isinstance(myList, Iterable))

# 实现了__iter__()和__next__()方法的是迭代器


class MyIterator(object):
    def __init__(self) -> None:
        pass

    def __iter__(self):
        pass

    def __next__(self):
        print('haha')
        return 100


myList_iter = iter(myList)  # 会调用__iter__()方法
num = next(myList_iter)  # 会调用__next__()方法
print(num)
# 迭代器一定是可迭代对象，可迭代对象不一定是迭代器。
print('myList是否是可迭代对象：', isinstance(myList, Iterable))  # True
print('myList是否是迭代器：', isinstance(myList, Iterator))  # False
print('myList_iter是否是可迭代对象：', isinstance(myList_iter, Iterable))  # True
print('myList_iter是否是迭代器：', isinstance(myList_iter, Iterator))  # True
