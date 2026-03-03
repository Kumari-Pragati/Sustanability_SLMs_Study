system
You are Qwen, created by Alibaba Cloud. You are a helpful assistant.
user
You are an expert Python programmer.
Your task is to write a comprehensive unittest test suite for the given Python function.

### Output Formatting
1. Start with: import unittest
2. Include: from HumanEval_2_code import truncate_number

3. End with:
if __name__ == '__main__':
    unittest.main()

Function:
def truncate_number(number: float) -> float:
    """Given a positive floating point number, it can be decomposed into
    an integer part (largest integer smaller than given number) and decimals
    (leftover part always smaller than 1).

    Return the decimal part of the number.
    >>> truncate_number(3.5)
    0.5
    """
    return number % 1.0


assistant

import unittest
from HumanEval_2_code import truncate_number

class TestTruncateNumber(unittest.TestCase):
    def test_truncate_number(self):
        self.assertAlmostEqual(truncate_number(3.5), 0.5, places=5)
        self.assertAlmostEqual(truncate_number(4.75), 0.75, places=5)
        self.assertAlmostEqual(truncate_number(9.9999), 0.9999, places=5)
        self.assertAlmostEqual(truncate_number(0.0), 0.0, places=5)

    def test_edge_cases(self):
        # Edge case: negative numbers should raise an error or handle appropriately
        with self.assertRaises(ValueError):
            truncate_number(-1.5)
        
        # Edge case: zero should return zero
        self.assertEqual(truncate_number(0.0), 0.0)

if __name__ == '__main__':
    unittest.main()


This code snippet defines a `TestTruncateNumber` class that inherits from `unittest.TestCase`. It includes two methods: `test_truncate_number`, which tests the main functionality of the `truncate_number` function, and `test_edge_cases`, which checks for edge cases such as negative numbers and zero. The `assertAlmostEqual` method is used to compare the output of `truncate_number` with expected values, ensuring accuracy up to five decimal places. Finally, the `unittest.main()` call at the end runs all the defined tests when the script is executed directly.