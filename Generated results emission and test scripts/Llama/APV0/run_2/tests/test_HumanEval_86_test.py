user

Generate a unittest test script for the following Python function.
The script should fully test the function and be runnable directly.

### Output Formatting
1. Start with: import unittest
2. Include: from HumanEval_86_code import anti_shuffle
3. End with:
if __name__ == '__main__':
    unittest.main()

Function:
def anti_shuffle(s):
    """
    Write a function that takes a string and returns an ordered version of it.
    Ordered version of string is a string where all words (separated by space)
    are replaced by a new word where all the characters are arranged in
    ascending order based on ASCII value.
    Note: You should keep the order of words and blank spaces in the sentence.

    For example:
    anti_shuffle('Hi') returns 'Hi'
    anti_shuffle('hello') returns 'ehllo'
    anti_shuffle('Hello World!!!') returns 'Hello!!!Wdlor'
    """

    return''.join([''.join(sorted(list(i))) for i in s.split(' ')])assistant

Here is the unittest test script for the given Python function:

Python
import unittest
from HumanEval_86_code import anti_shuffle

class TestAntiShuffle(unittest.TestCase):

    def test_anti_shuffle(self):
        self.assertEqual(anti_shuffle('Hi'), 'Hi')
        self.assertEqual(anti_shuffle('hello'), 'ehllo')
        self.assertEqual(anti_shuffle('Hello World!!!'), 'Hello!!!Wdlor')
        self.assertEqual(anti_shuffle(''), '')
        self.assertEqual(anti_shuffle('a'), 'a')
        self.assertEqual(anti_shuffle('abc'), 'abc')
        self.assertEqual(anti_shuffle('abc def'), 'abc def')
        self.assertEqual(anti_shuffle('abc def ghi'), 'abc def ghi')

if __name__ == '__main__':
    unittest.main()


This script includes several test cases to ensure the function is working correctly. The test cases cover different scenarios such as:

- Testing with single word strings
- Testing with multiple word strings
- Testing with empty string
- Testing with strings with special characters
- Testing with strings with different lengths

Each test case uses the `assertEqual` method to compare the output of the `anti_shuffle` function with the expected output. If the output of the function does not match the expected output, the test case will fail and an error message will be displayed.