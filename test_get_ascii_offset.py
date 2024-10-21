from unittest import TestCase

import Q3

class Test(TestCase):
    def test_get_ascii_offset_lowercase_letter(self):
        actual = Q3.get_ascii_offset("A")
        expected = 97

    def test_get_ascii_offset_uppercase_letter(self):
        actual = Q3.get_ascii_offset("a")
        expected = 65

