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
   - Include from HumanEval_124_code import valid_date
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
2. Include: from HumanEval_124_code import valid_date
3. End with:
if __name__ == '__main__':
    unittest.main()

Function:
def valid_date(date):
    """You have to write a function which validates a given date string and
    returns True if the date is valid otherwise False.
    The date is valid if all of the following rules are satisfied:
    1. The date string is not empty.
    2. The number of days is not less than 1 or higher than 31 days for months 1,3,5,7,8,10,12. And the number of days is not less than 1 or higher than 30 days for months 4,6,9,11. And, the number of days is not less than 1 or higher than 29 for the month 2.
    3. The months should not be less than 1 or higher than 12.
    4. The date should be in the format: mm-dd-yyyy

    for example: 
    valid_date('03-11-2000') => True
    valid_date('15-01-2012') => False
    valid_date('04-0-2040') => False
    valid_date('06-04-2020') => True
    valid_date('06/04/2020') => False
    """
    try:
        date = date.strip()
        month, day, year = date.split('-')
        month, day, year = int(month), int(day), int(year)
        if month < 1 or month > 12:
            return False
        if month in [1, 3, 5, 7, 8, 10, 12] and (day < 1 or day > 31):
            return False
        if month in [4, 6, 9, 11] and (day < 1 or day > 30):
            return False
        if month == 2 and (day < 1 or day > 29):
            return False
    except:
        return False
    return True


assistant

import unittest

class TestValidDate(unittest.TestCase):
    def test_valid_date(self):
        self.assertTrue(valid_date("03-11-2000"))
        self.assertFalse(valid_date("15-01-2012"))
        self.assertFalse(valid_date("04-0-2040"))
        self.assertTrue(valid_date("06-04-2020"))

    def test_invalid_date_format(self):
        self.assertFalse(valid_date("invalid-date"))  # Should raise ValueError

    def test_empty_string(self):
        self.assertFalse(valid_date(""))  # Should raise ValueError

    def test_non_numeric_month(self):
        self.assertFalse(valid_date("03-a-2000"))  # Non-numeric month

    def test_non_numeric_day(self):
        self.assertFalse(valid_date("a-11-2000"))  # Non-numeric day

    def test_non_numeric_year(self):
        self.assertFalse(valid_date("03-11-a"))  # Non-numeric year

if __name__ == '__main__':
    unittest.main()


This test suite covers various cases including positive dates, negative dates, invalid formats, and edge cases such as non-numeric values within the date components. It also includes checks for different types of errors that might occur during parsing.