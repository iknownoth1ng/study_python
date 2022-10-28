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
s = 'hello,python'
print(s.isidentifier())  # False
print('hello'.isidentifier())  # True
print('张三_'.isidentifier())  # True
print('张三_123'.isidentifier())  # True
print()
print('\t'.isspace())  # True
print()
print('abc'.isalpha())  # True
print('张三'.isalpha())  # True
print('张三1'.isalpha())  # False
print()
print('123'.isdecimal())  # True
print('123四'.isdecimal())  # False
print('Ⅲ'.isdecimal())  # False
print()
print('123'.isnumeric())  # True
print('123四'.isnumeric())  # True
print('Ⅲ'.isnumeric())  # True
print()
print('abc1'.isalnum())  # True
print('张三123'.isalnum())  # True
print('abc!'.isalnum())  # False

# 字符串的其他操作
# replace()替换
s = 'hello python'
print(s.replace('python', 'java'))
s = 'hello python python python'
print(s.replace('python', 'java', 2))  # 替换两次

# join()将列表或元组中的字符串合并成一个字符串
lst = ['hello', 'python', 'java']
print(''.join(lst))
print("|".join(lst))

t1 = ('hello', 'python', 'java')
print(''.join(t1))
print("|".join(t1))

print('*'.join('python'))


# 字符串的比较操作
print('apple' > 'app')
print('apple' > 'banana')
print(ord('a'), ord("b"))  # ord()原始值
print(chr(97), chr(98))  # chr()对应字符

'''
==比较的是value
is比较的内存地址id
'''
a = b = 'python'
c = 'python'
print(a == b, b == c)
print(id(a), id(b), id(c))

# 字符串的切片操作
s = 'hello,python'
s1 = s[:5]
s2 = s[6:]
s3 = '!'
newstr = s1+s3+s2
print(s1)
print(s2)
print(newstr)
print(id(s))
print(id(s1))
print(id(s2))
print(id(s3))
print(id(newstr))

print(s[:5:-1])
print(s[5::-1])

# 格式化字符串
# 1.使用%占位符
name = '张三'
age = 18
print('我的名字叫%s,今年%d岁了' % (name, age))
# 2.使用{}占位符
print("我的名字叫{0},今年{1}岁了,我真的叫{0}".format(name, age))
# 3.f-string
print(f'我的名字叫{name},今年{age}岁了')

print('%10d' % 99)  # 10表示的是总共宽度,右对齐
print('%-10d' % 99)  # 左对齐
print('%.3f' % 3.1415926)  # .3表示的是小数点后三位
print('%10.3f' % 3.1415926)  # 同时表示精度和宽度

print('growth rate: %d %%' % 7)  # 用%%来表示一个%

print('{0:.3}'.format(3.1415926))  # 3.14
print('{0:.3f}'.format(3.1415926))  # 3.142
print('{0:10.3f}'.format(3.1415926))  # 同时表示精度和宽度

# 字符串的编码和解码
s='天涯共此时'
# b代表二进制,一个中文在GBK占用2个字节，在UTF-8占用3个字节
print(s.encode(encoding='GBK')) #  b'\xcc\xec\xd1\xc4\xb9\xb2\xb4\xcb\xca\xb1'
print(s.encode(encoding='UTF-8'))# b'\xe5\xa4\xa9\xe6\xb6\xaf\xe5\x85\xb1\xe6\xad\xa4\xe6\x97\xb6'

b=s.encode(encoding='GBK')
print(b.decode(encoding="GBK")) #天涯共此时