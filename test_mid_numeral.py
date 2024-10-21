from unittest import TestCase
import Q2
class Test(TestCase):
    def test_mid_numeral__place_value_is_1(self):
        actual = Q2.mid_numeral(1)
        expected = 'V'

    def test_mid_numeral__place_value_is_2(self):
        actual = Q2.mid_numeral(2)
        expected = 'L'

    def test_mid_numeral__place_value_is_3(self):
        actual = Q2.mid_numeral(3)
        expected = 'D'


