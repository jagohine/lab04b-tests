from unittest import TestCase

import Q3

"""
Given a boolean, return 'encode' if true and 'decode' if false.

:param encode: a boolean
:precondition: the parameter encode has a value of True if the desired
               output is 'encode' and a value of False if the desired
               output is 'decode'
:postcondition: produce the string 'encode' if encode has the value
                True and produce the string 'decode' if encode has
                the value False.
:return: a string, either 'encode' or 'decode', depending on the input.

>>> coding_bool_to_string(True)
'encode'
>>> coding_bool_to_string(False)
'decode'
"""

class Test(TestCase):
    def test_coding_bool_to_string__encode_is_true(self):
        actual = Q3.coding_bool_to_string(True)
        expected = 'encode'

    def test_coding_bool_to_string__encode_is_false(self):
        actual = Q3.coding_bool_to_string(False)
        expected = 'decode'

