# type:ignore
import unittest

from tests.fixtures.bank_account import BankAccount


def setUpModule():
    print("calling setUpModule")


def tearDownModule():
    print("calling tearDownModule")


class TestBankAccount(unittest.TestCase):
    @classmethod
    def setUpClass(cls) -> None:
        print("calling setUpClass")

    @classmethod
    def tearDownClass(cls) -> None:
        print("calling tearDownClass")

    def setUp(self):
        print("calling setUp")
        self.bank_account = BankAccount(10)

    def tearDown(self):
        print("calling tearDown")
        self.bank_account = None

    def test_deposit_success(self):
        self.bank_account.deposit(10)
        self.assertEqual(20, self.bank_account.balance)

    def test_withdraw_success(self):
        self.bank_account.withdraw(10)
        self.assertEqual(0, self.bank_account.balance)


if __name__ == "__main__":
    unittest.main()
