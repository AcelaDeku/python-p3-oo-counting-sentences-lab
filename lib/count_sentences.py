
import io
import sys
import pytest
from my_string import MyString

class TestMyString:
    def test_value_string(self):
        '''prints "The value must be a string." if not string.'''
        captured_out = io.StringIO()
        sys.stdout = captured_out
        string = MyString()
        string.value = 123
        sys.stdout = sys.__stdout__
        print("Captured output:", captured_out.getvalue())  # Debug line
        assert(captured_out.getvalue() == "The value must be a string.\n")
