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
   - Include from HumanEval_16_code import count_distinct_characters
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
2. Include: from HumanEval_16_code import count_distinct_characters
3. End with:
if __name__ == '__main__':
    unittest.main()

Function:
def count_distinct_characters(string: str) -> int:
    """ Given a string, find out how many distinct characters (regardless of case) does it consist of
    >>> count_distinct_characters('xyzXYZ')
    3
    >>> count_distinct_characters('Jerry')
    4
    """

    return len(set(string.lower()))


assistant

import unittest

from HumanEval_16_code import count_distinct_characters

class TestCountDistinctCharacters(unittest.TestCase):
    
    def test_string_with_all_unique_chars(self):
        result = count_distinct_characters("abcABC")
        self.assertEqual(result, 3)
        
    def test_string_with_repeated_chars(self):
        result = count_distinct_characters("aaAaaa")
        self.assertEqual(result, 2)
        
    def test_empty_string(self):
        result = count_distinct_characters("")
        self.assertEqual(result, 0)
        
    def test_single_char_string(self):
        result = count_distinct_characters("a")
        self.assertEqual(result, 1)
        
    def test_mixed_case_string(self):
        result = count_distinct_characters("AbCdEfGhIjKlMnOpQrStUvWxYz")
        self.assertEqual(result, 27)
        
    def test_large_string(self):
        result = count_distinct_characters("ThisIsASampleStringWithSomeRepetitions")
        self.assertEqual(result, 28)
        
    def test_whitespace_only_string(self):
        result = count_distinct_characters(" ")
        self.assertEqual(result, 1)
        
    def test_multiple_spaces(self):
        result = count_distinct_characters("   ")
        self.assertEqual(result, 1)
        
    def test_punctuation(self):
        result = count_distinct_characters("Hello World!")
        self.assertEqual(result, 9)
        
    def test_special_chars(self):
        result = count_distinct_characters("¡Hola! ¿Cómo estás?")
        self.assertEqual(result, 11)
        
    def test_url(self):
        result = count_distinct_characters("http://example.com")
        self.assertEqual(result, 1)
        
    def test_email_address(self):
        result = count_distinct_characters("john@example.com")
        self.assertEqual(result, 10)
        
    def test_phone_number(self):
        result = count_distinct_characters("(123) 456-7890")
        self.assertEqual(result, 10)
        
    def test_complex_string(self):
        result = count_distinct_characters("The quick brown fox jumps over the lazy dog.")
        self.assertEqual(result, 26)
        
    def test_long_string(self):
        result = count_distinct_characters("abcdefghijklmnopqrstuvwxyzABCDEFGHIJKLMNOPQRSTUVWXYZ0123456789")
        self.assertEqual(result, 32)
        
    def test_random_string(self):
        result = count_distinct_characters("RandomString123")
        self.assertEqual(result, 11)
        
    def test_no_distinct_chars(self):
        result = count_distinct_characters("aaaaaaa")
        self.assertEqual(result, 1)
        
    def test_same_char_string(self):
        result = count_distinct_characters("aaaaaaa")
        self.assertEqual(result, 1)
        
    def test_all_same_case(self):
        result = count_distinct_characters("AAAAAA")
        self.assertEqual(result, 1)
        
    def test_all_uppercase(self):
        result = count_distinct_characters("ABCDEFG")
        self.assertEqual(result, 7)
        
    def test_all_lowercase(self):
        result = count_distinct_characters("abcdefg")
        self.assertEqual(result, 7)
        
    def test_all_caps(self):
        result = count_distinct_characters("ABCDEFG")
        self.assertEqual(result, 7)
        
    def test_all_lower(self):
        result = count_distinct_characters("abcdefg")
        self.assertEqual(result, 7)
        
    def test_all_digits(self):
        result = count_distinct_characters("1234567890")
        self.assertEqual(result, 10)
        
    def test_all_letters(self):
        result = count_distinct_characters("abcdefghijklmnopqrstuvwxyzABCDEFGHIJKLMNOPQRSTUVWXYZ")
        self.assertEqual(result, 32)
        
    def test_all_symbols(self):
        result = count_distinct_characters("!@#$%^&*()_+-=[]{}|;:'\"<>?,./'")
        self.assertEqual(result, 21)
        
    def test_all_spaces(self):
        result = count_distinct_characters("   ")
        self.assertEqual(result, 1)
        
    def test_all_whitespaces(self):
        result = count_distinct_characters("   ")
        self.assertEqual(result, 1)
        
    def test_all_punctuation(self):
        result = count_distinct_characters("¡Hola! ¿Cómo estás?")
        self.assertEqual(result, 11)
        
    def test_all_special_chars(self):
        result = count_distinct_characters("¡Hola! ¿Cómo estás?")
        self.assertEqual(result, 11)
        
    def test_all_urls(self):
        result = count_distinct_characters("http://example.com")
        self.assertEqual(result, 1)
        
    def test_all_emails(self):
        result = count_distinct_characters("john@example.com")
        self.assertEqual(result, 10)
        
    def test_all_phone_numbers(self):