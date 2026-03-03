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
   - Include from HumanEval_29_code import filter_by_prefix
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
2. Include: from HumanEval_29_code import filter_by_prefix
3. End with:
if __name__ == '__main__':
    unittest.main()

Function:
from typing import List


def filter_by_prefix(strings: List[str], prefix: str) -> List[str]:
    """Filter an input list of strings only for ones that start with a given prefix.
    >>> filter_by_prefix([], 'a')
    []
    >>> filter_by_prefix(['abc', 'bcd', 'cde', 'array'], 'a')
    ['abc', 'array']
    """
    return [x for x in strings if x.startswith(prefix)]


assistant

import unittest

# Importing the function from the provided code snippet
from HumanEval_29_code import filter_by_prefix

class TestFilterByPrefix(unittest.TestCase):
    def test_empty_input(self):
        self.assertEqual(filter_by_prefix([], 'a'), [])

    def test_single_element(self):
        self.assertEqual(filter_by_prefix(['apple'], 'a'), ['apple'])

    def test_multiple_elements_with_prefix(self):
        self.assertEqual(
            filter_by_prefix(['banana', 'apple', 'avocado', 'grape'], 'a'),
            ['apple', 'avocado']
        )

    def test_multiple_elements_without_prefix(self):
        self.assertEqual(
            filter_by_prefix(['cherry', 'date', 'fig', 'grape'], 'b'),
            ['cherry', 'date', 'fig', 'grape']
        )

    def test_case_insensitive(self):
        self.assertEqual(
            filter_by_prefix(['Banana', 'Apple', 'Avocado', 'Grape'], 'A'),
            ['Apple', 'Avocado']
        )

    def test_prefix_at_start(self):
        self.assertEqual(
            filter_by_prefix(['prefix', 'pre', 'prefixed', 'prefixes'], 'p'),
            ['prefix', 'pre', 'prefixed', 'prefixes']
        )

    def test_prefix_in_middle(self):
        self.assertEqual(
            filter_by_prefix(['prefix', 'middle', 'in', 'prefix'], 'p'),
            ['prefix', 'middle']
        )

    def test_prefix_at_end(self):
        self.assertEqual(
            filter_by_prefix(['prefix', 'end', 'at', 'prefix'], 'p'),
            ['prefix', 'end']
        )

    def test_prefix_not_found(self):
        self.assertEqual(
            filter_by_prefix(['nope', 'prefix', 'not', 'found'], 'z'),
            ['nope', 'prefix', 'not', 'found']
        )

    def test_prefix_only_one_char(self):
        self.assertEqual(
            filter_by_prefix(['onechar', 'twochars', 'threechars'], 'o'),
            ['onechar']
        )

    def test_prefix_only_two_chars(self):
        self.assertEqual(
            filter_by_prefix(['twocaracters', 'threecaracters', 'fourcaracters'], 'two'),
            ['twocaracters']
        )

    def test_prefix_only_three_chars(self):
        self.assertEqual(
            filter_by_prefix(['threecaracters', 'fourcaracters', 'fivecharacters'], 'three'),
            ['threecaracters']
        )

    def test_prefix_only_four_chars(self):
        self.assertEqual(
            filter_by_prefix(['fourcaracters', 'fivethings', 'sixthings'], 'four'),
            ['fourcaracters']
        )

    def test_prefix_only_five_chars(self):
        self.assertEqual(
            filter_by_prefix(['fivesomething', 'sixsomething', 'sevensomething'], 'five'),
            ['fivesomething']
        )

    def test_prefix_only_six_chars(self):
        self.assertEqual(
            filter_by_prefix(['sixthingssomething', 'seventhingssomething', 'eightthingssomething'], 'six'),
            ['sixthingssomething']
        )

    def test_prefix_only_seven_chars(self):
        self.assertEqual(
            filter_by_prefix(['seventhingsomething', 'eighthingsomething', 'ninthingsomething'], 'seven'),
            ['seventhingsomething']
        )

    def test_prefix_only_eight_chars(self):
        self.assertEqual(
            filter_by_prefix(['eighthingsomething', 'ninethingsomething', 'tenthingsomething'], 'eight'),
            ['eighthingsomething']
        )

    def test_prefix_only_nine_chars(self):
        self.assertEqual(
            filter_by_prefix(['ninethingsomething', 'tenthingsomething', 'eleventhingsomething'], 'nine'),
            ['ninethingsomething']
        )

    def test_prefix_only_ten_chars(self):
        self.assertEqual(
            filter_by_prefix(['tenthingsomething', 'eleventhingsomething', 'twelvethingsomething'], 'ten'),
            ['tenthingsomething']
        )

    def test_prefix_only_eleven_chars(self):
        self.assertEqual(
            filter_by_prefix(['eleventhingsomething', 'twelvethingsomething', 'thirteenthingsomething'], 'eleven'),
            ['eleventhingsomething']
        )

    def test_prefix_only_twelve_chars(self):
        self.assertEqual(
            filter_by_prefix(['twelfthingsomething', 'thirteenthingsomething', 'fourteenthingsomething'], 'twelve'),
            ['twelfthingsomething']
        )

    def test_prefix_only_thirteen_chars(self):
        self.assertEqual(
            filter_by_prefix(['thirteenthingsomething', 'fourteenthingsomething', 'fifteenthingsomething'], 'thirteen'),
            ['thirteenthingsomething']
        )

    def test_prefix_only_fourteen_chars(self):
        self.assertEqual(