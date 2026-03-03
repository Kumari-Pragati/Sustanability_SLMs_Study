system
You are an expert Python programmer whose primary role is to write comprehensive unittest test suites. Be professional, precise, and output only runnable Python code.
user
Write a complete unittest test suite for the following Python function.
Follow all rules carefully.

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

# Provided function
from HumanEval_85_code import add

class TestAdd(unittest.TestCase):

    def test_add(self):
        self.assertEqual(add([4, 2, 6, 7]), 2)
        self.assertEqual(add([1, 3, 5, 7, 9]), 0)
        self.assertEqual(add([2, 4, 6, 8]), 16)
        self.assertEqual(add([-2, -4, -6, -8]), -20)

if __name__ == '__main__':
    unittest.main()


This test suite includes several test cases to ensure the `add` function behaves as expected across different inputs.