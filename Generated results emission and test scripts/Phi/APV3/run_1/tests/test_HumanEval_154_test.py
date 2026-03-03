### Task Context
You are an expert Python programmer. Your only task is to write complete unittest test suites.

### Tone Context
Maintain a professional, precise, and methodical tone.

### Detailed Task Description & Rules
1. Analyze the provided Python function.
2. Generate a self-contained unittest test suite.
3. The output must:
   - Begin with import unittest
   - Include from HumanEval_154_code import cycpattern_check
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
 ### Immediate Task
Write the complete unittest test suite for the following Python function.

### Output Formatting
1. Start with: import unittest
2. Include: from HumanEval_154_code import cycpattern_check
3. End with:
if __name__ == '__main__':
    unittest.main()

Function:
def cycpattern_check(a, b):
    """You are given 2 words. You need to return True if the second word or any of its rotations is a substring in the first word
    cycpattern_check("abcd","abd") => False
    cycpattern_check("hello","ell") => True
    cycpattern_check("whassup","psus") => False
    cycpattern_check("abab","baa") => True
    cycpattern_check("efef","eeff") => False
    cycpattern_check("himenss","simen") => True

    """
    l = len(b)
    pat = b + b
    for i in range(len(a) - l + 1):
        for j in range(l + 1):
            if a[i:i + l] == pat[j:j + l]:
                return True
    return False

 import unittest

from HumanEval_154_code import cycpattern_check

class TestCycPatternCheck(unittest.TestCase):

    def test_normal_case_1(self):
        self.assertTrue(cycpattern_check("abcd", "abd"))

    def test_normal_case_2(self):
        self.assertTrue(cycpattern_check("hello", "ell"))

    def test_normal_case_3(self):
        self.assertTrue(cycpattern_check("whassup", "psus"))

    def test_normal_case_4(self):
        self.assertTrue(cycpattern_check("abab", "baa"))

    def test_normal_case_5(self):
        self.assertFalse(cycpattern_check("efef", "eeff"))

    def test_normal_case_6(self):
        self.assertTrue(cycpattern_check("himenss", "simen"))

    def test_edge_case_1(self):
        self.assertFalse(cycpattern_check("abcd", "abc"))

    def test_edge_case_2(self):
        self.assertFalse(cycpattern_check("hello", "lole"))

    def test_edge_case_3(self):
        self.assertFalse(cycpattern_check("whassup", "psup"))

    def test_edge_case_4(self):
        self.assertFalse(cycpattern_check("abab", "ba"))

    def test_edge_case_5(self):
        self.assertFalse(cycpattern_check("efef", "eff"))

    def test_edge_case_6(self):
        self.assertFalse(cycpattern_check("himenss", "sim"))

    def test_invalid_input_1(self):
        with self.assertRaises(TypeError):
            cycpattern_check("abcd", "123")

    def test_invalid_input_2(self):
        with self.assertRaises(TypeError):
            cycpattern_check("abcd", [1, 2, 3])

if __name__ == '__main__':
    unittest.main()