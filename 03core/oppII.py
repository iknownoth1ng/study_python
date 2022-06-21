#!/usr/bin/env python
# -*- encoding: utf-8 -*-
'''
@File    :   oppII.py
@Time    :   2022/06/13 10:27:14
@Author  :   owl
@Email   :   xxxxx@163.com
@Desp    :   面向对象基础
'''

# here put the import lib
'''
1.__slots__   限制实例的属性
'''
class Person():
    __slots__=('name','age')

p=Person()
p.name='张三'
p.age=18
# p.score=100 #AttributeError: 'Person' object has no attribute 'score'

# __slots__对子类不起作用
class Man(Person):
    pass

m=Man()
m.score=100

'''
2.property属性
'''

# 工作中经常使用属性进行存储数据，而对属性赋值有时容易粗心大意出问题
class Money():
    def __init__(self):
        self.money = 0
    
# 设置金额
a=Money()
a.money = 100
print("当前还剩余%d" % a.money)

# 容易出现问题，即可能给其错误的类型、数据范围越界等
# a.money = "hello"
# print("当前还剩余%d" % a.money)


'''
私有属性添加getter和setter方法
'''
class Money1():
    def __init__(self):
        self.__money=0
    
    def get_money(self):
        return self.__money
    
    def set_money(self,value):
        if isinstance(value, int):
            self.__money = value
        else:
            print("error:不是整型数字")
    
a=Money1()
a.set_money(100)
print("当前还剩余%d" % a.get_money())
a.set_money('100') # error:不是整型数字

'''
使用property升级getter和setter方法
'''
class Money2():
    def __init__(self):
        self.__money=0
    
    def get_money(self):
        return self.__money
    
    def set_money(self,value):
        if isinstance(value, int):
            self.__money = value
        else:
            print("error:不是整型数字")
    
    money=property(get_money,set_money)

a = Money2()
a.money = 100
print(a.money)
a.money = "hello"
print(a.money)

'''
使用property取代getter和setter方法
'''
class Money3():
    def __init__(self):
        self.__money=0
    
    @property
    def money(self):
        return self.__money
    
    @money.setter
    def money(self,value):
        if isinstance(value, int):
            self.__money = value
        else:
            print("error:不是整型数字")

a = Money3()
a.money = 100
print(a.money)
a.money = "hello"
print(a.money)



