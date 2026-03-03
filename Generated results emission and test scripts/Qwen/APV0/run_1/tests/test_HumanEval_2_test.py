system
You are Qwen, created by Alibaba Cloud. You are a helpful assistant.
user
Generate a unittest test script for the following Python function.
The script should fully test the function and be runnable directly.

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

# Importing the function to be tested
from HumanEval_2_code import truncate_number

class TestTruncateNumber(unittest.TestCase):
    def test_truncate_number(self):
        # Test cases to verify the correctness of the truncate_number function
        self.assertAlmostEqual(truncate_number(3.5), 0.5, places=5)
        self.assertAlmostEqual(truncate_number(7.9999), 0.9999, places=5)
        self.assertAlmostEqual(truncate_number(4.0), 0.0, places=5)
        self.assertAlmostEqual(truncate_number(1.1111), 0.1111, places=5)
        self.assertAlmostEqual(truncate_number(0.0), 0.0, places=5)

if __name__ == '__main__':
    unittest.main()


This script imports the `truncate_number` function and creates a test class named `TestTruncateNumber`. It includes several test cases using assertions to ensure that the function behaves as expected across different inputs. The `unittest.main()` call at the end makes the tests executable when run directly.