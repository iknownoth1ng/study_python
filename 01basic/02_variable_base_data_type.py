
#!/usr/bin/env python
# -*- encoding: utf-8 -*-
'''
@File    :   2.1_variable_base_data_type.py
@Time    :   2022/05/12 16:42:31
@Author  :   owl
@Email   :   xxxxx@163.com
@Desp    :   变量和基础数据类型
'''

# here put the import lib

'''
变量：
  在计算机程序中，变量不仅可以是数字，还可以是任意数据类型。
  命名规则：
  变量名必须是大小写英文、数字和_的组合,且不能用数字开头
  a = 1
  t_007 = 'T007'
  Answer = True
常量：
  就是不能变的变量，比如常用的数学常数π就是一个常量。
  在Python中，通常用全部大写的变量名表示常量。
  PI=3.14

'''
# 变量，规则：变量名 赋值运算符 值
from decimal import Decimal
a = 'maria'
print(a)
print('id: ', id(a))
print('type: ', type(a))
print('value: ', a)

a = 'machael'
print("id: ", id(a))

'''
基本数据类型
整数(int)
浮点数((float)
字符串(str)
布尔值(bool)
'''
# 整数
a = 10
b = 0b110
c = 0o170
d = 0xA
print(a, b, c, d, type(a), type(b), type(c), type(d))

# 浮点数
f = 3.1415
print(f, type(f))
f1 = 1.1
f2 = 2.2
print(f1+f2)  # 浮点数计算不精确
print(Decimal('1.1')+Decimal('2.2'))
# 布尔值
b1 = True
b2 = False
print(b1, type(b1))
print(b2, type(b2))

print(True+1)
print(False+1)

# 字符串
s1 = 'ok,fine'
s2 = "ok,fine"
s3 = '''ok,
fine'''
print(s3)
print(s1, s2, s3, type(s1), type(s2), type(s3))

'''
基本数据类型之间的转换
'''
# str()
name = '张三'
age = 18
print('我的名字叫：'+name+' 今年'+str(age)+'岁了')

a = 1.1415
c = False
print(type(a), type(c), type(str(a)), type(str(c)))

# int() 不能转文字类型和小数类型的字符串
a = 'abc'
b = '1.1'
#print(int(a), int(b))
c = False
# 浮点数会取整
d = 3.1
print(int(c), int(d))


# float() 文字类字符串类无法转成整数
print(float('1'))
print(float('1.12'))

# print(float("abc"))
# 整数转成浮点型，末尾会加.0
print(float(1))
print(float(True))
