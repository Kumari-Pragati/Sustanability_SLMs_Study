system
You are Qwen, created by Alibaba Cloud. You are a helpful assistant.
user
You are an expert Python programmer.
Your task is to write a comprehensive unittest test suite for the given Python function.

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


assistant

import unittest

# Function to be tested
from HumanEval_132_code import is_nested

class TestIsNested(unittest.TestCase):
    def test_is_nested(self):
        self.assertTrue(is_nested('[[]]')
                        )
        self.assertFalse(is_nested('[]]]]]]][[[[[]')
                        )
        self.assertFalse(is_nested('[][]')
                        )
        self.assertFalse(is_nested('[]')
                        )
        self.assertTrue(is_nested('[[][]]')
                        )
        self.assertTrue(is_nested('[[]][[')
                        )

if __name__ == '__main__':
    unittest.main()


This code snippet defines a `TestIsNested` class within the `unittest` module, which inherits from `unittest.TestCase`. It includes a single method `test_is_nested`, which tests various cases using assertions to ensure the correctness of the `is_nested` function. The `assertTrue` and `assertFalse` methods are used to check if the output of `is_nested` matches the expected results. If any assertion fails, it will raise an error indicating which case failed.