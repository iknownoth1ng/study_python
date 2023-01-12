#!/usr/bin/env python
# -*- encoding: utf-8 -*-
"""
@File    :   test_01.py
@Time    :   2023/01/11 18:55:29
@Author  :   owl
@Email   :   xxxxx@163.com
@Desp    :   01单元测试基础
"""

# %%[markdown]
# 单元测试基础
## 什么是单元测试
"""
单元测试是指一个自动化的测试：
- 用来验证一小段代码（单元）的正确性
- 可以快速执行
- 在独立的环境中执行
"""
# %%[markdown]
## 常用的文件结构
""" ![常用的文件结构](image\\03\\常用的文件结构.png)"""
## 编写第一个单元测试
"""
Python提供了unittest模块：
- 测试类继承unittest.TestCase
- 测试类的名字以Test开头
- 测试方法的名字以test_开头"""
# %%
import unittest
from test.basic.calculator import Calculator


class TestCalculator(unittest.TestCase):
    def test_add(self):
        # Setup
        cal = Calculator()
        expected_result = 10
        # Action
        actual_result = cal.add(2, 3, 5)
        # Assert
        self.assertEqual(actual_result, expected_result)


# %%[markdown]
## 运行单元测试
if __name__ == "__main__":
    unittest.main()
