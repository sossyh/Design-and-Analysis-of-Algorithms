import unittest
from Asymptotic_Analysis import compute_sum


class TestComputeSum(unittest.TestCase):

    def test_small_case(self):
        a = [i for i in range(20)]   # a = [0, 1, 2, ..., 19]
        b = [2*i for i in range(20)] # b = [0, 2, 4, ..., 38]
        result = compute_sum(a, b, 20)
        self.assertIsInstance(result, (int, float))  # must return number

    def test_equal_lists(self):
        a = [1] * 30
        b = [1] * 30
        result = compute_sum(a, b, 30)
        self.assertGreater(result, 0)  # must accumulate something

    def test_empty_lists(self):
        a, b = [0]*30, [0]*30
        result = compute_sum(a, b, 30)
        self.assertEqual(result, 0)    # multiplying zeros = 0


if __name__ == "__main__":
    unittest.main()