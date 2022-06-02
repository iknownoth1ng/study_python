#!/usr/bin/env python
# -*- encoding: utf-8 -*-
'''
@File    :   06_file.py
@Time    :   2022/06/02 17:56:31
@Author  :   owl
@Email   :   xxxxx@163.com
@Desp    :   文件操作
'''

# here put the import lib
# 文件操作
file=open('a.txt','r',encoding="utf-8")
print(file.readlines())
file.close()
