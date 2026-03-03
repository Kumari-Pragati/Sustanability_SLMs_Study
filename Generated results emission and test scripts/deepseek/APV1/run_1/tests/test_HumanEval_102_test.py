You are an AI programming assistant, utilizing the Deepseek Coder model, developed by Deepseek Company, and you only answer questions related to computer science. For politically sensitive questions, security and privacy issues, and other non-computer science questions, you will refuse to answer
### Instruction:
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


### Response:
Here is a unittest test suite for the given Python function:


import unittest
from HumanEval_102_code import choose_num

class TestChooseNum(unittest.TestCase):

    def test_choose_num(self):
        self.assertEqual(choose_num(12, 15), 14)
        self.assertEqual(choose_num(13, 12), -1)
        self.assertEqual(choose_num(14, 14), -1)
        self.assertEqual(choose_num(15, 15), -1)
        self.assertEqual(choose_num(16, 16), 16)
        self.assertEqual(choose_num(17, 18), 18)
        self.assertEqual(choose_num(19, 20), 20)
        self.assertEqual(choose_num(20, 21), 20)
        self.assertEqual(choose_num(21, 22), 22)
        self.assertEqual(choose_num(22, 23), -1)

if __name__ == '__main__':
    unittest.main()


This test suite includes a variety of test cases to ensure that the function is working as expected. It tests the function with a range of inputs, including both even and odd numbers, as well as cases where the function should return -1.