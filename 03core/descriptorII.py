#!/usr/bin/env python
# -*- encoding: utf-8 -*-
'''
@File    :   descriptorII.py
@Time    :   2022/06/22 10:23:05
@Author  :   owl
@Email   :   xxxxx@163.com
@Desp    :   描述符应用，实现classmethod
'''

# here put the import lib
# 尝试完成 classmethod
class classmethod_new(object):
    def __init__(self, func):
        self.func = func

    def __get__(self, instance, owner):
        print(self.func, instance, owner)

        # return self.func  # 此方法不能实现
        # return self.func(owner)  # 这是不可以的，而是要用

        def call(*args):
            self.func(owner, *args)

        return call


class A(object):

    M = 100

    def a(self):
        print("----a 是实例方法----")

    @classmethod_new
    def b(cls):
        print("----b 是类方法方法1----")
        print(cls.M)
        print("----b 是类方法方法2----")

    @classmethod_new
    def c(cls, num1, num2):
        print("----c 是类方法方法1----")
        print(cls.M + num1 + num2)
        print("----c 是类方法方法2----")

    # def d():
    #     print("----d 是静态方法----")


obj = A()
obj.b()
A.b()
obj.c(11, 22)

'''
1. 当Python解释器执行到底19行时，即定义A类时，就已经开始通过元类要创建这个类对象
    所以就需要将A类中的所有的类属性、方法都要通过字典的方式创建到type这个默认的元类中
    所以当遇到第25、26行时，就要通过装饰器确定此时b到底指向谁，此时b=classmethod_new(b)
2. 在执行classmethod_new时，创建了一个对象(其实就是描述符)
3. 当执行第42行diam时，可以分解为2步骤
    3.1 先要调用obj.b，得到一个返回值
    3.2 执行上一步得到的返回值，即返回值()
4. 在执行3.1时，需要得到一个返回值，又因为在通过实例对象调用类方法时，可能有实参进行传递，所以就需要
    这样一个函数，技能够调用原来b指向的函数，又能够再传递数据时接收数据，此时就用到了闭包
    注意：此题代码的精髓就在第12行定义的那个闭包(请细细体会)
5. 在执行3.2时，就调用了第12行的定义的闭包，其又调用了之前的b指向的函数，从而完成类方法的功能
'''