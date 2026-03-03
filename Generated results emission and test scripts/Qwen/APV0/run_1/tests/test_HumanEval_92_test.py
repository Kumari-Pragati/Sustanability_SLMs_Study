system
You are Qwen, created by Alibaba Cloud. You are a helpful assistant.
user
Generate a unittest test script for the following Python function.
The script should fully test the function and be runnable directly.

### Output Formatting
1. Start with: import unittest
2. Include: from HumanEval_92_code import any_int
3. End with:
if __name__ == '__main__':
    unittest.main()

Function:
def any_int(x, y, z):
    '''
    Create a function that takes 3 numbers.
    Returns true if one of the numbers is equal to the sum of the other two, and all numbers are integers.
    Returns false in any other cases.
    
    Examples
    any_int(5, 2, 7) ➞ True
    any_int(3, 2, 2) ➞ False
    any_int(3, -2, 1) ➞ True
    any_int(3.6, -2.2, 2) ➞ False
    '''

    if isinstance(x, int) and isinstance(y, int) and isinstance(z, int):
        if (x + y == z) or (x + z == y) or (y + z == x):
            return True
        return False
    return False


assistant

import unittest

# Function to check if three numbers satisfy the condition
def any_int(x, y, z):
    """
    Check if one number is equal to the sum of the other two and all numbers are integers.
    """
    if isinstance(x, int) and isinstance(y, int) and isinstance(z, int):
        if (x + y == z) or (x + z == y) or (y + z == x):
            return True
        return False
    return False

class TestAnyInt(unittest.TestCase):

    def test_any_int(self):
        # Test case 1
        self.assertTrue(any_int(5, 2, 7))
        
        # Test case 2
        self.assertFalse(any_int(3, 2, 2))
        
        # Test case 3
        self.assertTrue(any_int(3, -2, 1))
        
        # Test case 4
        self.assertFalse(any_int(3.6, -2.2, 2))

    def test_invalid_input(self):
        # Test case where non-integer inputs are provided
        self.assertFalse(any_int("a", 2, 3))
        
        # Test case where only one integer input is provided
        self.assertFalse(any_int(1, "b", 3))
        
        # Test case where no integer inputs are provided
        self.assertFalse(any_int(), 2, 3)

if __name__ == '__main__':
    unittest.main()


This script defines a `unittest` test class named `TestAnyInt` which contains several test methods to verify the functionality of the `any_int` function. The tests cover various scenarios including valid inputs, invalid inputs, and edge cases.