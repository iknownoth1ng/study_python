#!/usr/bin/env python
# -*- encoding: utf-8 -*-
'''
@File    :   03_operator.py
@Time    :   2022/05/16 11:16:00
@Author  :   owl
@Email   :   xxxxx@163.com
@Desp    :   运算符
'''

# here put the import lib
'''
赋值运算符 =
input 函数
'''
# present=input("想要什么礼物")
# print(present,type(present)) # input返回的是str类型

# 计算两个数字之和
# a=int(input("输入一个数字"))
# b=int(input("输入另一个数字"))
# print(a+b)

'''
运算符：
算术运算符
赋值运算符
比较运算符
身份运算符
布尔运算符
成员操作符
位运算符
'''


# 算术运算符：
# 标准运算符 + - * / //（整除）
# 取余运算符 %
# 幂运算符 **
print(11//2)
print(11 % 2)
print(2**4)
# 整除，一正一负向下取整
print(-9//4)
# 取模，一正一负，余数=被除数-除数*商
print(9 % -4)  # 9-4*-3
print(-9 % 4)  # -9-4*-3


# 赋值运算符
# 执行顺序从右到左
a = 20+10
print(a)
# 支持链式赋值
a = b = c = 20
print(id(a))
print(id(b))
print(id(c))
# 支持参数赋值
# +=、-=、*=、/=、//=、%=
a += a
print(id(a))
# 支持系列解包赋值
a, b, c = 20, 30, 40
print(id(a), id(b), id(c))

a, b = 20, 30
print('%d\t%d\t'.expandtabs(16) % (a, b))
print('%d\t%d\t' % (id(a), id(b)))
# 交换
a, b = b, a
print('%d\t%d\t'.expandtabs(16) % (a, b))
print('%d\t%d\t' % (id(a), id(b)))


# 比较运算符，结果为布尔值
# >,<,>=,<= !=
a, b = 10, 20
print(a > b, a < b, a >= b, a <= b, a != b)
# ==
print(a == b)

# 身份运算符
# is,is not 对象id的比较,==是value的比较
print(a is b, a is not b)

list1 = [11, 22, 33]
list2 = [11, 22, 33]
print(list1 == list2)
print(list1 is list2, list1 is not list2)

# 布尔运算符
# and, or, not,
a, b = 1, 2
print(a == 1 and b == 2)
print(a == 1 or b == 1)
print(not a == 1)

# 成员操作符 in, not in,
s = 'hello world'
print('h' in s)
print('h' not in s)

# 位运算符
# 位与&  对应数位都是1，结果数位才是1，否则为0
# 位或|  对应数位都是0，结果数位才是0，否则为1
# 左移<<  高位溢出舍弃，低位补0 相当于*2
# 右移>>  低位溢出舍弃，高位补0 相当于/2
# 异或^
# 取反~ 步骤，1.转为二进制 2.取反 3.计算补码 4.转为原码 5.转为10进制
# 负数（原码：符号位为1，负数绝对值的）、（反码：按位取反，符号位不参与）、（补码：反码加1）
a = 22
b = 21
print(bin(a))
print(bin(b))
print(a & b)  # 0b10100
print(a | b)
print(a ^ b)
c = ~a
print(bin(c))
print(~8)
print(c)
print(a << 2)
print(a >> 2)
print(3>>1)
print(-4>>1)
