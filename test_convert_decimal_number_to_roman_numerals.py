from unittest import TestCase
import Q2

class Test(TestCase):
    def test_convert_decimal_number_to_roman_numerals__decimal_number_is_1(self):
        actual = Q2.convert_decimal_number_to_roman_numerals("1")
        expected = "I"
        self.assertEqual(actual, expected)

    def test_convert_decimal_number_to_roman_numerals__decimal_number_is_5(self):
        actual = Q2.convert_decimal_number_to_roman_numerals("5")
        expected = "V"
        self.assertEqual(actual, expected)

    def test_convert_decimal_number_to_roman_numerals__decimal_number_is_10(self):
        actual = Q2.convert_decimal_number_to_roman_numerals("10")
        expected = 'X'
        self.assertEqual(actual, expected)

    def test_convert_decimal_number_to_roman_numerals__decimal_number_is_25(self):
        actual = Q2.convert_decimal_number_to_roman_numerals("25")
        expected = 'XXV'
        self.assertEqual(actual, expected)

    def test_convert_decimal_number_to_roman_numerals__decimal_number_is_50(self):
        actual = Q2.convert_decimal_number_to_roman_numerals("50")
        expected = 'L'
        self.assertEqual(actual, expected)

    def test_convert_decimal_number_to_roman_numerals__decimal_number_is_99(self):
        actual = Q2.convert_decimal_number_to_roman_numerals("99")
        expected = 'XCIX'
        self.assertEqual(actual, expected)

# 100 , 500 , 999

    def test_convert_decimal_number_to_roman_numerals__decimal_number_is_100(self):
        actual = Q2.convert_decimal_number_to_roman_numerals("100")
        expected = 'C'
        self.assertEqual(actual, expected)

    def test_convert_decimal_number_to_roman_numerals__decimal_number_is_500(self):
        actual = Q2.convert_decimal_number_to_roman_numerals("500")
        expected = 'D'
        self.assertEqual(actual, expected)

    def test_convert_decimal_number_to_roman_numerals__decimal_number_is_999(self):
        actual = Q2.convert_decimal_number_to_roman_numerals("999")
        expected = 'CMXCIX'
        self.assertEqual(actual, expected)

# 1000, 2000, 3000, 3999

    def test_convert_decimal_number_to_roman_numerals__decimal_number_is_1000(self):
        actual = Q2.convert_decimal_number_to_roman_numerals("1000")
        expected = 'M'
        self.assertEqual(actual, expected)

    def test_convert_decimal_number_to_roman_numerals__decimal_number_is_2000(self):
        actual = Q2.convert_decimal_number_to_roman_numerals("2000")
        expected = 'MM'
        self.assertEqual(actual, expected)

    def test_convert_decimal_number_to_roman_numerals__decimal_number_is_3000(self):
        actual = Q2.convert_decimal_number_to_roman_numerals("3000")
        expected = 'MMM'
        self.assertEqual(actual, expected)


    def test_convert_decimal_number_to_roman_numerals__decimal_number_is_3999(self):
        actual = Q2.convert_decimal_number_to_roman_numerals("3999")
        expected = 'MMMCMXCIX'
        self.assertEqual(actual, expected)

#  4000, 4500, 5000

    def test_convert_decimal_number_to_roman_numerals__decimal_number_is_4000(self):
        actual = Q2.convert_decimal_number_to_roman_numerals("4000")
        expected = 'MMMM'
        self.assertEqual(actual, expected)

    def test_convert_decimal_number_to_roman_numerals__decimal_number_is_4500(self):
        actual = Q2.convert_decimal_number_to_roman_numerals("4500")
        expected = 'MMMMD'
        self.assertEqual(actual, expected)


    def test_convert_decimal_number_to_roman_numerals__decimal_number_is_5000(self):
        actual = Q2.convert_decimal_number_to_roman_numerals("5000")
        expected = 'MMMMM'
        self.assertEqual(actual, expected)

