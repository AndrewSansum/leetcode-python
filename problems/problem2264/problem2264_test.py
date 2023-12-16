import unittest

from problem2264 import Solution


class Test2264Solution(unittest.TestCase):
    def test_example1(self):
        num = "6777133339"
        self.assertEqual(Solution().largestGoodInteger(num), "777")

    def test_example2(self):
        num = "2300019"
        self.assertEqual(Solution().largestGoodInteger(num), "000")

    def test_example3(self):
        num = "42352338"
        self.assertEqual(Solution().largestGoodInteger(num), "")


if __name__ == "__main__":
    unittest.main()
