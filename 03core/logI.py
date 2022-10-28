#!/usr/bin/env python
# -*- encoding: utf-8 -*-
'''
@File    :   logI.py
@Time    :   2022/06/23 14:29:15
@Author  :   owl
@Email   :   xxxxx@163.com
@Desp    :   loggin日志模块
'''

# here put the import lib
# DEBUG —>INFO —> WARNING —> ERROR —> CRITICAL
import logging

# logging.basicConfig(level=logging.WARNING,  
#                     format='%(asctime)s - %(filename)s[line:%(lineno)d] - %(levelname)s: %(message)s')  

# # 开始使用log功能
# logging.debug('这是 loggging debug message')  
# logging.info('这是 loggging info message')  
# logging.warning('这是 loggging a warning message')  
# logging.error('这是 an loggging error message')  
# logging.critical('这是 loggging critical message') 

  
logging.basicConfig(level=logging.WARNING,  
                    filename='./log.txt',  
                    filemode='w',  
                    format='%(asctime)s - %(filename)s[line:%(lineno)d] - %(levelname)s: %(message)s')  
# use logging  
logging.debug('这是 loggging debug message')
logging.info('这是 loggging info message')  
logging.warning('这是 loggging a warning message')  
logging.error('这是 an loggging error message')  
logging.critical('这是 loggging critical message')

'''
3、日志格式说明
logging.basicConfig函数中，可以指定日志的输出格式format，这个参数可以输出很多有用的信息，如下:

%(levelno)s: 打印日志级别的数值
%(levelname)s: 打印日志级别名称
%(pathname)s: 打印当前执行程序的路径，其实就是sys.argv[0]
%(filename)s: 打印当前执行程序名
%(funcName)s: 打印日志的当前函数
%(lineno)d: 打印日志的当前行号
%(asctime)s: 打印日志的时间
%(thread)d: 打印线程ID
%(threadName)s: 打印线程名称
%(process)d: 打印进程ID
%(message)s: 打印日志信息'''
