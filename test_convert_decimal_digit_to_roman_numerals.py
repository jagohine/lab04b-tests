from unittest import TestCase
import Q2

class Test(TestCase):
    def test_convert_decimal_digit_to_roman_numerals__0_1(self):
        actual = Q2.convert_decimal_digit_to_roman_numerals(0, 1)
        expected = ""
        self.assertEqual(actual, expected)

    def test_convert_decimal_digit_to_roman_numerals__0_2(self):
        actual = Q2.convert_decimal_digit_to_roman_numerals(0, 2)
        expected = ""
        self.assertEqual(actual, expected)

    def test_convert_decimal_digit_to_roman_numerals__0_3(self):
        actual = Q2.convert_decimal_digit_to_roman_numerals(0, 3)
        expected = ""
        self.assertEqual(actual, expected)

    def test_convert_decimal_digit_to_roman_numerals__0_4(self):
        actual = Q2.convert_decimal_digit_to_roman_numerals(0, 4)
        expected = ""
        self.assertEqual(actual, expected)

    def test_convert_decimal_digit_to_roman_numerals__1_1(self):
        actual = Q2.convert_decimal_digit_to_roman_numerals(1, 1)
        expected = "I"
        self.assertEqual(actual, expected)

    def test_convert_decimal_digit_to_roman_numerals__1_2(self):
        actual = Q2.convert_decimal_digit_to_roman_numerals(1, 2)
        expected = "X"
        self.assertEqual(actual, expected)

    def test_convert_decimal_digit_to_roman_numerals__1_3(self):
        actual = Q2.convert_decimal_digit_to_roman_numerals(1, 3)
        expected = "C"
        self.assertEqual(actual, expected)

    def test_convert_decimal_digit_to_roman_numerals__1_4(self):
        actual = Q2.convert_decimal_digit_to_roman_numerals(1, 4)
        expected = "M"
        self.assertEqual(actual, expected)

    def test_convert_decimal_digit_to_roman_numerals__5_1(self):
        actual = Q2.convert_decimal_digit_to_roman_numerals(5, 1)
        expected = "V"
        self.assertEqual(actual, expected)

    def test_convert_decimal_digit_to_roman_numerals__5_2(self):
        actual = Q2.convert_decimal_digit_to_roman_numerals(5, 2)
        expected = "L"
        self.assertEqual(actual, expected)

    def test_convert_decimal_digit_to_roman_numerals__5_3(self):
        actual = Q2.convert_decimal_digit_to_roman_numerals(5, 3)
        expected = "D"
        self.assertEqual(actual, expected)

    def test_convert_decimal_digit_to_roman_numerals__5_4(self):
        actual = Q2.convert_decimal_digit_to_roman_numerals(5, 4)
        expected = "MMMMM"
        self.assertEqual(actual, expected)

    def test_convert_decimal_digit_to_roman_numerals__9_1(self):
        actual = Q2.convert_decimal_digit_to_roman_numerals(9, 1)
        expected = "IX"
        self.assertEqual(actual, expected)

    def test_convert_decimal_digit_to_roman_numerals__9_2(self):
        actual = Q2.convert_decimal_digit_to_roman_numerals(9, 2)
        expected = "XC"
        self.assertEqual(actual, expected)

    def test_convert_decimal_digit_to_roman_numerals__9_3(self):
        actual = Q2.convert_decimal_digit_to_roman_numerals(9, 3)
        expected = "CM"
        self.assertEqual(actual, expected)

    def test_convert_decimal_digit_to_roman_numerals__9_4(self):
        actual = Q2.convert_decimal_digit_to_roman_numerals(9, 4)
        expected = "MMMMMMMMM"
        self.assertEqual(actual, expected)

