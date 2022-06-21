#!/usr/bin/env python
# -*- encoding: utf-8 -*-
'''
@File    :   04_oop.py
@Time    :   2022/06/01 14:50:59
@Author  :   owl
@Email   :   xxxxx@163.com
@Desp    :   Object Oriented Programming(面向对象编程-下)
'''

# here put the import lib
'''
·1、封装
·2、继承
·3、方法重写
·4、object类
·5、多态
·6、特殊方法和特殊属性'''

# 封装




import copy
class Car:
    def __init__(self, brand):
        self.brand = brand

    def start(self):
        print(self.brand+"汽车启动了")


c1 = Car("宝马X5")
print(c1.brand)
c1.start()

# 使用__来表示私有属性


class Student:
    def __init__(self, name, age):
        self.name = name
        self.__age = age

    def show(self):
        print(self.name, self.__age)


s1 = Student("张三", 18)
s1.show()
print(s1.name)
print(dir(s1))
print(s1._Student__age)

# 继承


class Person(object):
    def __init__(self, name, age):
        self.name = name
        self.age = age

    def info(self):
        print('姓名：{0}, 年龄：{1}'.format(self.name, self.age))

# 定义子类


class Student (Person):
    def __init__(self, name, age, score):
        super().__init__(name, age)
        self.score = score

    def info(self):  # 重写方法
        super().info()
        print("分数：{0}".format(self.score))


# 测试
stu = Student('Jack', 20, '1001')
stu.info()

# 多继承


class A:
    pass


class B:
    def __init__(self, name):
        self.name = name

    def __str__(self):
        return "我的名字是：{0}".format(self.name)


class C(A, B):
    pass


# object类
a = A()
print(dir(a))
print(a)  # <__main__.A object at 0x000001BBE36971C8>

b = B('小茶')
print(b)  # 我的名字是：小茶
print(type(b))

# 多态
'''
静态语言与动态语言
·静态语言和动态语言关于多态的区别
·静态语言实现多态的三个必要条件
·继承
·方法重写
·父类引用指向子类对象
·动态语言的多态崇尚“鸭子类型”当看到一只鸟走起来像鸭子、游泳起来像鸭子、
收起来也像鸭子，那么这只鸟就可以被称为鸭子。在鸭子类型中，不需要关心
对象是什么类型，到底是不是鸭子，只关心对象的行为。'''


class Animal():
    def eat(self):
        print('动物会吃')


class Dog(Animal):
    def eat(self):
        print('狗吃骨头')


class Cat(Animal):
    def eat(self):
        print('猫吃鱼')


class Person:
    def eat(self):
        print("人吃五谷杂粮")


def func(obj):
    obj.eat()


func(Animal())
func(Dog())
func(Cat())

func(Person())

# 特殊属性和特殊方法
# 特殊属性
print(b.__dict__)  # {'name': '小茶'} 实例对象的属性字典
print(B.__dict__)  # 类的属性、方法字典

print(a.__class__)  # 输出实例所属的类 <class '__main__.A'>
print(C.__bases__)  # 输出父类的元组(<class '__main__.A'>, <class '__main__.B'>)
print(C.__base__)  # 输出最近的父类 <class '__main__.A'>
print(C.__mro__)  # 类的层次结构
print(A.__subclasses__())  # A的子类列表

# 特殊方法
# __add__()方法
a = 20
b = 100
c = a+b
print(c)
d = a.__add__(b)
print(d)


class Food:
    def __init__(self, name):
        self.name = name

    def __add__(self, other):
        return self.name+other.name

    def __len__(self):
        return len(self.name)


f1 = Food('苹果')
f2 = Food("南瓜")
s = f1+f2  # 如果不重写__add__()方法会报错
print(s)  # 苹果南瓜

# __len__()
print(len(f1))  # 如果不重写__len__()方法会报错

# __new__()和__init__()


class Man(object):
    def __new__(cls, *args, **kw):
        print('__new__()方法被调用了，cls的id:{0}'.format(id(cls)))
        obj = super().__new__(cls)
        print('创建的对象id:{0}'.format(id(obj)))
        return obj

    def __init__(self, name) -> None:
        print('__init__()方法被调用了,self的id:{0}'.format(id(self)))
        self.name = name


print('object类:{0}'.format(id(object)))
print('Man类:{0}'.format(id(Man)))

m1 = Man('大壮')
print('m1这个实例的id:{0}'.format(id(m1)))

# 深拷贝和浅拷贝
'''
浅拷贝，
指的是重新分配一块内存，创建一个新的对象，
但里面的元素是原对象中各个子对象的引用。
深拷贝，
是指重新分配一块内存，创建一个新的对象，
并且将原对象中的元素，以递归的方式，通过创建新的子对象拷贝到新对象中。
因此，新对象和原对象没有任何关联。'''
a = [1, 2, 3, 4, ['a', 'b']]  # 原始对象

b = a  # 赋值，传对象的引用
c = copy.copy(a)  # 对象拷贝，浅拷贝
d = copy.deepcopy(a)  # 对象拷贝，深拷贝
print(id(a),id(b),id(c),id(d))

a.append(5)  # 修改对象a
a[4].append('c')  # 修改对象a中的['a', 'b']数组对象

print('a = ', a)  # [1, 2, 3, 4, ['a', 'b', 'c'], 5]
print('b = ', b)  # [1, 2, 3, 4, ['a', 'b', 'c'], 5]
print('c = ', c)  # [1, 2, 3, 4, ['a', 'b', 'c']]
print('d = ', d)  # [1, 2, 3, 4, ['a', 'b']]
