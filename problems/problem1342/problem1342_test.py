import unittest

from problem1342 import Solution


class TestStepCounter(unittest.TestCase):
    def test_valid_n(self):
        n = -1
        self.assertRaises(ValueError, Solution().numberOfSteps, n)

    def test_example_1(self):
        n = 14

        result = Solution().numberOfSteps(n)
        expected = 6
        self.assertEquals(result, expected)

    def test_example_2(self):
        n = 8

        result = Solution().numberOfSteps(n)
        expected = 4
        self.assertEquals(result, expected)

    def test_example_3(self):
        n = 123

        result = Solution().numberOfSteps(n)
        expected = 12
        self.assertEquals(result, expected)


if __name__ == "__main__":
    unittest.main()
