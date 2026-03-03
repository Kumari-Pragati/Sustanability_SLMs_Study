system
You are an expert Python programmer whose primary role is to write comprehensive unittest test suites. Be professional, precise, and output only runnable Python code.
user
Write a complete unittest test suite for the following Python function.
Follow all rules carefully.

### Output Formatting
1. Start with: import unittest
2. Include: from HumanEval_73_code import smallest_change
3. End with:
if __name__ == '__main__':
    unittest.main()

Function:
def smallest_change(arr):
    """
    Given an array arr of integers, find the minimum number of elements that
    need to be changed to make the array palindromic. A palindromic array is an array that
    is read the same backwards and forwards. In one change, you can change one element to any other element.

    For example:
        smallest_change([1, 2, 3, 5, 4, 7, 9, 6]) == 4
        smallest_change([1, 2, 3, 4, 3, 2, 2]) == 1
        smallest_change([1, 2, 3, 2, 1]) == 0
    """
    ans = 0
    for i in range(len(arr) // 2):
        if arr[i] != arr[len(arr) - i - 1]:
            ans += 1
    return ans


assistant

import unittest

# Function to check the correctness of the smallest_change function
def smallest_change_test():
    # Test cases
    test_cases = [
        ([1, 2, 3, 5, 4, 7, 9, 6], 4),
        ([1, 2, 3, 4, 3, 2, 2], 1),
        ([1, 2, 3, 2, 1], 0)
    ]
    
    # Iterate through each test case
    for input_arr, expected_output in test_cases:
        assert smallest_change(input_arr) == expected_output, f"Test failed for input {input_arr}. Expected {expected_output}, got {smallest_change(input_arr)}"
        
    print("All tests passed!")

class SmallestChangeTests(unittest.TestCase):
    def test_smallest_change(self):
        smallest_change_test()

if __name__ == '__main__':
    unittest.main()


This solution includes a `unittest` test suite that verifies the correctness of the `smallest_change` function against predefined test cases. The `test_smallest_change` method calls the `smallest_change` function with different inputs and compares its output against the expected results using assertions. If all tests pass, it prints "All tests passed!" to indicate successful execution.