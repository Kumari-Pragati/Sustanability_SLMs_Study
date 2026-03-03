Generate a unittest test script for the following Python function.
The script should fully test the function and be runnable directly.

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

 Here is a unittest test script for the `sum_to_n` function:


import unittest
from HumanEval_60_code import sum_to_n

class TestSumToN(unittest.TestCase):
    def test_sum_to_n(self):
        self.assertEqual(sum_to_n(30), 465)
        self.assertEqual(sum_to_n(100), 5050)
        self.assertEqual(sum_to_n(5), 15)
        self.assertEqual(sum_to_n(10), 55)
        self.assertEqual(sum_to_n(1), 1)

if __name__ == '__main__':
    unittest.main()


This script defines a test case class `TestSumToN` that inherits from `unittest.TestCase`. Inside the test case class, a method `test_sum_to_n` is defined to test the `sum_to_n` function. The `assertEqual` method is used to check if the output of the `sum_to_n` function matches the expected output for each test case.

When you run this script, it will execute the tests defined in the `test_sum_to_n` method and report the results. If all tests pass, it means the `sum_to_n` function is working correctly. If any test fails, it means there is an issue with the `sum_to_n` function that needs to be addressed.