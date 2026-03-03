### Task Context
You are an expert Python programmer. Your only task is to write complete unittest test suites.

### Tone Context
Maintain a professional, precise, and methodical tone.

### Detailed Task Description & Rules
1. Analyze the provided Python function.
2. Generate a self-contained unittest test suite.
3. The output must:
   - Begin with import unittest
   - Include from HumanEval_14_code import all_prefixes
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
2. Include: from HumanEval_14_code import all_prefixes
3. End with:
if __name__ == '__main__':
    unittest.main()

Function:
from typing import List


def all_prefixes(string: str) -> List[str]:
    """ Return list of all prefixes from shortest to longest of the input string
    >>> all_prefixes('abc')
    ['a', 'ab', 'abc']
    """
    result: List[str] = []
    for i in range(len(string)):
        result.append(string[: i + 1])
    return result

 import unittest

from HumanEval_14_code import all_prefixes

class TestAllPrefixes(unittest.TestCase):
    def test_normal_string(self):
        self.assertEqual(all_prefixes('abc'), ['a', 'ab', 'abc'])

    def test_empty_string(self):
        self.assertEqual(all_prefixes(''), [])

    def test_single_character_string(self):
        self.assertEqual(all_prefixes('a'), ['a'])

    def test_single_character_string_with_whitespace(self):
        self.assertEqual(all_prefixes(' a '), ['a', ' a'])

    def test_string_with_special_characters(self):
        self.assertEqual(all_prefixes('a!b@c#'), ['a', 'a!', 'a!b', 'a!b@', 'a!b@c'])

    def test_string_with_whitespace(self):
        self.assertEqual(all_prefixes('a b c'), ['a', 'a b', 'a b c'])

    def test_string_with_mixed_case(self):
        self.assertEqual(all_prefixes('AbC'), ['A', 'Ab', 'AbC'])

    def test_string_with_numbers(self):
        self.assertEqual(all_prefixes('123'), ['1', '12', '123'])

    def test_string_with_empty_characters(self):
        self.assertEqual(all_prefixes('a_b_c'), ['a', 'a_b', 'a_b_c'])

    def test_string_with_non_alphanumeric_characters(self):
        self0000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000