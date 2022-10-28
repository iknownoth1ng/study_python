#!/usr/bin/env python
# -*- encoding: utf-8 -*-
'''
@File    :   gcII.py
@Time    :   2022/06/23 10:37:18
@Author  :   owl
@Email   :   xxxxx@163.com
@Desp    :   垃圾回收
'''

import gc
# here put the import lib
import sys

'''
1. 小整数对象池
整数在程序中的使用非常广泛，Python为了优化速度，使用了小整数对象池， 避免为整数频繁申请和销毁内存空间。

Python 对小整数的定义是 [-5, 256] 这些整数对象是提前建立好的，不会被垃圾回收。

在一个 Python 的程序中，所有位于这个范围内的整数使用的都是同一个对象.

同理，单个字母也是这样的。

但是当定义2个相同的字符串时，引用计数为0，触发垃圾回收
'''

a = 1
b = 1
print(id(a) == id(b))

'''2. 大整数对象池
每一个大整数，均创建一个新的对象。
'''
c = 258888888888888888888888888888888888888
d = 258888888888888888888888888888888888888
print(c is d)
print(id(c) == id(d))
print(id(c), id(d))

'''
3. intern机制（字符串驻留）
python会不会创建9个对象呢？在内存中会不会开辟9个”HelloWorld”的内存空间呢？
 想一下，如果是这样的话，我们写10000个对象，比如a1=”HelloWorld”…..a1000=”HelloWorld”，
  那他岂不是开辟了1000个”HelloWorld”所占的内存空间了呢？如果真这样，内存不就爆了吗？
  所以python中有这样一个机制——intern机制，
让他只占用一个”HelloWorld”所占的内存空间。靠引用计数去维护何时释放。'''
a1 = "HelloWorld"
a2 = "HelloWorld"
a3 = "HelloWorld"
a4 = "HelloWorld"
a5 = "HelloWorld"
a6 = "HelloWorld"
a7 = "HelloWorld"
a8 = "HelloWorld"
a9 = "HelloWorld"

print(a1 is a2)
a10 = 'Hello World'
print(a1 is a10)
a1 = sys.intern(a10)
print(a1 is a10)
print(a1, a10)

'''
总结
小整数[-5,256]共用对象，常驻内存

大整数不共用内存，引用计数为0，销毁

单个单词，不可修改，默认开启intern机制，共用对象，引用计数为0，则销毁

字符串（含有空格），不可修改，没开启intern机制，不共用对象，引用计数为0，销毁'''


'''
有三种情况会触发垃圾回收：
当gc模块的计数器达到阈值的时候，自动回收垃圾
调用gc.collect()，手动回收垃圾
程序退出的时候，python解释器来回收垃圾'''


class ClassA():
    def __init__(self):
        print('object born,id:%s'%str(id(self)))


print(gc.get_count())  # (590, 8, 0)
a = ClassA()
print(gc.get_count())  # (591, 8, 0)
del a
print(gc.get_count())  # (590, 8, 0)
