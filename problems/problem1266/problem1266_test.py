import unittest

from problem1266 import Solution


class Test1266Solution(unittest.TestCase):
    def test_example1(self):
        points = [[1, 1], [3, 4], [-1, 0]]
        self.assertEqual(Solution().minTimeToVisitAllPoints(points), 6)

    def test_example2(self):
        points = [[3, 2], [-2, 2]]
        self.assertEqual(Solution().minTimeToVisitAllPoints(points), 5)


if __name__ == "__main__":
    unittest.main()
