from unittest import TestCase
import Q3


class Test(TestCase):
    def test_encode_letter__lowercase_letter_a(self):
        actual = Q3.encode_letter(letter='a', ascii_offset=97, shift=26, direction_of_shift=1)
        expected = 'a'
        self.assertEqual(actual, expected)

    def test_encode_letter__lowercase_letter_a(self):
        actual = Q3.encode_letter(letter='a', ascii_offset=97, shift=26, direction_of_shift=-1)
        expected = 'a'
        self.assertEqual(actual, expected)

    def test_encode_letter__lowercase_letter_a(self):
        actual = Q3.encode_letter(letter='a', ascii_offset=97, shift=27, direction_of_shift=1)
        expected = 'b'
        self.assertEqual(actual, expected)

    def test_encode_letter__lowercase_letter_a(self):
        actual = Q3.encode_letter(letter='a', ascii_offset=97, shift=1, direction_of_shift=1)
        expected = 'b'
        self.assertEqual(actual, expected)

    def test_encode_letter__lowercase_letter_f(self):
        actual = Q3.encode_letter(letter='f', ascii_offset=97, shift=1, direction_of_shift=1)
        expected = 'g'
        self.assertEqual(actual, expected)

    def test_encode_letter__lowercase_letter_z(self):
        actual = Q3.encode_letter(letter='z', ascii_offset=97, shift=1, direction_of_shift=1)
        expected = 'a'
        self.assertEqual(actual, expected)

    def test_encode_letter__uppercase_letter_A(self):
        actual = Q3.encode_letter(letter='A', ascii_offset=65, shift=1, direction_of_shift=1)
        expected = 'B'
        self.assertEqual(actual, expected)

    def test_encode_letter__uppercase_letter_F(self):
        actual = Q3.encode_letter(letter='F', ascii_offset=65, shift=1, direction_of_shift=1)
        expected = 'G'
        self.assertEqual(actual, expected)

    def test_encode_letter__uppercase_letter_Z(self):
        actual = Q3.encode_letter(letter='Z', ascii_offset=65, shift=1, direction_of_shift=1)
        expected = 'A'
        self.assertEqual(actual, expected)

    def test_encode_letter__shift_zero(self):
        actual = Q3.encode_letter(letter='a', ascii_offset=97, shift=0, direction_of_shift=1)
        expected = 'a'
        self.assertEqual(actual, expected)

    def test_encode_letter__shift_negative(self):
        actual = Q3.encode_letter(letter='a', ascii_offset=97, shift=-1, direction_of_shift=1)
        expected = 'z'
        self.assertEqual(actual, expected)

    def test_encode_letter__direction_of_shift_positive(self):
        actual = Q3.encode_letter(letter='a', ascii_offset=97, shift=2, direction_of_shift=1)
        expected = 'c'
        self.assertEqual(actual, expected)

    def test_encode_letter__direction_of_shift_negative(self):
        actual = Q3.encode_letter(letter='a', ascii_offset=97, shift=2, direction_of_shift=-1)
        expected = 'y'
        self.assertEqual(actual, expected)
