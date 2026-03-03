You are an expert Python programmer whose primary role is to write comprehensive unittest test suites. Be professional, precise, and output only runnable Python code.### Instruction:
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


### Response:
Here is a complete unittest test suite for the given function:


import unittest
from HumanEval_130_code import tri

class TestTri(unittest.TestCase):
    def test_tri_zero(self):
        self.assertEqual(tri(0), [1])

    def test_tri_one(self):
        self.assertEqual(tri(1), [1, 3])

    def test_tri_two(self):
        self.assertEqual(tri(2), [1, 3, 2, 2.5])

    def test_tri_three(self):
        self.assertEqual(tri(3), [1, 3, 2, 8])

    def test_tri_negative(self):
        with self.assertRaises(IndexError):
            tri(-1)

    def test_tri_non_integer(self):
        with self.assertRaises(TypeError):
            tri(1.5)

    def test_tri_large_number(self):
        with self.assertRaises(RecursionError):
            tri(1000)

if __name__ == '__main__':
    unittest.main()


This test suite includes tests for the function with different inputs, including the base cases (0, 1, 2, and 3), as well as tests for negative numbers, non-integers, and large numbers. The test for large numbers checks for a common issue with recursive functions: a large input can cause a stack overflow, resulting in a RecursionError.

Please note that the actual behavior of the function may vary depending on the specific implementation and the programming language used. The above tests are based on the provided Python function description.

Also, please note that the function `tri(3)` should return `[1, 3, 2, 8]` according to the provided description, but the actual output of the function is `[1, 3, 2, 8.5]` because of the way the last element is calculated. The description might be a bit misleading, as the function is not defined for even numbers greater than 2.