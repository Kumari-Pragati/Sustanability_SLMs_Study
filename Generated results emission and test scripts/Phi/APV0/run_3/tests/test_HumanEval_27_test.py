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

 import unittest
from HumanEval_27_code import flip_case

class TestFlipCase(unittest.TestCase):

    def test_flip_case_lowercase(self):
        self.assertEqual(flip_case('hello'), 'HELLO')

    def test_flip_case_mixed(self):
        self.assertEqual(flip_case('HeLLo'), 'hEllO')

    def test_flip_case_uppercase(self):
        self.assertEqual(flip_case('HELLO'), 'hello')

    def test_flip_case_empty_string(self):
        self.assertEqual(flip_case(''), '')

    def test_flip_case_special_characters(self):
        self.assertEqual(flip_case('Hello, World!'), 'hELLO, wORLD!')

    def test_flip_case_numeric(self):
        self.assertEqual(flip_case('123'), '123')

    def test_flip_case_whitespace(self):
        self.assertEqual(flip_case('   '), '   ')

if __name__ == '__main__':
    unittest.main()