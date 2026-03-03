You are an expert Python programmer.
Your task is to write a comprehensive unittest test suite for the given Python function.

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

    def test_valid_date_format(self):
        self.assertTrue(valid_date('03-11-2000'))
        self.assertFalse(valid_date('15-01-2012'))
        self.assertFalse(valid_date('04-0-2040'))
        self.assertTrue(valid_date('06-04-2020'))
        self.assertFalse(valid_date('06/04/2020'))

    def test_empty_string(self):
        self.assertFalse(valid_date(''))

    def test_invalid_month(self):
        self.assertFalse(valid_date('00-11-2000'))
        self.assertFalse(valid_date('13-11-2000'))
        self.assertFalse(valid_date('12-35-2000'))

    def test_invalid_day(self):
        self.assertFalse(valid_date('03-0-2000'))
        self.assertFalse(valid_date('03-32-2000'))
        self.assertFalse(valid_date('03-29-2000'))

    def test_invalid_year(self):
        self.assertFalse(valid_date('03-11-20000'))
        self.assertFalse(valid_date('03-11--2000'))

    def test_valid_date_with_leading_zeros(self):
        self.assertTrue(valid_date('03-11-2000'))
        self.assertTrue(valid_date('02-29-2000'))

    def test_invalid_date_with_leading_zeros(self):
        self.assertFalse(valid_date('003-11-2000'))
        self.assertFalse(valid_date('03-11-0000'))

if __name__ == '__main__':
    unittest.main()


This test suite covers various scenarios to ensure the `valid_date` function works as expected. It includes tests for valid dates, invalid dates, empty strings, invalid month, invalid day, and invalid year. It also tests dates with leading zeros to ensure they are still considered valid. The `unittest` framework will run these tests and report any failures, helping to identify issues with the `valid_date` function.