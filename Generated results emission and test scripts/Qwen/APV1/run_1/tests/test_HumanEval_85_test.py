system
You are Qwen, created by Alibaba Cloud. You are a helpful assistant.
user
You are an expert Python programmer.
Your task is to write a comprehensive unittest test suite for the given Python function.

### Output Formatting
1. Start with: import unittest
2. Include: from HumanEval_85_code import add

3. End with:
if __name__ == '__main__':
    unittest.main()

Function:
def add(lst):
    """Given a non-empty list of integers lst. Add the even elements that are at odd indices.

    Examples:
        add([4, 2, 6, 7]) ==> 2 
    """

    return sum([lst[i] for i in range(1, len(lst), 2) if lst[i] % 2 == 0])


assistant

import unittest

# Given code snippet
from HumanEval_85_code import add

class TestAdd(unittest.TestCase):

    def test_add(self):
        self.assertEqual(add([4, 2, 6, 7]), 2)
        self.assertEqual(add([1, 3, 5, 7, 9]), 0)
        self.assertEqual(add([10, 22, 34, 46, 58]), 22)
        self.assertEqual(add([-1, -3, -5, -7, -9]), 0)

if __name__ == '__main__':
    unittest.main()


This test suite includes several test cases to ensure the `add` function behaves as expected across different scenarios.