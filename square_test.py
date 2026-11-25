import unittest
import square


class SquareTestCase(unittest.TestCase):
    def test_zero_area(self):
        res = square.area(0)
        self.assertEqual(res, 0)

    def test_unit_area(self):
        res = square.area(1)
        self.assertEqual(res, 1)

    def test_int_area(self):
        res = square.area(10)
        self.assertEqual(res, 100)

    def test_float_area(self):
        res = square.area(5.5)
        self.assertAlmostEqual(res, 30.25)

    def test_zero_perimeter(self):
        res = square.perimeter(0)
        self.assertEqual(res, 0)

    def test_unit_perimeter(self):
        res = square.perimeter(1)
        self.assertEqual(res, 4)

    def test_int_perimeter(self):
        res = square.perimeter(20)
        self.assertEqual(res, 80)

    def test_float_perimeter(self):
        res = square.perimeter(3.5)
        self.assertAlmostEqual(res, 14)