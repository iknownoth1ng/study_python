import sys

import pytest

from tests.domain.student import Student


def is_skip():
    return sys.platform.casefold() == "win32".casefold()


# @pytest.mark.skip(reason="expired")
@pytest.mark.skipif(condition=is_skip(), reason="skip on windows")
def test_student():
    print("testing student __int__")
    # Action
    student = Student(id=1, name="Jack")

    # Assert
    assert student.id == 1
    assert student.name == "Jack"


class TestStudents:
    def test_student(self):
        # Action
        student = Student(id=1, name="Jack")

        # Assert
        assert student.id == 1
        assert student.name == "Jack"
