You are an expert Python programmer whose primary role is to write comprehensive unittest test suites. Be professional, precise, and output only runnable Python code. Write a complete unittest test suite for the following Python function.
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

 import unittest
from HumanEval_85_code import add

class TestAddFunction(unittest.TestCase):

    def test_add_with_even_elements_at_odd_indices(self):
        self.assertEqual(add([4, 2, 6, 7]), 2)

    def test_add_with_no_even_elements_at_odd_indices(self):
        self.assertEqual(add([1, 3, 5, 7]), 0)

    def test_add_with_all_odd_elements_at_odd_indices(self):
        self.assertEqual(add([1, 3, 5, 9]), 0)

    def test_add_with_even_elements_at_even_indices(self):
        self.assertEqual(add([4, 2, 6, 8]), 10)

    def test_add_with_mixed_elements(self):
        self.assertEqual(add([1, 2, 3, 4, 5, 6]), 2)

    def test_add_with_empty_list(self):
        self.assertEqual(add([]), 0)

    def test_add_with_single_element(self):
        self.assertEqual(add([2]), 2)

    def test_add_with_negative_numbers(self):
        self.assertEqual(add([-4, 2, -6, 7]), -4)

if __name__ == '__main__':
    unittest.main()