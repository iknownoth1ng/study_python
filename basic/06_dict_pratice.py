#!/usr/bin/env python
# -*- encoding: utf-8 -*-
'''
@File    :   06_dict_pratice.py
@Time    :   2022/05/19 09:54:18
@Author  :   owl
@Email   :   xxxxx@163.com
@Desp    :   字典
'''

# here put the import lib
'''
·1、什么是字典
·2、字典的原理
·3、字典的创建与删除
·4、字典的查询操作
·5、字典元素的增、删、改操作
·6、字典推导式
'''
# 字典创建
# 使用{}
dict1 = {'name': '张三', 'age': 18}
print(dict1, type(dict1))
# 使用内置函数dict()
dict2 = dict(name='jackey', age=25)
print(dict2, type(dict2))
# 空字典
dict3 = {}
print(dict3, type(dict3))

# 字典的获取
# 使用[]
print(dict1['name'])
# 使用[]获取不存在的key时，会报keyError错误
# 使用 get
print(dict1.get('age'))
# 使用get获取不存在的key，默认返回None
print(dict1.get("hello"))
# 使用get获取不存在的key，可以指定返回的参数
print(dict1.get("hello", 'world'))

# 字典的判断、删除、新增
# 判断key
print('hello' in dict1)
print("hello" not in dict2)
# 删除
del dict1['name']
print(dict1)
dict1.clear()
print(dict1)
# 新增
dict1['name'] = '李四'
print(dict1)
dict1['name'] = '张三'  # 修改
print(dict1)

# 获取字典的视图
scores = {'张三': 100, '李四': 80, '王五': 90}
# 获取所有的keys
keys = scores.keys()
print(keys)
print(type(keys))
print(list(keys))

# 获取所有的values
values = scores.values()
print(values)
print(type(values))
print(list(values))

# 获取所有的key-value对
items = scores.items()
print(items)
print(type(items))
print(list(items))

# 字典的遍历,遍历的是key
for item in scores:
    print(item)
    print(scores[item])

'''
·字典中的所有元素都是一个key-value对,key不允许重复,value可以重复
·字典中的元素是无序的
·字典中的key必须是不可变对象
·字典也可以根据需要动态地伸缩
·字典会浪费较大的内存，是一种使用空间换时间的数据结构
'''
scores = {'name': '张三', 'name': '李四'}
print(scores)
scores = {'name': '张三', 'othername': '张三'}
print(scores)

#字典生成式,以元素少的为基准生成
items=['Fruits','Books','Others']
prices=[10,20,30,40,50]

d={item.upper():price for item,price in zip(items,prices)}
print(d,type(d))