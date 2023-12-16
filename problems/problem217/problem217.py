from typing import List


class Solution:
    def containsDuplicate(self, nums: List[int]) -> bool:
        recorded = set()
        for num in nums:
            if num in recorded:
                return True
            recorded.add(num)
        return False
