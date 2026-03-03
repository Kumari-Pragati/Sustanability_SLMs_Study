You are an AI programming assistant, utilizing the Deepseek Coder model, developed by Deepseek Company, and you only answer questions related to computer science. For politically sensitive questions, security and privacy issues, and other non-computer science questions, you will refuse to answer
### Instruction:
You are an expert Python programmer.
Your task is to write a comprehensive unittest test suite for the given Python function.

### Output Formatting
1. Start with: import unittest
2. Include: from HumanEval_5_code import intersperse

3. End with:
if __name__ == '__main__':
    unittest.main()

Function:
from typing import List


def intersperse(numbers: List[int], delimeter: int) -> List[int]:
    """Insert a number 'delimeter' between every two consecutive elements of input list `numbers`.
    >>> intersperse([], 4)
    []
    >>> intersperse([1, 2, 3], 4)
    [1, 4, 2, 4, 3]
    """
    result: List[int] = []
    for i, x in enumerate(numbers):
        result.append(x)
        if i != len(numbers) - 1:
            result.append(delimeter)
    return result


### Response:
Here is a unittest test suite for the given Python function:


import unittest
from typing import List
from HumanEval_5_code import intersperse

class TestIntersperse(unittest.TestCase):
    def test_empty_list(self):
        self.assertEqual(intersperse([], 4), [])

    def test_single_element(self):
        self.assertEqual(intersperse([1], 4), [1])

    def test_multiple_elements(self):
        self.assertEqual(intersperse([1, 2, 3], 4), [1, 4, 2, 4, 3])

    def test_delimeter_in_list(self):
        self.assertEqual(intersperse([1, 4, 2, 4, 3], 4), [1, 4, 2, 4, 3])

    def test_negative_numbers(self):
        self.assertEqual(intersperse([-1, -2, -3], 0), [-1, 0, -2, 0, -3])

    def test_zero(self):
        self.assertEqual(intersperse([0, 1, 2, 3], 0), [0, 0, 1, 0, 2, 0, 3])

if __name__ == '__main__':
    unittest.main()


This test suite includes tests for different scenarios such as empty list, single element, multiple elements, delimeter in list, negative numbers, and zero.

Please note that the function `intersperse` is expected to be in a file named `HumanEval_5_code.py` in the same directory as the test file.

The function `assertEqual` is used to check if the output of the function matches the expected output. If the output does not match the expected output, the test will fail.

The `unittest.main()` function is used to run the test suite. If all tests pass, the program will exit with a status of 0. If any tests fail, the program will exit with a status of 1.