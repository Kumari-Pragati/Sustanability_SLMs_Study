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
    return number % 1.0assistant

Here is the unittest test script for the `truncate_number` function:

import unittest
from HumanEval_2_code import truncate_number

class TestTruncateNumber(unittest.TestCase):
    def test_truncate_number(self):
        # Test cases
        self.assertAlmostEqual(truncate_number(3.5), 0.5)
        self.assertAlmostEqual(truncate_number(2.0), 0.0)
        self.assertAlmostEqual(truncate_number(1.25), 0.25)
        self.assertAlmostEqual(truncate_number(0.75), 0.75)
        self.assertAlmostEqual(truncate_number(0.0), 0.0)
        self.assertAlmostEqual(truncate_number(1.0), 0.0)
        self.assertAlmostEqual(truncate_number(2.5), 0.5)
        self.assertAlmostEqual(truncate_number(3.75), 0.75)
        self.assertAlmostEqual(truncate_number(4.25), 0.25)
        self.assertAlmostEqual(truncate_number(4.5), 0.5)
        self.assertAlmostEqual(truncate_number(4.75), 0.75)
        self.assertAlmostEqual(truncate_number(4.99), 0.99)

    def test_invalid_input(self):
        # Test invalid input
        with self.assertRaises(TypeError):
            truncate_number("hello")
        with self.assertRaises(TypeError):
            truncate_number([1, 2, 3])
        with self.assertRaises(TypeError):
            truncate_number({"a": 1, "b": 2})

if __name__ == '__main__':
    unittest.main()

This script defines a `TestTruncateNumber` class that contains two test methods:

* `test_truncate_number`: This method tests the `truncate_number` function with various input values, including positive numbers, zero, and one. It uses the `assertAlmostEqual` method to check that the output is close to the expected value.
* `test_invalid_input`: This method tests the `truncate_number` function with invalid input values, such as strings, lists, and dictionaries. It uses the `assertRaises` method to check that the function raises a `TypeError` exception when given invalid input.

To run the script, simply execute it using Python, for example:

$ python test_truncate_number.py

This will run the tests and report any failures or errors.