You are an expert Python programmer.
Your task is to write a comprehensive unittest test suite for the given Python function.

### Output Formatting
1. Start with: import unittest
2. Include: from HumanEval_52_code import below_threshold

3. End with:
if __name__ == '__main__':
    unittest.main()

Function:
def below_threshold(l: list, t: int):
    """Return True if all numbers in the list l are below threshold t.
    >>> below_threshold([1, 2, 4, 10], 100)
    True
    >>> below_threshold([1, 20, 4, 10], 5)
    False
    """
    for e in l:
        if e >= t:
            return False
    return True

 import unittest
from HumanEval_52_code import below_threshold

class TestBelowThreshold(unittest.TestCase):

    def test_all_numbers_below_threshold(self):
        self.assertTrue(below_threshold([1, 2, 4, 10], 100))

    def test_some_numbers_above_threshold(self):
        self.assertFalse(below_threshold([1, 20, 4, 10], 5))

    def test_empty_list(self):
        self.assertTrue(below_threshold([], 100))

    def test_single_element_below_threshold(self):
        self.assertTrue(below_threshold([1], 100))

    def test_single_element_equal_to_threshold(self):
        self.assertFalse(below_threshold([100], 100))

    def test_single_element_above_threshold(self):
        self.assertFalse(below_threshold([101], 100))

    def test_negative_numbers(self):
        self.assertTrue(below_threshold([-1, -2, -4, -10], 100))

    def test_threshold_is_zero(self):
        self.assertTrue(below_threshold([1, 2, 4, 10], 0))

    def test_threshold_is_negative(self):
        self.assertTrue(below_threshold([1, 2, 4, 10], -1))

if __name__ == '__main__':
    unittest.main()