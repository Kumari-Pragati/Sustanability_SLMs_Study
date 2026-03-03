Generate a unittest test script for the following Python function.
The script should fully test the function and be runnable directly.

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
        # Test with a list that has even numbers at odd indices
        self.assertEqual(add([4, 2, 6, 7]), 2)

    def test_add_no_even_at_odd_indices(self):
        # Test with a list that has no even numbers at odd indices
        self.assertEqual(add([1, 3, 5, 7]), 0)

    def test_add_empty_list(self):
        # Test with an empty list
        self.assertEqual(add([]), 0)

    def test_add_single_element(self):
        # Test with a list with a single element
        self.assertEqual(add([4]), 0)

    def test_add_all_even_at_odd_indices(self):
        # Test with a list where all even numbers are at odd indices
        self.assertEqual(add([2, 4, 6, 8]), 12)

    def test_add_all_odd_at_odd_indices(self):
        # Test with a list where all odd numbers are at odd indices
        self.assertEqual(add([1, 3, 5, 7]), 0)

    def test_add_mixed_indices(self):
        # Test with a list that has a mix of even and odd numbers at odd indices
        self.assertEqual(add([1, 4, 3, 8]), 4)

if __name__ == '__main__':
    unittest.main()