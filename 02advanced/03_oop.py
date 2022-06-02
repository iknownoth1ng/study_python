#!/usr/bin/env python
# -*- encoding: utf-8 -*-
'''
@File    :   03_oop.py
@Time    :   2022/06/01 13:14:56
@Author  :   owl
@Email   :   xxxxx@163.com
@Desp    :   Object Oriented Programming(面向对象编程-上)
'''

# here put the import lib
'''
·1、两大编程思想
·2、类和对象的创建
·3、类对象与类属性
·4、类方法与静态方法'''

# 类的创建


class Student:  # 类名，首字母大写其余小写，采用驼峰命名法
    pass


# python中一切皆对象,开辟了内存空间
print(id(Student))  # 2708413367384
# <class 'type'> type是元类,也就是python中所有的类其实本质上都是type这个类的实例化后的对象。
print(type(Student))
print(Student)  # <class '__main__.Student'>


# 类的组成
'''
类属性
实例方法
静态方法
类方法
'''


class Teacher:
    # 直接写在类里的变量，称为类属性
    native_pace = '吉林'

    # 初始化函数，给实例属性赋值
    def __init__(self, name, age):
        self.name = name
        self.age = age

    # 实例方法
    def eat(self):
        print(self.name+'在吃饭')

    # 静态方法
    @staticmethod
    def sm():
        print("静态方法sm")

    # 类方法
    @classmethod
    def cm(cls):
        print("类方法cm")


# 对象的创建
teacher1 = Teacher("张三", "18")
print(id(teacher1))  # 2053196151880
print(type(teacher1))  # <class '__main__.Teacher'>
print(teacher1)  # <__main__.Teacher object at 0x000001DE0C06FC48>

teacher1.eat()  # 对象.方法
Teacher.eat(teacher1)  # 类.方法(类的对象)

# 类的属性与方法
print(Teacher.native_pace)  # 吉林
t2 = Teacher("李四", "18")
t3 = Teacher("王五", "20")
print(t2.native_pace)  # 吉林
print(t3.native_pace)  # 吉林
Teacher.native_pace = '天津'
print(t2.native_pace)  # 天津
print(t3.native_pace)  # 天津

Teacher.cm()  # 类方法cm
Teacher.sm()  # 静态方法sm

# 动态绑定属性和方法
t2.gender='女'
print(t2.gender)
def show():
    print("定义在类外为函数")

t2.show=show
t2.show()
