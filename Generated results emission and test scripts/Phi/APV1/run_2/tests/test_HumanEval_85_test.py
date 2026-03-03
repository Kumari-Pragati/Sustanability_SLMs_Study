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

 import unittest
from HumanEval_85_code import add

class TestAddFunction(unittest.TestCase):

    def test_add_even_at_odd_indices(self):
        self.assertEqual(add([4, 2, 6, 7]), 2)

    def test_add_empty_list(self):
        self.assertEqual(add([]), 0)

    def test_add_single_element_list(self):
        self.assertEqual(add([4]), 0)

    def test_add_all_even_at_odd_indices(self):
        self.assertEqual(add([2, 4, 6, 8]), 10)

    def test_add_no_even_at_odd_indices(self):
        self.assertEqual(add([1, 3, 5, 7]), 0)

    def test_add_mixed_indices(self):
        self.assertEqual(add([1, 2, 3, 4, 5, 6]), 2 + 4 + 6)

    def test_add_negative_even_at_odd_indices(self):
        self.assertEqual(add([-2, -4, -6, -8]), -12)

    def test_add_large_numbers(self):
        self.assertEqual(add([1000000, 2000000, 3000000, 4000000]), 2000000)

    def test_add_zero_at_odd_indices(self):
        self.assertEqual(add([0, 1, 0, 3, 0, 5]), 0)

if __name__ == '__main__':
    unittest.main()