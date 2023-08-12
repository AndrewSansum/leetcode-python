import unittest

from problem876 import ListNode, Solution


class TestMiddleNode(unittest.TestCase):
    def test_example_1(self):
        expected = ListNode(3, ListNode(4, ListNode(5)))
        head = ListNode(1, ListNode(2, expected))

        result = Solution().middleNode(head)
        self.assertIs(result, expected)

    def test_example_2(self):
        expected = ListNode(4, ListNode(5, ListNode(6)))
        head = ListNode(1, ListNode(2, ListNode(3, expected)))

        result = Solution().middleNode(head)
        self.assertIs(result, expected)

    def test_single(self):
        head = ListNode(876)
        result = Solution().middleNode(head)
        self.assertIs(result, head)


if __name__ == "__main__":
    unittest.main()
