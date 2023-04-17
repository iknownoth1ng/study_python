#!/usr/bin/env python
# -*- encoding: utf-8 -*-
"""
@File    :   test_scope.py
@Time    :   2023/04/16 23:01:35
@Author  :   owl
@Email   :   xxxxx@163.com
@Desp    :   测试fixture作用域
"""

import pytest


@pytest.fixture(scope="function")
def func_scope():
    """A function scope fixture."""


@pytest.fixture(scope="module")
def mod_scope():
    """A module scope fixture."""


@pytest.fixture(scope="session")
def sess_scope():
    """A session scope fixture."""


@pytest.fixture(scope="class")
def class_scope():
    """A class scope fixture."""


@pytest.fixture(scope="package")
def package_scope():
    """新增的特性 A package scope fixture."""


def test_1(sess_scope, mod_scope, func_scope):
    """Test using session, module, and function scope fixtures."""


def test_2(sess_scope, mod_scope, func_scope):
    """Demo is more fun with multiple tests."""


@pytest.mark.usefixtures("class_scope")
class TestSomething:
    """Demo class scope fixtures."""

    def test_3(self):
        """Test using a class scope fixture."""

    def test_4(self):
        """Again, multiple tests are more fun."""
