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
   - Include from HumanEval_48_code import is_palindrome
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
2. Include: from HumanEval_48_code import is_palindrome
3. End with:
if __name__ == '__main__':
    unittest.main()

Function:
def is_palindrome(text: str):
    """
    Checks if given string is a palindrome
    >>> is_palindrome('')
    True
    >>> is_palindrome('aba')
    True
    >>> is_palindrome('aaaaa')
    True
    >>> is_palindrome('zbcd')
    False
    """
    for i in range(len(text)):
        if text[i] != text[len(text) - 1 - i]:
            return False
    return True


assistant

import unittest

from HumanEval_48_code import is_palindrome

class TestIsPalindrome(unittest.TestCase):
    def test_empty_string(self):
        self.assertTrue(is_palindrome(''))

    def test_single_character(self):
        self.assertTrue(is_palindrome('a'))
        self.assertTrue(is_palindrome('b'))

    def test_double_character(self):
        self.assertFalse(is_palindrome('ab'))

    def test_triple_character(self):
        self.assertTrue(is_palindrome('abc'))
        self.assertTrue(is_palindrome('bac'))

    def test_quad_character(self):
        self.assertTrue(is_palindrome('abcd'))
        self.assertTrue(is_palindrome('dcba'))

    def test_odd_length(self):
        self.assertTrue(is_palindrome('race'))
        self.assertTrue(is_palindrome('level'))

    def test_even_length(self):
        self.assertTrue(is_palindrome('radar'))
        self.assertTrue(is_palindrome('noon'))

    def test_mixed_case(self):
        self.assertTrue(is_palindrome('A man, a plan, a canal, Panama!'))
        self.assertTrue(is_palindrome('Madam, I'm Adam.'))

    def test_non_alpha_numeric(self):
        self.assertTrue(is_palindrome('12321'))
        self.assertTrue(is_palindrome('12345'))

    def test_special_characters(self):
        self.assertTrue(is_palindrome('Hello, World!'))
        self.assertTrue(is_palindrome('Python Programming'))

    def test_spaces(self):
        self.assertTrue(is_palindrome('The quick brown fox jumps over the lazy dog '))
        self.assertTrue(is_palindrome('I am not a palindrome'))

    def test_whitespace(self):
        self.assertTrue(is_palindrome('This is a palindrome'))
        self.assertTrue(is_palindrome('This is also a palindrome'))

    def test_url(self):
        self.assertTrue(is_palindrome('https://www.example.com/'))
        self.assertTrue(is_palindrome('http://example.com/test?query=hello'))

    def test_url_with_query(self):
        self.assertTrue(is_palindrome('http://example.com/?query=hello'))
        self.assertTrue(is_palindrome('https://www.example.com/?query=hello'))

    def test_url_with_fragment(self):
        self.assertTrue(is_palindrome('http://example.com/#fragment'))
        self.assertTrue(is_palindrome('https://www.example.com/#fragment'))

    def test_url_with_question_mark(self):
        self.assertTrue(is_palindrome('http://example.com/?question=mark'))
        self.assertTrue(is_palindrome('https://www.example.com/?question=mark'))

    def test_url_with_colon(self):
        self.assertTrue(is_palindrome('http://example.com/:colon'))
        self.assertTrue(is_palindrome('https://www.example.com/:colon'))

    def test_url_with_slash(self):
        self.assertTrue(is_palindrome('http://example.com/'))
        self.assertTrue(is_palindrome('https://www.example.com/'))

    def test_url_with_dots(self):
        self.assertTrue(is_palindrome('http://example.com/'))
        self.assertTrue(is_palindrome('https://www.example.com/'))

    def test_url_with_exclamation(self):
        self.assertTrue(is_palindrome('http://example.com/!'))
        self.assertTrue(is_palindrome('https://www.example.com/!'))

    def test_url_with_ampersand(self):
        self.assertTrue(is_palindrome('http://example.com/&amp;'))
        self.assertTrue(is_palindrome('https://www.example.com/&amp;'))

    def test_url_with_space(self):
        self.assertTrue(is_palindrome('http://example.com/ space'))
        self.assertTrue(is_palindrome('https://www.example.com/ space'))

    def test_url_with_dash(self):
        self.assertTrue(is_palindrome('http://example.com/-dash-'))
        self.assertTrue(is_palindrome('https://www.example.com/-dash-'))

    def test_url_with_number(self):
        self.assertTrue(is_palindrome('http://example.com/number-123'))
        self.assertTrue(is_palindrome('https://www.example.com/number-123'))

    def test_url_with_uppercase(self):
        self.assertTrue(is_palindrome('http://example.com/uppercase'))
        self.assertTrue(is_palindrome('https://www.example.com/uppercase'))

    def test_url_with_lowercase(self):
        self.assertTrue(is_palindrome('http://example.com/lowercase'))
        self.assertTrue(is_palindrome('https://www.example.com/lowercase'))

    def test_url_with_punctuation(self):
        self.assertTrue(is_palindrome('http://example.com/punctuation!@#'))
        self.assertTrue(is_palindrome('https://www.example.com/punctuation!@#'))

    def test_url_with_multiple_punctuation(self):
        self.assertTrue(is_palindrome('http://example.com/multiple-punctuation!@#'))
        self.assertTrue(is_palindrome('https://www.example.com/multiple-punctuation!@#'))

    def test_url_with_complex(self):
        self.assertTrue(is_palindrome('http://example.com/complex-url-with-complex-query-parameters'))
        self