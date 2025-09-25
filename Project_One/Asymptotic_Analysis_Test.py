import unittest
import random
import time
from Asymptotic_Analysis import compute_sum
import math

class TestComputeSum(unittest.TestCase):

    def setUp(self):
        # List of n values to test
        self.test_n_values = [
    1000, 5000, 25000, 125000, 625000, 3125000, 15625000, 78125000
]

    def generate_random_list(self, n):
        return [random.randint(1, 100) for _ in range(n)]

    def run_and_time(self, n, repeat=1000):
        a = self.generate_random_list(n)
        b = self.generate_random_list(n)
        start = time.perf_counter()
        for _ in range(repeat):
            result = compute_sum(a, b, n)
        end = time.perf_counter()
        elapsed = (end - start) / repeat
        print(f"n={n:>8}, result={result:>12}, time={elapsed:.8f} seconds")


    def test_various_sizes(self):
        print("\nRunning compute_sum for different n values (with scaling):")
        for n in self.test_n_values:
            self.run_and_time(n)

    def test_correctness_large_arrays(self):
        # Use large enough arrays so loops execute
        n = 20
        a = [1] * n
        b = [1] * n
        result = compute_sum(a, b, n)
        self.assertGreater(result, 0)

        a = [0] * n
        b = [0] * n
        result = compute_sum(a, b, n)
        self.assertEqual(result, 0)

if __name__ == "__main__":
    unittest.main()
