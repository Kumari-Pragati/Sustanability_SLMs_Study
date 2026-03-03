user

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
    return len(ans)assistant

Here is the unittest test script for the given Python function:

Python
import unittest
from HumanEval_147_code import get_max_triples

class TestGetMaxTriples(unittest.TestCase):

    def test_get_max_triples(self):
        self.assertEqual(get_max_triples(5), 1)
        self.assertEqual(get_max_triples(10), 2)
        self.assertEqual(get_max_triples(15), 4)
        self.assertEqual(get_max_triples(20), 7)
        self.assertEqual(get_max_triples(25), 11)
        self.assertEqual(get_max_triples(30), 16)
        self.assertEqual(get_max_triples(35), 22)
        self.assertEqual(get_max_triples(40), 29)
        self.assertEqual(get_max_triples(45), 37)
        self.assertEqual(get_max_triples(50), 46)

    def test_get_max_triples_edge_cases(self):
        self.assertEqual(get_max_triples(1), 0)
        self.assertEqual(get_max_triples(2), 0)
        self.assertEqual(get_max_triples(3), 0)

if __name__ == '__main__':
    unittest.main()


This script includes two test cases: `test_get_max_triples` and `test_get_max_triples_edge_cases`. The first test case checks the function with different inputs and compares the output with the expected output. The second test case checks the function with edge cases (n = 1, 2, 3) and ensures that the function returns the expected output.