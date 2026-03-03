### Task Context
You are an expert Python programmer. Your only task is to write complete unittest test suites.

### Tone Context
Maintain a professional, precise, and methodical tone.

### Detailed Task Description & Rules
1. Analyze the provided Python function.
2. Generate a self-contained unittest test suite.
3. The output must:
   - Begin with import unittest
   - Include from HumanEval_125_code import split_words
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
2. Include: from HumanEval_125_code import split_words
3. End with:
if __name__ == '__main__':
    unittest.main()

Function:
def split_words(txt):
    '''
    Given a string of words, return a list of words split on whitespace, if no whitespaces exists in the text you
    should split on commas ',' if no commas exists you should return the number of lower-case letters with odd order in the
    alphabet, ord('a') = 0, ord('b') = 1, ... ord('z') = 25
    Examples
    split_words("Hello world!") ➞ ["Hello", "world!"]
    split_words("Hello,world!") ➞ ["Hello", "world!"]
    split_words("abcdef") == 3 
    '''
    if " " in txt:
        return txt.split()
    elif "," in txt:
        return txt.replace(',', ' ').split()
    else:
        return len([i for i in txt if i.islower() and ord(i) % 2 == 0])

 import unittest

from HumanEval_125_code import split_words

class TestSplitWords(unittest.TestCase):

    def test_normal_whitespace(self):
        self.assertEqual(split_words("Hello world!"), ["Hello", "world!"])

    def test_normal_comma(self):
        self.assertEqual(split_words("Hello,world!"), ["Hello", "world!"])

    def test_no_whitespace_or_comma(self):
        self.assertEqual(split_words("abcdef"), 3)

    def test_empty_string(self):
        self.assertEqual(split_words(""), [])

    def test_single_word(self):
        self.assertEqual(split_words("Hello"), ["Hello"])

    def test_multiple_words_with_whitespace(self):
        self.assertEqual(split_words("Hello   world!"), ["Hello", "world!"])

    def test_multiple_words_with_comma(self):
        self.assertEqual(split_words("Hello,world!"), ["Hello", "world!"])

    def test_no_lowercase_letters_with_odd_order(self):
        self.assertEqual(split_words("ABCDE"), 0)

    def test_all_lowercase_letters_with_odd_order(self):
        self.assertEqual(split_words("abcde"), 3)

    def test_mixed_case_letters_with_odd_order(self):
        self.assertEqual(split_words("AbCde"), 3)

    def test_uppercase_letters_with_odd_order(self):
        self.assertEqual(split_words("ABCD"), 0)

    def test_mixed_case_letters_with_even_order(self):
        self.assertEqual(split_words("AbCde"), 3)

    def test_all_uppercase_letters_with_even_order(self):
        self.assertEqual(split_words("ABCDE"), 0)

    def test_mixed_case_letters_with_no_odd_order(self):
        self.assertEqual(split_words("AbCdeF"), 3)

    def test_all_uppercase_letters_with_no_odd_order(self):
        self.assertEqual(split_words("ABCDEF"), 0)

if __name__ == '__main__':
    unittest.main()