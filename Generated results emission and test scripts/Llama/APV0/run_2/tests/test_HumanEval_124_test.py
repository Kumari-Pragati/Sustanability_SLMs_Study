user

Generate a unittest test script for the following Python function.
The script should fully test the function and be runnable directly.

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
    return Trueassistant

Here is the unittest test script for the given Python function:

Python
import unittest
from HumanEval_124_code import valid_date

class TestValidDate(unittest.TestCase):

    def test_valid_date(self):
        self.assertTrue(valid_date('03-11-2000'))
        self.assertTrue(valid_date('06-04-2020'))
        self.assertTrue(valid_date('12-31-1999'))
        self.assertTrue(valid_date('01-01-2000'))

    def test_invalid_date(self):
        self.assertFalse(valid_date('15-01-2012'))
        self.assertFalse(valid_date('04-0-2040'))
        self.assertFalse(valid_date('13-13-2020'))
        self.assertFalse(valid_date('02-30-2020'))
        self.assertFalse(valid_date('13-05-2020'))
        self.assertFalse(valid_date('02-29-2020'))  # 2020 is not a leap year

    def test_invalid_date_format(self):
        self.assertFalse(valid_date('03/11/2000'))  # format is not '-'
        self.assertFalse(valid_date('03 11 2000'))  # format is not '-'
        self.assertFalse(valid_date('03-11'))  # year is missing
        self.assertFalse(valid_date('03-11-'))  # year is missing
        self.assertFalse(valid_date('03-11-200'))  # year is missing

    def test_empty_date(self):
        self.assertFalse(valid_date(''))  # date is empty

if __name__ == '__main__':
    unittest.main()


This script includes four test cases:

1. `test_valid_date`: Tests valid dates.
2. `test_invalid_date`: Tests invalid dates.
3. `test_invalid_date_format`: Tests dates with invalid formats.
4. `test_empty_date`: Tests an empty date.

Each test case includes several assertions to verify the expected results.