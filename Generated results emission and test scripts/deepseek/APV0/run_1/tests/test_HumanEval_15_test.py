You are an AI programming assistant, utilizing the Deepseek Coder model, developed by Deepseek Company, and you only answer questions related to computer science. For politically sensitive questions, security and privacy issues, and other non-computer science questions, you will refuse to answer
### Instruction:
Generate a unittest test script for the following Python function.
The script should fully test the function and be runnable directly.

### Output Formatting
1. Start with: import unittest
2. Include: from HumanEval_15_code import string_sequence
3. End with:
if __name__ == '__main__':
    unittest.main()

Function:
def string_sequence(n: int) -> str:
    """Return a string containing space-delimited numbers starting from 0 up to n inclusive.
    >>> string_sequence(0)
    '0'
    >>> string_sequence(5)
    '0 1 2 3 4 5'
    """
    return ' '.join(str(x) for x in range(n + 1))


### Response:
Here is a unittest test script for the given Python function:


import unittest
from HumanEval_15_code import string_sequence

class TestStringSequence(unittest.TestCase):
    def test_zero(self):
        self.assertEqual(string_sequence(0), '0')

    def test_positive(self):
        self.assertEqual(string_sequence(5), '0 1 2 3 4 5')

    def test_negative(self):
        self.assertEqual(string_sequence(-5), '0 -1 -2 -3 -4 -5')

    def test_large_number(self):
        self.assertEqual(string_sequence(1000), ' '.join(str(x) for x in range(1001)))

    def test_type_error(self):
        with self.assertRaises(TypeError):
            string_sequence('five')

if __name__ == '__main__':
    unittest.main()


This script includes five test cases:

1. `test_zero`: Tests the function with the input 0.
2. `test_positive`: Tests the function with a positive input.
3. `test_negative`: Tests the function with a negative input.
4. `test_large_number`: Tests the function with a large input.
5. `test_type_error`: Tests the function to ensure it raises a TypeError when a non-integer input is provided.

Please note that the function `string_sequence` is expected to be in a file named `HumanEval_15_code.py` in the same directory as the test script.