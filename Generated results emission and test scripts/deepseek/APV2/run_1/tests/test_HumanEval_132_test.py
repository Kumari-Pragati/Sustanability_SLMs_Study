You are an expert Python programmer whose primary role is to write comprehensive unittest test suites. Be professional, precise, and output only runnable Python code.### Instruction:
Write a complete unittest test suite for the following Python function.
Follow all rules carefully.

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
    return cnt >= 2


### Response:
Here is the complete unittest test suite for the given function:


import unittest
from HumanEval_132_code import is_nested

class TestIsNested(unittest.TestCase):

    def test_true_cases(self):
        self.assertTrue(is_nested('[[]]'))
        self.assertTrue(is_nested('[[][]]'))
        self.assertTrue(is_nested('[[]][[[]]]'))

    def test_false_cases(self):
        self.assertFalse(is_nested('[]]]]]]][[[[[]'))
        self.assertFalse(is_nested('[][]'))
        self.assertFalse(is_nested('[]'))
        self.assertFalse(is_nested('[[]][[]]'))

if __name__ == '__main__':
    unittest.main()


This test suite includes two test methods: `test_true_cases` and `test_false_cases`. The first method tests the function with inputs that should return True, while the second method tests the function with inputs that should return False. Each test method uses the `assertTrue` and `assertFalse` methods to check if the function's output matches the expected result.

Please note that the function `is_nested` is assumed to be in a file named `HumanEval_132_code.py` in the same directory as the test file. If the function is in a different location, you will need to adjust the import statement accordingly.