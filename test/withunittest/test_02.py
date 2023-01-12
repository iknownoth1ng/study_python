import sys
import unittest
from pprint import pprint

pprint(sys.path)
from test.basic.calculator import Calculator 


class TestCalculator(unittest.TestCase):
    def test_add(self):
        # Setup
        cal = Calculator()
        expected_result = 10
        # Action
        actual_result = cal.add(2, 3, 5)

        # Assert
        self.assertEqual(actual_result, expected_result)


if __name__ == "__main__":
    unittest.main()
