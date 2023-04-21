from typing import Literal

import pytest


@pytest.fixture()
def some_data() -> Literal[42]:
    """Return answer to ultimate question."""
    return 42


def test_some_data(some_data: Literal[42]) -> None:
    """Use fixture return value in a test"""
    assert some_data == 42


@pytest.fixture()
def some_other_data():
    """Raise an exception from fixture."""
    x = 43
    assert x == 42


def test_other_data(some_other_data):
    assert some_other_data


@pytest.fixture()
def a_tuple():
    return (1, "foo", None, {"bar": 23})


def test_a_tuple(a_tuple) -> None:
    assert a_tuple[3]["bar"] == 32


# * 练习
# 添加返回数据的fixture函数，例如返回列表、元组、字典等
@pytest.fixture(scope="module")
def list_data():
    print("fixture-list_data运行前")
    yield [1, 2, 3]
    print("fixture-list_data运行后")


@pytest.fixture()
def tuple_data():
    return (1, 2, 3)


@pytest.fixture()
def dict_data():
    return {1: "hello", 2: "world"}


def test_list_data1(list_data):
    l = list_data
    assert l == [1, 2, 3]


def test_list_data2(list_data):
    l = list_data
    assert type(l) is list
