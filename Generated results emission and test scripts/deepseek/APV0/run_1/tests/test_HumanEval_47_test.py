You are an AI programming assistant, utilizing the Deepseek Coder model, developed by Deepseek Company, and you only answer questions related to computer science. For politically sensitive questions, security and privacy issues, and other non-computer science questions, you will refuse to answer
### Instruction:
Generate a unittest test script for the following Python function.
The script should fully test the function and be runnable directly.

### Output Formatting
1. Start with: import unittest
2. Include: from HumanEval_47_code import median
3. End with:
if __name__ == '__main__':
    unittest.main()

Function:
def median(l: list):
    """Return median of elements in the list l.
    >>> median([3, 1, 2, 4, 5])
    3
    >>> median([-10, 4, 6, 1000, 10, 20])
    15.0
    """
    l = sorted(l)
    if len(l) % 2 == 1:
        return l[len(l) // 2]
    else:
        return (l[len(l) // 2 - 1] + l[len(l) // 2]) / 2.0


### Response:
Here is a unittest test script for the given Python function:


import unittest
from HumanEval_47_code import median

class TestMedian(unittest.TestCase):
    def test_odd_length(self):
        self.assertEqual(median([3, 1, 2, 4, 5]), 3)
        self.assertEqual(median([-10, 4, 6, 1000, 10, 20]), 15.0)
        self.assertEqual(median([1]), 1)
        self.assertEqual(median([1, 2]), 1.5)

    def test_even_length(self):
        self.assertEqual(median([3, 1, 2, 4]), 2.5)
        self.assertEqual(median([-10, 4, 6, 10]), 5)
        self.assertEqual(median([1, 2, 3, 4, 5, 6]), 3.5)

    def test_empty_list(self):
        with self.assertRaises(IndexError):
            median([])

if __name__ == '__main__':
    unittest.main()


This script includes three test methods:

- `test_odd_length` tests the function with lists of odd length.
- `test_even_length` tests the function with lists of even length.
- `test_empty_list` tests the function with an empty list, which should raise an `IndexError` because the function attempts to access an element at index 0 of an empty list.

To run the tests, you can simply execute this script. If you're using a command line, you can do so by navigating to the directory containing this script and running `python test_script.py`.

Please note that the function `median` from the `HumanEval_47_code` module should be defined in a separate Python file.