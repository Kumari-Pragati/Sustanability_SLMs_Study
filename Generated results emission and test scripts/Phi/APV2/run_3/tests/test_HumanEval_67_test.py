You are an expert Python programmer whose primary role is to write comprehensive unittest test suites. Be professional, precise, and output only runnable Python code. Write a complete unittest test suite for the following Python function.
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

 import unittest
from HumanEval_67_code import fruit_distribution

class TestFruitDistribution(unittest.TestCase):

    def test_fruit_distribution_apples_oranges(self):
        self.assertEqual(fruit_distribution("5 apples and 6 oranges", 19), 8)

    def test_fruit_distribution_zero_apples_oranges(self):
        self.assertEqual(fruit_distribution("0 apples and 1 oranges", 3), 2)

    def test_fruit_distribution_large_numbers(self):
        self.assertEqual(fruit_distribution("2 apples and 3 oranges", 100), 95)

    def test_fruit_distribution_large_numbers_with_apples(self):
        self.assertEqual(fruit_distribution("100 apples and 1 oranges", 120), 19)

    def test_fruit_distribution_empty_string(self):
        self.assertEqual(fruit_distribution("", 10), 10)

    def test_fruit_distribution_negative_numbers(self):
        self.assertEqual(fruit_distribution("-5 apples and 6 oranges", 19), 14)

    def test_fruit_distribution_no_apples_or_oranges(self):
        self.assertEqual(fruit_distribution("10 apples and 0 oranges", 10), 10)

    def test_fruit_distribution_only_apples(self):
        self.assertEqual(fruit_distribution("10 apples", 10), 0)

    def test_fruit_distribution_only_oranges(self):
        self.assertEqual(fruit_distribution("6 oranges", 6), 0)

    def test_fruit_distribution_no_numbers(self):
        self.assertEqual(fruit_distribution("apples and oranges", 10), 10)

if __name__ == '__main__':
    unittest.main()