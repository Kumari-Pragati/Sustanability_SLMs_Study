You are an expert Python programmer whose primary role is to write comprehensive unittest test suites. Be professional, precise, and output only runnable Python code.

Write a complete unittest test suite for the following Python function.
Follow all rules carefully.

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

 Here is a comprehensive unittest test suite for the `valid_date` function:


import unittest
from HumanEval_124_code import valid_date

class TestValidDate(unittest.TestCase):

    def test_empty_string(self):
        self.assertFalse(valid_date(''))

    def test_invalid_format(self):
        self.assertFalse(valid_date('06/04/2020'))
        self.assertFalse(valid_date('06-04-2020'))
        self.assertFalse(valid_date('06-04-2020T12:34:56'))
        self.assertFalse(valid_date('06-04-2020Z'))

    def test_invalid_month(self):
        self.assertFalse(valid_date('00-11-2020'))
        self.assertFalse(valid_date('13-11-2020'))
        self.assertFalse(valid_date('01-00-2020'))
        self.assertFalse(valid_date('01-13-2020'))

    def test_invalid_day_for_month(self):
        self.assertFalse(valid_date('02-30-2020'))
        self.assertFalse(valid_date('02-29-2019'))
        self.assertFalse(valid_date('02-31-2020'))
        self.assertFalse(valid_date('04-31-2020'))
        self.assertFalse(valid_date('06-31-2020'))
        self.assertFalse(valid_date('12-32-2020'))

    def test_valid_dates(self):
        self.assertTrue(valid_date('03-11-2000'))
        self.assertTrue(valid_date('06-04-2020'))
        self.assertTrue(valid_date('12-31-2020'))
        self.assertTrue(valid_date('01-31-2020'))  # Leap year

if __name__ == '__main__':
    unittest.main()


This test suite includes various test cases to cover different scenarios such as an empty string, invalid date formats, invalid months, invalid days for a given month, and valid dates. It uses the `unittest.TestCase.assertFalse()` and `unittest.TestCase.assertTrue()` methods to verify the expected results.