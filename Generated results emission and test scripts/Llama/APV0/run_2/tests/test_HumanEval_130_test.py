user

Generate a unittest test script for the following Python function.
The script should fully test the function and be runnable directly.

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
    return my_triassistant

Here is the unittest test script for the given Python function:

Python
import unittest
from HumanEval_130_code import tri

class TestTri(unittest.TestCase):

    def test_tri_0(self):
        self.assertEqual(tri(0), [1])

    def test_tri_1(self):
        self.assertEqual(tri(1), [1, 3])

    def test_tri_2(self):
        self.assertEqual(tri(2), [1, 3, 2])

    def test_tri_3(self):
        self.assertEqual(tri(3), [1, 3, 2, 8])

    def test_tri_4(self):
        self.assertEqual(tri(4), [1, 3, 2, 8, 11])

    def test_tri_5(self):
        self.assertEqual(tri(5), [1, 3, 2, 8, 11, 24])

    def test_tri_6(self):
        self.assertEqual(tri(6), [1, 3, 2, 8, 11, 24, 44])

    def test_tri_7(self):
        self.assertEqual(tri(7), [1, 3, 2, 8, 11, 24, 44, 81])

    def test_tri_8(self):
        self.assertEqual(tri(8), [1, 3, 2, 8, 11, 24, 44, 81, 149])

    def test_tri_9(self):
        self.assertEqual(tri(9), [1, 3, 2, 8, 11, 24, 44, 81, 149, 264])

    def test_tri_10(self):
        self.assertEqual(tri(10), [1, 3, 2, 8, 11, 24, 44, 81, 149, 264, 463])

    def test_tri_negative(self):
        with self.assertRaises(ValueError):
            tri(-1)

    def test_tri_non_integer(self):
        with self.assertRaises(TypeError):
            tri(1.5)

if __name__ == '__main__':
    unittest.main()


This script includes 11 test cases to cover different scenarios, including edge cases and normal cases. It also includes two error handling test cases to test the function's behavior when given a negative number or a non-integer number.