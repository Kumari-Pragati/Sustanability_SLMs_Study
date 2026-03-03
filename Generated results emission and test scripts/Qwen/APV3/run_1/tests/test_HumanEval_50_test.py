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
   - Include from HumanEval_50_code import decode_shift
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
2. Include: from HumanEval_50_code import decode_shift
3. End with:
if __name__ == '__main__':
    unittest.main()

Function:
def encode_shift(s: str):
    """
    Returns encoded string by shifting every character by 5 in the alphabet.
    """
    return "".join([chr(((ord(ch) + 5 - ord("a")) % 26) + ord("a")) for ch in s])


def decode_shift(s: str):
    """
    Takes as input a string encoded with encode_shift function. Returns decoded string.
    """
    return "".join([chr(((ord(ch) - 5 - ord("a")) % 26) + ord("a")) for ch in s])


assistant

import unittest

from HumanEval_50_code import encode_shift, decode_shift

class TestEncodeShiftAndDecodeShift(unittest.TestCase):
    
    def test_encode_shift(self):
        # Normal case
        result = encode_shift("abc")
        expected_result = "fgh"
        self.assertEqual(result, expected_result)
        
        # Edge case: empty string
        result = encode_shift("")
        expected_result = ""
        self.assertEqual(result, expected_result)
        
        # Invalid input (non-string)
        try:
            encode_shift(123)
            self.fail("Expected TypeError for non-string input")
        except TypeError:
            pass
    
    def test_decode_shift(self):
        # Normal case
        result = decode_shift("fgh")
        expected_result = "abc"
        self.assertEqual(result, expected_result)
        
        # Edge case: empty string
        result = decode_shift("")
        expected_result = ""
        self.assertEqual(result, expected_result)
        
        # Invalid input (non-string)
        try:
            decode_shift(123)
            self.fail("Expected TypeError for non-string input")
        except TypeError:
            pass
        
        # Normal case with different shift value
        result = decode_shift("xyz", shift=7)
        expected_result = "abc"
        self.assertEqual(result, expected_result)
        
        # Edge case: shift larger than 26
        try:
            decode_shift("abc", shift=27)
            self.fail("Expected ValueError for shift larger than 26")
        except ValueError:
            pass
        
        # Edge case: shift smaller than 1
        try:
            decode_shift("abc", shift=-1)
            self.fail("Expected ValueError for shift smaller than 1")
        except ValueError:
            pass

if __name__ == '__main__':
    unittest.main()