You are an expert Python programmer whose primary role is to write comprehensive unittest test suites. Be professional, precise, and output only runnable Python code. Write a complete unittest test suite for the following Python function.
Follow all rules carefully.

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

 import unittest
from HumanEval_147_code import get_max_triples

class TestGetMaxTriples(unittest.TestCase):

    def test_get_max_triples_empty_input(self):
        self.assertEqual(get_max_triples(0), 0)

    def test_get_max_triples_single_element(self):
        self.assertEqual(get_max_triples(1), 0)

    def test_get_max_triples_multiple_elements(self):
        self.assertEqual(get_max_triples(5), 1)
        self.assertEqual(get_max_triples(10), 2)
        self.assertEqual(get_max_triples(15), 3)

    def test_get_max_triples_large_input(self):
        self.assertEqual(get_max_triples(100), 10)

    def test_get_max_triples_edge_case(self):
        self.assertEqual(get_max_triples(1), 0)
        self.assertEqual(get_max_triples(2), 0)

if __name__ == '__main__':
    unittest.main()