import unittest

from tests.assert_methods.my_service import MyService


class TestMyService(unittest.TestCase):
    def test_download_img_success(self):
        # Setup
        my_service = MyService()
        # Action
        result = my_service.download_img("http://localhost")
        # Assert
        self.assertEqual(result, True)
        # self.assertTrue(result)

    def test_download_img_exception(self):
        # Setup
        my_service = MyService()
        # Assert
        with self.assertRaises(ValueError):
            my_service.download_img("")
