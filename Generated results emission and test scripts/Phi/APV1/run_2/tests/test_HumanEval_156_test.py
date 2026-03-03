You are an expert Python programmer.
Your task is to write a comprehensive unittest test suite for the given Python function.

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
    return res.lower()

 import unittest
from HumanEval_156_code import int_to_mini_roman

class TestIntToMiniRoman(unittest.TestCase):

    def test_single_digit(self):
        self.assertEqual(int_to_mini_roman(1), 'i')

    def test_two_digit_under_100(self):
        self.assertEqual(int_to_mini_roman(15), 'cli')

    def test_two_digit_over_100(self):
        self.assertEqual(int_to_mini_roman(152), 'clii')

    def test_three_digit_under_1000(self):
        self.assertEqual(int_to_mini_roman(426), 'cdxxvi')

    def test_edge_case_1(self):
        self.assertEqual(int_to_mini_roman(1), 'i')

    def test_edge_case_1000(self):
        self.assertEqual(int_to_mini_roman(1000), 'm')

    def test_invalid_input(self):
        with self.assertRaises(ValueError):
            int_to_mini_roman(-1)
        with self.assertRaises(ValueError):
            int_to_mini_roman(1001)

if __name__ == '__main__':
    unittest.main()