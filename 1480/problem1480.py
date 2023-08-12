from typing import List


class Solution:
    def runningSum(self, nums: List[int]) -> List[int]:
        if not nums:
            raise ValueError("nums may not be empty")

        sums = []
        for n in nums:
            if len(sums) < 1:
                sums.append(n)
            else:
                sums.append(n + sums[-1])

        return sums
