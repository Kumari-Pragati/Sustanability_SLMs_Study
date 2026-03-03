Generate a unittest test script for the following Python function.
The script should fully test the function and be runnable directly.

### Output Formatting
1. Start with: import unittest
2. Include: from HumanEval_14_code import all_prefixes
3. End with:
if __name__ == '__main__':
    unittest.main()

Function:
from typing import List


def all_prefixes(string: str) -> List[str]:
    """ Return list of all prefixes from shortest to longest of the input string
    >>> all_prefixes('abc')
    ['a', 'ab', 'abc']
    """
    result: List[str] = []
    for i in range(len(string)):
        result.append(string[: i + 1])
    return result

 Here is a unittest test script for the `all_prefixes` function:


import unittest
from HumanEval_14_code import all_prefixes

class TestAllPrefixes(unittest.TestCase):
    def test_all_prefixes(self):
        self.assertEqual(all_prefixes('abc'), ['a', 'ab', 'abc'])
        self.assertEqual(all_prefixes(''), [''])
        self.assertEqual(all_prefixes('a'), ['a'])
        self.assertEqual(all_prefixes('abcd'), ['a', 'ab', 'abc', 'abcd'])
        self.assertEqual(all_prefixes('xyz'), ['x', 'xy', 'xyz'])
        self.assertEqual(all_prefixes(''), [''])

if __name__ == '__main__':
    unittest.main()


This test script includes a test case for the edge cases and a few common input strings. You can add more test cases as needed to ensure comprehensive testing of the function. To run the tests, save the script as a .py file (e.g., `test_all_prefixes.py`) and execute it using the command line:


python test_all_prefixes.py


If the tests pass, you should see a message indicating that all tests passed. If any tests fail, you will see a detailed error message explaining which test failed and why.