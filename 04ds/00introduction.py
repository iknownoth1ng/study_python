#!/usr/bin/env python
# -*- encoding: utf-8 -*-
'''
@File    :   00introduction.py
@Time    :   2022/06/22 14:31:38
@Author  :   owl
@Email   :   xxxxx@163.com
@Desp    :   引入
'''

# here put the import lib
'''
先来看一道题:
如果 a+b+c=1000，且 a^2+b^2=c^2（a,b,c 为自然数），如何求出所有a、b、c可能的组合?'''

# 初次尝试
import time
# start_time = time.time()

# for i in range(0,1001):
#     for j in range(0,1001):
#         for k in range(1,1001):
#             if (i+j+k)==1000:
#                 if (i**2+j**2)==(k**2):
#                     print(tuple((i,j,k)))

# end_time = time.time()
# print('spent time : {}'.format(end_time-start_time)) # spent time : 115.2543683052063


# 优化
start_time = time.time()
for i in range(0,1001):
    for j in range(0,1001-i):
        k=1000-j-i
        if (i**2+j**2)==k**2:
            print(tuple((i,j,k)))

end_time = time.time()
print('spent time : {}'.format(end_time-start_time)) # spent time : 0.4270362854003906

# 通过上面的例子能够说明，对于完成同一个任务，不同的计算方法最终执行的效率是千差万别的