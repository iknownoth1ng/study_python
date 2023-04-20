#!/usr/bin/env python
# -*- encoding: utf-8 -*-
"""
@File    :   test_rename_fixture.py
@Time    :   2023/04/20 23:40:59
@Author  :   owl
@Email   :   xxxxx@163.com
@Desp    :   使用@pytest.fixture(name='xxx')对fixture重命名。
"""
import pytest


@pytest.fixture(name="lue")
def ultimate_answer_to_life_the_universe_and_everything():
    """Return ultimate answer."""
    return 42


def test_everything(lue):
    assert lue == 42


if __name__ == "__main__":
    # pytest.main(["--setup-show", __file__])
    pytest.main(["--fixtures", __file__])
# end main
