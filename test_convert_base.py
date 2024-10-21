from unittest import TestCase
import Q1

class Test(TestCase):
    def test_convert_base_new_base_is_2_and_base_10_integer_is_5(self):
        actual = Q1.convert_base(5, 2)
        expected = '101'
        self.assertEqual(actual, expected)

    def test_convert_base_new_base_is_4_and_base_10_integer_is_5(self):
        actual = Q1.convert_base(5, 4)
        expected = '11'
        self.assertEqual(actual, expected)

    def test_convert_base_new_base_is_8_and_base_10_integer_is_5(self):
        actual = Q1.convert_base(5, 8)
        expected = '5'
        self.assertEqual(actual, expected)

    def test_convert_base_new_base_is_2_and_base_10_integer_is_25(self):
        actual = Q1.convert_base(25, 2)
        expected = '11001'
        self.assertEqual(actual, expected)

    def test_convert_base_new_base_is_5_and_base_10_integer_is_25(self):
        actual = Q1.convert_base(25, 5)
        expected = '100'
        self.assertEqual(actual, expected)

    def test_convert_base_new_base_is_9_and_base_10_integer_is_25(self):
        actual = Q1.convert_base(25, 9)
        expected = '27'
        self.assertEqual(actual, expected)

    def test_convert_base_new_base_is_3_and_base_10_integer_is_123(self):
        actual = Q1.convert_base(123, 3)
        expected = '11120'
        self.assertEqual(actual, expected)

    def test_convert_base_new_base_is_6_and_base_10_integer_is_123(self):
        actual = Q1.convert_base(123, 6)
        expected = '323'
        self.assertEqual(actual, expected)

    def test_convert_base_new_base_is_9_and_base_10_integer_is_123(self):
        actual = Q1.convert_base(123, 9)
        expected = '146'
        self.assertEqual(actual, expected)

    def test_convert_base_new_base_is_2_and_base_10_integer_is_15(self):
        actual = Q1.convert_base(15, 2)
        expected = '1111'
        self.assertEqual(actual, expected)

    def test_convert_base_new_base_is_3_and_base_10_integer_is_8(self):
        actual = Q1.convert_base(8, 3)
        expected = '22'
        self.assertEqual(actual, expected)

    def test_convert_base_new_base_is_4_and_base_10_integer_is_15(self):
        actual = Q1.convert_base(15, 4)
        expected = '33'
        self.assertEqual(actual, expected)

    def test_convert_base_new_base_is_5_and_base_10_integer_is_20(self):
        actual = Q1.convert_base(20, 5)
        expected = '40'
        self.assertEqual(actual, expected)

    def test_convert_base_new_base_is_6_and_base_10_integer_is_37(self):
        actual = Q1.convert_base(37, 6)
        expected = '101'
        self.assertEqual(actual, expected)

    def test_convert_base_new_base_is_7_and_base_10_integer_is_22(self):
        actual = Q1.convert_base(22, 7)
        expected = '31'
        self.assertEqual(actual, expected)

    def test_convert_base_new_base_is_8_and_base_10_integer_is_30(self):
        actual = Q1.convert_base(30, 8)
        expected = '36'
        self.assertEqual(actual, expected)

    def test_convert_base_new_base_is_9_and_base_10_integer_is_55(self):
        actual = Q1.convert_base(55, 9)
        expected = '61'
        self.assertEqual(actual, expected)
