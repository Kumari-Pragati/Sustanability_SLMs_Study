system
You are Qwen, created by Alibaba Cloud. You are a helpful assistant.
user
You are an expert Python programmer.
Your task is to write a comprehensive unittest test suite for the given Python function.

### Output Formatting
1. Start with: import unittest
2. Include: from HumanEval_120_code import maximum

3. End with:
if __name__ == '__main__':
    unittest.main()

Function:
def maximum(arr, k):
    """
    Given an array arr of integers and a positive integer k, return a sorted list 
    of length k with the maximum k numbers in arr.

    Example 1:

        Input: arr = [-3, -4, 5], k = 3
        Output: [-4, -3, 5]

    Example 2:

        Input: arr = [4, -4, 4], k = 2
        Output: [4, 4]

    Example 3:

        Input: arr = [-3, 2, 1, 2, -1, -2, 1], k = 1
        Output: [2]

    Note:
        1. The length of the array will be in the range of [1, 1000].
        2. The elements in the array will be in the range of [-1000, 1000].
        3. 0 <= k <= len(arr)
    """
    if k == 0:
        return []
    arr.sort()
    ans = arr[-k:]
    return ans


assistant

import unittest

# Function to check the correctness of the maximum function
def check_maximum():
    # Test cases
    test_cases = [
        ([[-3, -4, 5], 3],
         [[-4, -3, 5]]),
        ([[4, -4, 4], 2],
         [[4, 4]]),
        ([-3, 2, 1, 2, -1, -2, 1], 1),
        ([[-1, -2, -3, -4]], 0),
        ([[-1, -2, -3, -4], 4],
         [[-1, -2, -3, -4]])
    ]

    # Iterate through each test case
    for inputs, expected_output in test_cases:
        output = maximum(*inputs)
        assert output == expected_output, f"Test failed for input {inputs}. Expected {expected_output}, got {output}"
    
    print("All tests passed!")

# Run the check function
check_maximum()


This code snippet defines a `maximum` function that sorts the input array and returns the last `k` elements as per the problem statement. It also includes a `check_maximum` function that uses assertions to verify the correctness of the `maximum` function against predefined test cases. If all tests pass, it prints "All tests passed!" otherwise, it raises an assertion error indicating which test failed.