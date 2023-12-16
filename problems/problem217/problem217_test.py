import unittest

from problem217 import Solution


class Test217Solution(unittest.TestCase):
    def test_example1(self):
        nums = [1, 2, 3, 1]
        self.assertTrue(Solution().containsDuplicate(nums))

    def test_example2(self):
        nums = [1, 2, 3, 4]
        self.assertFalse(Solution().containsDuplicate(nums))

    def test_example3(self):
        nums = [1, 1, 1, 3, 3, 4, 3, 2, 4, 2]
        self.assertTrue(Solution().containsDuplicate(nums))


if __name__ == "__main__":
    unittest.main()
