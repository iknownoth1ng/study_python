#!/usr/bin/env python
# -*- encoding: utf-8 -*-
"""
@File    :   test_autouse.py
@Time    :   2023/04/19 23:52:09
@Author  :   owl
@Email   :   xxxxx@163.com
@Desp    :   Demonstrate autouse fixtures
"""
import time

import pytest


@pytest.fixture(autouse=True, scope="session")
def footer_session_scope():
    """Report the time at the end of a session."""
    yield
    now = time.time()
    print("--")
    print(f"finished: {time.strftime('%d %b %X',time.localtime(now))}")
    print("---------------")


@pytest.fixture(autouse=True)
def foot_function_scope():
    """Report test durations after each function."""
    start = time.time()
    yield
    stop = time.time()
    delta = stop - start
    print(f"\ntest duration : {delta:0.3} second ")


def test_1():
    """Simulate long-ish running test."""
    time.sleep(1)


def test_2():
    """Simulate slightly longer test."""
    time.sleep(1.23)
