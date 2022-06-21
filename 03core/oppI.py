#!/usr/bin/env python
# -*- encoding: utf-8 -*-
'''
@File    :   oppI.py
@Time    :   2022/06/13 10:26:32
@Author  :   owl
@Email   :   xxxxx@163.com
@Desp    :   面向对象基础
'''

# here put the import lib
'''
1.引入面向对象
2.类和对象
3.定义类、创建对象
4.实例属性、实例方法
5self
6__init__方法
'''
# 使用面向过程编程
# 遍历打印所有姓名+年龄
def print_info(names,ages):
    print("姓名：{0}、年龄：{1}".format(names,ages))

'''
# 定义一个变量存储姓名
name='王老师'
# 定义一个变量存储年龄
age='24'
# 遍历姓名+年龄
print_info(name,age)

# 定义第1个人的信息，然后输出
name = "王老师"
age = 20
print_info(name, age)

# 定义第2个人的信息，然后输出
name = "王老师2"
age = 22
print_info(name, age)

# 定义第3个人的信息，然后输出
name = "王老师3"
age = 23
print_info(name, age)
'''
# 定义第1个人的信息，然后输出
names = ["王老师", "王老师2", "王老师3"]
ages = [20, 22, 23]
print_info(names[0], ages[0])
print_info(names[1], ages[1])
print_info(names[2], ages[2])

'''
上面我们使用了列表进行了升级，避免了定义定义多个变量的问题
你是否有这样的感觉，即便是升级了总感觉还是不够好
如果有这种感觉就对了，因为上面的这种方式就是“面向过程”开发，这种开发模式就是一步步的对需要的数据以及方法进行操作
因此出现代码“乱”的情况，在所难免'''


# 使用面向对象编程
class Person(object):
    def __init__(self,name,age) -> None:
        self.name=name
        self.age=age
    
    def print_info(self):
        print("姓名：",self.name,"年龄：",self.age)
    

# 创建一个对象
p = Person("王老师", 20)
p.print_info()

# 创建另外2个对象
p2 = Person("王老师2", 22)
p2.print_info()
p3 = Person("王老师3", 23)
p3.print_info()



'''
二、对比分析通过上述2种代码的实现方式（面向过程、面向对象）我们能够的粗以下几个结论：
	* 
面向过程：根据业务逻辑从上到下写代码
	* 
面向对象：将数据与函数绑定到一起，进行封装，这样能够更快速的开发程序，减少了重复代码的重写过程
	* 
面向过程编程最易被初学者接受，其往往用一长段代码来实现指定功能，开发过程的思路是将数据与函数按照执行的逻辑顺序组织在一起，数据与函数分开考虑。

三、总结
面向对象编程(Object Oriented Programming-OOP) 是一种解决软件复用的设计和编程方法。
这种方法把软件系统中相近相似的操作逻辑和操作 应用数据、状态,以类的型式描述出来,以对象实例的形式在软件系统中复用,以达到提高软件开发效率的作用。
大白话来一句：面向对象能实现的功能，面向过程也能实现，往往程序的代码量都比较大，如果用面向过程的方式实现则代码冗余且不已升级，使用面向对象将数据与功能进行封装在中大程序开发中首先考虑使用'''