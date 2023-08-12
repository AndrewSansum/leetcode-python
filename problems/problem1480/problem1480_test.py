import unittest
from problem1480 import Solution


class TestRunningSum(unittest.TestCase):
    def test_base_case(self):
        nums = [3, 1, 2, 10, 1]
        sol = Solution()
        result = sol.runningSum(nums)
        expected = [3, 4, 6, 16, 17]
        self.assertEqual(result, expected)

    def test_empty(self):
        nums = []
        sol = Solution()
        self.assertRaises(ValueError, sol.runningSum, nums)

    def test_negative_values(self):
        sol = Solution()

        nums = [-1, -2, -3]

        result = sol.runningSum(nums)
        expected = [-1, -3, -6]

        self.assertEqual(result, expected)


if __name__ == "__main__":
    unittest.main()
