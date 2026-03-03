Generate a unittest test script for the following Python function.
The script should fully test the function and be runnable directly.

### Output Formatting
1. Start with: import unittest
2. Include: from HumanEval_137_code import compare_one
3. End with:
if __name__ == '__main__':
    unittest.main()

Function:
def compare_one(a, b):
    """
    Create a function that takes integers, floats, or strings representing
    real numbers, and returns the larger variable in its given variable type.
    Return None if the values are equal.
    Note: If a real number is represented as a string, the floating point might be . or ,

    compare_one(1, 2.5) ➞ 2.5
    compare_one(1, "2,3") ➞ "2,3"
    compare_one("5,1", "6") ➞ "6"
    compare_one("1", 1) ➞ None
    """
    temp_a, temp_b = a, b
    if isinstance(temp_a, str):
        temp_a = temp_a.replace(',', '.')
    if isinstance(temp_b, str):
        temp_b = temp_b.replace(',', '.')
    if float(temp_a) == float(temp_b):
        return None
    return a if float(temp_a) > float(temp_b) else b

 Here is a unittest test script for the `compare_one` function:


import unittest
from HumanEval_137_code import compare_one

class TestCompareOne(unittest.TestCase):

    def test_compare_one(self):
        self.assertEqual(compare_one(1, 2.5), 2.5)
        self.assertEqual(compare_one(1, "2,3"), "2,3")
        self.assertEqual(compare_one("5,1", "6"), "6")
        self.assertIsNone(compare_one("1", 1))
        self.assertIsNone(compare_one(1.0, 1.0))
        self.assertIsNone(compare_one("1.0", "1.0"))
        self.assertIsNone(compare_one("1.00", "1.00"))
        self.assertIsNone(compare_one("1.0", "1.00"))
        self.assertIsNone(compare_one("1.00", "1.0"))
        self.assertEqual(compare_one(2.5, 1), 2.5)
        self.assertEqual(compare_one("2,3", 1), "2,3")
        self.assertEqual(compare_one("6", "5,1"), "6")
        self.assertIsNone(compare_one("1", "1"))
        self.assertIsNone(compare_one("1.0", "1"))
        self.assertIsNone(compare_one("1", "1.0"))

if __name__ == '__main__':
    unittest.main()


This test script includes various test cases to ensure the function works correctly with different data types and edge cases. It uses the `assertEqual` method to compare the expected output with the actual output of the function. The test cases cover both integer, float, and string inputs, as well as cases where the input is represented as a string with commas or periods as decimal separators.