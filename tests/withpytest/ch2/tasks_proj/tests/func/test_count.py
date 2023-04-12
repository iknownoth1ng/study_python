"""Test the tasks.count() API function."""

import pytest
import tasks
from tasks import Task


def test_count_return_numberof_tasks():
    """tasks.count() should return the number of tasks in db."""
    # GIVEN an initialized tasks db
    # WHEN a new task is added
    # THEN returned task_id is of type int
    tasks.add(Task("do something"))
    task_count = tasks.count()
    assert task_count == 1


@pytest.fixture(autouse=True)
def initialized_tasks_db(tmpdir):
    """Connect to db before testing, disconnect after."""
    # Setup : start db
    tasks.start_tasks_db(
        str(tmpdir), "tiny"
    )  # * tmpdir是属于pytest中的一个内置函数，这个函数表示的意思是在测试开始运行前创建一个临时文件目录，并在测试结束后进行删除。

    yield  # this is where the testing happens

    # Teardown : stop db
    tasks.stop_tasks_db()


if __name__ == "__main__":
    pytest.main(["-sv", __file__])
# end main
