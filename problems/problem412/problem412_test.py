import unittest

from problem412 import Solution


class TestFizzBuzz(unittest.TestCase):
    def test_invalid_n(self):
        n = 0
        self.assertRaises(ValueError, Solution().fizzBuzz, n)

    def test_example_1(self):
        n = 3
        result = Solution().fizzBuzz(n)
        expected = ["1", "2", "Fizz"]
        self.assertEqual(result, expected)

    def test_example_2(self):
        n = 5
        result = Solution().fizzBuzz(n)
        expected = ["1", "2", "Fizz", "4", "Buzz"]
        self.assertEqual(result, expected)

    def test_example_3(self):
        n = 15
        result = Solution().fizzBuzz(n)
        expected = [
            "1",
            "2",
            "Fizz",
            "4",
            "Buzz",
            "Fizz",
            "7",
            "8",
            "Fizz",
            "Buzz",
            "11",
            "Fizz",
            "13",
            "14",
            "FizzBuzz",
        ]
        self.assertEqual(result, expected)


if __name__ == "__main__":
    unittest.main()
