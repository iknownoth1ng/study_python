#!/usr/bin/env python
# -*- encoding: utf-8 -*-
'''
@File    :   08_customize_iterator.py
@Time    :   2022/06/09 14:29:11
@Author  :   owl
@Email   :   xxxxx@163.com
@Desp    :   自定义迭代器
'''

# here put the import lib
class StuSystem(object):
    """
    学生管理系统
    """
    def __init__(self):
        self.stus = []
        self.current_num = 0

    def add(self):
        """
        添加一个新的学生
        :return:
        """
        name = input("请输入新学生的姓名:")
        tel = input("请输入新学生的手机号:")
        address = input("请输入新学生的住址:")
        new_stu = dict()
        new_stu["name"] = name
        new_stu["tel"] = tel
        new_stu["address"] = address
        self.stus.append(new_stu)

    def __iter__(self):
        return self

    def __next__(self):
        if self.current_num < len(self.stus):
            ret = self.stus[self.current_num]
            self.current_num += 1
            return ret
        else:
            self.current_num = 0
            raise StopIteration


# 创建管理系统对象
stu_sys = StuSystem()

# 添加3个学生信息到系统中
stu_sys.add()
stu_sys.add()
stu_sys.add()

# 问题1：怎样才能实现用for循环遍历系统中所有的学生信息呢？下面的方式能实现吗？
for temp in stu_sys:
     print(temp)

# 问题2：如果需要一个列表，这个列表 样子例如 [("张三", "10086"), ("李四", "10010")]
# stu_list = [ ...列表推导式...]
# 这个列表推导式改怎样写才能实现呢？
stu_list = [x for x in stu_sys]
print(stu_list)

stu_list=list(stu_sys)
print(stu_list)