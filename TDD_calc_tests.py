import pytest
import unittest

from TDD_simple_calc import SimpleCalc

class Calc_Test(unittest.TestCase):  # helps us test

    calc_test = SimpleCalc()

    def test_add(self):
        # this naming convention is essential as 'test' is the word that we need to use when naming tests so python interpreter can recognise it so it can run
        self.assertEqual(self.calc_test.add(2, 4), 6)  # 2 + 4 = 6

    def test_subtract(self):
        self.assertEqual(self.calc_test.subtract(4, 2), 2)  # 4 - 2 = 2

    def test_multiply(self):
        self.assertEqual(self.calc_test.multiply(2, 2), 4)  # 2 * 2 = 4

    def test_divide(self):
        self.assertEqual(self.calc_test.divide(6, 3), 2)  # 4 / 2 = 2