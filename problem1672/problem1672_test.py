import unittest

from problem1672.problem1672 import Solution


class TestMaximumWealth(unittest.TestCase):
    def test_empty(self):
        accounts = []
        self.assertRaises(ValueError, Solution().maximumWealth, accounts)

    def test_no_banks(self):
        accounts = [[]]
        self.assertRaises(ValueError, Solution().maximumWealth, accounts)

    def test_example_1(self):
        accounts = [[1, 2, 3], [3, 2, 1]]
        result = Solution().maximumWealth(accounts)
        expected = 6
        self.assertEqual(result, expected)

    def test_example_2(self):
        accounts = [[1, 5], [7, 3], [3, 5]]
        result = Solution().maximumWealth(accounts)
        expected = 10
        self.assertEqual(result, expected)

    def test_example_3(self):
        accounts = [[2, 8, 7], [7, 1, 3], [1, 9, 5]]
        result = Solution().maximumWealth(accounts)
        expected = 17
        self.assertEqual(result, expected)


if __name__ == "__main__":
    unittest.main()
