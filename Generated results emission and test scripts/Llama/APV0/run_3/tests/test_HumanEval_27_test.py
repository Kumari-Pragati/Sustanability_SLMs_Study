user

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
    return string.swapcase()assistant

Here is the unittest test script for the `flip_case` function:

import unittest
from HumanEval_27_code import flip_case

class TestFlipCase(unittest.TestCase):
    def test_flip_case_lowercase(self):
        self.assertEqual(flip_case('hello'), 'HELLO')

    def test_flip_case_uppercase(self):
        self.assertEqual(flip_case('HELLO'), 'hello')

    def test_flip_case_mixedcase(self):
        self.assertEqual(flip_case('HeLlO'), 'hElLo')

    def test_flip_case_emptystring(self):
        self.assertEqual(flip_case(''), '')

    def test_flip_case_singlecharacter(self):
        self.assertEqual(flip_case('a'), 'A')

    def test_flip_case_multiplecharacters(self):
        self.assertEqual(flip_case('abcdefg'), 'ABCDEFg')

if __name__ == '__main__':
    unittest.main()

This script defines a `TestFlipCase` class with six test methods:

1. `test_flip_case_lowercase`: Tests that the function correctly flips lowercase characters to uppercase.
2. `test_flip_case_uppercase`: Tests that the function correctly flips uppercase characters to lowercase.
3. `test_flip_case_mixedcase`: Tests that the function correctly flips a mixed-case string.
4. `test_flip_case_emptystring`: Tests that the function returns an empty string for an empty input.
5. `test_flip_case_singlecharacter`: Tests that the function correctly flips a single character.
6. `test_flip_case_multiplecharacters`: Tests that the function correctly flips a multi-character string.

Each test method uses the `assertEqual` method to check that the output of the `flip_case` function matches the expected result.

You can run this script directly to execute the tests.