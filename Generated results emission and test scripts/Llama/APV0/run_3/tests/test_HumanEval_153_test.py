user

Generate a unittest test script for the following Python function.
The script should fully test the function and be runnable directly.

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

Here is the unittest test script for the given Python function:

Python
import unittest
from HumanEval_153_code import Strongest_Extension

class TestStrongestExtension(unittest.TestCase):

    def test_strongest_extension(self):
        self.assertEqual(Strongest_Extension('my_class', ['AA', 'Be', 'CC']),'my_class.AA')
        self.assertEqual(Strongest_Extension('Slices', ['SErviNGSliCes', 'Cheese', 'StuFfed']), 'Slices.SErviNGSliCes')
        self.assertEqual(Strongest_Extension('Class1', ['Aa', 'Bb', 'Cc']), 'Class1.Aa')
        self.assertEqual(Strongest_Extension('Class2', ['AA', 'BB', 'CC']), 'Class2.AA')
        self.assertEqual(Strongest_Extension('Class3', ['aA', 'bB', 'cC']), 'Class3.aA')
        self.assertEqual(Strongest_Extension('Class4', ['Aa', 'Bb', 'Cc']), 'Class4.Aa')
        self.assertEqual(Strongest_Extension('Class5', ['AA', 'BB', 'CC']), 'Class5.AA')

    def test_strongest_extension_with_multiple_extensions_with_same_strength(self):
        self.assertEqual(Strongest_Extension('Class1', ['AA', 'BB', 'CC']), 'Class1.AA')
        self.assertEqual(Strongest_Extension('Class2', ['aA', 'bB', 'cC']), 'Class2.aA')
        self.assertEqual(Strongest_Extension('Class3', ['Aa', 'Bb', 'Cc']), 'Class3.Aa')

if __name__ == '__main__':
    unittest.main()


This script includes two test methods: `test_strongest_extension` and `test_strongest_extension_with_multiple_extensions_with_same_strength`. The first method tests the function with different inputs and expected outputs. The second method tests the function with multiple extensions that have the same strength, and the function should return the first one in the list.