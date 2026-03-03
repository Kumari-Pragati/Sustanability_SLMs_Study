user

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

    return sum([lst[i] for i in range(1, len(lst), 2) if lst[i] % 2 == 0])assistant

Here is the unittest test script for the given Python function:

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

if __name__ == '__main__':
    unittest.main()


This script includes five test cases:

1. `test_add_even_odd_indices`: Tests the function with the example given in the problem statement.
2. `test_add_empty_list`: Tests the function with an empty list, which should raise an `IndexError`.
3. `test_add_list_with_no_even_elements`: Tests the function with a list that contains only odd numbers.
4. `test_add_list_with_all_even_elements`: Tests the function with a list that contains only even numbers.
5. `test_add_list_with_mixed_elements`: Tests the function with a list that contains both even and odd numbers.

Each test case uses the `assertEqual` method to check if the output of the function matches the expected result. The `assertRaises` method is used in the `test_add_empty_list` test case to check if the function raises an `IndexError` when given an empty list.