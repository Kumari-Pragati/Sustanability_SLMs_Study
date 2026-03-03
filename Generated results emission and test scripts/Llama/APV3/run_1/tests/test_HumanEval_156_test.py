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
   - Include from HumanEval_156_code import int_to_mini_roman
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
    unittest.main()user

### Immediate Task
Write the complete unittest test suite for the following Python function.

### Output Formatting
1. Start with: import unittest
2. Include: from HumanEval_156_code import int_to_mini_roman
3. End with:
if __name__ == '__main__':
    unittest.main()

Function:
def int_to_mini_roman(number):
    """
    Given a positive integer, obtain its roman numeral equivalent as a string,
    and return it in lowercase.
    Restrictions: 1 <= num <= 1000

    Examples:
    >>> int_to_mini_roman(19) == 'xix'
    >>> int_to_mini_roman(152) == 'clii'
    >>> int_to_mini_roman(426) == 'cdxxvi'
    """
    num = [1, 4, 5, 9, 10, 40, 50, 90,
           100, 400, 500, 900, 1000]
    sym = ["I", "IV", "V", "IX", "X", "XL",
           "L", "XC", "C", "CD", "D", "CM", "M"]
    i = 12
    res = ''
    while number:
        div = number // num[i]
        number %= num[i]
        while div:
            res += sym[i]
            div -= 1
        i -= 1
    return res.lower()assistant

Here is the complete unittest test suite for the given Python function:


import unittest
from HumanEval_156_code import int_to_mini_roman

class TestIntToMiniRoman(unittest.TestCase):
    def test_single_digit_numbers(self):
        self.assertEqual(int_to_mini_roman(1), 'i')
        self.assertEqual(int_to_mini_roman(2), 'ii')
        self.assertEqual(int_to_mini_roman(3), 'iii')
        self.assertEqual(int_to_mini_roman(4), 'iv')
        self.assertEqual(int_to_mini_roman(5), 'v')
        self.assertEqual(int_to_mini_roman(6), 'vi')
        self.assertEqual(int_to_mini_roman(7), 'vii')
        self.assertEqual(int_to_mini_roman(8), 'viii')
        self.assertEqual(int_to_mini_roman(9), 'ix')
        self.assertEqual(int_to_mini_roman(10), 'x')

    def test_teen_numbers(self):
        self.assertEqual(int_to_mini_roman(11), 'xi')
        self.assertEqual(int_to_mini_roman(12), 'xii')
        self.assertEqual(int_to_mini_roman(13), 'xiii')
        self.assertEqual(int_to_mini_roman(14), 'xiv')
        self.assertEqual(int_to_mini_roman(15), 'xv')
        self.assertEqual(int_to_mini_roman(16), 'xvi')
        self.assertEqual(int_to_mini_roman(17), 'xvii')
        self.assertEqual(int_to_mini_roman(18), 'xviii')
        self.assertEqual(int_to_mini_roman(19), 'xix')

    def test_numbers_in_twenties(self):
        self.assertEqual(int_to_mini_roman(20), 'xx')
        self.assertEqual(int_to_mini_roman(21), 'xxi')
        self.assertEqual(int_to_mini_roman(22), 'xxii')
        self.assertEqual(int_to_mini_roman(23), 'xxiii')
        self.assertEqual(int_to_mini_roman(24), 'xxiv')
        self.assertEqual(int_to_mini_roman(25), 'xxv')
        self.assertEqual(int_to_mini_roman(26), 'xxvi')
        self.assertEqual(int_to_mini_roman(27), 'xxvii')
        self.assertEqual(int_to_mini_roman(28), 'xxviii')
        self.assertEqual(int_to_mini_roman(29), 'xxix')

    def test_numbers_in_fifties(self):
        self.assertEqual(int_to_mini_roman(50), 'l')
        self.assertEqual(int_to_mini_roman(51), 'li')
        self.assertEqual(int_to_mini_roman(52), 'lii')
        self.assertEqual(int_to_mini_roman(53), 'liii')
        self.assertEqual(int_to_mini_roman(54), 'liv')
        self.assertEqual(int_to_mini_roman(55), 'lv')
        self.assertEqual(int_to_mini_roman(56), 'lvi')
        self.assertEqual(int_to_mini_roman(57), 'lvii')
        self.assertEqual(int_to_mini_roman(58), 'lviii')
        self.assertEqual(int_to_mini_roman(59), 'lix')

    def test_numbers_in_hundreds(self):
        self.assertEqual(int_to_mini_roman(100), 'c')
        self.assertEqual(int_to_mini_roman(101), 'ci')
        self.assertEqual(int_to_mini_roman(102), 'cii')
        self.assertEqual(int_to_mini_roman(103), 'ciii')
        self.assertEqual(int_to_mini_roman(104), 'civ')
        self.assertEqual(int_to_mini_roman(105), 'cv')
        self.assertEqual(int_to_mini_roman(106), 'cvi')
        self.assertEqual(int_to_mini_roman(107), 'cvii')
        self.assertEqual(int_to_mini_roman(108), 'cviii')
        self.assertEqual(int_to_mini_roman(109), 'cix')

    def test_numbers_in_hundreds_and_twenties(self):
        self.assertEqual(int_to_mini_roman(200), 'cc')
        self.assertEqual(int_to_mini_roman(201), 'cci')
        self.assertEqual(int_to_mini_roman(202), 'ccii')
        self.assertEqual(int_to_mini_roman(203), 'cciii')
        self.assertEqual(int_to_mini_roman(204), 'cciv')
        self.assertEqual(int_to_mini_roman(205), 'ccv')
        self.assertEqual(int_to_mini_roman(206), 'ccvi')
        self.assertEqual(int_to_mini_roman(207), 'ccvii')
        self.assertEqual(int_to_mini_roman(208), 'ccviii')
        self.assertEqual(int_to_mini_roman(209), 'ccix')

    def test_numbers_in_hundreds_and_fifties(self):
        self.assertEqual(int_to_mini_roman(500), 'd')
        self.assertEqual(int_to_mini_roman(501), 'di')
        self.assertEqual(int_to_mini_roman(502), 'dii')