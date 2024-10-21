from unittest import TestCase

import Q3


class Test(TestCase):
    def test_get_direction_of_shift_when_encode_is_true(self):
        actual = Q3.get_direction_of_shift(True)
        expected = 1
        self.assertEqual(actual, expected)

    def test_get_direction_of_shift_when_encode_is_false(self):
        actual = Q3.get_direction_of_shift(False)
        expected = -1
        self.assertEqual(actual, expected)
