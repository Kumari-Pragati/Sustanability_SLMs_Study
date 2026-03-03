You are an AI programming assistant, utilizing the Deepseek Coder model, developed by Deepseek Company, and you only answer questions related to computer science. For politically sensitive questions, security and privacy issues, and other non-computer science questions, you will refuse to answer
### Instruction:
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


### Response:
Here is a unittest test suite for the given Python function:


import unittest
from HumanEval_156_code import int_to_mini_roman

class TestIntToMiniRoman(unittest.TestCase):
    def test_single_digit(self):
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

    def test_double_digit(self):
        self.assertEqual(int_to_mini_roman(11), 'xi')
        self.assertEqual(int_to_mini_roman(12), 'xii')
        self.assertEqual(int_to_mini_roman(13), 'xiii')
        self.assertEqual(int_to_mini_roman(14), 'xiv')
        self.assertEqual(int_to_mini_roman(15), 'xv')
        self.assertEqual(int_to_mini_roman(16), 'xvi')
        self.assertEqual(int_to_mini_roman(17), 'xvii')
        self.assertEqual(int_to_mini_roman(18), 'xviii')
        self.assertEqual(int_to_mini_roman(19), 'xix')
        self.assertEqual(int_to_mini_roman(20), 'xx')

    def test_triple_digit(self):
        self.assertEqual(int_to_mini_roman(30), 'xxx')
        self.assertEqual(int_to_mini_roman(40), 'xl')
        self.assertEqual(int_to_mini_roman(50), 'l')
        self.assertEqual(int_to_mini_roman(60), 'lx')
        self.assertEqual(int_to_mini_roman(70), 'lxx')
        self.assertEqual(int_to_mini_roman(80), 'lxxx')
        self.assertEqual(int_to_mini_roman(90), 'xc')
        self.assertEqual(int_to_mini_roman(100), 'c')

    def test_four_digit(self):
        self.assertEqual(int_to_mini_roman(400), 'cd')
        self.assertEqual(int_to_mini_roman(500), 'd')
        self.assertEqual(int_to_mini_roman(600), 'dc')
        self.assertEqual(int_to_mini_roman(700), 'dcc')
        self.assertEqual(int_to_mini_roman(800), 'dccc')
        self.assertEqual(int_to_mini_roman(900), 'cm')
        self.assertEqual(int_to_mini_roman(1000), 'm')

    def test_edge_cases(self):
        self.assertEqual(int_to_mini_roman(0), '')
        self.assertEqual(int_to_mini_roman(1001), '')

if __name__ == '__main__':
    unittest.main()


This test suite includes tests for single-digit numbers, double-digit numbers, triple-digit numbers, and four-digit numbers. It also includes tests for edge cases where the input is 0 or greater than 1000.