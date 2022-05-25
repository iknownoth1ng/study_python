#!/usr/bin/env python
# -*- encoding: utf-8 -*-
'''
@File    :   05_list_pratice.py
@Time    :   2022/05/18 11:12:19
@Author  :   owl
@Email   :   xxxxx@163.com
@Desp    :   列表
'''

# here put the import lib
'''
·1、列表的创建与删除
·2、列表的查询操作
·3、列表元素的增、删、改操作
·4、列表元素的排序
·5、列表推导式
'''
# 创建列表

list1 = ['hello', 'world', 98]
list2 = list(['hello', 'world', 98])
print(id(list1))
print(id(list2))

# 列表查询
# 获取指定元素的索引
list3 = list(['hello', 'world', 98, 'hello'])
# 如查列表中存在个相同元素，只返回相同元素中的第一个元素的索引
print(list3.index('hello'))
# 如果查询的元素在列表中不存在，则会抛出ValueError
# print(list3.index('python'))
# 还可以在指定的starti和stop之间进行查找
print(list3.index('hello', 1, 4))

# 获取列表中的单个元素
print(list3[3])
print(list3[-1])
# print(list3[4])

# 获取列表中的多个元素
list3a = [10, 20, 30, 40, 50, 60, 70, 80, 90]
list3b = list3a[1:6]
print(id(list3a), id(list3b))
print(list3a[1:6])
print(list3a[1:6:2])
print(list3a[:6])
print(list3a[:6:2])
print(list3a[1:])
print(list3a[1::2])
print(list3a[::-1])
print(list3a[7::-1])
print(list3a[7:0:-1])

print(list3a[-6:-1:1])

for i in list3a:
    print(i, end=" ")
print()
# 列表的增加操作
lst = [10, 20, 30]
print(lst, id(lst))
lst.append(10)
print(lst, id(lst))

# append
lst = [10, 20, 30]
print('%-18s\t' % str(lst), id(lst))
lst.append(10)
print('%-18s\t' % str(lst), id(lst))

# extend,相当于切片增加 a[len(a):] = iterable
lst2 = ['hello', 'python']
lst.extend(lst2)  # [10, 20, 30, 10, 'hello', 'python']
# lst.append(lst2) #[10, 20, 30, 10, ['hello', 'python']]
print(lst)

# insert
lst.insert(1, 'heihei')
print(lst)

# 切片增加
lst[1:] = ['hello', 'python']
print(lst, id(lst))


# 列表的删除操作
# remove 一次删除一个元素
lst = [10, 20, 10, 30, 10, 40, 50]
lst.remove(10)  # 重复元素只别除第一个
# lst.remove(90)#元素不存在抛出ValueError
print(lst)
# pop 删除一个指定索引位置上的元素
lst.pop(1)
print(lst)
# lst.pop(10)#指定索引不存在抛出IndexError
# 不指定索引，删除列表中最后一个元素
lst.pop()
print(lst)

# 切片删除，一次至少删除一个元素，但是产生一个新的对象
lst = [10, 20, 30, 40, 50, 60]
print(lst, id(lst))

# 产生新对象
new_list = lst[1:3]
print(new_list, id(new_list))

# 不产生新对象
lst[1:3] = []
print(lst, id(lst))

# clear 清空列表
lst.clear()
print(lst)
# del 删除列表
del lst
# print(lst) #NameError: name 'lst' is not defined

# 修改操作
lst = [10, 20, 30, 40]
print(lst, id(lst))
lst[2] = 100
print(lst, id(lst))
lst[1:3] = [100, 200, 300, 400]
print(lst, id(lst))

# 列表的排序
lst=[20,40,10,98,54]
print('排序前的列表',lst, id(lst)) 
# sort方法，默认升序排序
lst.sort()
print('排序后的列表',lst, id(lst)) 
lst.sort(reverse=True)
print('倒序后的列表',lst, id(lst)) 

# sorted()内置函数，产生一个新列表，对原列表不改变
lst=[20,40,10,98,54]
print(lst, id(lst))
new_list=sorted(lst)
print(new_list, id(new_list))
new_list = sorted(lst, reverse=True)
print(new_list, id(new_list))

# 列表生成式
lst=[i*i for i in range(1,10)]
print(lst, id(lst))