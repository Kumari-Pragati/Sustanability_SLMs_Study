system
You are Qwen, created by Alibaba Cloud. You are a helpful assistant.
user
You are an expert Python programmer.
Your task is to write a comprehensive unittest test suite for the given Python function.

### Output Formatting
1. Start with: import unittest
2. Include: from HumanEval_102_code import choose_num

3. End with:
if __name__ == '__main__':
    unittest.main()

Function:
def choose_num(x, y):
    """This function takes two positive numbers x and y and returns the
    biggest even integer number that is in the range [x, y] inclusive. If 
    there's no such number, then the function should return -1.

    For example:
    choose_num(12, 15) = 14
    choose_num(13, 12) = -1
    """

    if x > y:
        return -1
    if y % 2 == 0:
        return y
    if x == y:
        return -1
    return y - 1


assistant

import unittest

# Importing the chosen function
from HumanEval_102_code import choose_num

class TestChooseNum(unittest.TestCase):

    def test_choose_num(self):
        # Test cases to verify the correctness of the function
        self.assertEqual(choose_num(12, 15), 14)
        self.assertEqual(choose_num(13, 12), -1)
        self.assertEqual(choose_num(16, 17), -1)
        self.assertEqual(choose_num(8, 9), 8)
        self.assertEqual(choose_num(10, 10), -1)

    def test_edge_cases(self):
        # Testing edge cases where one or both inputs are out of bounds
        self.assertEqual(choose_num(-1, 10), -1)
        self.assertEqual(choose_num(10, -1), -1)
        self.assertEqual(choose_num(10, 10), -1)
        self.assertEqual(choose_num(10, 10), -1)

if __name__ == '__main__':
    unittest.main()


In this solution, I've created a `TestChooseNum` class within the `unittest` framework to run our tests on the `choose_num` function. The test cases cover various scenarios including valid ranges, invalid ranges (one or both inputs being out of bounds), and specific examples provided in the problem description. This ensures that the function behaves as expected across different conditions.