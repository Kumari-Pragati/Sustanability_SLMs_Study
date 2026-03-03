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

 import unittest

from HumanEval_124_code import valid_date

class TestValidDate(unittest.TestCase):

    def test_valid_date_1(self):
        self.assertTrue(valid_date('03-11-2000'))

    def test_valid_date_2(self):
        self.assertFalse(valid_date('15-01-2012'))

    def test_valid_date_3(self):
        self.assertFalse(valid_date('04-0-2040'))

    def test_valid_date_4(self):
        self.assertTrue(valid_date('06-04-2020'))

    def test_valid_date_5(self):
        self.assertFalse(valid_date('06/04/2020'))

    def test_valid_date_6(self):
        self.assertFalse(valid_date('02-30-2020'))

    def test_valid_date_7(self):
        self.assertFalse(valid_date('12-31-2020'))

    def test_valid_date_8(self):
        self.assertTrue(valid_date('11-30-2020'))

    def test_valid_date_9(self):
        self.assertFalse(valid_date('02-29-2001'))

    def test_valid_date_10(self):
        self.assertTrue(valid_date('02-28-2000'))

    def test_valid_date_11(self):
        self.assertFalse(valid_date('02-29-2019'))

    def test_valid_date_12(self):
        self.assertTrue(valid_date('02-28-2016'))

    def test_valid_date_13(self):
        self.assertFalse(valid_date('02-29-2017'))

    def test_valid_date_14(self):
        self.assertTrue(valid_date('02-28-2018'))

    def test_valid_date_15(self):
        self.assertFalse(valid_date('02-29-2015'))

    def test_valid_date_16(self):
        self.assertTrue(valid_date('02-28-2014'))

    def test_valid_date_17(self):
        self.assertFalse(valid_date('02-29-2013'))

    def test_valid_date_18(self):
        self.assertTrue(valid_date('02-28-2012'))

    def test_valid_date_19(self):
        self.assertFalse(valid_date('02-29-2011'))

    def test_valid_date_20(self):
        self.assertTrue(valid_date('02-28-2010'))

    def test_valid_date_21(self):
        self.assertFalse(valid_date('02-29-2009'))

    def test_valid_date_22(self):
        self.assertTrue(valid_date('02-28-2008'))

    def test_valid_date_23(self):
        self.assertFalse(valid_date('02-29-2007'))

    def test_valid_date_24(self):
        self.assertTrue(valid_date('02-28-2006'))

    def test_valid_date_25(self):
        self.assertFalse(valid_date('02-29-2005'))

    def test_valid_date_26(self):
        self.assertTrue(valid_date('02-28-2004'))

    def test_valid_date_27(self):
        self.assertFalse(valid_date('02-29-2003'))