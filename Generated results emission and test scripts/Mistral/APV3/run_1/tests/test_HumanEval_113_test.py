### Task Context
You are an expert Python programmer. Your only task is to write complete unittest test suites.

### Tone Context
Maintain a professional, precise, and methodical tone.

### Detailed Task Description & Rules
1. Analyze the provided Python function.
2. Generate a self-contained unittest test suite.
3. The output must:
   - Begin with import unittest
   - Include from HumanEval_113_code import odd_count
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
2. Include: from HumanEval_113_code import odd_count
3. End with:
if __name__ == '__main__':
    unittest.main()

Function:
def odd_count(lst):
    """Given a list of strings, where each string consists of only digits, return a list.
    Each element i of the output should be "the number of odd elements in the
    string i of the input." where all the i's should be replaced by the number
    of odd digits in the i'th string of the input.

    >>> odd_count(['1234567'])
    ["the number of odd elements 4n the str4ng 4 of the 4nput."]
    >>> odd_count(['3', "11111111"])
    ["the number of odd elements 1n the str1ng 1 of the 1nput.",
     "the number of odd elements 8n the str8ng 8 of the 8nput."]
    """

    res = []
    for arr in lst:
        n = sum(int(d) % 2 == 1 for d in arr)
        res.append(
            "the number of odd elements "
            + str(n)
            + "n the str"
            + str(n)
            + "ng "
            + str(n)
            + " of the "
            + str(n)
            + "nput."
        )
    return res

 import unittest

from HumanEval_113_code import odd_count

class TestOddCount(unittest.TestCase):
    def test_single_odd_number(self):
        self.assertEqual(odd_count(['1']), ["the number of odd elements 1n the str1ng 1 of the 1nput."])

    def test_single_even_number(self):
        self.assertEqual(odd_count(['2']), ["the number of odd elements 0n the str0ng 0 of the 0nput."])

    def test_multiple_odd_numbers(self):
        self.assertEqual(odd_count(['1', '3', '5']), ["the number of odd elements 1n the str1ng 1 of the 1nput.", "the number of odd elements 1n the str3ng 3 of the 3nput.", "the number of odd elements 1n the str5ng 5 of the 5nput."])

    def test_multiple_even_numbers(self):
        self.assertEqual(odd_count(['2', '4', '6']), ["the number of odd elements 0n the str0ng 0 of the 0nput.", "the number of odd elements 0n the str4ng 4 of the 4nput.", "the number of odd elements 0n the str6ng 6 of the 6nput."])

    def test_mixed_numbers(self):
        self.assertEqual(odd_count(['1', '2', '3', '4', '5']), ["the number of odd elements 1n the str1ng 1 of the 1nput.", "the number of odd elements 0n the str2ng 2 of the 2nput.", "the number of odd elements 1n the str3ng 3 of the 3nput.", "the number of odd elements 0n the str4ng 4 of the 4nput.", "the number of odd elements 1n the str5ng 5 of the 5nput."])

    def test_empty_list(self):
        self.assertEqual(odd_count([]), [])

if __name__ == '__main__':
    unittest.main()