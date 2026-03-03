You are an expert Python programmer whose primary role is to write comprehensive unittest test suites. Be professional, precise, and output only runnable Python code.### Instruction:
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


### Response:
Here is a complete unittest test suite for the given Python function:


import unittest
from HumanEval_85_code import add

class TestAdd(unittest.TestCase):

    def test_add(self):
        self.assertEqual(add([4, 2, 6, 7]), 2)
        self.assertEqual(add([1, 2, 3, 4, 5, 6, 7, 8, 9]), 6)
        self.assertEqual(add([10, 11, 12, 13, 14, 15]), 12)
        self.assertEqual(add([1, 3, 5, 7, 9]), 0)
        self.assertEqual(add([1, 2, 3, 4, 5, 6, 7, 8, 9, 10]), 6)
        self.assertEqual(add([1, 3, 5, 7, 9, 11]), 0)
        self.assertEqual(add([1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11]), 6)
        self.assertEqual(add([1, 3, 5, 7, 9, 11, 13]), 0)

if __name__ == '__main__':
    unittest.main()


This test suite includes a variety of test cases, including both even and odd length lists, and lists with both even and odd numbers. The test cases check that the function returns the correct sum for each of these cases.