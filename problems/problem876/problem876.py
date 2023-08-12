from typing import Optional


class ListNode:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next


class Solution:
    def middleNode(self, head: Optional[ListNode]) -> Optional[ListNode]:
        if head == None:
            return None
        pointer_1 = head
        pointer_2 = head
        while True:
            if pointer_2.next == None:
                return pointer_1
            pointer_1 = pointer_1.next
            pointer_2 = pointer_2.next

            if pointer_2.next == None:
                return pointer_1
            pointer_2 = pointer_2.next
