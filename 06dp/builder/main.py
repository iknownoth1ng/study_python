#!/usr/bin/env python
# -*- encoding: utf-8 -*-
"""
@File    :   main.py
@Time    :   2023/03/18 17:48:40
@Author  :   owl
@Email   :   xxxxx@163.com
@Desp    :   Builder Design Pattern
"""
from __future__ import annotations  # 引入新版本特性，支持类型注解

from abc import ABC, abstractmethod
from typing import Any


class Car:
    def __init__(self) -> None:
        self.parts = []

    def add(self, part: Any) -> None:
        self.parts.append(part)

    def list_parts(self) -> None:
        print(f"Car parts: {', '.join(self.parts)}")


class Manual:
    def __init__(self) -> None:
        self.parts = []

    def add(self, part: Any) -> None:
        self.parts.append(part)

    def list_parts(self) -> None:
        print(f"Manual parts: {', '.join(self.parts)}", end="")


class Builder(ABC):
    @abstractmethod
    def reset(self) -> None:
        pass

    @property
    @abstractmethod
    def product(self) -> None:
        pass

    @abstractmethod
    def produce_part_engine(self) -> None:
        pass

    @abstractmethod
    def produce_part_battery(self) -> None:
        pass

    @abstractmethod
    def produce_part_gps(self) -> None:
        pass


class BYDBuidler(Builder):
    def __init__(self) -> None:
        self.reset()

    def reset(self) -> None:
        self._car = Car()

    def product(self) -> Car:
        car = self._car
        self.reset()
        return car

    def produce_part_engine(self) -> None:
        self._car.add("引擎：1.5T")

    def produce_part_battery(self) -> None:
        self._car.add("电池：刀片电池")

    def produce_part_gps(self) -> None:
        self._car.add("定位技术：北斗")


class BYDManualBuidler(Builder):
    def __init__(self) -> None:
        self.reset()

    def reset(self) -> None:
        self._manual = Manual()

    def product(self) -> Manual:
        manual = self._manual
        self.reset()
        return manual

    def produce_part_engine(self) -> None:
        self._manual.add("byd引擎操作手册")

    def produce_part_battery(self) -> None:
        self._manual.add("byd电池保养手册")

    def produce_part_gps(self) -> None:
        self._manual.add("byd定位技术北斗手册")


class TeslaBuidler(Builder):
    def __init__(self) -> None:
        self.reset()

    def reset(self) -> None:
        self._car = Car()

    def product(self) -> Car:
        car = self._car
        self.reset()
        return car

    def produce_part_engine(self) -> None:
        self._car.add("引擎：双电机全轮驱动")

    def produce_part_battery(self) -> None:
        self._car.add("电池：三元锂离子电池")

    def produce_part_gps(self) -> None:
        self._car.add("定位技术：美国GPS")


class TeslaManualBuidler(Builder):
    def __init__(self) -> None:
        self.reset()

    def reset(self) -> None:
        self._manual = Manual()

    def product(self) -> Manual:
        manual = self._manual
        self.reset()
        return manual

    def produce_part_engine(self) -> None:
        self._manual.add("tesla引擎操作手册")

    def produce_part_battery(self) -> None:
        self._manual.add("tesla电池保养手册")

    def produce_part_gps(self) -> None:
        self._manual.add("tesla定位技术GPS手册")


class Director:
    @property
    def builder(self) -> Builder:
        return self._builder

    @builder.setter
    def builder(self, builder: Builder) -> None:
        self._builder = builder

    def construct_byd_car(self):  # sourcery skip: class-extract-method
        self.builder.reset()
        self.builder.produce_part_engine()
        self.builder.produce_part_battery()
        self.builder.produce_part_gps()

    def construct_byd_manual(self):
        self.builder.reset()
        self.builder.produce_part_engine()
        self.builder.produce_part_battery()
        self.builder.produce_part_gps()


if __name__ == "__main__":
    # * byd新能源车
    director = Director()
    byd = BYDBuidler()
    director.builder = byd
    director.construct_byd_car()
    byd.product().list_parts()

    # * 自定义车辆
    byd.produce_part_battery()
    byd.produce_part_engine()
    byd.product().list_parts()


# end main
