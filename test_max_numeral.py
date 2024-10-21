from unittest import TestCase
import Q2



class Test(TestCase):
    def test_max_numeral__place_value_is_1(self):
        actual = Q2.max_numeral(1)
        expected = 'X'

    def test_max_numeral__place_value_is_2(self):
        actual = Q2.min_numeral(2)
        expected = 'C'

    def test_max_numeral__place_value_is_3(self):
        actual = Q2.min_numeral(3)
        expected = 'M'
