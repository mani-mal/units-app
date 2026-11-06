"""Tests for the unit converter."""

import math
import unittest

from units import convert, supported


class ConvertTest(unittest.TestCase):
    def test_identity(self):
        self.assertEqual(convert(5, "meters", "meters"), 5)

    def test_celsius_fahrenheit(self):
        self.assertAlmostEqual(convert(100, "celsius", "fahrenheit"), 212)

    def test_feet_meters(self):
        self.assertAlmostEqual(convert(1, "meters", "feet"), 3.28084)

    def test_case_insensitive(self):
        self.assertAlmostEqual(convert(0, "CELSIUS", "fahrenheit"), 32)

    def test_unsupported(self):
        with self.assertRaises(ValueError):
            convert(1, "celsius", "miles")

    def test_supported_lists_pairs(self):
        self.assertIn("celsius -> fahrenheit", supported())


if __name__ == "__main__":
    unittest.main()
