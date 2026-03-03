Generate a unittest test script for the following Python function.
The script should fully test the function and be runnable directly.

### Output Formatting
1. Start with: import unittest
2. Include: from HumanEval_27_code import flip_case
3. End with:
if __name__ == '__main__':
    unittest.main()

Function:
def flip_case(string: str) -> str:
    """For a given string, flip lowercase characters to uppercase and uppercase to lowercase.
    >>> flip_case('Hello')
    'hELLO'
    """
    return string.swapcase()

 Here is a complete unittest test script for the `flip_case` function:


import unittest
from HumanEval_27_code import flip_case

class TestFlipCase(unittest.TestCase):
    def test_flip_case(self):
        self.assertEqual(flip_case('Hello'), 'hELLO')
        self.assertEqual(flip_case('hello'), 'HELLO')
        self.assertEqual(flip_case('World'), 'wORLD')
        self.assertEqual(flip_case('world'), 'WORLD')
        self.assertEqual(flip_case('MixedCase'), 'mIXEDCASE')
        self.assertEqual(flip_case('mixedcase'), 'MIXEDCASE')
        self.assertEqual(flip_case(''), '')
        self.assertEqual(flip_case('123'), '123')
        self.assertEqual(flip_case('12345'), '12345')
        self.assertEqual(flip_case('Hello, World!'), 'hELLO, wORLD!')
        self.assertEqual(flip_case('Hello, world!'), 'hELLO, WORLD!')
        self.assertEqual(flip_case('Hello, World! 123'), 'hELLO, wORLD! 123')
        self.assertEqual(flip_case('Hello, world! 123'), 'hELLO, WORLD! 123')

if __name__ == '__main__':
    unittest.main()


This test script includes various test cases to ensure the `flip_case` function works correctly for different input strings, including empty strings, numbers, and mixed case strings. The test cases are defined in the `TestFlipCase` class, and the test suite is run using `unittest.main()`.