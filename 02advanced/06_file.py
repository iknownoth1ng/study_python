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

# 读写操作、常用打开模式
src_file=open("logo.png","rb")
target_file=open('copyfile.png','wb')
target_file.write(src_file.read())

src_file.close()
target_file.close()

# 文件对象的常用操作
file1=open('a.txt','r', encoding="utf-8")
print(file1.read(2))
print(file1.readline())
print(file1.readlines())
print(file1.seek(2))
print(file1.tell())
file1.close()

file2=open('b.txt','w',encoding="utf-8")    
file2.write('hello')
file2.flush()
file2.write('python')
file2.close()

# with语句（上下文管理器）
with open('a.txt','r',encoding="utf-8") as f:
    print(f.read())

class MyContentMgr(object):
    def __enter__(self):
        print('enter方法被调用了')
        return self
    
    def __exit__(self, type, value, traceback):
        print("exit方法被调用了")

    def show(self):
        print('show方法被调用了')
    
with MyContentMgr() as contentMgr:
    contentMgr.show()

# 目录操作
import os
import os.path

print(os.getcwd())
print(os.listdir('../../STUDY_PYTHON'))

print(os.path.abspath('a.txt'))
print(os.path.exists('c.txt'))
print(os.path.join(os.getcwd(),'c.txt'))
print(os.path.split(r'd:\cs\language\python\study_python\02advanced\a.txt'))
print(os.path.splitext('a.txt'))
print(os.path.basename(r'd:\cs\language\python\study_python\02advanced\a.txt'))
print(os.path.dirname(r'd:\cs\language\python\study_python\02advanced\a.txt'))
print(os.path.isdir(r'd:\cs\language\python\study_python\02advanced\a.txt'))

path=os.getcwd()
lst_files=os.walk(path)
for dirpath,dirpathnames, filenames in lst_files:
    print(dirpath)
    print(dirpathnames)
    print(filenames)
    print('********************')