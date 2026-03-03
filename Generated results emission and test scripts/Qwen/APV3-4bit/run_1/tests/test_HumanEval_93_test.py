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
   - Include from HumanEval_93_code import encode
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
2. Include: from HumanEval_93_code import encode
3. End with:
if __name__ == '__main__':
    unittest.main()

Function:
def encode(message):
    """
    Write a function that takes a message, and encodes in such a 
    way that it swaps case of all letters, replaces all vowels in 
    the message with the letter that appears 2 places ahead of that 
    vowel in the english alphabet. 
    Assume only letters. 
    
    Examples:
    >>> encode('test')
    'TGST'
    >>> encode('This is a message')
    'tHKS KS C MGSSCGG'
    """

    vowels = "aeiouAEIOU"
    vowels_replace = dict([(i, chr(ord(i) + 2)) for i in vowels])
    message = message.swapcase()
    return ''.join([vowels_replace[i] if i in vowels else i for i in message])


assistant

import unittest

from HumanEval_93_code import encode

class TestEncode(unittest.TestCase):
    def test_normal_case(self):
        self.assertEqual(encode("test"), "TGST")
    
    def test_complex_message(self):
        self.assertEqual(encode("This is a message"), "tHKS KS C MGSSCGG")

    def test_empty_string(self):
        self.assertEqual(encode(""), "")

    def test_uppercase_only(self):
        self.assertEqual(encode("HELLO"), "hELLO")
    
    def test_lowercase_only(self):
        self.assertEqual(encode("world"), "wORLD")
    
    def test_vowel_replacement(self):
        # Check replacement of vowels
        self.assertEqual(encode("hello world"), "hKLS KSGY hKLS KSGY")
        
        # Check replacement of non-vowel characters
        self.assertEqual(encode("abc xyz"), "aBc dXz")
        
        # Check replacement of special characters
        self.assertEqual(encode("Hello World!"), "Hkls WOrld!")
        
        # Check replacement of numbers
        self.assertEqual(encode("12345"), "12345")
        
        # Check replacement of spaces
        self.assertEqual(encode(" "), " ")


If you run this script, it will execute the tests defined within `TestEncode` class. Each test should pass without any assertion errors. If there's a failure, the corresponding test case will fail and indicate which line caused the error.