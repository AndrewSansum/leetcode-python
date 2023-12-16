import unittest

from problem1662 import Solution


class Test1662Solution(unittest.TestCase):
    def test_example_1(self):
        word1 = ["ab", "c"]
        word2 = ["a", "bc"]
        self.assertTrue(Solution().arrayStringsAreEqual(word1, word2))

    def test_example_2(self):
        word1 = ["a", "cb"]
        word2 = ["ab", "c"]
        self.assertFalse(Solution().arrayStringsAreEqual(word1, word2))

    def test_example_3(self):
        word1 = ["abc", "d", "defg"]
        word2 = ["abcddefg"]
        self.assertTrue(Solution().arrayStringsAreEqual(word1, word2))


if __name__ == "__main__":
    unittest.main()
