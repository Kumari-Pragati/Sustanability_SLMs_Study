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

 Here is a unittest test script for the `choose_num` function:


import unittest
from HumanEval_102_code import choose_num

class TestChooseNum(unittest.TestCase):
    def test_choose_num(self):
        self.assertEqual(choose_num(12, 15), 14)
        self.assertEqual(choose_num(13, 12), -1)
        self.assertEqual(choose_num(10, 10), -1)
        self.assertEqual(choose_num(5, 6), 6)
        self.assertEqual(choose_num(1, 2), -1)
        self.assertEqual(choose_num(2, 2), 2)
        self.assertEqual(choose_num(100, 102), 100)
        self.assertEqual(choose_num(102, 100), -1)
        self.assertEqual(choose_num(0, 2), -1)
        self.assertEqual(choose_num(2, 0), -1)

if __name__ == '__main__':
    unittest.main()


This test script includes several test cases to ensure the function works correctly for various inputs. The test cases cover scenarios where the even number is within the given range, the even number is at the edge of the range, the even number is not in the range, and edge cases like x=y, x=0, y=0.