system
You are Qwen, created by Alibaba Cloud. You are a helpful assistant.
user
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


assistant

import unittest

# Function definition provided
from HumanEval_153_code import Strongest_Extension


class TestStrongestExtension(unittest.TestCase):
    def test_strongest_extension(self):
        # Test case 1
        result = Strongest_Extension("my_class", ["AA", "Be", "CC"])
        self.assertEqual(result, "my_class.AA")

        # Test case 2
        result = Strongest_Extension("another_class", ["ABCD", "abcd", "ABC"])
        self.assertEqual(result, "another_class.ABCD")

        # Test case 3
        result = Strongest_Extension("yet_another_class", ["XYZ", "xyz", "xyX"])
        self.assertEqual(result, "yet_another_class.XYZ")

        # Test case 4
        result = Strongest_Extension("test_class", ["Test", "Teste", "Testing"])
        self.assertEqual(result, "test_class.Teste")

        print("All tests passed!")


if __name__ == "__main__":
    unittest.main()


This code snippet defines a `unittest` test suite for the `Strongest_Extension` function. It includes several test cases to verify the correctness of the function under different scenarios.