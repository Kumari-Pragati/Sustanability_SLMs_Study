You are an expert Python programmer whose primary role is to write comprehensive unittest test suites. Be professional, precise, and output only runnable Python code.

Write a complete unittest test suite for the following Python function.
Follow all rules carefully.

### Output Formatting
1. Start with: import unittest
2. Include: from HumanEval_135_code import can_arrange
3. End with:
if __name__ == '__main__':
    unittest.main()

Function:
def can_arrange(arr):
    """Create a function which returns the largest index of an element which
    is not greater than or equal to the element immediately preceding it. If
    no such element exists then return -1. The given array will not contain
    duplicate values.

    Examples:
    can_arrange([1,2,4,3,5]) = 3
    can_arrange([1,2,3]) = -1
    """
    ind = -1
    i = 1
    while i < len(arr):
        if arr[i] < arr[i - 1]:
            ind = i
        i += 1
    return ind

 Here is the complete unittest test suite for the `can_arrange` function:


import unittest
from HumanEval_135_code import can_arrange

class TestCanArrange(unittest.TestCase):

    def test_can_arrange_example_1(self):
        self.assertEqual(can_arrange([1, 2, 4, 3, 5]), 3)

    def test_can_arrange_example_2(self):
        self.assertEqual(can_arrange([1, 2, 3]), -1)

    def test_can_arrange_example_3(self):
        self.assertEqual(can_arrange([6, 3, 2, 4, 5]), -1)

    def test_can_arrange_example_4(self):
        self.assertEqual(can_arrange([7, 6, 5, 4, 3, 2, 1]), 0)

    def test_can_arrange_example_5(self):
        self.assertEqual(can_arrange([10, 9, 8, 7, 6, 5, 4, 3, 2, 1]), 9)

if __name__ == '__main__':
    unittest.main()


This test suite includes five test cases, each testing the function with a different example from the provided examples. The `unittest.TestCase.assertEqual` method is used to compare the expected output with the actual output of the function. If the function returns the correct output for all test cases, the test suite will pass. If not, the test suite will fail, and the specific test case that failed will be indicated.