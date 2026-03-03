system
You are Qwen, created by Alibaba Cloud. You are a helpful assistant.
user
Generate a unittest test script for the following Python function.
The script should fully test the function and be runnable directly.

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

# Importing the chosen function from the provided code snippet
from HumanEval_102_code import choose_num

class TestChooseNum(unittest.TestCase):

    def test_choose_num(self):
        # Test cases to verify the correctness of the choose_num function
        self.assertEqual(choose_num(12, 15), 14)
        self.assertEqual(choose_num(13, 12), -1)
        self.assertEqual(choose_num(16, 17), 16)
        self.assertEqual(choose_num(18, 19), 18)
        self.assertEqual(choose_num(10, 20), 20)
        self.assertEqual(choose_num(21, 22), 22)

    def test_edge_cases(self):
        # Edge case tests to ensure edge conditions are handled correctly
        self.assertEqual(choose_num(1, 1), -1)
        self.assertEqual(choose_num(100, 100), 100)
        self.assertEqual(choose_num(100, 101), -1)
        self.assertEqual(choose_num(100, 1000), 1000)

if __name__ == '__main__':
    unittest.main()


In this solution, I've created a `TestChooseNum` class within the `unittest` framework. This class contains several test methods (`test_choose_num`, `test_edge_cases`) to thoroughly test the `choose_num` function. Each method uses assertions to check whether the output of the function matches the expected results. The `if __name__ == '__main__':` block ensures that when you run the script directly (not as part of another module), it will execute all the test methods.