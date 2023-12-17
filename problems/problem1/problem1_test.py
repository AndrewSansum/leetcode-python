import unittest

from problem1 import Solution


class Test1Solution(unittest.TestCase):
    def test_example1(self):
        nums = [2, 7, 11, 15]
        target = 9
        self.assertSetEqual(set(Solution().twoSum(nums, target)), set([0, 1]))

    def test_example2(self):
        nums = [3, 2, 4]
        target = 6
        self.assertSetEqual(set(Solution().twoSum(nums, target)), set([1, 2]))

    def test_example3(self):
        nums = [3, 3]
        target = 6
        self.assertSetEqual(set(Solution().twoSum(nums, target)), set([0, 1]))


if __name__ == "__main__":
    unittest.main()
