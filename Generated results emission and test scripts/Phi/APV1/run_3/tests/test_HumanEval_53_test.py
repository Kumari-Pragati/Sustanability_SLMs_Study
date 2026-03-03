You are an expert Python programmer.
Your task is to write a comprehensive unittest test suite for the given Python function.

### Output Formatting
1. Start with: import unittest
2. Include: from HumanEval_53_code import add

3. End with:
if __name__ == '__main__':
    unittest.main()

Function:
def add(x: int, y: int):
    """Add two numbers x and y
    >>> add(2, 3)
    5
    >>> add(5, 7)
    12
    """
    return x + y

 import unittest
from HumanEval_53_code import add

class TestAddFunction(unittest.TestCase):

    def test_add_positive_numbers(self):
        self.assertEqual(add(2, 3), 5)
        self.assertEqual(add(5, 7), 12)

    def test_add_zero(self):
        self.assertEqual(add(0, 0), 0)

    def test_add_negative_numbers(self):
        self.assertEqual(add(-1, -1), -2)
        self.assertEqual(add(-5, -7), -12)

    def test_add_mixed_numbers(self):
        self.assertEqual(add(2, -3), -1)
        self.assertEqual(add(-5, 7), 2)

    def test_add_large_numbers(self):
        self.assertEqual(add(1000000, 2000000), 3000000)
        self.assertEqual(add(-1000000, -2000000), -3000000)

    def test_add_float_numbers(self):
        self.assertAlmostEqual(add(2.5, 3.5), 6.0, places=1)
        self.assertAlmostEqual(add(-2.5, -3.5), -6.0, places=1)

    def test_add_string_numbers(self):
        with self.assertRaises(TypeError):
            add("2", "3")

    def test_add_non_numeric_values(self):
        with self.assertRaises(TypeError):
            add("2", [3])

if __name__ == '__main__':
    unittest.main()