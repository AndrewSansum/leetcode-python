import unittest

from problem1672.problem1672 import Solution


class TestMaximumWealth(unittest.TestCase):
    def test_empty(self):
        accounts = []
        self.assertRaises(ValueError, Solution().maximumWealth, accounts)
