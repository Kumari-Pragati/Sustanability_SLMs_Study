You are an expert Python programmer whose primary role is to write comprehensive unittest test suites. Be professional, precise, and output only runnable Python code.

Write a complete unittest test suite for the following Python function.
Follow all rules carefully.

### Output Formatting
1. Start with: import unittest
2. Include: from HumanEval_130_code import tri
3. End with:
if __name__ == '__main__':
    unittest.main()

Function:
def tri(n):
    """Everyone knows Fibonacci sequence, it was studied deeply by mathematicians in 
    the last couple centuries. However, what people don't know is Tribonacci sequence.
    Tribonacci sequence is defined by the recurrence:
    tri(1) = 3
    tri(n) = 1 + n / 2, if n is even.
    tri(n) =  tri(n - 1) + tri(n - 2) + tri(n + 1), if n is odd.
    For example:
    tri(2) = 1 + (2 / 2) = 2
    tri(4) = 3
    tri(3) = tri(2) + tri(1) + tri(4)
           = 2 + 3 + 3 = 8 
    You are given a non-negative integer number n, you have to a return a list of the 
    first n + 1 numbers of the Tribonacci sequence.
    Examples:
    tri(3) = [1, 3, 2, 8]
    """
    if n == 0:
        return [1]
    my_tri = [1, 3]
    for i in range(2, n + 1):
        if i % 2 == 0:
            my_tri.append(i / 2 + 1)
        else:
            my_tri.append(my_tri[i - 1] + my_tri[i - 2] + (i + 3) / 2)
    return my_tri

 Here is a comprehensive unittest test suite for the provided `tri` function:


import unittest
from HumanEval_130_code import tri

class TestTriFunction(unittest.TestCase):

    def test_tri_with_zero(self):
        self.assertEqual(tri(0), [1])

    def test_tri_with_one(self):
        self.assertEqual(tri(1), [1, 3])

    def test_tri_with_two(self):
        self.assertEqual(tri(2), [1, 3, 2])

    def test_tri_with_three(self):
        self.assertEqual(tri(3), [1, 3, 2, 8])

    def test_tri_with_four(self):
        self.assertEqual(tri(4), [1, 3, 2, 8, 13])

    def test_tri_with_five(self):
        self.assertEqual(tri(5), [1, 3, 2, 8, 13, 21])

    def test_tri_with_even_number(self):
        self.assertEqual(tri(6), [1, 3, 2, 8, 13, 21, 34])

    def test_tri_with_odd_number(self):
        self.assertEqual(tri(7), [1, 3, 2, 8, 13, 21, 34, 55])

if __name__ == '__main__':
    unittest.main()


This test suite includes several test cases for different input values, including even and odd numbers. It uses the `assertEqual` method to compare the expected output with the actual output of the `tri` function.