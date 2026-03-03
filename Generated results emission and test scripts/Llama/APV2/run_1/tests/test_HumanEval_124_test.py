system

You are an expert Python programmer whose primary role is to write comprehensive unittest test suites. Be professional, precise, and output only runnable Python code.user

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
    return Trueassistant

Here is the complete unittest test suite for the given Python function:


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
        self.assertFalse(valid_date('13-12-1999'))
        self.assertFalse(valid_date('02-30-2000'))
        self.assertFalse(valid_date('02-29-2001'))  # 2001 is not a leap year
        self.assertFalse(valid_date('02-29-2000'))  # 2000 is a leap year
        self.assertFalse(valid_date('02-30-2000'))  # 2000 is a leap year
        self.assertFalse(valid_date('02-29-1999'))  # 1999 is not a leap year
        self.assertFalse(valid_date('02-30-1999'))  # 1999 is not a leap year
        self.assertFalse(valid_date('02-29-1998'))  # 1998 is not a leap year
        self.assertFalse(valid_date('02-30-1998'))  # 1998 is not a leap year
        self.assertFalse(valid_date('02-29-1997'))  # 1997 is not a leap year
        self.assertFalse(valid_date('02-30-1997'))  # 1997 is not a leap year
        self.assertFalse(valid_date('02-29-1996'))  # 1996 is a leap year
        self.assertFalse(valid_date('02-30-1996'))  # 1996 is a leap year
        self.assertFalse(valid_date('02-29-1995'))  # 1995 is not a leap year
        self.assertFalse(valid_date('02-30-1995'))  # 1995 is not a leap year
        self.assertFalse(valid_date('02-29-1994'))  # 1994 is not a leap year
        self.assertFalse(valid_date('02-30-1994'))  # 1994 is not a leap year
        self.assertFalse(valid_date('02-29-1993'))  # 1993 is not a leap year
        self.assertFalse(valid_date('02-30-1993'))  # 1993 is not a leap year
        self.assertFalse(valid_date('02-29-1992'))  # 1992 is a leap year
        self.assertFalse(valid_date('02-30-1992'))  # 1992 is a leap year
        self.assertFalse(valid_date('02-29-1991'))  # 1991 is not a leap year
        self.assertFalse(valid_date('02-30-1991'))  # 1991 is not a leap year
        self.assertFalse(valid_date('02-29-1990'))  # 1990 is a leap year
        self.assertFalse(valid_date('02-30-1990'))  # 1990 is a leap year
        self.assertFalse(valid_date('02-29-1989'))  # 1989 is not a leap year
        self.assertFalse(valid_date('02-30-1989'))  # 1989 is not a leap year
        self.assertFalse(valid_date('02-29-1988'))  # 1988 is a leap year
        self.assertFalse(valid_date('02-30-1988'))  # 1988 is a leap year
        self.assertFalse(valid_date('02-29-1987'))  # 1987 is not a leap year
        self.assertFalse(valid_date('02-30-1987'))  # 1987 is not a leap year
        self.assertFalse(valid_date('02-29-1986'))  # 1986 is a leap year
        self.assertFalse(valid_date('02-30-1986'))  # 1986 is a leap year
        self.assertFalse(valid_date('02-29-1985'))  # 1985 is not a leap year
        self.assertFalse(valid_date('02-30-1985'))  # 1985 is not a leap year
        self.assertFalse(valid_date('02-29-1984'))  # 1984 is a leap year
        self.assertFalse(valid_date('02-30-1984'))  # 1984 is a leap year
        self.assertFalse(valid_date('02-29-1983'))  # 1983 is not a leap year
        self.assertFalse(valid_date('02-30-1983'))  # 1983 is not