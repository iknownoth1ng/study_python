"""Test the tasks.add() API function."""

import pytest
import tasks
from tasks import Task


def test_add_returns_valid_id():
    """tasks.add(<valid task>) should return an integer."""
    # GIVEN an initialized tasks db
    # WHEN a new task is added
    # THEN returned task_id is of type int
    new_task = Task("do something")
    task_id = tasks.add(new_task)
    assert isinstance(task_id, int)


def test_add_conflict_task_id():
    """add some id raise an exception"""
    t1_id = tasks.add(task=tasks.Task(summary="do something", owner="owl", done=True))
    t2_id = tasks.add(task=tasks.Task(summary="do something", owner="owl", done=True))
    assert t1_id != t2_id


@pytest.mark.smoke
def test_added_task_has_id_set():
    """Make sure the task_id field is set by tasks.add()."""
    # GIVEN an initialized tasks db
    #   AND a new task is added
    new_task = Task("sit in chair", owner="me", done=True)
    task_id = tasks.add(new_task)

    # WHEN task is retrieved
    task_from_db = tasks.get(task_id)

    # THEN task_id matches id field
    assert task_from_db.id == task_id


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
    pytest.main(["-sv", "-m", "smoke", __file__])
# end main
