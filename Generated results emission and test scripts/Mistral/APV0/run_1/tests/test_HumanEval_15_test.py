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

 Here is a unittest test script for the `string_sequence` function:


import unittest
from HumanEval_15_code import string_sequence

class TestStringSequence(unittest.TestCase):
    def test_string_sequence(self):
        self.assertEqual(string_sequence(0), '0')
        self.assertEqual(string_sequence(1), '0')
        self.assertEqual(string_sequence(2), '0 1')
        self.assertEqual(string_sequence(3), '0 1 2')
        self.assertEqual(string_sequence(4), '0 1 2 3')
        self.assertEqual(string_sequence(5), '0 1 2 3 4')
        self.assertEqual(string_sequence(6), '0 1 2 3 4 5')
        self.assertEqual(string_sequence(7), '0 1 2 3 4 5 6')
        self.assertEqual(string_sequence(8), '0 1 2 3 4 5 6 7')
        self.assertEqual(string_sequence(9), '0 1 2 3 4 5 6 7 8')
        self.assertEqual(string_sequence(10), '0 1 2 3 4 5 6 7 8 9 10')

if __name__ == '__main__':
    unittest.main()


This test script defines a test case class `TestStringSequence` with a single test method `test_string_sequence`. The test method checks the function's behavior for various input values from 0 to 10. If you run this script, it will execute the tests and print the results.