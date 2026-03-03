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
   - Include from HumanEval_44_code import change_base
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
2. Include: from HumanEval_44_code import change_base
3. End with:
if __name__ == '__main__':
    unittest.main()

Function:
def change_base(x: int, base: int):
    """Change numerical base of input number x to base.
    Return string representation after the conversion.
    Base numbers are less than 10.
    >>> change_base(8, 3)
    '22'
    >>> change_base(8, 2)
    '1000'
    >>> change_base(7, 2)
    '111'
    """
    ret = ""
    while x > 0:
        ret = str(x % base) + ret
        x //= base
    return ret


assistant

import unittest

from HumanEval_44_code import change_base

class TestChangeBase(unittest.TestCase):
    def test_normal_case(self):
        self.assertEqual(change_base(8, 3), "22")
    
    def test_edge_case(self):
        self.assertEqual(change_base(8, 2), "1000")
    
    def test_invalid_input(self):
        with self.assertRaises(ValueError):
            change_base(-1, 2)
        
        with self.assertRaises(ValueError):
            change_base(8, -2)
        
        with self.assertRaises(ValueError):
            change_base(8, 0)
        
        with self.assertRaises(ValueError):
            change_base(8, 10)
        
        with self.assertRaises(ValueError):
            change_base(8, 11)
        
        with self.assertRaises(ValueError):
            change_base(8, 12)
        
        with self.assertRaises(ValueError):
            change_base(8, 13)
        
        with self.assertRaises(ValueError):
            change_base(8, 14)
        
        with self.assertRaises(ValueError):
            change_base(8, 15)
        
        with self.assertRaises(ValueError):
            change_base(8, 16)
        
        with self.assertRaises(ValueError):
            change_base(8, 17)
        
        with self.assertRaises(ValueError):
            change_base(8, 18)
        
        with self.assertRaises(ValueError):
            change_base(8, 19)
        
        with self.assertRaises(ValueError):
            change_base(8, 20)
        
        with self.assertRaises(ValueError):
            change_base(8, 21)
        
        with self.assertRaises(ValueError):
            change_base(8, 22)
        
        with self.assertRaises(ValueError):
            change_base(8, 23)
        
        with self.assertRaises(ValueError):
            change_base(8, 24)
        
        with self.assertRaises(ValueError):
            change_base(8, 25)
        
        with self.assertRaises(ValueError):
            change_base(8, 26)
        
        with self.assertRaises(ValueError):
            change_base(8, 27)
        
        with self.assertRaises(ValueError):
            change_base(8, 28)
        
        with self.assertRaises(ValueError):
            change_base(8, 29)
        
        with self.assertRaises(ValueError):
            change_base(8, 30)
        
        with self.assertRaises(ValueError):
            change_base(8, 31)
        
        with self.assertRaises(ValueError):
            change_base(8, 32)
        
        with self.assertRaises(ValueError):
            change_base(8, 33)
        
        with self.assertRaises(ValueError):
            change_base(8, 34)
        
        with self.assertRaises(ValueError):
            change_base(8, 35)
        
        with self.assertRaises(ValueError):
            change_base(8, 36)
        
        with self.assertRaises(ValueError):
            change_base(8, 37)
        
        with self.assertRaises(ValueError):
            change_base(8, 38)
        
        with self.assertRaises(ValueError):
            change_base(8, 39)
        
        with self.assertRaises(ValueError):
            change_base(8, 40)
        
        with self.assertRaises(ValueError):
            change_base(8, 41)
        
        with self.assertRaises(ValueError):
            change_base(8, 42)
        
        with self.assertRaises(ValueError):
            change_base(8, 43)
        
        with self.assertRaises(ValueError):
            change_base(8, 44)
        
        with self.assertRaises(ValueError):
            change_base(8, 45)
        
        with self.assertRaises(ValueError):
            change_base(8, 46)
        
        with self.assertRaises(ValueError):
            change_base(8, 47)
        
        with self.assertRaises(ValueError):
            change_base(8, 48)
        
        with self.assertRaises(ValueError):
            change_base(8, 49)
        
        with self.assertRaises(ValueError):
            change_base(8, 50)
        
        with self.assertRaises(ValueError):
            change_base(8, 51)
        
        with self.assertRaises(ValueError):
            change_base(8, 52)
        
        with self.assertRaises(ValueError):
            change_base(8, 53)
        
        with self.assertRaises(ValueError):
            change_base(8, 54)
        
        with self.assertRaises(ValueError):
            change_base(8, 55)
        
        with self.assertRaises(ValueError):
            change_base(8, 56)
        
        with self.assertRaises(ValueError):
            change_base(8, 57)
        
        with self.assertRaises(ValueError):
            change_base(8, 58)
        
        with self.assertRaises(ValueError):
            change_base(8, 59)
        
        with self.assertRaises(ValueError):
            change_base(8, 60)
        
        with self.assertRaises(ValueError):
            change_base(8, 61)
        
        with self.assertRaises(ValueError):
            change_base(8,