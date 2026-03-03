You are an AI programming assistant, utilizing the Deepseek Coder model, developed by Deepseek Company, and you only answer questions related to computer science. For politically sensitive questions, security and privacy issues, and other non-computer science questions, you will refuse to answer
### Instruction:
Generate a unittest test script for the following Python function.
The script should fully test the function and be runnable directly.

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
Here is a unittest script for the given function:


import unittest
from HumanEval_156_code import int_to_mini_roman

class TestIntToMiniRoman(unittest.TestCase):
    def test_int_to_mini_roman(self):
        self.assertEqual(int_to_mini_roman(19), 'xix')
        self.assertEqual(int_to_mini_roman(152), 'clii')
        self.assertEqual(int_to_mini_roman(426), 'cdxxvi')
        self.assertEqual(int_to_mini_roman(9), 'ix')
        self.assertEqual(int_to_mini_roman(10), 'x')
        self.assertEqual(int_to_mini_roman(40), 'xl')
        self.assertEqual(int_to_mini_roman(50), 'l')
        self.assertEqual(int_to_mini_roman(90), 'xc')
        self.assertEqual(int_to_mini_roman(100), 'c')
        self.assertEqual(int_to_mini_roman(400), 'cd')
        self.assertEqual(int_to_mini_roman(500), 'd')
        self.assertEqual(int_to_mini_roman(900), 'cm')
        self.assertEqual(int_to_mini_roman(1000), 'm')
        self.assertEqual(int_to_mini_roman(1), 'i')
        self.assertEqual(int_to_mini_roman(5), 'v')
        self.assertEqual(int_to_mini_roman(11), 'xi')
        self.assertEqual(int_to_mini_roman(14), 'xiv')
        self.assertEqual(int_to_mini_roman(15), 'xv')
        self.assertEqual(int_to_mini_roman(16), 'xvi')
        self.assertEqual(int_to_mini_roman(20), 'xx')
        self.assertEqual(int_to_mini_roman(21), 'xxi')
        self.assertEqual(int_to_mini_roman(24), 'xxiv')
        self.assertEqual(int_to_mini_roman(25), 'xxv')
        self.assertEqual(int_to_mini_roman(26), 'xxvi')
        self.assertEqual(int_to_mini_roman(30), 'xxx')
        self.assertEqual(int_to_mini_roman(31), 'xxxi')
        self.assertEqual(int_to_mini_roman(34), 'xxxiv')
        self.assertEqual(int_to_mini_roman(35), 'xxxv')
        self.assertEqual(int_to_mini_roman(36), 'xxvi')
        self.assertEqual(int_to_mini_roman(41), 'xli')
        self.assertEqual(int_to_mini_roman(44), 'xliv')
        self.assertEqual(int_to_mini_roman(45), 'xlix')
        self.assertEqual(int_to_mini_roman(46), 'xlii')
        self.assertEqual(int_to_mini_roman(51), 'lli')
        self.assertEqual(int_to_mini_roman(54), 'liv')
        self.assertEqual(int_to_mini_roman(55), 'lv')
        self.assertEqual(int_to_mini_roman(56), 'lvi')
        self.assertEqual(int_to_mini_roman(60), 'lxx')
        self.assertEqual(int_to_mini_roman(61), 'lxxxi')
        self.assertEqual(int_to_mini_roman(64), 'lxxxiv')
        self.assertEqual(int_to_mini_roman(65), 'lxxxv')
        self.assertEqual(int_to_mini_roman(66), 'lxxvi')
        self.assertEqual(int_to_mini_roman(70), 'lxxx')
        self.assertEqual(int_to_mini_roman(71), 'lxxxi')
        self.assertEqual(int_to_mini_roman(74), 'lxxxiv')
        self.assertEqual(int_to_mini_roman(75), 'lxxxv')