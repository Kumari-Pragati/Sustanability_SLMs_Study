You are an expert Python programmer whose primary role is to write comprehensive unittest test suites. Be professional, precise, and output only runnable Python code.### Instruction:
Write a complete unittest test suite for the following Python function.
Follow all rules carefully.

### Output Formatting
1. Start with: import unittest
2. Include: from HumanEval_67_code import fruit_distribution
3. End with:
if __name__ == '__main__':
    unittest.main()

Function:
def fruit_distribution(s, n):
    """
    In this task, you will be given a string that represents a number of apples and oranges 
    that are distributed in a basket of fruit. This basket contains 
    apples, oranges, and mango fruits. Given the string that represents the total number of 
    the oranges and apples and an integer that represents the total number of the fruits 
    in the basket, return the number of the mango fruits in the basket.
    
    For example:
    fruit_distribution("5 apples and 6 oranges", 19) -> 19 - 5 - 6 = 8
    fruit_distribution("0 apples and 1 oranges", 3) -> 3 - 0 - 1 = 2
    fruit_distribution("2 apples and 3 oranges", 100) -> 100 - 2 - 3 = 95
    fruit_distribution("100 apples and 1 oranges", 120) -> 120 - 100 - 1 = 19
    """
    lis = []
    for i in s.split(' '):
        if i.isdigit():
            lis.append(int(i))
    return n - sum(lis)


### Response:
Here is a complete unittest test suite for the given Python function:


import unittest
from HumanEval_67_code import fruit_distribution

class TestFruitDistribution(unittest.TestCase):

    def test_with_apples_and_oranges(self):
        self.assertEqual(fruit_distribution("5 apples and 6 oranges", 19), 8)
        self.assertEqual(fruit_distribution("0 apples and 1 oranges", 3), 2)
        self.assertEqual(fruit_distribution("2 apples and 3 oranges", 100), 95)
        self.assertEqual(fruit_distribution("100 apples and 1 oranges", 120), 19)

    def test_with_only_apples(self):
        self.assertEqual(fruit_distribution("100 apples and 0 oranges", 100), 0)

    def test_with_only_oranges(self):
        self.assertEqual(fruit_distribution("0 apples and 100 oranges", 100), 0)

    def test_with_no_fruits(self):
        self.assertEqual(fruit_distribution("0 apples and 0 oranges", 0), 0)

    def test_with_negative_values(self):
        self.assertEqual(fruit_distribution("-5 apples and -6 oranges", -19), -8)

    def test_with_large_values(self):
        self.assertEqual(fruit_distribution("1000000 apples and 1000000 oranges", 2000000), 0)

if __name__ == '__main__':
    unittest.main()


This test suite includes a variety of test cases to ensure that the function is working correctly under a variety of conditions. It tests with both apples and oranges, with only apples, only oranges, no fruits, negative values, and large values.