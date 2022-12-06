#!/usr/bin/env python
# -*- encoding: utf-8 -*-
'''
@File    :   07_tuple_pratice.py
@Time    :   2022/05/19 13:12:55
@Author  :   owl
@Email   :   xxxxx@163.com
@Desp    :   元组
'''

# here put the import lib
# 可变序列，列表、字典
lst = [10, 20]
print(id(lst))
lst.append(30)
print(id(lst))
# 不可变序列，字符串、元组
s = 'hello'
print(s, id(s))
s = s+' world'
print(s, id(s))

# 元组的创建方式
# 使用小括号()
t1 = (10, 20, 'hello')
print(t1, type(t1))
# 使用内置函数tuple()
t2 = tuple((20, 30, 'world'))
print(t2, type(t2))
# 只包含一个元组的元素需要使用逗号和小括号
s = ('python')
print(s, type(s))
t3 = ('python',)
print(t3, type(t3))
t4 = 'hello', 'python'
print(t4, type(t4))
# 空元组
t5 = ()
t6 = tuple()
print(t5, type(t5))
print(t6, type(t6))

'''
列表不可变
·注意事项：元组中存储的是对象的引用
a)如果元组中对象本身不可变对象，则不能再引用其它对象
b)如果元组中的对象是可变对象，则可变对象的引用不允许
改变，但数据可以改变
'''
t=(10,[20,30],9)
print(t,type(t),id(t))
print(t[0],type(t[0]),id(t[0]))
print(t[1],type(t[1]),id(t[1]))
print(t[2],type(t[2]),id(t[2]))
# 不可以修改元组，比如t[1]=100
#如果元组中的对象是可变对象，则可变对象的引用不允许改变，但数据可以改变
t[1].append(100)
print(t[1],id(t[1]))

# 元组的遍历
t=('hello','python',98)
print(t, type(t), id(t))
# 使用索引获取
print(t[0])
print(t[1])
print(t[2])
# print(t[3]) IndexError: tuple index out of range
# 使用 for……in
for i in t:
    print(i)

