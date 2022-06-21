#!/usr/bin/env python
# -*- encoding: utf-8 -*-
'''
@File    :   meta_class.py
@Time    :   2022/06/16 13:33:54
@Author  :   owl
@Email   :   xxxxx@163.com
@Desp    :   metaclass
'''

# here put the import lib
from typing import Any


class MyMetaClass(type):
    def __init__(self,name,bases,dic):
        super().__init__(name,bases,dic)
        print('===>MyMetaClass.__init__')
        print(self.__name__)
        print(dic)
        print(self.yaml_tag)

    def __new__(cls,*args,**kws):
        print('===>MyMetaClass.__new__')
        print(cls.__name__)
        return type.__new__(cls,*args,**kws)

    def __call__(cls, *args: Any, **kwds: Any) -> Any:
        print('===>MyMetaClass.__call__')
        obj=cls.__new__(cls)
        cls.__init__(cls,*args,**kwds)
        return obj


class Foo(metaclass=MyMetaClass):
    yaml_tag='!Foo'

    def __init__(self,name):
        print('===>Foo.__init__')
        self.name = name

    def __new__(cls,*args,**kws):
        print('===>Foo.__new___')
        return super().__new__(cls)

        
foo=Foo('foo')