class Solution:
    def isAnagram(self, s: str, t: str) -> bool:
        s_count = {}
        for letter in s:
            if letter in s_count:
                s_count[letter] += 1
            else:
                s_count[letter] = 1

        for letter in t:
            if not letter in s_count:
                return False

            if s_count[letter] < 1:
                return False

            s_count[letter] -= 1

        for letter in s_count:
            if s_count[letter] > 0:
                return False

        return True
