import unittest
from unittest.mock import MagicMock, patch

from tests.service.product_service import ProductService


class TestProductService(unittest.TestCase):
    def setUp(self) -> None:
        self.service = ProductService()

    def tearDown(self) -> None:
        self.service = None

    @patch("tests.service.product_service.urlopen")
    @patch("tests.service.product_service.Request.__new__")
    def test_download_img_with_exception(self, request_mock, urlopen_mock):
        # SetUp
        url = "https://www.bing.com/cn"

        urlopen_return_mock = MagicMock()
        webfile_mock = MagicMock()

        urlopen_mock.return_value = urlopen_return_mock
        urlopen_return_mock.__enter__.return_value = webfile_mock
        webfile_mock.read.return_value = None

        with self.assertRaises(ValueError):
            # Action
            self.service.download_img(url)  # type:ignore

    @patch("builtins.open")
    @patch("os.path.basename")
    @patch("tests.service.product_service.urlopen")
    @patch("tests.service.product_service.Request.__new__")
    def test_download_img_with_success(
        self, request_mock, urlopen_mock, basename_mock, open_mock
    ) -> None:
        url = "https://www.bing.com/cn"

        urlopen_return_mock = MagicMock()
        webfile_mock = MagicMock()

        urlopen_mock.return_value = urlopen_return_mock
        urlopen_return_mock.__enter__.return_value = webfile_mock
        webfile_mock.read.return_value = "not none"

        basename_mock.return_value = "fff"

        # Action
        result = self.service.download_img(url)  # type:ignore

        # Assert
        self.assertEqual("Download image successfully, fff", result)
