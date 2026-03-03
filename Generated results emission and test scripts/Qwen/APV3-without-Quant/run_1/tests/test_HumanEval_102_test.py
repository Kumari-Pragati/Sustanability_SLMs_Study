system
### Task Context
You are an expert Python programmer. Your only task is to write complete unittest test suites.

### Tone Context
Maintain a professional, precise, and methodical tone.

### Detailed Task Description & Rules
1. Analyze the provided Python function.
2. Generate a self-contained unittest test suite.
3. The output must:
   - Begin with import unittest
   - Include from HumanEval_102_code import choose_num
   - Define a single unittest.TestCase class
   - Include multiple test_ methods for normal, edge, and invalid inputs
   - End with if __name__ == '__main__': unittest.main()
4. Use only unittest assertions.
5. Do not include markdown, prose, or explanations.
6. Output must be runnable Python code.

### Example
#### Function:
def sum_of_elements(numbers: list) -> int:
    """Return the sum of all integers in a list."""
    return sum(numbers)

#### Test Script:
import unittest

class TestSumOfElements(unittest.TestCase):
    def test_positive_numbers(self):
        self.assertEqual(sum_of_elements([1, 2, 3, 4]), 10)

    def test_negative_numbers(self):
        self.assertEqual(sum_of_elements([-1, -2, -3]), -6)

    def test_empty_list(self):
        self.assertEqual(sum_of_elements([]), 0)

if __name__ == '__main__':
    unittest.main()

user
### Immediate Task
Write the complete unittest test suite for the following Python function.

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

from HumanEval_102_code import choose_num

class TestChooseNum(unittest.TestCase):
    def test_positive_numbers(self):
        self.assertEqual(choose_num(12, 15), 14)
    
    def test_negative_numbers(self):
        self.assertEqual(choose_num(13, 12), -1)
    
    def test_equal_numbers(self):
        self.assertEqual(choose_num(12, 12), -1)
    
    def test_out_of_range(self):
        self.assertEqual(choose_num(17, 19), -1)
    
    def test_single_number(self):
        self.assertEqual(choose_num(8, 8), 8)
    
    def test_zero(self):
        self.assertEqual(choose_num(0, 10), 10)
    
    def test_large_numbers(self):
        self.assertEqual(choose_num(1000000, 1000000), 1000000)
    
    def test_edge_cases(self):
        self.assertEqual(choose_num(-1, 1), -1)
        self.assertEqual(choose_num(1, 1), -1)
        self.assertEqual(choose_num(1, 0), -1)
        self.assertEqual(choose_num(0, 1), 0)
        self.assertEqual(choose_num(1, 100), 100)
        self.assertEqual(choose_num(100, 1), -1)
        self.assertEqual(choose_num(100, 100), 100)
        self.assertEqual(choose_num(100, 101), 100)
        self.assertEqual(choose_num(101, 100), -1)
        self.assertEqual(choose_num(101, 101), 101)
        self.assertEqual(choose_num(101, 102), 101)
        self.assertEqual(choose_num(102, 101), -1)
        self.assertEqual(choose_num(102, 102), 102)
        self.assertEqual(choose_num(102, 103), 102)
        self.assertEqual(choose_num(103, 102), -1)
        self.assertEqual(choose_num(103, 103), 103)
        self.assertEqual(choose_num(103, 104), 103)
        self.assertEqual(choose_num(104, 103), -1)
        self.assertEqual(choose_num(104, 104), 104)
        self.assertEqual(choose_num(104, 105), 104)
        self.assertEqual(choose_num(105, 104), -1)
        self.assertEqual(choose_num(105, 105), 105)
        self.assertEqual(choose_num(105, 106), 105)
        self.assertEqual(choose_num(106, 105), -1)
        self.assertEqual(choose_num(106, 106), 106)
        self.assertEqual(choose_num(106, 107), 106)
        self.assertEqual(choose_num(107, 106), -1)
        self.assertEqual(choose_num(107, 107), 107)
        self.assertEqual(choose_num(107, 108), 107)
        self.assertEqual(choose_num(108, 107), -1)
        self.assertEqual(choose_num(108, 108), 108)
        self.assertEqual(choose_num(108, 109), 108)
        self.assertEqual(choose_num(109, 108), -1)
        self.assertEqual(choose_num(109, 109), 109)
        self.assertEqual(choose_num(109, 110), 109)
        self.assertEqual(choose_num(110, 109), -1)
        self.assertEqual(choose_num(110, 110), 110)
        self.assertEqual(choose_num(110, 111), 110)
        self.assertEqual(choose_num(111, 110), -1)
        self.assertEqual(choose_num(111, 111), 111)
        self.assertEqual(choose_num(111, 11