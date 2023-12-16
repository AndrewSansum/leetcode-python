import unittest

from problem1160 import Solution


class Test1160Solution(unittest.TestCase):
    def test_example1(self):
        words = ["cat", "bt", "hat", "tree"]
        chars = "atach"
        self.assertEqual(Solution().countCharacters(words, chars), 6)

    def test_example2(self):
        words = ["hello", "world", "leetcode"]
        chars = "welldonehoneyr"
        self.assertEqual(Solution().countCharacters(words, chars), 10)


if __name__ == "__main__":
    unittest.main()
