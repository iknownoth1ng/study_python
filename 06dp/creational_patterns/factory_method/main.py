#!/usr/bin/env python
# -*- encoding: utf-8 -*-
"""
@File    :   main.py
@Time    :   2023/04/11 13:49:42
@Author  :   owl
@Email   :   xxxxx@163.com
@Desp    :   工厂方法模式
"""
from __future__ import annotations

from abc import ABC, abstractmethod


class Product(ABC):
    @abstractmethod
    def operation(self):
        pass


class ConcreteProductA(Product):
    def operation(self):
        return "{Result of the ConcreteProductA}"


class ConcreteProductB(Product):
    def operation(self):
        return "{Result of the ConcreteProductB}"


class Creator(ABC):
    @abstractmethod
    def factory_method(self) -> Product:
        pass

    def some_operation(self):
        product = self.factory_method()
        return f"Creator: The same creator's code has just worked with {product.operation()}"


class ConcreteCreatorA(Creator):
    def factory_method(self) -> Product:
        return ConcreteProductA()


class ConcreteCreatorB(Creator):
    def factory_method(self) -> Product:
        return ConcreteProductB()


def client_code(creator: Creator):
    print(
        f"Client: I'm not aware of the creator's class, but it still works.\n"
        f"{creator.some_operation()}",
        end="",
    )


if __name__ == "__main__":
    print("App: Launched with the ConcreteCreatorA.")
    client_code(ConcreteCreatorA())
    print("\n")

    print("App: Launched with the ConcreteCreatorB.")
    client_code(ConcreteCreatorB())

# end main
