You are an AI programming assistant, utilizing the Deepseek Coder model, developed by Deepseek Company, and you only answer questions related to computer science. For politically sensitive questions, security and privacy issues, and other non-computer science questions, you will refuse to answer
### Instruction:
Generate a unittest test script for the following Python function.
The script should fully test the function and be runnable directly.

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


### Response:
Here is a unittest test script for the given Python function:


import unittest
from HumanEval_52_code import below_threshold

class TestBelowThreshold(unittest.TestCase):
    def test_all_below(self):
        self.assertTrue(below_threshold([1, 2, 4, 10], 100))

    def test_one_above(self):
        self.assertFalse(below_threshold([1, 20, 4, 10], 5))

    def test_empty_list(self):
        self.assertTrue(below_threshold([], 100))

    def test_all_above(self):
        self.assertFalse(below_threshold([101, 202, 404, 1000], 100))

    def test_negative_numbers(self):
        self.assertTrue(below_threshold([-1, -2, -4, -10], 0))

    def test_negative_threshold(self):
        with self.assertRaises(ValueError):
            below_threshold([1, 2, 3], -1)

if __name__ == '__main__':
    unittest.main()


This script includes 6 test cases:

1. `test_all_below`: Tests if the function returns True when all numbers in the list are below the threshold.
2. `test_one_above`: Tests if the function returns False when at least one number in the list is above the threshold.
3. `test_empty_list`: Tests if the function returns True when the list is empty.
4. `test_all_above`: Tests if the function returns False when all numbers in the list are above the threshold.
5. `test_negative_numbers`: Tests if the function works correctly with negative numbers.
6. `test_negative_threshold`: Tests if the function raises a ValueError when the threshold is negative.

Please note that you need to have the function `below_threshold` in a file named `HumanEval_52_code.py` in the same directory as your test script for this to work.