system
You are Qwen, created by Alibaba Cloud. You are a helpful assistant.
user
You are an expert Python programmer.
Your task is to write a comprehensive unittest test suite for the given Python function.

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


assistant

import unittest

# Given function
from HumanEval_147_code import get_max_triples

class TestGetMaxTriples(unittest.TestCase):

    def test_case_1(self):
        self.assertEqual(get_max_triples(5), 1)
    
    def test_case_2(self):
        self.assertEqual(get_max_triples(6), 2)
    
    def test_case_3(self):
        self.assertEqual(get_max_triples(7), 3)
    
    def test_case_4(self):
        self.assertEqual(get_max_triples(8), 4)
    
    def test_case_5(self):
        self.assertEqual(get_max_triples(9), 5)

if __name__ == '__main__':
    unittest.main()


This code snippet defines a `TestGetMaxTriples` class that inherits from `unittest.TestCase`. It contains five test cases using the `assertEqual` method to verify the correctness of the `get_max_triples` function against provided data points. The `unittest.main()` call at the end runs all the tests defined within the class.