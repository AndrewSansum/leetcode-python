import unittest

from problem242 import Solution


class Test242Solution(unittest.TestCase):
    def test_example1(self):
        s = "anagram"
        t = "nagaram"
        self.assertTrue(Solution().isAnagram(s, t))

    def test_example2(self):
        s = "rat"
        t = "car"
        self.assertFalse(Solution().isAnagram(s, t))


if __name__ == "__main__":
    unittest.main()
