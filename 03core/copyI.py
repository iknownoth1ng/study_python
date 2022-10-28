#!/usr/bin/env python
# -*- encoding: utf-8 -*-
'''
@File    :   copyI.py
@Time    :   2022/06/15 13:50:49
@Author  :   owl
@Email   :   xxxxx@163.com
@Desp    :   浅拷贝与深拷贝
'''

# here put the import lib
import copy
import os


def count_file(files):
    """
    测试列表中，非隐藏文件的个数
    :param files:
    :return:
    """
    # 4. 提出隐藏文件名
    temp = ""
    for temp in files:
        if temp.startswith("."):
            files.remove(temp)

    # 5. 排序打印测试
    files.sort()
    for file in files:
        print(file)


# 1. 遍历出当前文件夹中所有的文件
file_names = os.listdir("../../")

print("-" * 30)

# 2. 打印所有的文件名
for file in file_names:
    print(file)

print("-" * 30)

# 2. 调用一个函数，用来测试除了隐藏文件之外的文件的个数
count_file(file_names)
# count_file(copy.deepcopy(file_names)) # ----------这行修改了------------

print("-" * 30)

# 3. 打印所有的文件名
for file in file_names:
    print(file)

'''
看到有什么问题吗？
有没有发现在调用函数count_file之后，
原来的列表也被修改了，在开发过程中，往往要保留原列表的样子，
此时为了能够在调用count_file时，不让这个函数对原数据修改，
需要将备份传递，而不是默认的引用传递
'''

a = [11,22,33]
b = copy.copy(a)
print(id(a),id(b)) # 2755594102536 2755593759880
