from collections import namedtuple
from time import sleep

import pytest

Task = namedtuple("Task", ["summary", "owner", "done", "id"])
Task.__new__.__defaults__ = (None, None, False, None)


def test_asdict():
    """_asdict() should return a dictionary."""
    t1 = Task("do something", "okken", True, 21)
    d1 = t1._asdict()
    expected = {"summary": "do something", "owner": "okken", "done": True, "id": 21}
    assert d1 == expected


@pytest.mark.run_these_please
def test_relace():
    """replace() should change passed in fields."""
    sleep(0.1)
    t_before = Task("finish book", "brian", True)
    t_after = t_before._replace(done=False, id=10)
    expected = Task("finish book", "brian", False, 11)
    assert t_after == expected
