You are an expert Python programmer.
Your task is to write a comprehensive unittest test suite for the given Python function.

### Output Formatting
1. Start with: import unittest
2. Include: from HumanEval_60_code import sum_to_n

3. End with:
if __name__ == '__main__':
    unittest.main()

Function:
def sum_to_n(n: int):
    """sum_to_n is a function that sums numbers from 1 to n.
    >>> sum_to_n(30)
    465
    >>> sum_to_n(100)
    5050
    >>> sum_to_n(5)
    15
    >>> sum_to_n(10)
    55
    >>> sum_to_n(1)
    1
    """
    return sum(range(n + 1))

 import unittest
from HumanEval_60_code import sum_to_n

class TestSumToN(unittest.TestCase):
    def test_sum_to_n_with_positive_integers(self):
        self.assertEqual(sum_to_n(30), 465)
        self.assertEqual(sum_to_n(100), 5050)
        self.assertEqual(sum_to_n(5), 15)
        self.assertEqual(sum_to_n(10), 55)

    def test_sum_to_n_with_zero(self):
        self.assertEqual(sum_to_n(0), 0)

    def test_sum_to_n_with_one(self):
        self.assertEqual(sum_to_n(1), 1)

    def test_sum_to_n_with_negative_integers(self):
        with self.assertRaises(ValueError):
            sum_to_n(-1)

    def test_sum_to_n_with_non_integer_values(self):
        with self.assertRaises(TypeError):
            sum_to_n(30.5)

if __name__ == '__main__':
    unittest.main()