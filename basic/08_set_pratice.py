#!/usr/bin/env python
# -*- encoding: utf-8 -*-
'''
@File    :   08_set_pratice.py
@Time    :   2022/05/23 18:14:57
@Author  :   owl
@Email   :   xxxxx@163.com
@Desp    :   集合
'''

# here put the import lib
'''
·Python语言提供的内置数据结构
·与列表、字典一样都属于可变类型的序列
·集合是没有value的字典
'''
# 集合的创建方式
# 第一种直接使用{}
s = {1, 1, 2, 3, 2, 3, 5, 6}  # 集合中不允许重复
print(s)
# 第二种方式，使用内置函数set()
s1 = set(range(10))
print(s1, type(s1))
s2 = set([2, 3, 4, 2, 3, 5, 65])  # 集合是无序的
print(s2, type(s2))
s3 = set((2, 3, 4, 2, 3, 5, 65))
print(s3, type(s3))
s4 = set('python')
print(s4, type(s4))
s5 = set({2, 3, 4, 2, 3, 5, 65})
print(s5, type(s5))
# 空集合
s = set()
print(s)

# 集合的相关操作
s = {1, 1, 2, 3, 2, 3, 5, 6}
# 判断操作
print(1 in s)
print(1 not in s)
# 新增操作
s.add(80)
print(s)
s.update({100, 200, 300})
print(s)
s.update([10, 20, 30])
print(s)
s.update((101, 202, 303))
print(s)
s.update('python')
print(s)
# 删除操作
s.remove(100)
print(s)
# s.remove(500) # KeyError: 500
s.discard(500)  # 不会报错，能删就删，不能删也不报错
s.discard(202)
print(s)
s.pop()  # 任意删一个
print(s)
# s.pop(2) 不能指定元素删除
# #TypeError: pop() takes no arguments (1 given)
s.clear()
print(s)  # 清空所有

'''
集合间的关系
·两个集合是否相等
·可以使用运算符==或！=进行判断

·一个集合是否是另一个集合的子集
。可以调用方法issubseti进行判断
·B是A的子集

·一个集合是否是另一个集合的超集
·可以调用方法issuperset:进行判断
·A是B的超集

·两个集合是否没有交集
·可以调用方法isdisjoint:进行判断
'''
s1 = {10, 20, 30, 40}
s2 = {20, 30, 40, 10}
print(s1 == s2, s1 != s2)  # 元素相同，就相同


s1 = {10, 20, 30, 40}
s2 = {20, 30, 40, 10}
s3 = {20, 30, 40, 10, 50, 60}
print(s1.issubset(s2))  # 子集
print(s1.issubset(s3))
print(s1.issuperset(s3))  # 超集
print(s3.issuperset(s1))
print(s1.isdisjoint(s3))  # 交集
s4 = {100, 200, 300}
print(s1.isdisjoint(s4))

# 集合之间的数学操作
# 交集
print(s1.intersection(s3))
print(s1 & s3)
print(s1)
print(s3)
# 并集
print(s1.union(s4))
print(s1 | s4)
print(s1)
print(s4)
# 差集
print(s1.difference(s3))
print(s1-s3)
print(s1)
print(s3)
# 对称差集
s1 = {1, 2, 10, 20, 30, 40}
s2 = {20, 30, 40, 10, 5, 6}
print(s1.symmetric_difference(s2))
print(s1 ^ s2)
print(s1)
print(s2)

# 集合生成式
s = {i*i for i in range(10)}
print(s, type(s))
