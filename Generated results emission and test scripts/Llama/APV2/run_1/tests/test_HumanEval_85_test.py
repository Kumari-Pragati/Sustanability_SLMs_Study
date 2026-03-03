system

You are an expert Python programmer whose primary role is to write comprehensive unittest test suites. Be professional, precise, and output only runnable Python code.user

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

    return sum([lst[i] for i in range(1, len(lst), 2) if lst[i] % 2 == 0])assistant

Here is the complete unittest test suite for the given Python function:

Python
import unittest
from HumanEval_85_code import add

class TestAddFunction(unittest.TestCase):

    def test_add_even_odd_indices(self):
        self.assertEqual(add([4, 2, 6, 7]), 2)

    def test_add_empty_list(self):
        with self.assertRaises(IndexError):
            add([])

    def test_add_list_with_no_even_elements(self):
        self.assertEqual(add([1, 3, 5, 7]), 0)

    def test_add_list_with_all_even_elements(self):
        self.assertEqual(add([2, 4, 6, 8]), 12)

    def test_add_list_with_mixed_elements(self):
        self.assertEqual(add([1, 2, 3, 4, 5, 6]), 6)

    def test_add_list_with_negative_elements(self):
        self.assertEqual(add([-2, 4, -6, 8]), 10)

    def test_add_list_with_zero(self):
        self.assertEqual(add([0, 2, 0, 4]), 4)

if __name__ == '__main__':
    unittest.main()