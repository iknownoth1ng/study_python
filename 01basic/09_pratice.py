#!/usr/bin/env python
# -*- encoding: utf-8 -*-
'''
@File    :   09_pratice.py
@Time    :   2022/05/24 18:58:20
@Author  :   owl
@Email   :   xxxxx@163.com
@Desp    :   字符串
'''

# here put the import lib
'''
·1、字符串的驻留机制
·2、字符串的常用操作
·3、字符串的比较
·4、字符串的切片操作
·5、格式化字符串
·6、字符串的编码转换'''

# 字符串的驻留机制


import sys
a = 'python'
b = "python"
c = '''python'''
print(a, id(a))
print(b, id(b))
print(c, id(c))

'''
字符串的驻留机制
·驻留机制的几种情况（交互模式）
·字符串的长度为0或1时
·符合标识符的字符串
·字符串只在编译时进行驻留，而非运行时
·[-5,256]之间的整数数字
·sys中的intern方法强制2个字符串指向同一个对象
·PyCharm对字符串进行了优化处理'''
# 字符串的长度为0或1时
s1 = ""
s2 = ''
print(s1 is s2)
print(id(s1))
s3 = 'abc'
s4 = 'abc'
print(s3 is s4)
print(id(s3))
# 符合标识符的字符串
s5 = 'abc%'
s6 = 'abc%'
print(s5 is s6)  # 不能在开发工具里，有优化处理,在交互模式里运行
# 字符串只在编译时进行驻留，而非运行时
s7 = 'abc'
s8 = 'ab'+'c'
s9 = ''.join(['ab', 'c'])
print(s7 is s8)
print(s7 is s9)
# [-5,256]之间的整数数字
s10 = -6
s11 = -6
print(s10 is s11)
s12 = -5
s13 = -5
print(s12 is s13)
# sys中的intern方法强制2个字符串指向同一个对象
s5 = 'abc%'
s6 = 'abc%'
s5 = sys.intern(s6)
print(s5 is s6)
'''
·字符串驻留机制的优缺点
·当需要值相同的字符串时，可以直接从字符串池里拿来使用，避免频繁
的创建和销毁，提升效率和节约内存，因此拼接字符串和修改字符串是
会比较影响性能的。
·在需要进行字符串拼接时建议使用str类型的join方法，而非+，因为join(O
方法是先计算出所有字符中的长度，然后再拷贝，只new一次对象，效
率要比"+"效率高'''

# 字符串的查询操作
s = 'hello,hello'
print(s.index('lo'))  # 找到不会返回ValueError
print(s.rindex('lo'))

print(s.find('lo'))  # 找到不会返回-1
print(s.rfind('lo'))


# 字符串的大小写转换操作,转换后会产生一个新的对象
s = 'hello,python'
a = s.upper()
print(s)
print(a)
print(s.lower(), id(s.lower()))
print(s, id(s))

s2 = 'Hello,Python'
s3 = s2.swapcase()
print(s3)

s4 = s.capitalize()
print(s4)

s5 = s.title()
print(s2 is s5, s5)

# 字符串内容对齐操作
s = 'hello,python'
print(s.center(20, '*'))

print(s.ljust(20, '-'))
print(s.ljust(10))  # 返回原字符
print(s.ljust(20))  # 默认空格填充

print(s.rjust(20, '-'))  # 同左对齐

print(s.zfill(20))
print('-8910'.zfill(10))  # 正负号会放到首位
print('+8910'.zfill(10))


# 字符串的劈分操作
s = 'hello world python'
s1 = 'hello|world|python'
# split()
print(s.split())
print(s1.split(sep='|'))
print(s1.split(sep='|', maxsplit=1))
# rsplit()
print(s.rsplit())
print(s1.rsplit(sep='|'))
print(s1.rsplit(sep='|', maxsplit=1))

# 判断字符串的操作方法
s='hello,python'
print(s.isidentifier()) # False
print('hello'.isidentifier()) #True
print('张三_'.isidentifier()) # True
print('张三_123'.isidentifier()) # True
print()
print('\t'.isspace()) # True
print()
print('abc'.isalpha()) # True
print('张三'.isalpha()) # True
print('张三1'.isalpha())# False
print()
print('123'.isdecimal()) # True
print('123四'.isdecimal()) # False
print('Ⅲ'.isdecimal())  # False
print()
print('123'.isnumeric())  # True
print('123四'.isnumeric()) # True
print('Ⅲ'.isnumeric()) # True
print()
print('abc1'.isalnum()) # True
print('张三123'.isalnum()) # True
print('abc!'.isalnum()) # False