You are an expert Python programmer.
Your task is to write a comprehensive unittest test suite for the given Python function.

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

 Here is a comprehensive unittest test suite for the given Python function `tri`. The test suite includes a variety of test cases to ensure the function works correctly for different inputs.


import unittest
from HumanEval_130_code import tri

class TestTriFunction(unittest.TestCase):
    def test_tri_with_single_input(self):
        self.assertEqual(tri(3), [1, 3, 2, 8])
        self.assertEqual(tri(4), [1, 3, 2, 8, 13])
        self.assertEqual(tri(5), [1, 3, 2, 8, 13, 21, 31])
        self.assertEqual(tri(6), [1, 3, 2, 8, 13, 21, 31, 55])
        self.assertEqual(tri(7), [1, 3, 2, 8, 13, 21, 31, 55, 96])
        self.assertEqual(tri(8), [1, 3, 2, 8, 13, 21, 31, 55, 96, 169])
        self.assertEqual(tri(9), [1, 3, 2, 8, 13, 21, 31, 55, 96, 169, 297])
        self.assertEqual(tri(10), [1, 3, 2, 8, 13, 21, 31, 55, 96, 169, 297, 514])

    def test_tri_with_zero(self):
        self.assertEqual(tri(0), [1])

    def test_tri_with_negative_input(self):
        with self.assertRaises(ValueError):
            tri(-1)

    def test_tri_with_large_input(self):
        self.assertEqual(tri(1000), [1, 3, 2, 8, 13, 21, 31, 55, 96, 169, 297, 514, 895, 1597, 2882, 5165, 9319, 17016, 31181, 57028, 102759, 189510, 341859, 632458, 1166409, 2189229, 4052736, 7577853, 14073341, 26791423, 50752708, 96704559, 186555305, 350066606, 673197505, 1293838231, 2463609384, 4787396071, 9185865396, 17978365277, 35937383605, 71873097017, 139512268033, 275510664068, 546102440861, 1082667440983, 2149534772365, 4265389440380, 8510640680769, 17010384457639, 34020638310480, 68053144608121, 136206938121664, 272413869043329, 544827738086658, 10896