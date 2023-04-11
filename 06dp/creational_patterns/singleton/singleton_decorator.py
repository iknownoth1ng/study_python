#!/usr/bin/env python
# -*- encoding: utf-8 -*-
"""
@File    :   singleton_decorator.py
@Time    :   2023/04/11 12:25:41
@Author  :   owl
@Email   :   xxxxx@163.com
@Desp    :   单例-装饰器实现 https://blog.csdn.net/Spade_/article/details/108425896  (Python 的模块就是天然的单例模式，因为模块在第一次导入时，会生成 .pyc 文件，当第二次导入时，就会直接加载 .pyc 文件，而不会再次执行模块代码。)
"""


def singleton(cls):
    print("singleton==>is_called...")
    _instance = {}

    def getinstance(*args, **kwargs):
        print("getinstance==>is_called...")
        if cls not in _instance:
            _instance[cls] = cls(*args, **kwargs)
        return _instance[cls]

    return getinstance


@singleton
class MyClass:
    def __init__(self) -> None:
        print("__init__==>is_called...")
        super().__init__()

    def __new__(cls):
        print("__new__==>is_called...")
        return super().__new__(cls)


if __name__ == "__main__":
    print(MyClass() is MyClass())
# end main
