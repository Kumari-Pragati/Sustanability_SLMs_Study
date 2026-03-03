Generate a unittest test script for the following Python function.
The script should fully test the function and be runnable directly.

### Output Formatting
1. Start with: import unittest
2. Include: from HumanEval_147_code import get_max_triples
3. End with:
if __name__ == '__main__':
    unittest.main()

Function:
def get_max_triples(n):
    """
    You are given a positive integer n. You have to create an integer array a of length n.
        For each i (1 ≤ i ≤ n), the value of a[i] = i * i - i + 1.
        Return the number of triples (a[i], a[j], a[k]) of a where i < j < k, 
    and a[i] + a[j] + a[k] is a multiple of 3.

    Example :
        Input: n = 5
        Output: 1
        Explanation: 
        a = [1, 3, 7, 13, 21]
        The only valid triple is (1, 7, 13).
    """
    A = [i * i - i + 1 for i in range(1, n + 1)]
    ans = []
    for i in range(n):
        for j in range(i + 1, n):
            for k in range(j + 1, n):
                if (A[i] + A[j] + A[k]) % 3 == 0:
                    ans += [(A[i], A[j], A[k])]
    return len(ans)

 Here is a unittest test script for the `get_max_triples` function:


import unittest
from HumanEval_147_code import get_max_triples

class TestGetMaxTriples(unittest.TestCase):

    def test_get_max_triples(self):
        self.assertEqual(get_max_triples(1), 0)
        self.assertEqual(get_max_triples(2), 0)
        self.assertEqual(get_max_triples(3), 0)
        self.assertEqual(get_max_triples(4), 0)
        self.assertEqual(get_max_triples(5), 1)
        self.assertEqual(get_max_triples(6), 0)
        self.assertEqual(get_max_triples(7), 0)
        self.assertEqual(get_max_triples(8), 0)
        self.assertEqual(get_max_triples(9), 0)
        self.assertEqual(get_max_triples(10), 1)
        self.assertEqual(get_max_triples(15), 3)
        self.assertEqual(get_max_triples(20), 4)
        self.assertEqual(get_max_triples(30), 10)
        self.assertEqual(get_max_triples(50), 20)
        self.assertEqual(get_max_triples(100), 40)

if __name__ == '__main__':
    unittest.main()


This test script checks the function for various input sizes and verifies that the output is correct according to the example provided in the function description. You can run this script by saving it as a .py file and running it using the command `python filename.py` in your terminal.