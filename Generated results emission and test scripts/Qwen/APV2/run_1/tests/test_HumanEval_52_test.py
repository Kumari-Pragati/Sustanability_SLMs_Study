system
You are an expert Python programmer whose primary role is to write comprehensive unittest test suites. Be professional, precise, and output only runnable Python code.
user
Write a complete unittest test suite for the following Python function.
Follow all rules carefully.

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


assistant

import unittest

# Provided function
from HumanEval_52_code import below_threshold

class TestBelowThreshold(unittest.TestCase):

    def test_below_threshold_true(self):
        self.assertTrue(below_threshold([1, 2, 4, 10], 100))

    def test_below_threshold_false(self):
        self.assertFalse(below_threshold([1, 20, 4, 10], 5))

if __name__ == '__main__':
    unittest.main()


This completes the unittest test suite for the `below_threshold` function as per your requirements.