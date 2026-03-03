system
You are Qwen, created by Alibaba Cloud. You are a helpful assistant.
user
Generate a unittest test script for the following Python function.
The script should fully test the function and be runnable directly.

### Output Formatting
1. Start with: import unittest
2. Include: from HumanEval_155_code import even_odd_count
3. End with:
if __name__ == '__main__':
    unittest.main()

Function:
def even_odd_count(num):
    """Given an integer. return a tuple that has the number of even and odd digits respectively.

     Example:
        even_odd_count(-12) ==> (1, 1)
        even_odd_count(123) ==> (1, 2)
    """
    even_count = 0
    odd_count = 0
    for i in str(abs(num)):
        if int(i) % 2 == 0:
            even_count += 1
        else:
            odd_count += 1
    return (even_count, odd_count)


assistant

import unittest

# Function to be tested
from HumanEval_155_code import even_odd_count

class TestEvenOddCount(unittest.TestCase):

    def test_even_odd_count(self):
        # Test case 1: Negative number
        self.assertEqual(even_odd_count(-12), (1, 1))
        
        # Test case 2: Positive number
        self.assertEqual(even_odd_count(123), (1, 2))

        # Test case 3: Zero
        self.assertEqual(even_odd_count(0), (1, 0))

        # Test case 4: Single digit negative number
        self.assertEqual(even_odd_count(-7), (0, 1))

        # Test case 5: Single digit positive number
        self.assertEqual(even_odd_count(9), (1, 0))

        # Test case 6: Multiple digits number
        self.assertEqual(even_odd_count(12345), (3, 2))

        # Test case 7: Large number
        self.assertEqual(even_odd_count(9876543210), (5, 4))

        # Test case 8: Edge cases
        self.assertEqual(even_odd_count(0), (1, 0))  # Edge case where input is zero
        self.assertEqual(even_odd_count(-1), (0, 1))  # Edge case where input is negative one

if __name__ == '__main__':
    unittest.main()


This script imports `unittest` module and defines a class `TestEvenOddCount` which inherits from `unittest.TestCase`. It contains several test methods (`test_*`) to verify the correctness of the `even_odd_count` function using assertEqual method. The `assertEqual` method checks whether the output of the function matches the expected result. Finally, it calls `unittest.main()` to run all tests when the script is executed directly.