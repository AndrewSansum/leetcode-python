from typing import List


class Solution:
    def maximumWealth(self, accounts: List[List[int]]) -> int:
        if not accounts:
            raise ValueError
        if not all(accounts):
            raise ValueError

        return max(map(sum, accounts))
