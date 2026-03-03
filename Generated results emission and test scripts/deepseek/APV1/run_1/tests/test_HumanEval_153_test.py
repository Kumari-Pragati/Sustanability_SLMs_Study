You are an AI programming assistant, utilizing the Deepseek Coder model, developed by Deepseek Company, and you only answer questions related to computer science. For politically sensitive questions, security and privacy issues, and other non-computer science questions, you will refuse to answer
### Instruction:
You are an expert Python programmer.
Your task is to write a comprehensive unittest test suite for the given Python function.

### Output Formatting
1. Start with: import unittest
2. Include: from HumanEval_153_code import Strongest_Extension

3. End with:
if __name__ == '__main__':
    unittest.main()

Function:
def Strongest_Extension(class_name, extensions):
    """You will be given the name of a class (a string) and a list of extensions.
    The extensions are to be used to load additional classes to the class. The
    strength of the extension is as follows: Let CAP be the number of the uppercase
    letters in the extension's name, and let SM be the number of lowercase letters 
    in the extension's name, the strength is given by the fraction CAP - SM. 
    You should find the strongest extension and return a string in this 
    format: ClassName.StrongestExtensionName.
    If there are two or more extensions with the same strength, you should
    choose the one that comes first in the list.
    For example, if you are given "Slices" as the class and a list of the
    extensions: ['SErviNGSliCes', 'Cheese', 'StuFfed'] then you should
    return 'Slices.SErviNGSliCes' since 'SErviNGSliCes' is the strongest extension 
    (its strength is -1).
    Example:
    for Strongest_Extension('my_class', ['AA', 'Be', 'CC']) == 'my_class.AA'
    """
    strong = extensions[0]
    my_val = len([x for x in extensions[0] if x.isalpha() and x.isupper()]) - len([x for x in extensions[0] if x.isalpha() and x.islower()])
    for s in extensions:
        val = len([x for x in s if x.isalpha() and x.isupper()]) - len([x for x in s if x.isalpha() and x.islower()])
        if val > my_val:
            strong = s
            my_val = val

    ans = class_name + "." + strong
    return ans


### Response:
Here is a unittest test suite for the given Python function:


import unittest
from HumanEval_153_code import Strongest_Extension

class TestStrongestExtension(unittest.TestCase):
    def test_basic(self):
        self.assertEqual(Strongest_Extension('my_class', ['AA', 'Be', 'CC']), 'my_class.AA')

    def test_same_strength(self):
        self.assertEqual(Strongest_Extension('my_class', ['AA', 'bb', 'CC']), 'my_class.AA')

    def test_different_strength(self):
        self.assertEqual(Strongest_Extension('my_class', ['AA', 'bb', 'cc']), 'my_class.AA')

    def test_all_uppercase(self):
        self.assertEqual(Strongest_Extension('my_class', ['AAA', 'BBB', 'CCC']), 'my_class.AAA')

    def test_all_lowercase(self):
        self.assertEqual(Strongest_Extension('my_class', ['aaa', 'bbb', 'ccc']), 'my_class.aaa')

    def test_mixed_case(self):
        self.assertEqual(Strongest_Extension('my_class', ['aAa', 'bBb', 'cCc']), 'my_class.aAa')

    def test_empty_extensions(self):
        with self.assertRaises(IndexError):
            Strongest_Extension('my_class', [])

if __name__ == '__main__':
    unittest.main()


This test suite includes tests for different scenarios, including:

- Basic case: when the strongest extension has the same number of uppercase and lowercase letters.
- Same strength: when there are multiple extensions with the same strength, the function should return the first one.
- Different strength: when the strongest extension has more uppercase letters than lowercase letters.
- All uppercase: when all extensions have only uppercase letters.
- All lowercase: when all extensions have only lowercase letters.
- Mixed case: when extensions have a mix of uppercase and lowercase letters.
- Empty extensions: when the list of extensions is empty, the function should raise an IndexError.

Please note that the function `Strongest_Extension` should be defined in the file `HumanEval_153_code.py` for these tests to work.