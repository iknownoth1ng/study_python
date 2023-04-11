#!/usr/bin/env python
# -*- encoding: utf-8 -*-
"""
@File    :   main.py
@Time    :   2023/04/11 14:37:28
@Author  :   owl
@Email   :   xxxxx@163.com
@Desp    :   抽象工厂模式
"""
import platform
from abc import ABC, abstractmethod


class Button(ABC):
    @abstractmethod
    def paint(self):
        pass


class WindowsButton(Button):
    def paint(self):
        print("windows按钮渲染")


class MacOSButton(Button):
    def paint(self):
        print("MacOS按钮渲染")


class Checkbox(ABC):
    @abstractmethod
    def paint(self):
        pass


class WindowsCheckbox(Checkbox):
    def paint(self):
        print("windows检查框渲染")


class MacOSCheckbox(Checkbox):
    def paint(self):
        print("MacOS检查框渲染")


class GUIFactory(ABC):
    @abstractmethod
    def create_button(self) -> Button:
        pass

    @abstractmethod
    def create_checkbox(self) -> Checkbox:
        pass


class WindowsFactory(GUIFactory):
    def create_button(self) -> Button:
        return WindowsButton()

    def create_checkbox(self) -> Checkbox:
        return WindowsCheckbox()


class MacOSFactory(GUIFactory):
    def create_button(self) -> Button:
        return MacOSButton()

    def create_checkbox(self) -> Checkbox:
        return MacOSCheckbox()


def client_code(factory: GUIFactory):
    button = factory.create_button()
    button.paint()
    checkbox = factory.create_checkbox()
    checkbox.paint()


if __name__ == "__main__":
    factory = None
    os = platform.system()
    if os == "Windows":
        factory = WindowsFactory()
    elif os == "MacOS":
        factory = MacOSFactory()
    else:
        raise ValueError(f"未知的操作系统{os}！！！")

    if factory:
        client_code(factory)
# end main
