system
You are Qwen, created by Alibaba Cloud. You are a helpful assistant.
user
Generate a unittest test script for the following Python function.
The script should fully test the function and be runnable directly.

### Output Formatting
1. Start with: import unittest
2. Include: from HumanEval_94_code import skjkasdkd
3. End with:
if __name__ == '__main__':
    unittest.main()

Function:
def skjkasdkd(lst):
    """You are given a list of integers.
    You need to find the largest prime value and return the sum of its digits.

    Examples:
    For lst = [0,3,2,1,3,5,7,4,5,5,5,2,181,32,4,32,3,2,32,324,4,3] the output should be 10
    For lst = [1,0,1,8,2,4597,2,1,3,40,1,2,1,2,4,2,5,1] the output should be 25
    For lst = [1,3,1,32,5107,34,83278,109,163,23,2323,32,30,1,9,3] the output should be 13
    For lst = [0,724,32,71,99,32,6,0,5,91,83,0,5,6] the output should be 11
    For lst = [0,81,12,3,1,21] the output should be 3
    For lst = [0,8,1,2,1,7] the output should be 7
    """

    def isPrime(n):
        for i in range(2, int(n**0.5) + 1):
            if n % i == 0:
                return False
        return True

    maxx = 0
    i = 0
    while i < len(lst):
        if lst[i] > maxx and isPrime(lst[i]):
            maxx = lst[i]
        i += 1

    result = sum(int(digit) for digit in str(maxx))
    return result


assistant

import unittest

# Function to check the correctness of the provided solution
def check_solution():
    # Test cases
    test_cases = [
        ([0, 3, 2, 1, 3, 5, 7, 4, 5, 5, 5, 2, 181, 32, 4, 32, 3, 2, 32, 324, 4, 3], 10),
        ([1, 0, 1, 8, 2, 4597, 2, 1, 3, 40, 1, 2, 1, 2, 4, 2, 5, 1], 25),
        ([1, 3, 1, 32, 5107, 34, 83278, 109, 163, 23, 2323, 32, 30, 1, 9, 3], 13),
        ([0, 724, 32, 71, 99, 32, 6, 0, 5, 91, 83, 0, 5, 6], 11),
        ([0, 81, 12, 3, 1, 21], 3),
        ([0, 8, 1, 2, 1, 7], 7)
    ]

    # Iterate through each test case and verify the results
    for inputs, expected_output in test_cases:
        assert skjkasdkd(inputs) == expected_output, f"Test failed for input {inputs}. Expected {expected_output}, got {skjkasdkd(inputs)}"
    
    print("All tests passed!")

# Run the check function to validate the solution
check_solution()


This code snippet defines a `check_solution` function that runs several test cases against the `skjkasdkd` function. If all test cases pass without any assertion errors, it prints "All tests passed!" otherwise it raises an AssertionError indicating which test case failed.