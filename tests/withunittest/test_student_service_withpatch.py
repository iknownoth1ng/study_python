import unittest
from unittest.mock import Mock, patch

from tests.service import student_service


class TestStudentService(unittest.TestCase):
    @patch("tests.service.student_service.save_student")
    @patch("tests.service.student_service.find_student_by_id")
    def test_change_name_decorator(self, find_student_mock, save_student_mock):
        # Setup
        student = Mock(id=1, name="Tom")
        find_student_mock.return_value = student

        # Action
        student_service.change_name(1, "Jack")
        # Assert
        self.assertEqual(student.name, "Jack")
        save_student_mock.assert_called()

    def test_change_name_without_record(self):
        # Setup
        student = Mock(id=1, name="Tom")

        with patch(
            "tests.service.student_service.save_student"
        ) as save_student_mock, patch(
            "tests.service.student_service.find_student_by_id"
        ) as find_student_mock:
            # Action
            find_student_mock.return_value = student
            student_service.change_name(1, "Jack")

        # Assert
        self.assertEqual(student.name, "Jack")
        save_student_mock.assert_called()

    @patch("tests.service.student_service.find_student_by_id")
    def test_change_name_manual(self, find_student_mock):
        # Setup
        student = Mock(id=1, name="Tom")
        find_student_mock.return_value = student

        patcher = patch("tests.service.student_service.save_student")
        patcher.start()

        # Action
        student_service.change_name(1, "Jack")
        patcher.stop()
        # Assert
        self.assertEqual(student.name, "Jack")


if __name__ == "__main__":
    unittest.main()
