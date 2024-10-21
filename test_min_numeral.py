from unittest import TestCase

import Q2


class Test(TestCase):
    def test_min_numeral__place_value_is_1(self):
        actual = Q2.min_numeral(1)
        expected = 'I'

    def test_min_numeral__place_value_is_2(self):
        actual = Q2.min_numeral(2)
        expected = 'X'

    def test_min_numeral__place_value_is_3(self):
        actual = Q2.min_numeral(3)
        expected = 'C'
