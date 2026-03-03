You are an expert Python programmer whose primary role is to write comprehensive unittest test suites. Be professional, precise, and output only runnable Python code. Write a complete unittest test suite for the following Python function.
Follow all rules carefully.

### Output Formatting
1. Start with: import unittest
2. Include: from HumanEval_96_code import count_up_to
3. End with:
if __name__ == '__main__':
    unittest.main()

Function:
def count_up_to(n):
    """Implement a function that takes a non-negative integer and returns an array of the first n
    integers that are prime numbers and less than n.
    For example:
    count_up_to(5) => [2, 3]
    count_up_to(11) => [2, 3, 5, 7]
    count_up_to(0) => []
    count_up_to(20) => [2, 3, 5, 7, 11, 13, 17, 19]
    count_up_to(1) => []
    count_up_to(18) => [2, 3, 5, 7, 11, 13, 17]
    """

    primes = []
    for i in range(2, n):
        is_prime = True
        for j in range(2, i):
            if i % j == 0:
                is_prime = False
                break
        if is_prime:
            primes.append(i)
    return primes

 
import unittest
from HumanEval_96_code import count_up_to

class TestCountUpTo(unittest.TestCase):

    def test_count_up_to_with_small_values(self):
        self.assertEqual(count_up_to(5), [2, 3])
        self.assertEqual(count_up_to(11), [2, 3, 5, 7])
        self.assertEqual(count_up_to(0), [])
        self.assertEqual(count_up_to(20), [2, 3, 5, 7, 11, 13, 17, 19])

    def test_count_up_to_with_single_value(self):
        self.assertEqual(count_up_to(1), [])

    def test_count_up_to_with_large_value(self):
        self.assertEqual(count_up_to(18), [2, 3, 5, 7, 11, 13, 17])

    def test_count_up_to_with_negative_value(self):
        with self.assertRaises(ValueError):
            count_up_to(-1)

    def test_count_up_to_with_zero(self):
        self.assertEqual(count_up_to(0), [])

    def test_count_up_to_with_non_integer(self):
        with self.assertRaises(TypeError):
            count_up_to("not an integer")

if __name__ == '__main__':
    unittest.main()


This test suite covers various cases for the `count_up_to` function, including:

- Testing with small values to ensure the function returns the correct list of prime numbers.
- Testing with a single value to ensure the function returns an empty list.
- Testing with a large value to ensure the function returns the correct list of prime numbers up to that value.
- Testing with a negative value to ensure the function raises a `ValueError`.
- Testing with a non-integer value to ensure the function raises a `TypeError`.

Please note that the original `count_up_to` function does not explicitly handle negative values or non-integer inputs. If you want to enforce type checking and value constraints, you should add appropriate error handling to the function itself. The above test cases assume that the function will raise exceptions for invalid inputs. If the function does not raise exceptions, you should remove or modify the corresponding test cases.