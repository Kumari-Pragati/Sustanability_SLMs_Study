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
   - Include from HumanEval_153_code import Strongest_Extension
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

# Importing the required module
from HumanEval_153_code import Strongest_Extension

class TestStrongestExtension(unittest.TestCase):
    def test_normal_case(self):
        # Test case with positive numbers
        result = Strongest_Extension("MyClass", ["AA", "BE", "CC"])
        self.assertEqual(result, "MyClass.AA")

    def test_edge_case_uppercase_only(self):
        # Test case with all uppercase letters
        result = Strongest_Extension("MyClass", ["AAAA", "BBB", "CCC"])
        self.assertEqual(result, "MyClass.AAAA")

    def test_edge_case_lowercase_only(self):
        # Test case with all lowercase letters
        result = Strongest_Extension("MyClass", ["aaa", "bbb", "ccc"])
        self.assertEqual(result, "MyClass.AAA")

    def test_edge_case_mixed_case(self):
        # Test case with mixed uppercase and lowercase letters
        result = Strongest_Extension("MyClass", ["ABCD", "abcd", "ABC"])
        self.assertEqual(result, "MyClass.ABCD")

    def test_invalid_input(self):
        # Test case with empty list
        result = Strongest_Extension("MyClass", [])
        self.assertIsNone(result)

    def test_multiple_extensions_with_same_strength(self):
        # Test case with multiple extensions having the same strength
        result = Strongest_Extension("MyClass", ["AA", "BE", "CC", "DD"])
        self.assertEqual(result, "MyClass.AA")

if __name__ == '__main__':
    unittest.main()