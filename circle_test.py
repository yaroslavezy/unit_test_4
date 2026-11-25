import unittest
import math
import circle


class CircleTestCase(unittest.TestCase):
    def test_zero_area(self):
        res = circle.area(0)
        self.assertEqual(res, 0)

    def test_unit_area(self):
        res = circle.area(1)
        self.assertAlmostEqual(res, math.pi)

    def test_int_area(self):
        res = circle.area(12)
        self.assertAlmostEqual(res, 144 * math.pi)

    def test_float_area(self):
        res = circle.area(3.5)
        self.assertAlmostEqual(res, 12.25 * math.pi)

    def test_zero_perimeter(self):
        res = circle.perimeter(0)
        self.assertEqual(res, 0)

    def test_unit_perimeter(self):
        res = circle.perimeter(1)
        self.assertAlmostEqual(res, 2 * math.pi)

    def test_int_perimeter(self):
        res = circle.perimeter(14)
        self.assertAlmostEqual(res, 28 * math.pi)

    def test_float_perimeter(self):
        res = circle.perimeter(5.5)
        self.assertAlmostEqual(res, 11 * math.pi)