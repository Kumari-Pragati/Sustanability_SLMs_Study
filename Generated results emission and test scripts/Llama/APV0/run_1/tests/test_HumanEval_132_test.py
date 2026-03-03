user

Generate a unittest test script for the following Python function.
The script should fully test the function and be runnable directly.

### Output Formatting
1. Start with: import unittest
2. Include: from HumanEval_132_code import is_nested
3. End with:
if __name__ == '__main__':
    unittest.main()

Function:
def is_nested(string):
    '''
    Create a function that takes a string as input which contains only square brackets.
    The function should return True if and only if there is a valid subsequence of brackets 
    where at least one bracket in the subsequence is nested.

    is_nested('[[]]') ➞ True
    is_nested('[]]]]]]][[[[[]') ➞ False
    is_nested('[][]') ➞ False
    is_nested('[]') ➞ False
    is_nested('[[][]]') ➞ True
    is_nested('[[]][[') ➞ True
    '''
    opening_bracket_index = []
    closing_bracket_index = []
    for i in range(len(string)):
        if string[i] == '[':
            opening_bracket_index.append(i)
        else:
            closing_bracket_index.append(i)
    closing_bracket_index.reverse()
    cnt = 0
    i = 0
    l = len(closing_bracket_index)
    for idx in opening_bracket_index:
        if i < l and idx < closing_bracket_index[i]:
            cnt += 1
            i += 1
    return cnt >= 2assistant

Here is the unittest test script for the `is_nested` function:

import unittest
from HumanEval_132_code import is_nested

class TestIsNested(unittest.TestCase):
    def test_nested(self):
        self.assertTrue(is_nested('[[]]'))
        self.assertTrue(is_nested('[[]][['))
        self.assertTrue(is_nested('[[][]]'))

    def test_not_nested(self):
        self.assertFalse(is_nested('[]]]]]]][[[[[]'))
        self.assertFalse(is_nested('[][]'))
        self.assertFalse(is_nested('[]'))

    def test_edge_cases(self):
        self.assertFalse(is_nested(''))
        self.assertFalse(is_nested('['))
        self.assertFalse(is_nested(']'))

if __name__ == '__main__':
    unittest.main()

This script defines three test methods:

* `test_nested`: Tests the function with examples where the input string has a valid subsequence of nested brackets.
* `test_not_nested`: Tests the function with examples where the input string does not have a valid subsequence of nested brackets.
* `test_edge_cases`: Tests the function with edge cases, such as an empty string, a string with only an opening bracket, and a string with only a closing bracket.

You can run this script directly to execute the tests. If all tests pass, you should see an output indicating that all tests were successful. If any tests fail, you will see an error message indicating which test failed and why.