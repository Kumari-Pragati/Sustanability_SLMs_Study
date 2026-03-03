system

You are an expert Python programmer whose primary role is to write comprehensive unittest test suites. Be professional, precise, and output only runnable Python code.user

Write a complete unittest test suite for the following Python function.
Follow all rules carefully.

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
    for Strongest_Extension('my_class', ['AA', 'Be', 'CC']) =='my_class.AA'
    """
    strong = extensions[0]
    my_val = len([x for x in extensions[0] if x.isalpha() and x.isupper()]) - len([x for x in extensions[0] if x.isalpha() and x.islower()])
    for s in extensions:
        val = len([x for x in s if x.isalpha() and x.isupper()]) - len([x for x in s if x.isalpha() and x.islower()])
        if val > my_val:
            strong = s
            my_val = val

    ans = class_name + "." + strong
    return ansassistant

Here is the complete unittest test suite for the given Python function:

Python
import unittest
from HumanEval_153_code import Strongest_Extension

class TestStrongest_Extension(unittest.TestCase):

    def test_strongest_extension(self):
        self.assertEqual(Strongest_Extension('my_class', ['AA', 'Be', 'CC']),'my_class.AA')

    def test_strongest_extension2(self):
        self.assertEqual(Strongest_Extension('Slices', ['SErviNGSliCes', 'Cheese', 'StuFfed']), 'Slices.SErviNGSliCes')

    def test_strongest_extension3(self):
        self.assertEqual(Strongest_Extension('my_class', ['AA', 'Be', 'CC', 'DD']),'my_class.AA')

    def test_strongest_extension4(self):
        self.assertEqual(Strongest_Extension('my_class', ['AA', 'Be', 'CC', 'EE']),'my_class.AA')

    def test_strongest_extension5(self):
        self.assertEqual(Strongest_Extension('my_class', ['AA', 'Be', 'CC', 'EE', 'FF']),'my_class.AA')

    def test_strongest_extension6(self):
        self.assertEqual(Strongest_Extension('my_class', ['AA', 'Be', 'CC', 'EE', 'FF', 'GG']),'my_class.AA')

    def test_strongest_extension7(self):
        self.assertEqual(Strongest_Extension('my_class', ['AA', 'Be', 'CC', 'EE', 'FF', 'GG', 'HH']),'my_class.AA')

    def test_strongest_extension8(self):
        self.assertEqual(Strongest_Extension('my_class', ['AA', 'Be', 'CC', 'EE', 'FF', 'GG', 'HH', 'II']),'my_class.AA')

    def test_strongest_extension9(self):
        self.assertEqual(Strongest_Extension('my_class', ['AA', 'Be', 'CC', 'EE', 'FF', 'GG', 'HH', 'II', 'JJ']),'my_class.AA')

    def test_strongest_extension10(self):
        self.assertEqual(Strongest_Extension('my_class', ['AA', 'Be', 'CC', 'EE', 'FF', 'GG', 'HH', 'II', 'JJ', 'KK']),'my_class.AA')

if __name__ == '__main__':
    unittest.main()